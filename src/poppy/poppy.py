import html
from poppy import fetch_questions



def main():
    question_set = fetch_questions.fetch_response()
    points = 0

    for index, each_question in enumerate(question_set):

        question = html.unescape(each_question["question"])
        correct_answer = each_question["correct_answer"]
        incorrect_answer = each_question["incorrect_answers"]
        incorrect_answer.append(correct_answer)
        all_answers = sorted(incorrect_answer)

        print(f"{index + 1}. {question}")

        for answer in all_answers:
            print(f"=> {answer}")
    
        stringo = input("Enter Answer or Option: ")

        if int(stringo) == all_answers.index(correct_answer) + 1:
            print("You got it right!")
            points += 3


    print(f"You got a total of {points} points.")

if __name__ == "__main__":
    main()