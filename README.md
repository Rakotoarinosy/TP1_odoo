# TP1 Odoo - Vente Extension  

Ce repository contient une extension personnalisée pour le module **Ventes** d'Odoo. Ce projet a été réalisé dans le cadre du TP1 et vise à enrichir les fonctionnalités existantes du module standard de gestion des ventes.  

## Structure du Projet  

La structure du projet doit respecter l'organisation suivante :  

```bash  
odoo/  
├── addons/                  # Modules standard d'Odoo  
├── custom_addons/           # Extensions et modules personnalisés  
│   └── vente_extension/     # Module personnalisé du TP1  
├── debian/                  # Fichiers de configuration Debian  
├── doc/                     # Documentation du projet  
├── odoo/                    # Source principale d'Odoo  
├── odoo-bin                 # Script de lancement d'Odoo  
├── requirements.txt         # Dépendances Python nécessaires  
├── setup.py                 # Script d'installation du projet  
├── setup.cfg                # Configuration de l'installation  
├── MANIFEST.in              # Liste des fichiers à inclure dans la distribution  
├── SECURITY.md              # Notes de sécurité  
├── CONTRIBUTING.md          # Guide de contribution  
├── LICENSE                  # Licence du projet  
├── README.md                # Présentation et instructions du projet  
├── venv/                    # Environnement virtuel Python  
└── file.conf                # Fichier de configuration personnalisé  

## Détails Techniques  

- **Version de Python** : 3.11+  
- **Version d'Odoo** : V17  
- **Version de PostgreSQL** : 12  

## Fonctionnalité : Vente Extension  

Le module **vente_extension** est une extension personnalisée du module **Ventes** d'Odoo. Voici ce qu’il offre :  

- **Amélioration de la gestion des ventes** :  
  - Ajout de nouvelles fonctionnalités pour mieux gérer les flux de vente.  

- **Personnalisation des vues** :  
  - Nouvelles interfaces utilisateur adaptées aux besoins spécifiques.  

- **Sécurité améliorée** :  
  - Gestion fine des accès via des règles de sécurité personnalisées.  

## Installation  

1. **Clonez le repository** :  
   ```bash  
   git clone https://github.com/Rakotoarinosy/TP1_odoo.git  
## Installation  

2. **Assurez-vous que les modules personnalisés se trouvent dans `custom_addons/`.**  

3. **Activez l'environnement virtuel** :  
   ```bash  
   source venv/bin/activate 

4. Lancez Odoo :

./odoo-bin -d <nom_de_base> -u vente_extension  


## Utilisation

    Après l'installation, vous pouvez accéder à la nouvelle fonctionnalité via le module Ventes.
    Les nouvelles vues et règles de sécurité seront automatiquement appliquées.

## Remerciements

Merci pour votre intérêt pour ce projet. N’hésitez pas à ouvrir des issues ou à proposer des améliorations via des pull requests.
