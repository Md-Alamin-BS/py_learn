from class_test import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "What color are bananas?\n(a) Red\n(b) Blue\n(c) Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

def que_ans(QA):
    score = 0
    for question in QA:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} correct answear out of {len(QA)} questions.")
    
que_ans(questions)