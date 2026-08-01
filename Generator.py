import secrets
import string
import argparse
parser = argparse.ArgumentParser(description="Générateur de mot de passe")
parser.add_argument("-l", "--longueur", type=int, default=12, help="La longueur du mot de passe")
args = parser.parse_args()

alphabet = string.ascii_letters + string.digits
longueur = args.longueur  
password = ""

for i in range(longueur):
    password = password + secrets.choice(alphabet)

print(password) 