from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Retrieve the API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['text']
    response_text = ask_openai(user_input)
    return jsonify({"response": response_text})

def ask_openai(question):
    # Assuming you have configured the API key and openai
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message['content']

if __name__ == '__main__':
    app.run(debug=True)