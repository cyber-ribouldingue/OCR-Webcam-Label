# OCR-Webcam-Label

Ce projet permet de lire une étiquette à l'aide d'une webcam sur un PC Windows 10.  
Il réalise les actions suivantes :  
1. Capture une image depuis la webcam.  
2. Extrait le texte présent sur l'étiquette grâce à Tesseract OCR.  
3. Enregistre le texte extrait dans un fichier `extracted_text.txt`.

## Prérequis

- **Python 3.6+**  
- **Windows 10**

## Installation et Configuration

### 1. Installer Python

Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).  
Pendant l'installation, cochez l'option *Add Python to PATH*.

### 2. Cloner le Dépôt

Ouvrez une invite de commande et clonez ce dépôt :

```bash
git clone https://github.com/<votre-nom-utilisateur>/OCR-Webcam-Label.git
cd OCR-Webcam-Label
