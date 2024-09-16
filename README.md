# AI Chatbot Using GPT Models

This project creates an AI chatbot using **GPT-2**, which generates responses to user input in natural language. The chatbot can be integrated with web platforms like **Telegram** or **Slack** for real-time conversations.

## Features:
- Powered by GPT-2 for conversational AI.
- Simple web-based interface for interacting with the chatbot.
- Easy integration with platforms like Telegram or Slack via APIs.

## Setup:

1. Clone this repository:
   ```bash
   git clone https://github.com/Shashwat1729/AI-Chatbot-Using-GPT.git
   cd AI-Chatbot-Using-GPT
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/` to interact with the chatbot.

## Integrations:
To integrate the chatbot with **Telegram** or **Slack**, you need to add your API tokens in the `config.py` file:
```python
TELEGRAM_API_KEY = "your-telegram-api-key"
SLACK_API_TOKEN = "your-slack-api-token"
```

---

**Contributions**:
Feel free to contribute by opening issues or creating pull requests!

