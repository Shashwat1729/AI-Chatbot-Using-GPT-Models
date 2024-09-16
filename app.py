from flask import Flask, render_template, request
from chatbot import ChatBot
import os

app = Flask(__name__)

# Initialize the chatbot
bot = ChatBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    bot_response = bot.get_response(user_input)
    return render_template('index.html', user_input=user_input, bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
