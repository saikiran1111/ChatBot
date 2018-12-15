from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named sapchow
chatbot = ChatBot('sapchow')

chatbot.set_trainer(ListTrainer)

chatbot.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])
# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')

print(response)
