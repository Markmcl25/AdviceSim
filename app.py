import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # New client object for v1+

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-advice", methods=["POST"])
def get_advice():
    user_question = request.json.get("question", "")

    prompt = f"""You are a humorous advice-giving AI. Always answer with a funny twist and throw in a few emojis. 
    Here's a question: "{user_question}" 
    Respond with funny but somewhat helpful advice."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.9
        )
        advice = response.choices[0].message.content
        return jsonify({"advice": advice})
    except Exception as e:
        print("Error from OpenAI:", e)
        return jsonify({"advice": "Bollox! 🤖 Something went wrong. Try again later."})

if __name__ == "__main__":
    app.run(debug=True)
