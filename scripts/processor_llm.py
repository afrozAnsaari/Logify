from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()


def classify_with_llm(log_message: str) -> str | None:
    prompt = f"""Classify the log message into on of the three categories:
    (1) Workflow error, (2) Depricated Warning.
    if you can't figure out a specific category, return "Unclassified".
    Only return the category name. No preamble.
    Log Message: {log_message}"""

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    print(
        classify_with_llm(
            "Case estimation for ticket ID-2343 failed because  the assigned support decision assigned collapsed"
        )
    )

    print(
        classify_with_llm(
            "The 'report generator module  will be retire  in version 4.0. Please migrate to another source'"
        )
    )

    print(classify_with_llm("System reboote initialised by user 1243."))
