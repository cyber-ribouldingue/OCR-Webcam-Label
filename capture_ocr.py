import cv2
import pytesseract
import os

# Pour Windows : décommentez et modifiez le chemin vers l'exécutable Tesseract si nécessaire
 pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_image(output_path='images/captured_image.jpg'):
    """
    Capture une image via la webcam et la sauvegarde dans le chemin spécifié.
    """
    # Vérifier et créer le dossier images s'il n'existe pas
    if not os.path.exists('images'):
        os.makedirs('images')

    # Ouvrir la webcam (l'index 0 correspond à la première webcam)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erreur : Impossible d'accéder à la webcam.")
        return False

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_path, frame)
        print(f"Image sauvegardée sous {output_path}")
    else:
        print("Erreur : Échec de la capture d'image.")
        cap.release()
        return False

    cap.release()
    return True

def extract_text(image_path='images/captured_image.jpg', lang='fra'):
    """
    Extrait le texte d'une image en utilisant Tesseract OCR.
    """
    img = cv2.imread(image_path)
    if img is None:
        print("Erreur : L'image n'a pas pu être chargée.")
        return ""

    # Conversion en niveaux de gris pour améliorer l'OCR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Optionnel : Appliquer un seuillage pour améliorer la détection
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Extraction du texte avec Tesseract
    text = pytesseract.image_to_string(gray, lang=lang)
    return text

def save_text(text, output_file='extracted_text.txt'):
    """
    Sauvegarde le texte extrait dans un fichier.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Texte extrait sauvegardé dans {output_file}")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")

if __name__ == "__main__":
    # Étape 1 : Capture de l'image
    if capture_image():
        # Étape 2 : Extraction du texte de l'image capturée
        extracted_text = extract_text()
        if extracted_text:
            print("Texte extrait :")
            print(extracted_text)
            # Étape 3 : Sauvegarder le texte extrait dans un fichier
            save_text(extracted_text)
        else:
            print("Aucun texte n'a été extrait.")

