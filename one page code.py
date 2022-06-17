question_list=[("A slug's blood is green."),
               ("The loudest animal is the African Elephant."),
               ("Approximately one quarter of human bones are in the feet."),
              ("The total surface area of a human lungs is the size of a football pitch."),
              ("In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to "),
              ("In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral."),
              ("It is illegal to pee in the Ocean in Portugal."),
              ("You can lead a cow down stairs but not up stairs."),
              ("Google was originally called 'Backrub'."),
              ("Buzz Aldrin's mother's maiden name was 'Moon'."),
              ("No piece of square dry paper can be folded in half more than 7 times."),
              ("A few ounces of chocolate can to kill a small dog.")
              ]
Question_answer=[("True"),
                ("False"),
                ("True"),
                ("True"),
                ("True"),
                ("False"),
                ("True"),
                ("False"),
                ("True"),
                ("True"),
                ("False"),
                ("True")
                ]
score=0
for i in range(len(question_list)):
    print(f"{i+1}. "+question_list[i]+" (True/False) : ")
    answer=input()
    if answer==Question_answer[i].lower():
        score=score+1
        print("you got it right")
        print("The correct answer is:" + answer)
        print(f"Your current score is: {score}/{(i+1)}.")
        print()
    else:
        print("You are wrong")
        print("The correct answer is:" + Question_answer[i])
        print(f"your current score is: {score}/{(i+1)}.")
        print()
