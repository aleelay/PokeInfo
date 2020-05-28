import requests


class Pokemon:
    '''
    En este clase se acceda al URL de la API pokemon para poder acceder a la informacion.
    '''
    URL_BASE = 'https://pokeapi.co/api/v2/pokemon/'

    '''
    Esta es una funcion para poder acceder a la informacion de los pokemons mediante su ID o su nombre.
    '''
    def __init__(self, id:int=None, nombre:str=None):
        if nombre:
             self.nombre = nombre
             self.url = '{}/{}/'.format(self.URL_BASE, nombre)
             self.data = self.obtener_data(self.url)
             self.id = data['id']
        if id:
            self.id = id
            self.url = '{}/{}/'.format(self.URL_BASE, id)
            self.data = self.obtener_data(self.url)
            self.nombre = self.data['name']
        self.vida = self.data['stats'][0]['base_stat']
    #Crear string con datos de Pokemon    
    def info(self):
            return "Nombre: {} ID: {}, Vida: {}".format(self.nombre, self.id, self.vida)
        
    def obtener_data(self, url):
        return requests.get(url).json()
        
    def __str__(self):
        return '{:^10}: {:^10} '.format('Nombre Pokemon',self.name)


def crear_pokemon_id(id):
    pokemon = Pokemon(id=id)
    return pokemon

def crear_pokemon_nombre(nombre):
    nombre = int(input("Nombre Pokemon: "))
    pokemon = Pokemon(nombre=nombre)
    return pokemon



