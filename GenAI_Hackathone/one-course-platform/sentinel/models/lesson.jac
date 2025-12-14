node lesson {
    has title: str;
    has content: str;
    has concept: str;     # Only one concept for simplicity
    has quiz: list = [];  # byLLM-generated questions
}
