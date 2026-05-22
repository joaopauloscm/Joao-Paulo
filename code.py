
class JoaoPaulo:
    def __init__(self):
        self.name = "João Paulo Pereira Santana"
        self.role = "Computer Science Student"
        self.main_language = "Python"
        self.current_focus = [
            "Python fundamentals",
            "Git and GitHub",
            "Problem solving",
            "Portfolio projects"
        ]
        self.goals = [
            "Junior Developer position",
            "AI and automation",
            "Build real-world projects"
        ]

    def status(self):
        return "Studying Python and building my developer portfolio."


me = JoaoPaulo()
print(me.status())
