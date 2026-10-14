# LinkedIn Icebreaker Bot

An AI-powered tool that generates personalized icebreakers and conversation starters based on LinkedIn profiles. This project uses OpenAI model and LlamaIndex to create a tool that helps make introductions more personal and engaging.

## Project Overview

Imagine you're heading to a big networking event, surrounded by potential employers and industry leaders. You want to make a great first impression, but you're struggling to come up with more than the usual, "What do you do?"

This AI icebreaker bot does the research for you. You input a name, and within seconds, the bot searches LinkedIn, generating personalized icebreakers based on someone's career highlights, interests, and even fun facts.

## Features

- Extract LinkedIn profile data using ProxyCurl API or mock data
- Process and index the data using LlamaIndex and IBM watsonx embeddings
- Generate interesting facts about a person's career or education
- Answer specific questions about the LinkedIn profile
- Interact with the bot through a command-line interface or a Gradio web UI

## Project Structure

```
AI_Icebreaker_bot/
├── requirements.txt           # Dependencies
├── config.py                  # Configuration settings
├── modules/
│   ├── __init__.py
│   ├── data_extraction.py     # LinkedIn profile data extraction
│   ├── data_processing.py     # Data splitting and indexing
│   ├── llm_interface.py       # LLM setup and interaction
│   └── query_engine.py        # Query processing and response generation
├── app.py                     # Gradio interface
└── main.py                    # Main script to run without Gradio
```


## License

This project is licensed under the MIT License - see the LICENSE file for details.

