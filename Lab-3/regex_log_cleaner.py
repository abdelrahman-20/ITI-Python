# 2) Regex Log Cleaner
#    - Create a file called "access.log" with 10 fake log lines
#      (mix valid emails and invalid strings).
#    - Use regex to extract all valid emails.
#    - Save them into "valid_emails.txt".
#    - Print how many unique emails were found.

import re


def regex_log_cleaner():
    with open("access.log", "w") as f:
        # Ai Generated Fake Data To Clear:
        f.writelines(
            [
                "User login: john.doe@example.com\n",
                "Invalid attempt: notanemail@@example..com\n",
                "Contact: alice_123@gmail.com\n",
                "Test entry: hello world\n",
                "Support: support@my-site.org\n",
                "Another bad: user#mail.com\n",
                "Admin: admin@company.co\n",
                "Message: just_a_string\n",
                "Signup: new.user@domain.net\n",
                "Fake: email@invalid,com\n",
            ]
        )
        f.close()

    # Regex For Valid Emails
    pattern = r"[a-zA-Z0-9._%]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    valid_emails = set()

    # Reading File Data And Extracting Valid Emails
    with open("access.log", "r") as f:
        for line in f:
            match = re.findall(pattern, line)
            valid_emails.update(match)
        f.close()

    # Save Valid Emails Into "valid_emails.txt"
    with open("valid_emails.txt", "w") as f:
        for email in valid_emails:
            f.write(email + "\n")
        f.close()

    # Print Unique Emails Found:
    print(f"Found {len(valid_emails)} unique valid emails.")
    for email in valid_emails:
        print(email)


if __name__ == "__main__":
    regex_log_cleaner()
