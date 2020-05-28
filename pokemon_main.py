from pokemon_project import Pokemon, crear_pokemon_id, crear_pokemon_nombre
import json
# Funcion para crear un archivo con los datos del pokemon con Ids de la primera generacion
def primera_generacion(file_name='primera_generacion.json'):
    #pokemones primera generacion
    with open(file_name, 'w') as archivo:
        lista = [{'id': pokemon.id, 'nombre': pokemon.nombre, 'vida': pokemon.vida} for pokemon in [Pokemon(id) for id in range(1,152)]]
        archivo.write(json.dumps(lista))
            
           

if __name__ == '__main__':
    primera_generacion()
    print(primera_generacion)
