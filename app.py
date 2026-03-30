from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey! 👋 How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! What about you?"

    elif "your name" in user_input:
        return "I'm Sohail's Smart Chatbot 🤖"

    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    elif "help" in user_input:
        return "Sure! Ask me anything 😄"

    elif "cloud" in user_input:
        return "Cloud computing allows apps to run over the internet ☁️"

    elif "aws" in user_input:
        return "AWS is Amazon's cloud platform 🚀"

    elif "who made you" in user_input:
        return "I was created by Sohail 😎"

    elif "thank" in user_input:
        return "You're welcome! 😊"

    elif "what can you do" in user_input:
        return "I can chat with you and answer basic questions!"

    else:
        return "Hmm 🤔 I didn't understand that. Try asking something else!"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
