# 💱 Currency Converter Chatbot 

This project is a **Currency Converter Chatbot** that integrates:
- **Dialogflow** for Natural Language Understanding (NLU)
- **Telegram** for user interaction
- **Flask** for backend handling and currency conversion logic

It enables users to ask queries like:
> "Can you convert 100 USD to INR?"

And receive instant currency conversion replies within Telegram.

---

## 🔧 Tech Stack

- 🧠 [Dialogflow](https://dialogflow.cloud.google.com/) – for intent detection and NLP
- 📬 [Telegram Bot](https://core.telegram.org/bots) – for frontend/chat interface
- 🐍 Python + Flask – for backend and webhook handling
- 🌐 REST API – for fetching live currency exchange rates (e.g., [API Layer](https://apilayer.com/), [ExchangeRate-API](https://www.exchangerate-api.com/))

---

## ⚙️ Features

- Supports natural language queries via Dialogflow
- Converts any currency pair (e.g., USD to INR, EUR to JPY)
- Deployed locally with webhook setup for Telegram
- Easily extendable with more intents

---

## 📸 Telegram Bot Demo

Here’s a screenshot showing how the bot works on Telegram:

![Telegram Bot Demo](https://github.com/user-attachments/assets/ec116dfc-140f-4808-95d3-6d98a9dae54f)




---

## 🚀 How It Works

1. **User sends a message** in Telegram.
2. **Telegram forwards** the message to your Dialogflow webhook.
3. **Dialogflow detects the intent** (like "CurrencyConversion").
4. **Webhook (Flask)** receives the parsed intent and entities.
5. The server **fetches live exchange rates** and responds with the converted value.

---

## 🧪 Sample Dialog

**User**: Convert 100 USD to INR  
**Bot**: 100.0 USD is ₹8599.99 INR

---

## 📝 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/currency_convertor_chatbot_backend.git
cd currency_convertor_chatbot_backend
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Flask Server
```bash
python app.py
```

### 4. Connect Dialogflow to Flask Webhook
In Dialogflow:

Go to Fulfillment > Webhook

Enable webhook and set URL to your server (e.g., via ngrok):
```bash
https://your-ngrok-url.ngrok.io/webhook
```

### 5. Set Telegram Bot Webhook
Use curl to link your Flask endpoint to Telegram:
```bash
curl -F "url=https://your-ngrok-url.ngrok.io/webhook" https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook
```

---
## 🙌 Acknowledgements

- [Dialogflow](https://dialogflow.cloud.google.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Exchange Rate APIs](https://apilayer.com/)
- [Flask](https://flask.palletsprojects.com/)

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

