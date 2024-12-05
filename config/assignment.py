import os
from datetime import datetime
from agents.ocr.claude_ocr import extracttext
from anthropic import Anthropic
# assignment.py

class Assignments:
    def __init__(self, title: str, due_date: str, weight: float):
        self.title = title
        try:
            # Parse the due_date string into a datetime.date object
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("due_date should be in 'YYYY-MM-DD'")
        self.weight = weight

    def __str__(self):
        return f"Assignment(title='{self.title}', due_date='{self.due_date}', weight={self.weight})"
