# first_day/exercise1.py

def clasificar_temperaturas(days: list[int]) -> None:
    cold = [x for x in days if x < 15]
    mild = [x for x in days if (x >= 15 and x <= 25)]
    hot = [x for x in days if x > 25]
    
    maximum = max(days)
    minimum = min(days)
    
    print(f"Frios: {cold}\n \
        Templados: {mild}\n \
        Calurosos: {hot}\n \
        Máxima: {maximum} ºC\n \
        Mínima: {minimum} ºC")
    
# Example
clasificar_temperaturas([12, 14, 25, 30, 20, 28])
