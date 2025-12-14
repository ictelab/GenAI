walker generate_quiz {
    can lesson;
    has num: int = 3;

    with entry {
        report "Generating quiz for " + here.title;
    }

    res = std.byllm_question_gen(
        concept=here.concept,
        num=num
    );

    here.quiz = res;
    report "Quiz generated.";
    report res;
}
