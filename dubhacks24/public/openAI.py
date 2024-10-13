import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
from flask_cors import CORS  # Move this import here

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return "Welcome to the Chat API! Use the /api/chat endpoint to interact."

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('messages', [])
    print(f"User Input: {user_input}")  # Log user input
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=user_input
        )
        print(f"Response: {response}")  # Log the response
        return jsonify(response)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)