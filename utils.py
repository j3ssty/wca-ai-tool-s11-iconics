from datetime import datetime


def save_output(question, answer):
    with open("output.txt", "a", encoding="utf-8") as file:
        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"Customer: {question}\n")
        file.write(f"Assistant: {answer}\n")


def display_response(answer):
    print("\nAssistant:")
    print(answer)
