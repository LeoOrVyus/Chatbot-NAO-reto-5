from flask import Flask, render_template, request
from chatbot_controller import ChatbotController

app = Flask(__name__)
chatbot = ChatbotController(api_key='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')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot.generate_response(user_input)
    return response

if __name__ == '__main__':
    app.run()
