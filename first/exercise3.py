# first_day/exercise3.py

def analizar_titulares ( titulares: list[str]):
    words: set[str]= set()
    for frase in titulares:
        for palabra in frase.split():
            if len(palabra) > 6:
                words.add(palabra.lower())
    
    
    words = sorted(list(words))
    
    print(f"Palabras Relevantes: {words}")
    print(f"Total de palabras: {len(words)}")
    
    

# Example
analizar_titulares([
    "El presidente anuncia nuevas medidas económicas",
    "El ministro de cultura visita la exposición de arte",
    "El alcalde inaugura un nuevo parque en la ciudad"
])