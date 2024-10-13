from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')  # Make sure your environment variable is set

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    message = data.get('message')

    if message:
        # Call OpenAI API with the user message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        
        # Extract the bot's reply
        bot_response = response['choices'][0]['message']['content']
        return jsonify({"response": bot_response})
    else:
        return jsonify({"response": "Sorry, I couldn't get a response."}), 400

if __name__ == '__main__':
    app.run(debug=True)

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
