import json
import re
import random_response

def load_json(file):
    with open(file) as bot_responses:
        print(f'loaded "{file}" successfully')
        return json.load(bot_responses)

response_data: dict = load_json('responses.json')

def get_response(input_string: str):
    split_message: list[str] = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list: list[int] = []

    for response in response_data:
        response_score: int = 0
        required_score: int =0
        required_words: list[str] = response['required_words']

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1
        if required_score == len(required_words):
            for word in split_message:
                if word in response['user_input']:
                    response_score += 1
        score_list.append(response_score)

    best_response: int = max(score_list)
    response_index: int = score_list.index(best_response)

    if input_string == "":
        return "please type something"

    if best_response != 0:
        return response_data[response_index]['bot_response']

    return random_response.random_string()

def main():
    while True:
        user_input: str = input('You: ')
        print('Bot:', get_response(user_input))

if __name__ == '__main__':
    main()