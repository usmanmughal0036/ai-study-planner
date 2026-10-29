from pathlib import Path

print("=== My AI Study Planner ===")

name = input("Your name: ").strip()
goal = input("Your AI learning goal: ").strip()
days_text = input("Study days each week: ").strip()
hours_text = input("Study hours per day: ").strip()

days = int(days_text)
hours = float(hours_text)

weekly_hours = days * hours

print(f"{name}, you can study {weekly_hours:g} hours per week.")

plan = f"""MY AI STUDY PLAN

Student: {name}
Learning goal: {goal}
Study days: {days}
Hours per day: {hours:g}
Weekly total: {weekly_hours:g} hours

SUGGESTED ACTIVITIES
1. Learn Python fundamentals
2. Practice Python programming
3. Explore AI automation tools
4. Build a small AI-related project
5. Review and update GitHub
"""

print(plan)

Path("study_plan.txt").write_text(plan, encoding="utf-8")

print("Saved: study_plan.txt")

readme = f"""# My AI Study Planner

A beginner-friendly Python project by {name}.

Learning Goal: {goal}

Features:
- Collects student information.
- Calculates weekly study hours.
- Generates a personalized study plan.
- Saves the plan to study_plan.txt.
- Generates this README.md file.

Technologies:
- Python 3
- pathlib
- Basic input and output
- File handling

How to Run:
py planner.py

Output:
study_plan.txt

This is an educational project demonstrating basic Python.
"""

Path("README.md").write_text(readme, encoding="utf-8")

print("Saved: README.md")
