walker tutor {
    can user;

    has weakest: str;

    with entry {
        report "Tutor analyzing user " + here.username;
    }

    for k = key, v = value in here.progress {
        if(!weakest or v < here.progress[weakest]) {
            weakest = k;
        }
    }

    if(!weakest) {
        weakest = "jac.walkers.basics";
    }

    lessons = [];
    for l in root::lesson {
        if(l.concept == weakest) {
            lessons.push(l);
        }
    }

    take(lessons[0]);
    report "Recommended lesson: " + lessons[0].title;
}
