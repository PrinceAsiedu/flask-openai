from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os


app = Flask(__name__)

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']

    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-instruct",
            messages=[
                {"role": "system", "content": "You are ChatGPT, a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = chat_completion.choices[0].message['content']
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
