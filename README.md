

``class JoaoPaulo:
    def __init__(self):
        self.skills = [
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

print("\nSkills:")
for skill in me.skills:
    print("-", skill)

print("\nGoals:")
for goal in me.goals:
    print("-", goal)
```
