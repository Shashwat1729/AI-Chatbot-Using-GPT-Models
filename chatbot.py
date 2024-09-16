from transformers import pipeline

class ChatBot:
    def __init__(self):
        # Load the pre-trained GPT model for conversational AI
        self.chat_model = pipeline("text-generation", model="gpt2", max_length=100)

    def get_response(self, user_input):
        # Generate a response using GPT-2 model
        response = self.chat_model(user_input, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']
