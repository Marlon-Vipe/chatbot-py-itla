import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

from preguntas import check_all_messages

while True:
    print("Bot: " + get_response(input('You: ')))