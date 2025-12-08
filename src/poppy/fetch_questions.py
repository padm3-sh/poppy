import requests


TRIVIA_URL = "https://opentdb.com/api.php?amount=10&type=multiple"


def fetch_response():
    response = requests.get(TRIVIA_URL)
    data = response.json()

    if data['response_code'] == 0:
        question_set = data['results']
        return question_set
    
    return ValueError("can not connect.")