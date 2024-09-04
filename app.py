import requests
import streamlit as st
from chatbot_module import Chatbot
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.76 Safari/537.36',
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://www.google.com/"
}


# Function to scrape content from website URL
def scrapeContent(url):
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url
    res = requests.get(url, headers=headers, timeout=180)
    if str(res.status_code).startswith("4"):
        return None
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(res.content, 'html.parser')

    # Remove inline CSS styles and class attributes
    for tag in soup.find_all():
        for style in ['style', 'class']:
            del tag[style]

    # Define the tags you want to extract
    tags_to_extract = ['p', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', "li"]

    # Extract and concatenate the text content of the selected tags
    contentChecker = []
    extracted_content = ' '
    for tag in soup.find_all(tags_to_extract):
        temp = tag.get_text(strip=True)
        temp = temp.replace('\xa0', ' ').replace("Â", ' ').strip()
        if temp not in contentChecker:
            contentChecker.append(temp)
            extracted_content += " {}".format(temp)

    content = extracted_content.replace("\n", ' ')
    # storing content in txt file
    with open('content.txt', 'w') as file:
        file.write(content)
    return content


# Function to display input form for website URL
def display_input_form():
    st.title('Customer Support Chatbot Application')
    st.header('Enter Website URL to Scrape')

    website_url = st.text_input('Enter Website URL')
    if st.button('Submit'):
        try:
            content = scrapeContent(website_url)
            if content:
                st.session_state.website_url = website_url
                st.experimental_rerun()
            else:
                st.error('Invalid URL. Please enter a valid website URL.')
                st.stop()
        except Exception as e:
            st.error(f'An error occurred: {e}')
            st.stop()


# Function to display the chatbot interface with conversation history
def display_chatbot_interface():
    st.title('Customer Support Chatbot')
    st.header('Chat Interface')

    # Initialize chatbot with website URL
    website_url = st.session_state.website_url
    chatbot = Chatbot(website_url)  # Initialize chatbot with scraped data

    # Initialize conversation history if not already initialized
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Chat interface with conversation history and avatars
    conversation_history = st.session_state.conversation_history
    user_input = st.text_input('You:', key='user_input')

    if st.button('Send'):
        # Get bot response and update conversation history
        bot_response = chatbot.get_response(user_input, conversation_history)
        conversation_history.append({'sender': 'user', 'message': user_input})
        conversation_history.append({'sender': 'bot', 'message': bot_response})

        # Save updated conversation history in session state
        st.session_state.conversation_history = conversation_history

    # Display conversation history with avatars in a scrollable area
    st.subheader('Conversation History:')
    history_text = ""
    for idx, message in enumerate(conversation_history):
        if message['sender'] == 'user':
            history_text += f"You: {message['message']}\n\n"
        else:
            history_text += f"Bot: {message['message']}\n\n"

    st.text_area(label='Chat History', value=history_text, height=400, max_chars=None, key=None)


# Main function to control flow
def main():
    if 'website_url' not in st.session_state:
        display_input_form()
    else:
        display_chatbot_interface()


if __name__ == '__main__':
    main()
