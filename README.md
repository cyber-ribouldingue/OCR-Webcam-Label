# OCR-Webcam-Label

Ce projet permet de lire une étiquette à l'aide d'une webcam sur Windows 10.  
Il effectue les opérations suivantes :
1. Capture d'une image depuis la webcam.
2. Extraction du texte présent sur l'étiquette via Tesseract OCR.
3. Enregistrement du texte extrait dans un fichier `extracted_text.txt`.

## Prérequis

- **Python 3.6+**
- **Windows 10**
- **Tesseract OCR** installé et accessible dans le PATH

## Installation et Configuration

1. Cloner ce dépôt :
   ```bash
   git clone https://github.com/<votre-nom-utilisateur>/OCR-Webcam-Label.git
