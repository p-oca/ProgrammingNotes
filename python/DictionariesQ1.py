# This script iterates through the email dictionary that contains the domain names as keys and users as values
# which are stored as an array. It then forms a string in the <user>@<domain> format and returns these values
# in an array.

def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return emails


print(email_list({
    "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
    "yahoo.com": ["barbara.gordon", "jean.grey"],
    "hotmail.com": ["bruce.wayne"]
}))
