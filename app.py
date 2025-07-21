from flask import Flask, render_template, request, jsonify
import g4f
import g4f.models

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
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,  # You can replace this with another model name like gpt_4o or llama_3_70b
            messages=[{"role": "user", "content": prompt}],
        )
        return jsonify({"advice": response})
    except Exception as e:
        print("Error using g4f:", e)
        return jsonify({"advice": "Oops! 🤖 Something funny went wrong. Try again soon!"})

if __name__ == "__main__":
    app.run(debug=True)
