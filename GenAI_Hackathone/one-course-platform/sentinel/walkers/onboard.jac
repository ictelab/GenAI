walker onboard {
    has name: str;

    root {
        u = spawn node::user;
        u.username = name;
        u.progress = {};
        take(u);

        report "User created: " + name;
    }
}
