
import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)

        elif tag == "input":
            self.inputs.append(attrs)

        elif tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html = Path("index.html").read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(html)

    def test_form_exists(self):
        self.assertTrue(self.parser.forms, "Form is missing")

    def test_name_field_exists(self):
        self.assertTrue(any(
            i.get("name") == "name"
            and i.get("type") == "text"
            for i in self.parser.inputs
        ), "Name field is missing")

    def test_email_field_exists(self):
        self.assertTrue(any(
            i.get("name") == "email"
            and i.get("type") == "email"
            for i in self.parser.inputs
        ), "Email field is missing")

    def test_contact_field_exists(self):
        self.assertTrue(any(
            i.get("name") == "contact"
            and i.get("type") == "tel"
            for i in self.parser.inputs
        ), "Contact field is missing")

    def test_required_fields(self):
        for field in ("name", "email", "contact"):
            with self.subTest(field=field):
                self.assertTrue(any(
                    i.get("name") == field
                    and "required" in i
                    for i in self.parser.inputs
                ), f"{field} must be required")

    def test_submit_button_exists(self):
        self.assertTrue(any(
            b.get("type") == "submit"
            for b in self.parser.buttons
        ), "Submit button is missing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
