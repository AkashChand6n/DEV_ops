import re
file = input("Enter the dir:")
email_pattern = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}'
with open(file, 'r') as file:
    file_content = file.read()
emails = re.findall(email_pattern, file_content)
if emails:
    print("Email addresses found in the file:")
    for email in emails:
        print(email)
else:
    print("No email addresses found.")
