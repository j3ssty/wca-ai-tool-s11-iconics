from business_info import BUSINESS_INFO
from prompts import create_prompt
from openai_api import ask_openai
from utils import save_output, display_response


def main():
    print("=" * 50)
    print("     MAHANAIM CAFÉ AI CUSTOMER ASSISTANT")
    print("=" * 50)

    print("\nAsk a question about Mahanaim Café.")
    print("Type 'exit' to close the program.\n")

    while True:
        question = input("Customer: ")

        if question.lower() == "exit":
            print("\nThank you for using Mahanaim Café AI Assistant.")
            break

        if not question.strip():
            print("Please enter a question.")
            continue

        prompt = create_prompt(BUSINESS_INFO, question)

        answer = ask_openai(prompt)

        display_response(answer)

        save_output(question, answer)


if __name__ == "__main__":
    main()