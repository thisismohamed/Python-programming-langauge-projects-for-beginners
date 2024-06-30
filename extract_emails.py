import re
import requests
from bs4 import BeautifulSoup

def extract_emails(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = set(re.findall(email_regex, str(soup)))

    return sorted(list(emails), key=str.lower)

if __name__ == "__main__":
    url = input("Enter URL to scan for emails: ")
    results = extract_emails(url)
    print(f"Emails found on {url}")
    for email in results:
        print(email)
