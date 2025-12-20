from byllm import LLM

llm = LLM(
    provider="openai",
    model="gpt-4",
    temperature=0.3
)

def ask_llm(prompt: str) -> str:
    return llm(prompt)

