import secrets
import string
import argparse
parser = argparse.ArgumentParser(description="Générateur de mot de passe")
parser.add_argument("-l", "--longueur", type=int, default=12, help="La longueur du mots de passe")
parser.add_argument("-s", "--symboles", action="store_true", help="Rajout de symbole dans le mots de passe")
args = parser.parse_args()

alphabet = string.ascii_letters + string.digits
longueur = args.longueur 
password = ""

if args.symboles:
    alphabet += string.punctuation

for i in range(longueur):
    password = password + secrets.choice(alphabet)

print(password) 