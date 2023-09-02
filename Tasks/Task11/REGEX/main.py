import re

file_path = "C:\\Users\\pc\\Documents\\GitHub\\AI_Diploma_Tasks\\Tasks\\Task11\\REGEX\\Test.txt"
file = open(file_path, 'r')

file_contents = file.read()
file.close()

email_pattern = re.compile(r"[a-zA-Z0-9-.]+@[a-zA-Z-]+\.\w{3}")
email_matches = email_pattern.finditer(file_contents)

phone_number_pattern = re.compile(r"01[0|1|2|5]+\d{8}")
phone_number_matches = phone_number_pattern.finditer(file_contents)

DOB_pattern = re.compile(r"\d{2}[-/]\d{2}[-/]\d{4}")
DOB_matches = DOB_pattern.finditer(file_contents)

for match in email_matches:
    print(match)

for match in phone_number_matches:
    print(match)

for match in DOB_matches:
    print(match)
