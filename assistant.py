import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_assistant(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    question = input("Ask your assistant something: ")
    print(ask_assistant(question))

