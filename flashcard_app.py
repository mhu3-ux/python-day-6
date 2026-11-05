#In Comments write out what functions yout think the function should be

import random

# Flashcards for reviewing Python questions
flashcard = [
    {"question": "What is a variable?",
     "answer": "A variable stores a value in Python."},

    {"question": "What is a string?",
     "answer": "A string is text enclosed in quotation marks."},

    {"question": "What is a list?",
     "answer": "A list stores multiple items in one variable."},


]


# Select a random question
def get_random_question():
    return random.choice(flashcard)


# Display the question
def show_question(card):
    print("\nQuestion:", card["question"])


# Display the answer
def show_answer(card):
    print("Answer:", card["answer"])


# Main application
while True:
    user = input("\nPress Enter for a question or 'q' to quit: ")

    if user.lower() == "q":
        quit_app()
        break

    card = get_random_question()
    show_question(card)

    input("Press Enter to reveal the answer...")
    show_answer(card)





    flashcards = [
    {"question": "What is a list?", "answer": "A collection of items"},
    {"question": "What is a dictionary?", "answer": "A collection of key-value pairs"},
    {"question": "What is a loop?", "answer": "Repeats a block of code"}
]

card = get_random_questions(flashcards)
print(card["question"])


import random

flashcards = [
    {"question": "What is a list?", "answer": "A collection of items"},
    {"question": "What is a dictionary?", "answer": "A collection of key-value pairs"},
    {"question": "What is a loop?", "answer": "Repeats a block of code"}
]


def get_random_question(cards):
    return random.choice(cards)


def show_question(card):
    print(card["question"])


def show_answer(card):
    print(card["answer"])


def flashcard_app():
    while True:
        card = get_random_question(flashcards)
        show_question(card)

        while True:
            choice = input("See answer or quit? ").lower().strip()

            if choice == "see answer":
                show_answer(card)
                break

            elif choice == "quit":
                print("Goodbye!")
                return

            else:
                print("Invalid input. Try again.")


flashcard_app()