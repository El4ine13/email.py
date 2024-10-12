import re

def validar_email_com_subdominio(email):

    padrao_email = r'^\w+@[\w.-]+\.\w{2,}$'
    
    if re.match(padrao_email, email):
        return True
    else:
        return False

emails_exemplo = [
    "usuario@dominio.com",
    "usuario@sub.dominio.com",
    "usuario@sub.sub.dominio.com",
    "usuario@dominio",
    "usuario@dominio.c",
]

for email in emails_exemplo:
    if validar_email_com_subdominio(email):
        print(f"'{email}' é um e-mail válido.")
    else:
        print(f"'{email}' é um e-mail inválido.")
