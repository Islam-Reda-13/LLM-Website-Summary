# Landing Page Summary Generator

This project provides a streamlined interface to generate concise, markdown-formatted summaries of company landing pages. It leverages large language models (LLMs) to extract and articulate key information suitable for potential customers, investors, or recruits.
# Overview

The application allows users to:

    Input a company name and URL

    Choose from three LLMs: Qwen, DeepSeek, or LLaMA

    Automatically scrape and clean website content

    Generate a structured summary in real-time

# Features

    Interactive user interface built with Gradio

    Web scraping via BeautifulSoup

    Real-time streaming of model output

    Support for multiple models via OpenRouter

# Technologies Used

    Python

    Gradio (UI framework)

    BeautifulSoup (HTML parsing and cleaning)

    OpenRouter API (multi-model access)

    dotenv (secure environment variable management)
# Setup Instructions
1. Clone the repository

`git clone https://github.com/yourusername/landing-page-summary-generator.git
cd landing-page-summary-generator
`
2. Install dependencies

pip install -r requirements.txt

3. Configure API keys

# Create a .env file in the root directory and add:

`OPENAI_API_KEY=your_key_here
OPENROUTER_API_KEY=your_openrouter_key_here
`
4. Launch the application

python main.py

# Repository Structure
`
├── main.py                  # Gradio interface and app layout
├── models_and_prompting.py # Prompt handling and model streaming logic
├── web_scraping.py         # HTML content scraper using BeautifulSoup
├── .env                    # API keys (excluded from version control)
└── requirements.txt        # Python package dependencies`
