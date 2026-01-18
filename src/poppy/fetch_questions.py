import requests


TRIVIA_URL = "https://opentdb.com/api.php?amount=10&type=multiple"


def fetch_response():
    question_category = input("Enter question category (eg. random, animals): ")
    
    response = ""
    
    if question_category.lower() == "animals": 
        response = requests.get(TRIVIA_URL+"&category=27")
    elif question_category.lower() == "mythology":
        response = requests.get(TRIVIA_URL+"&category=20")
    elif question_category.lower() == "vehicles":
        response = requests.get(TRIVIA_URL+"&category=28")
    else:
        response = requests.get(TRIVIA_URL)
        
    data = response.json()

    if data['response_code'] == 0:
        question_set = data['results']
        return question_set
    
    return ValueError("can not connect.")