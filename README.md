
def pad(text, width):
	return text + ' ' * (width - len(text))

profile = [
	"João Paulo Pereira Santana",
	"Computer Science Student",
	"Main Language: Python"
]

stack = [
	("[language]",   "Python"),
	("[tools]",      "Git • GitHub • VS Code"),
	("[learning]",   "Python Fundamentals • Problem Solving"),
	("[focus]",      "Portfolio Projects • Junior Developer Skills"),
	("[interests]",  "AI • Automation • Software Development")
]

goals = [
	"Build real-world Python projects",
	"Improve my GitHub portfolio",
	"Prepare for junior developer opportunities",
	"Learn AI and automation with Python"
]

status = "Studying Python and building my developer portfolio."

width = 63
border = "┌" + "─" * (width - 2) + "┐"
sep    = "├" + "─" * (width - 2) + "┤"
footer = "└" + "─" * (width - 2) + "┘"

def print_centered(text):
	print("│ " + text.center(width - 4) + " │")

print(border)
for line in profile:
	print_centered(line)
print(sep)
for key, value in stack:
	print(f"│ {pad(key, 13)} {pad(value, width - 17)} │")
print(sep)
print("│ Goals:" + " " * (width - 9) + "│")
for g in goals:
	print(f"│   • {pad(g, width - 7)}│")
print(sep)
print_centered(f"Status: {status}")
print(footer)
