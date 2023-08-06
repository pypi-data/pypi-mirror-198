import argparse
import json
import os
import shutil

def mover_archivos(info_json, archivo1, archivo2):
    # Leer el archivo info.json y obtener el nombre de la carpeta
    with open(info_json, 'r') as info:
        nombre_carpeta = json.load(info)['nombre']
        
    # Obtener la ruta del directorio donde se encuentra lp.py
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la carpeta en el directorio lenguajes
    nueva_carpeta = os.path.join(directorio_actual, 'lenguajes', nombre_carpeta)
    os.makedirs(nueva_carpeta, exist_ok=True)
    
    # Mover los archivos a la nueva carpeta
    shutil.move(archivo1, nueva_carpeta)
    shutil.move(archivo2, nueva_carpeta)
    shutil.move(info_json, nueva_carpeta)

def traduce_archivo(archivo, lenguaje):
    # Obtener la ruta del directorio donde se encuentra lp.py
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Obtener la ruta de los archivos keys.json y values.json
    keys_json = os.path.join(directorio_actual, 'lenguajes', lenguaje, 'keys.json')
    values_json = os.path.join(directorio_actual, 'lenguajes', lenguaje, 'values.json')
    
    # Leer los archivos keys.json y values.json
    with open(keys_json, 'r') as keys_file:
        keys = json.load(keys_file)
    with open(values_json, 'r') as values_file:
        values = json.load(values_file)
    
    # Leer el archivo original y reemplazar las palabras clave
    with open(archivo, 'r') as f:
        contenido = f.read()
        for i in range(len(keys)):
            contenido = contenido.replace(keys[i], values[i])
    
    # Obtener la extensión del archivo a crear desde info.json
    info_json = os.path.join(directorio_actual, 'lenguajes', lenguaje, 'info.json')
    with open(info_json, 'r') as info:
        extension = json.load(info)['extension-original']
    
    # Crear el nombre del archivo a crear
    nombre_archivo, _ = os.path.splitext(os.path.basename(archivo))
    nuevo_nombre_archivo = f"{nombre_archivo}.{extension}"
    
    # Escribir el archivo traducido en la misma ubicación que el original
    with open(os.path.join(os.path.dirname(archivo), nuevo_nombre_archivo), 'w') as f:
        f.write(contenido)

def traduce_al_reves(archivo, lenguaje):
    # Obtener la ruta del directorio donde se encuentra lp.py
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Obtener la ruta de los archivos keys.json y values.json
    keys_json = os.path.join(directorio_actual, 'lenguajes', lenguaje, 'keys.json')
    values_json = os.path.join(directorio_actual, 'lenguajes', lenguaje, 'values.json')
    
    # Leer los archivos keys.json y values.json
    with open(keys_json, 'r') as keys_file:
        keys = json.load(keys_file)
    with open(values_json, 'r') as values_file:
        values = json.load(values_file)
    
    # Crear diccionario de mapeo inverso
    mapeo_inverso = dict(zip(values, keys))
    
    # Leer el archivo traducido y reemplazar las palabras clave para volver al idioma original
    with open(archivo, 'r') as f:
        contenido = f.read()
        for value, key in mapeo_inverso.items():
            contenido = contenido.replace(value, key)
    
    # Obtener la extensión del archivo original desde info.json
    info_json = os.path.join(directorio_actual, 'lenguajes', lenguaje, 'info.json')
    with open(info_json, 'r') as info:
        extension = json.load(info)['extension']
    
    # Crear el nombre del archivo a crear
    nombre_archivo, _ = os.path.splitext(os.path.basename(archivo))
    nuevo_nombre_archivo = f"{nombre_archivo}.{extension}"
    
    # Escribir el archivo traducido al revés en la misma ubicación que el archivo traducido
    with open(os.path.join(os.path.dirname(archivo), nuevo_nombre_archivo), 'w') as f:
        f.write(contenido)


def main():
    # Definir el parser para recibir los parámetros
    parser = argparse.ArgumentParser(prog='lp')
    subparsers = parser.add_subparsers(dest='subcomando')

    # Subcomando "anade"
    parser_anade = subparsers.add_parser('anade')
    parser_anade.add_argument('info_json', type=str, help='Dirección del archivo info.json del lenguaje')
    parser_anade.add_argument('keys', type=str, help='Dirección del archivo keys.json')
    parser_anade.add_argument('values', type=str, help='Dirección del archivo values.json')

    # Subcomando "traduce"
    parser_traduce = subparsers.add_parser('traduce')
    parser_traduce.add_argument('archivo', type=str, help='Dirección del archivo')
    parser_traduce.add_argument('lenguaje', type=str, help='nombre del lenguaje del archivo(info.json)')

    # Subcomando "reversa"
    parser_reversa = subparsers.add_parser('reversa')
    parser_reversa.add_argument('archivo', type=str, help='Dirección del archivo')
    parser_reversa.add_argument('lenguaje', type=str, help='nombre del lenguaje del archivo(info.json)')
    
    
    # Obtener los parámetros y ejecutar la función correspondiente
    args = parser.parse_args()
    if args.subcomando == 'anade':
        mover_archivos(args.info_json, args.keys, args.values)
    elif args.subcomando == 'traduce':
        traduce_archivo(args.archivo, args.lenguaje)
    elif args.subcomando == 'reversa':
        traduce_al_reves(args.archivo, args.lenguaje)
    else:
        print("comando no encontrado")
        
if __name__ == '__main__':
  main()
        #Un generador de lenguajes de programación transpilados que permite crear nuevos lenguajes de programación que luego serán convertidos en código fuente de otro lenguaje de programación preexistente.
        #lepoa anade C:\Users\aland\OneDrive\Escritorio\lp-commad\pruebas\rb\info.json C:\Users\aland\OneDrive\Escritorio\lp-commad\pruebas\rb\keys.json C:\Users\aland\OneDrive\Escritorio\lp-commad\pruebas\rb\values.json
        #lepoa traduce C:\Users\aland\OneDrive\Escritorio\lp-commad\pruebas\rb\uli.esrb esrb
        #lepoa reversa C:\Users\aland\OneDrive\Escritorio\lp-commad\pruebas\rb\uli.rb esrb