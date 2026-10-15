"""Module for processing LinkedIn profile data."""

import json
import logging
from typing import Dict, List, Any, Optional

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

from modules.llm_interface import create_openai_embedding
import config

logger = logging.getLogger(__name__)

def split_profile_data(profile_data: Dict[str, Any]) -> List[Document]:
    """Splits LinkedIn profile data into individual documents.
    
    Args:
        profile_data: LinkedIn profile data.
    
    Returns:
        List of documents containing the profile data.
    """
    
    try:
        profile_json = json.dumps(profile_data)
        documents = Document(text=profile_json)
        
        splitter = SentenceSplitter(
            chunk_size=config.CHUNK_SIZE)
        
        
        nodes = splitter.get_nodes_from_documents([documents])
        
        logger.info(f"Created {len(nodes)} nodes from profile data")
        
        return nodes
    
    except Exception as e:
        logger.error(f"Error splitting profile data: {e}")
        return []
    
    
    
def create_vector_database(nodes: List) -> Optional[VectorStoreIndex]:
    """Stores the document chunks (nodes) in a vector database.
    
    Args:
        nodes: List of document nodes to be indexed.
        
    Returns:
        VectorStoreIndex or None if indexing fails.
    """
    
    try:
        embedding_model = create_openai_embedding()
        
        index = VectorStoreIndex(
            nodes=nodes,
            embed_model=embedding_model,
            show_progress=True
        )
        
        logger.info("Vector database created successfully.")
        return index
    
    except Exception as e:
        logger.error(f"Error creating vector database: {e}")
        return None
    
    
def verify_embeddings(index: VectorStoreIndex) -> bool:
    """Verify that all nodes have been properly embedded.
    
    Args:
        index: VectorStoreIndex to verify.
        
    Returns:
        True if all embeddings are valid, False otherwise.
    """
    
    try:
        vectore_store = index._storage_context.vector_store
        node_ids = list(index.index_struct.nodes_dict.keys())
        
        missing_embeddings = False
        
        for node_id in node_ids:
            embedding = vectore_store.get(node_id)
            
            if embedding is None:
                logger.warning(f"Node ID {node_id} has no embedding.")
                missing_embeddings = True
                
            else:
                logger.debug(f"Node ID {node_id} has a valid embedding")
                
                
        if missing_embeddings:
            logger.warning("Missing embeddings in vector database.")
            return False
        else:
            logger.info("All embeddings are valid in vector database.")
            return True
        
    except Exception as e:    
        logger.error(f"Error verifying embeddings: {e}")
        return False