import openai
import os

# set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"

# initialize OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]

# function to generate an answer from GPT-3
def generate_answer(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

# main program loop
while True:
    question = input("What is your question? ")
    if question.lower() == "quit":
        break

    # generate answer from GPT-3
    answer = generate_answer(question)

    # display the answer
    print("Answer: ", answer)
