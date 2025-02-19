import unittest
from solve_re import find_all_emails, extract_phone_numbers, remove_html_tags, validate_ip_address, split_by_multiple_delimiters

class TestRegexFunctions(unittest.TestCase):

    def test_find_all_emails(self):
        text = "Contact us at support@example.com or sales@example.org. Ignore invalid@com."
        expected = ['support@example.com', 'sales@example.org']
        self.assertEqual(find_all_emails(text), expected)

    def test_extract_phone_numbers(self):
        text = "Call me at (123) 456-7890 or 098-765-4321."
        expected = ['(123) 456-7890', '098-765-4321']
        self.assertEqual(extract_phone_numbers(text), expected)

    def test_remove_html_tags(self):
        html_text = "<html><body><h1>Title</h1><p>Paragraph.</p></body></html>"
        expected = "TitleParagraph."
        self.assertEqual(remove_html_tags(html_text), expected)

    def test_validate_ip_address(self):
        self.assertTrue(validate_ip_address("192.168.1.1"))
        self.assertFalse(validate_ip_address("256.100.50.25"))
        self.assertFalse(validate_ip_address("192.168.1.1.1"))
        self.assertFalse(validate_ip_address("192.168.1"))

    def test_split_by_multiple_delimiters(self):
        text = "apple#banana;orange|grape"
        delimiters = ['#', ';', '|']
        expected = ['apple', 'banana', 'orange', 'grape']
        self.assertEqual(split_by_multiple_delimiters(text, delimiters), expected)

if __name__ == "__main__":
    unittest.main()
