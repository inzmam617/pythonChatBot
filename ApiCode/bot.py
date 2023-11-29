# from flask import Flask, render_template, request
# import os
# import aiml
# from autocorrect import spell
#
# app = Flask(__name__)
#
# BRAIN_FILE="./pretrained_model/aiml_pretrained_model.dump"
# k = aiml.Kernel()
#
# if os.path.exists(BRAIN_FILE):
#     print("Loading from brain file: " + BRAIN_FILE)
#     k.loadBrain(BRAIN_FILE)
# else:
#     print("Parsing aiml files")
#     k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
#     print("Saving brain file: " + BRAIN_FILE)
#     k.saveBrain(BRAIN_FILE)
#
#
# @app.route("/get")
# def get_bot_response():
#     query = request.args.get('msg')
#     query = query.replace('"',"")
#     query = [spell(w) for w in (query.split())]
#     question = " ".join(query)
#     response = k.respond(question)
#     if response:
#         return (str(response))
#     else:
#         return (str(":)"))
#
#
# if __name__ == "__main__":
#     # app.run()
#     app.run(host='0.0.0.0', port='5000')
#
from flask import Flask, request
import os
import aiml
from autocorrect import Speller  # Import the Speller class

app = Flask(__name__)

BRAIN_FILE = "./pretrained_model/aiml_pretrained_model.dump"
k = aiml.Kernel()
spell = Speller(lang='en')  # Create a Speller instance for English

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)


def correct_spelling(input_text):
    corrected_text = []
    words = input_text.split()
    for word in words:
        corrected_word = spell(word)  # Use Speller to correct words
        corrected_text.append(corrected_word)
    return ' '.join(corrected_text)


@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    query = query.replace('"', "")
    corrected_query = correct_spelling(query)  # Correct user input
    response = k.respond(corrected_query)
    if response:
        return str(response)
    else:
        return ":)"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
