from openai import OpenAI


def main() -> None:
    """Run a simple AI-powered Paris travel guide conversation."""
    client = OpenAI()
    model = "gpt-4o-mini"

    conversation = [
        {
            "role": "system",
            "content": (
                "You are a helpful Paris travel guide. "
                "Answer clearly, accurately, and briefly for tourists visiting Paris."
            ),
        }
    ]

    questions = [
        "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
        "Where is the Arc de Triomphe?",
        "What are the must-see artworks at the Louvre Museum?",
    ]

    for question in questions:
        conversation.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model=model,
            messages=conversation,
            temperature=0.0,
            max_tokens=100,
        )

        assistant_answer = response.choices[0].message.content or ""
        conversation.append({"role": "assistant", "content": assistant_answer.strip()})

    for message in conversation:
        print(f"{message['role'].upper()}: {message['content']}\n")


if __name__ == "__main__":
    main()
