import random

lista = {
    'A': 'Clavel',
    'B': 'Calahua',
    'C': 'Jugo de piña',
    'D': 'Jugo de fresa',
    'E': 'Sprite',
    'F': 'Amper',
    'G': 'Curacao',
    'H': 'Clamato',
    'I': 'Jarabe',
    'J': 'Agua Mineral',
    'K': 'Squirt',
    'L': 'Sangria',
    'M': 'Jugo de limón',
    'N': 'Jugo de naranja',
    'O': 'Jugo de toronja',
    'P': 'Tequila',
    'Q': 'Vodka',
    'R': 'Cerveza',
    'S': 'Menta',
    'T': 'Jugo de mango',
    'U': 'Valentina',
    'V': 'Tamarindo',
}

ingredientes = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V']

def generarReceta():
    return random.sample(ingredientes, len(ingredientes))

def corteAleatorio():
    return random.randint(1, 21)


