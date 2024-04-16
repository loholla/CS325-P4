from openai import OpenAI

def test_API_key():
    client = OpenAI()
    prompt = "Respond with Yes or No. Can you see this message?"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are an assistant who is great at answering Yes or No questions."},
            {"role":"user","content":prompt}
        ]
    )

    print(str(response.choices[0].message.content))

if __name__ == "__main__":
    test_API_key()