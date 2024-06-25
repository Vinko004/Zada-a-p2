import re

#ovdje provjeravamo mail
email_regex = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'

#Ovdje provjeravamo eduid
eduId_regex = r'^[a-zA-Z]+\.[a-zA-Z]+@sum\.ba$'

#3 - 7 koristim AI

# Ovdje od korisnika trazimo da unese email i duide
email=input("Molimo unesite e.mail: ")
eduId=input("Molimo unesite  eduId: ")


if re.match(email_regex, email):
    print("e-mail je ispravan!")
else:
    print("e-mail nije ispravan!")

if re.match(eduId_regex, eduId):
    print("eduId je ispravan!")
else:
    print("eduId nije ispravan!")