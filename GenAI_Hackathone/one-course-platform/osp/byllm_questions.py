from jaseci.actions.live_actions import jaseci_action
from openai import OpenAI

client = OpenAI()

@jaseci_action
def byllm_question_gen(concept: str, num: int = 3):
    prompt = f"""
    Generate {num} beginner questions about the concept: {concept}.
    Return a JSON array of:
    - question
    - answer
    """
    res = client.responses.create(
        model="gpt-5.1",
        input=prompt
    )
    return res.output_text
