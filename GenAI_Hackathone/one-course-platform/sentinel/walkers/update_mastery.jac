walker update_mastery {
    can user;

    has concept: str;
    has question: str;
    has expected: str;
    has answer: str;

    # Evaluate through byLLM
    eval = std.byllm_eval(
        question=question,
        answer=answer,
        expected=expected
    );

    score = eval.score;

    if(!(concept in here.progress)) {
        here.progress[concept] = 0.0;
    }

    here.progress[concept] = min(1.0, here.progress[concept] + (score * 0.3));

    report "Updated mastery: " + str(here.progress[concept]);
}
