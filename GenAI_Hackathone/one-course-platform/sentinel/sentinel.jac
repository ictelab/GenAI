object course_platform {
    has lessons: list = [];
    has concepts: list = [];

    root {
        # Concept
        c = spawn node::concept;
        c.name = "jac.walkers.basics";
        concepts.push(c);

        # Lesson
        l = spawn node::lesson;
        l.title = "Introduction to Walkers";
        l.content = "Walkers allow traversal of nodes and edges in Jac.";
        l.concept = "jac.walkers.basics";
        lessons.push(l);

        report "One-course platform initialized.";
    }
}
