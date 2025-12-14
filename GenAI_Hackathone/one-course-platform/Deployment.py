import os
import time
from jaseci.actions.live_actions import jaseci_action
from openai import OpenAI

# Initialize OpenAI client from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@jaseci_action
def byllm_eval(question: str, answer: str, expected: str):
    """
    Evaluates a learner's answer against an expected answer
    using an LLM and returns a JSON score between 0 and 1.
    """
    prompt = f"""
Evaluate the user's answer to the question.

Question: {question}
Expected: {expected}
User: {answer}

Return JSON strictly in this format:
{{"score": 0-1}}
"""

    response = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )

    return response.output_text


# Keeps container alive for Jaseci to load actions
if __name__ == "__main__":
    print("Jaseci LLM Evaluation Action Loaded...")
    while True:
        time.sleep(3600)


