print("Ahoj")

import imaplib

server = "imap.gmail.com"
moj_mail = "TVOJ_EMAIL"
moje_heslo = "TVOJE_HESLO" (aplikacne heslo)

print("Pripájam sa...")
mail = imaplib.IMAP4_SSL(server)
mail.login(moj_mail, moje_heslo)
print("Pripojený")

mail.select("inbox")
status, data = mail.search(None, "FROM", "adresa@odosielatela.com")

pocet = 0
for num in data[0].split():
    mail.store(num, "+X-GM-LABELS", "\\Trash")
    pocet += 1
print(f"Mazanie dokončené, odstránených správ: {pocet}")

mail.logout()
