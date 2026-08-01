# Générateur de mots de passe

Générateur de mots de passe en ligne de commande, écrit en Python. Il produit des mots de passe aléatoires et robustes grâce au module secrets. Projet réalisé dans le cadre de mon apprentissage en systèmes, réseaux et sécurité.

## Sécurité

Ce générateur utilise le module `secrets` de Python plutôt que `random`.
Contrairement à `random`, `secrets` fournit un aléatoire cryptographiquement
sûr, adapté à la génération de mots de passe et de jetons : les valeurs
produites ne sont pas prévisibles, même en connaissant le fonctionnement du
programme.

## Fonctionnalités

- Génère un mot de passe aléatoire à partir de lettres et de chiffres
- Longueur configurable en ligne de commande
- à implanter : rajouter des symboles, faciliter l'accès au générateur (interface utilisateur simplifier)

## Prérequis

- Python 3.14.6
- Aucune bibliothèque externe 

## Utilisation

Lancer depuis le terminal :

​```py generator.py            # longueur par défaut (12)
py generator.py -l 20      # mot de passe de 20 caractères​```

## Exemple de sortie

​```
fAH2 ; oWz2RkmZMDmx ; 7YpPSxsxZvie
​```