"""Tests for the student application; no external packages needed."""
import importlib.util
import os
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("devops_app", ROOT / "app" / "main.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class StudentAppTests(TestCase):
    def test_default_student_data(self):
        with patch.dict(os.environ, {
            "STUDENT_NAME": "Nurdos",
            "STUDENT_SURNAME": "Kanatbek",
            "STUDENT_GROUP": "IT2-2310",
            "STUDENT_ID": "37253",
        }):
            self.assertEqual(app.student_info()["Student ID"], "37253")
            self.assertIn("Group: IT2-2310", app.render_student_info())

    def test_environment_override(self):
        with patch.dict(os.environ, {
            "STUDENT_NAME": "TestName",
            "STUDENT_SURNAME": "TestSurname",
            "STUDENT_GROUP": "TEST-GROUP",
            "STUDENT_ID": "999",
        }):
            self.assertIn("Name: TestName", app.render_student_info())
            self.assertIn("Student ID: 999", app.render_student_info())

    def test_all_four_student_fields_present(self):
        self.assertEqual(set(app.student_info()), {"Name", "Surname", "Group", "Student ID"})
