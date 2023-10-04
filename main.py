import nltk
from nltk.chat.util import Chat, reflections

# Define rules for the chatbot
pairs = [
    ['hello', ['Hi there!', 'Hello!']],
    ['how are you', ['I am doing well, thank you!', 'I am just a chatbot. How can I assist you?']],
    ['hi riley', []]
    # Add more patterns and responses here
]

chatbot = Chat(pairs, reflections)

# Start chatting
chatbot.converse()
