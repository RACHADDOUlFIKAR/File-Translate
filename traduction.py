# -*- coding: utf-8 -*-
 #Tapez la commande : pip install PyMuPDF googletrans==4.0.0-rc1
import fitz  
from googletrans import Translator 


pdf_path = "C:/Users/pc/Desktop/projet_traduction/Antigone.pdf"

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def translate_text_chunks(text_fr, chunk_size=500):
    translator = Translator()
    text_chunks = [text_fr[i:i + chunk_size] for i in range(0, len(text_fr), chunk_size)]
    text_en_chunks = []
    for chunk in text_chunks:
        if chunk.strip():  # Vérifier que le morceau de texte n'est pas vide
            try:
                translation = translator.translate(chunk, src='fr', dest='en')
                if translation.text:
                    text_en_chunks.append(translation.text)
                    print(translation.text)
                else:
                    text_en_chunks.append("Erreur lors de la traduction")
            except Exception as e:
                text_en_chunks.append(f"Erreur : {str(e)}")
        else:
            text_en_chunks.append("Le morceau de texte à traduire est vide")
    return " ".join(text_en_chunks)  # Fusionner les morceaux traduits en un seul texte

text_fr = extract_text_from_pdf(pdf_path)
text_en = ""
try:
    text_en = translate_text_chunks(text_fr)
except Exception as e:
    print(f"Une erreur s'est produite lors de la traduction : {str(e)}")

output_file_path = "C:/Users/pc/Desktop/projet_traduction/Antigone_en.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(text_en)

print("La traduction a été stockée avec succès dans", output_file_path)
