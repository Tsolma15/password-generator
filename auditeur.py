import string
import argparse
import getpass

courants = ["password", "123456", "azerty", "qwerty", "motdepasse", "admin", "000000"]

parser = argparse.ArgumentParser(description="Auditeur de mot de passe")
parser.add_argument("-m", "--motdepasse", default=None, help="Entrez votre mot de passe à auditer : ")
args = parser.parse_args()

mot_de_passe = args.motdepasse
score = 0

if mot_de_passe is None:
    mot_de_passe = getpass.getpass("Entrez le mot de passe à auditer : ")

if mot_de_passe.lower() in courants:
    print("Votre mot de passe est courant, veuillez le modifier")
    exit()

if len(mot_de_passe) >= 12:
    score += 1
    
if any(caracter.isupper() for caracter in mot_de_passe):
    score += 1
if any(caracter.islower() for caracter in mot_de_passe):
    score += 1
if any(caracter.isdigit() for caracter in mot_de_passe):
    score += 1
if any(caracter in string.punctuation for caracter in mot_de_passe):
    score += 1

if score >= 4:
    print("Votre mot de passe est fort")
elif score == 3:
    print("Votre mot de passe est moyen")
else:
    print("Votre mot de passe est faible")
