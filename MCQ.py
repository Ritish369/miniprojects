class Question:
    def __init__(self, question_prompt, answer):
        self.question_prompt = question_prompt
        self.answer = answer


def main():
    initializer()
    run_mcq_test(questions)


def initializer():
    global questions, questions_to_user
    questions_to_user = [
        "What's \\n in programming?\n(a) New line\n(b) Tab\n\n",
        "What's int?\n(a) Data type\n(b) Format specifier\n\n",
        "What's a class in programming?\n(a) User-defined data type\n(b) Pre-defined data type\n\n",
    ]
    questions = [
        Question(questions_to_user[0], "a"),
        Question(questions_to_user[1], "a"),
        Question(questions_to_user[2], "a"),
    ]


def run_mcq_test(questions):
    score = 0
    for question in questions:
        answer = input(question.question_prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")


if __name__ == "__main__":
    main()
