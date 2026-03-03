# first_day/exercise2.py

def añadir_libro (d: dict[str, int], titulo: str) -> None:
    d[titulo] = 1
    
def actualizar_existencias (d: dict[str, int], titulo: str, num: int) -> None:
    d[titulo] = num 
    
def promedio_ejemplares (d: dict[str, int]) -> None:
    total: int = 0
    for value in d.values():
        total += value 
        
    total /= len(d)
    
    print(f"Promedio de Ejemplares: {total}")
    
def mostrar_resumen (d: dict[str, int]) -> None:
    empty: list[str] = []
    for name, value in d.items():
        if value <= 0:
            empty.append(name)
            
    for name in empty:
        print(f"Advertencia: {name} está agotado")
        
# Example
inventario = {
    "El Quijote": 7,
    "Don Juan Tenorio": 5,
    "La Celestina": 0
}

añadir_libro(inventario, "El Lazarillo de Tormes")
actualizar_existencias(inventario, "El Quijote", 8)
print(inventario) # Inventario actualizado

promedio_ejemplares(inventario)
mostrar_resumen(inventario)