import html
from poppy import fetch_response



def main():
    question_set = fetch_response.fetch_response()
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

        if len(stringo.strip()) < 2:
            if int(stringo) == all_answers.index(correct_answer) + 1:
                print("You got it right!")
                points += 3
            else:
                print("That is not right!")
        else:
            if stringo == correct_answer:
                print("You got it right!")
                points += 3
            else:
                print("That is not right!")


    print(f"You got a total of {points} points.")

if __name__ == "__main__":
    main()