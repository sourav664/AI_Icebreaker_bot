"""Module for interfacing with IBM watsonx.ai LLMs."""

import logging
from typing import Dict, Any, Optional

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import config

logger = logging.getLogger(__name__)

def create_openai_embedding() -> OpenAIEmbedding:
    """Creates an OpenAI Embedding model for vector representation.
    
    Returns:
        OpenAIEmbedding model.
    """
    try:
        api_key_embedding = config.API_KEY
        model_name = config.EMBEDDING_MODEL
        embed_model = OpenAIEmbedding(model=model_name, api_key=api_key_embedding)
        
        logger.info("OpenAIEmbedding model created successfully.")
        return embed_model
    
    except Exception as e:
        logger.error(f"Error creating OpenAIEmbedding model: {e}")
        return None
        

def create_openai_llm(
    temperature: float = 0.0,
) -> OpenAI:
    """Creates an OpenAI LLM for generating responses.
    
    Args:
        temperature: Temperature for controlling randomness in generation (0.0 to 1.0).
    Returns:
        OpenAI model.
    """
    
    try:
        api_key_llm = config.API_KEY
        model_name = config.LLM_MODEL
        llm = OpenAI(model=model_name, api_key=api_key_llm, temperature=temperature)
        
        logger.info("OpenAI LLM created successfully.")
        return llm
    
    except Exception as e:
        logger.error(f"Error creating OpenAI LLM: {e}")
        return None

def change_llm_model(new_model_id: str) -> None:
    """Change the LLM model to use.
    
    Args:
        new_model_id: New LLM model ID to use.
    """
    global config
    config.LLM_MODEL = new_model_id
    logger.info(f"Changed LLM model to: {new_model_id}")
