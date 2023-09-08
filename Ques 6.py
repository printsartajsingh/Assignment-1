n = int(input("Enter the number of students: "))

emails = []
for i in range(n):
    email = input(f"Enter the email ID for student {i+1}: ")
    emails.append(email)
    usernames=[]
    domains=[]

    for email in emails:
        
        parts = email.split('@')
        if len(parts) == 2:
            username, domain = parts
            usernames.append(username)
            domains.append(domain)

    email_tuple=tuple(emails)
    username_tuple=tuple(usernames) 
    domain_tuple=tuple(domains)


print("Email IDs tuple:", email_tuple)
print("Usernames tuple:", username_tuple)
print("Domains tuple:", domain_tuple)