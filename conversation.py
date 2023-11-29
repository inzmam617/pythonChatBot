# import aiml
# from autocorrect import Speller
#
# BRAIN_FILE = "./pretrained_model/aiml_pretrained_model.dump"
#
# # Creating a new AIML kernel instance
# k = aiml.Kernel()
#
# # Parsing AIML files and saving a new brain file
# print("Parsing AIML files")
# k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
# print("Saving a new brain file: " + BRAIN_FILE)
# k.saveBrain(BRAIN_FILE)
# spell = Speller(lang='en')
#
#
# def correct_spelling(input_text):
#     corrected_text = []
#     words = input_text.split()
#     for word in words:
#         corrected_word = spell(word)
#         corrected_text.append(corrected_word)
#     return ' '.join(corrected_text)
#
#
# try:
#     while True:
#         query = input("User > ")
#         corrected_query = correct_spelling(query)
#         response = k.respond(corrected_query)
#         print("Corrected Query > ", corrected_query)
#         if response:
#             print("Bot > ", response)
#         else:
#             print("Bot > :) ")
# except KeyboardInterrupt:
#     print("\nProgram interrupted by the user. Exiting.")
