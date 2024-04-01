import fitz  # PyMuPDF
from googletrans import Translator

# Chemin vers votre fichier PDF
pdf_path = "C:/Users/RACHAD/Desktop/traduction/Antigone.pdf"

# Fonction pour extraire le texte d'un fichier PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Fonction pour traduire un texte du français vers l'anglais en morceaux
def translate_text_chunks(text_fr, chunk_size=500):
    translator = Translator()
    text_chunks = [text_fr[i:i+chunk_size] for i in range(0, len(text_fr), chunk_size)]
    text_en_chunks = []
    for chunk in text_chunks:
        if chunk.strip():  # Vérifier que le morceau de texte n'est pas vide
            try:
                translation = translator.translate(chunk, src='fr', dest='en')
                if translation:
                    text_en_chunks.append(translation.text)
                else:
                    text_en_chunks.append("Erreur lors de la traduction")
            except Exception as e:
                text_en_chunks.append(f"Erreur : {str(e)}")
        else:
            text_en_chunks.append("Le morceau de texte à traduire est vide")
    return " ".join(text_en_chunks)  # Fusionner les morceaux traduits en un seul texte

# Extraire le texte du fichier PDF
text_fr = extract_text_from_pdf(pdf_path)

# Traduire le texte extrait
text_en = translate_text_chunks(text_fr)

# Chemin du fichier de sortie pour stocker la traduction
output_file_path = "C:/Users/RACHAD/Desktop/traduction/Antigone_en.txt"

# Écrire le texte traduit dans le fichier de sortie
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(text_en)

print("La traduction a été stockée avec succès dans", output_file_path)
