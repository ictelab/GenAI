from jaseci.actions.live_actions import jaseci_action
from openai import OpenAI

client = OpenAI()

@jaseci_action
def byllm_eval(question: str, answer: str, expected: str):
    prompt = f"""
    Evaluate the user's answer to the question.

    Question: {question}
    Expected: {expected}
    User: {answer}

    Return JSON: {{"score": 0-1}}
    """
    res = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )
    return res.output_text
