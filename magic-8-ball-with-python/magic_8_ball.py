import random

def main():
    try:
        # Get user input
        user_name = input("What is your name? ")
        if not user_name:
            raise EOFError

        while True:
            # Get user input
            user_question = input("What is your question? ")
            if not user_question:
                raise EOFError

            # List of possible answers
            possible_answers = [
                "Yes",
                "No",
                "Maybe",
                "It is certain",
                "Very doubtful",
                "Ask again later",
                "Cannot predict now",
                "Outlook good"
            ]

            # Generate random index
            random_index = random.randint(0, len(possible_answers) - 1)

            # Assign answer based on random_index
            selected_answer = possible_answers[random_index]

            # Print output
            if user_name:
                print(user_name + " asks: " + user_question)
            else:
                print("Question: " + user_question)

            if not user_question:
                print("Please ask a question!")
            else:
                print("Magic 8-Ball's answer: " + selected_answer)

            # Ask user if they want to play again
            while True:
                play_again = input("Do you want to ask another question? (y/n) ")
                if play_again.lower() == 'y':
                    break
                elif play_again.lower() == 'n':
                    print("Thanks for playing!")
                    raise EOFError
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

    except EOFError:
        print("Exit...")
    except KeyboardInterrupt:
        print("Exit...")

if __name__ == "__main__":
    main()
