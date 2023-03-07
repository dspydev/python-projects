import openai
import random

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up GPT-3 parameters
model_engine = "text-davinci-002"
prompt_prefix = "Q: "
temperature = 0.5
max_tokens = 100

def generate_response(prompt):
    # Generate response using GPT-3
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_prefix + prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the response text from the API result
    response_text = response.choices[0].text.strip()

    return response_text

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

            # Generate response
            response = generate_response(user_question)

            # Print output
            if user_name:
                print(user_name + " asks: " + user_question)
            else:
                print("Question: " + user_question)

            if not user_question:
                print("Please ask a question!")
            else:
                print("Magic 8-Ball's answer: " + response)

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
