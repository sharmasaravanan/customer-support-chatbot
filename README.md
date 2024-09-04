# Customer Support Chatbot using ChatGPT API with Streamlit and Knowledge Base from Website Scraping

## Overview

This project implements a Customer Support Chatbot leveraging the capabilities of the ChatGPT API. The chatbot is designed to provide accurate and context-aware responses to customer queries by accessing a dynamically updated knowledge base built from website scraping. The application is built using Streamlit for a user-friendly and interactive interface.

## Features

- **AI-Powered Responses:** Utilizes the ChatGPT API for generating human-like responses.
- **Dynamic Knowledge Base:** Scrapes relevant websites to build and update the knowledge base.
- **Streamlit Interface:** Provides a simple and intuitive UI for interacting with the chatbot.
- **Customizable:** Easily configurable to adapt to different websites and support various customer service needs.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/customer-support-chatbot.git
   cd customer-support-chatbot
  
2. **Install the Required Dependencies:**
  Ensure you have Python 3.x installed. Then, run:

  ```bash
  pip install -r requirements.txt
  ```

3. **Set Up Environment Variables:**

    OPENAI_API_KEY: Your API key for accessing the ChatGPT API

4. **Run the Application:**

   ```bash
   streamlit run app.py
  
## Usage
  * Starting the Chatbot: Open the Streamlit app in your browser. You can start interacting with the chatbot by typing your queries in the input box.
  * Customizing the Knowledge Base: Modify the SCRAPING_URLS in the .env file to point to the websites relevant to your support queries. The bot will scrape these sites and update its knowledge base accordingly.

## Project Structure

```plaintext
📁 customer-support-chatbot/
├── 📄 app.py                   # Main application file for Streamlit
├── 📄 chatbot_module.py        # Chatbot logic and API integration
├── 📄 requirements.txt         # Python dependencies
└── 📄 README.md                # Project documentation

