
# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly
cybersecurity project developed using Python.

Its purpose is to identify selected warning signs in a URL
that may indicate suspicious characteristics.

The program examines URL text only. It does not visit websites,
open links, or send information over the internet.

## 2. Project Objectives

- Understand common URL warning signs.
- Learn basic Python programming.
- Practice defensive cybersecurity concepts.
- Develop a simple URL inspection tool.

## 3. Features

The checker looks for six warning signs:

1. The URL contains an @ symbol.
2. The URL is longer than 100 characters.
3. The hostname is an IP address.
4. The hostname contains five or more sections.
5. The hostname contains the punycode marker xn--.
6. The URL uses HTTP instead of HTTPS.

The program also allows users to check multiple URLs
until they type exit.

## 4. Technologies Used

- Python 3.10 or later
- Python standard library
- Command Prompt (CMD)
- Windows operating system

## 5. Requirements

Python 3.10 or later is required.

No external Python packages or API keys are needed.

## 6. How to Run the Project

1. Download or clone this repository.
2. Open the project folder.
3. Open Command Prompt in that folder.
4. Run this command:

   python phishing_checker.py

5. Enter a URL when prompted.
6. Type exit to close the program.

## 7. Example Output

Input:

https://www.example.com/login

Output:

No listed warning signs were detected.

Important: This tool does not prove whether a URL is safe.
It only checks the URL text for selected warning signs.

## 8. Testing

The program is tested using five fictional sample URLs
provided in the project workbook.

See tests/test_samples.md for the test cases and results.

## 9. Improvements Included

- Repeat checking: Users can check multiple URLs without
  restarting the program.
- Warning explanations: The program displays a separate
  message for each detected warning sign.

## 10. Limitations

- The tool examines URL text only.
- It does not visit or verify websites.
- It cannot guarantee that a URL is safe or malicious.
- HTTPS alone does not prove that a website is trustworthy.
- Some suspicious URLs may not trigger any of the six checks.

## 11. Ethical Use

This project is intended only for cybersecurity education
and defensive awareness.

Only fictional sample URLs from the workbook are used
for testing.

The program does not scan websites or access user data.

## 12. Author

Created as a beginner cybersecurity learning project.
