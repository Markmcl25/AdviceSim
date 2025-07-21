from flask import Flask, render_template, request, jsonify
import g4f
import g4f.models
import random

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
        return jsonify({"advice": "Shite! 🤖 Something funny went wrong. Try again soon!"})

@app.route('/quote')
def quote():
    gen_z_quotes = [
        "Rise and grind, sigma. The smurf cat believes in your hustle today",
        "If you’re feeling down, just remember: even John Pork kept calling",
        "Don’t let Monday leave you broken — go hit the griddy instead",
        "You got this, king. Kai Cenat didn’t stream 24 hours for you to give up",
        "Today’s vibe: bussin' through the cringe like a goofy ahh gladiator",
        "Be the biggest bird. Not just a bird... the BIGGEST",
        "Remember: Livvy Dunne didn't rizz up Baby Gronk for you to skip leg day",
        "Goon cave is temporary, but the grindset is eternal",
        "If you’re ever lost, just ask: 'Did you pray today?' and follow the pibby glitch",
        "Never forget: hit or miss, I guess they never miss huh... but you? You never miss",
        "Keep pushing, king. Andrew Tate is somewhere doing pushups in Crocs for you"
    ]

    return jsonify({'quote': random.choice(gen_z_quotes)})
if __name__ == "__main__":
    app.run(debug=True)
