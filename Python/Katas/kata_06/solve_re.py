import re

def find_all_emails(text: str) -> list:
    """
    TODO: Implement a function that takes a string `text` and returns all valid email addresses found in it.
    Use the `re` module to perform this task.
    """
    # Your implementation here
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails


def extract_phone_numbers(text: str)->list:
    """
    TODO: Implement a function that takes a string `text` and returns all phone numbers in the format 
    (XXX) XXX-XXXX or XXX-XXX-XXXX found in it.
    Use the `re` module to perform this task.
    """
    # Your implementation here
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers


def remove_html_tags(html_text: str)->str:
    """
    TODO: Implement a function that takes a string `html_text` containing HTML content and removes all HTML tags from it.
    The result should only contain the plain text without any tags.
    Use the `re` module to perform this task.
    """
    # Your implementation here
    tag_pattern = r'<[^>]+>'
    plain_text = re.sub(tag_pattern, '', html_text)
    return plain_text


def validate_ip_address(ip:str)->bool:
    """
    TODO: Implement a function that checks if the given string `ip` is a valid IPv4 address.
    Return True if it's valid, otherwise return False.
    Use the `re` module to perform this task.
    """
    # Your implementation here
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ip_pattern, ip):
        parts = ip.split('.')
        for part in parts:
            if int(part) > 255:
                return False
        return True
    return False


def split_by_multiple_delimiters(text: str, delimiters: list)->list:
    """
    TODO: Implement a function that splits the string `text` by multiple delimiters provided in the `delimiters` list.
    Use the `re` module to perform this task.
    """
    # Your implementation here
    pass
