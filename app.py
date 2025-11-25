from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"reply": "Please type something!"})

        # New OpenAI API (2024–2025)
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"""
You are FitBot, a friendly health & fitness expert.
Answer the following user input:

{user_input}
"""
        )

        bot_reply = response.output_text

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("🔥 Error:", e)
        return jsonify({"reply": f"⚠️ Server Error: {str(e)}"})
