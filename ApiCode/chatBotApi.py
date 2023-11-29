from flask import Flask, request, jsonify
import aiml

app = Flask(__name__)
kernel = aiml.Kernel()


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    bot_response = kernel.respond(user_input)
    return jsonify({'bot_response': bot_response})


if __name__ == '__main__':
    app.run()
