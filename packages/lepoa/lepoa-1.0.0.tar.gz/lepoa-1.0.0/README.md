# LEPOA

Lepoa es un generador de lenguajes de programación transpilados que permite crear nuevos lenguajes de programación que luego serán convertidos en código fuente de otro lenguaje de programación preexistente(lenguaje origen).

## Instalación

Para instalar lepoa, se puede utilizar pip:

`pip install lepoa`


## Uso

### Añadir un nuevo lenguaje

Para añadir un nuevo lenguaje, se utiliza el subcomando `anade`. Este subcomando toma tres argumentos:

- `info_json`: la dirección del archivo info.json del lenguaje
- `keys`: la dirección del archivo keys.json del lenguaje
- `values`: la dirección del archivo values.json del lenguaje

Ejemplo:

`lepoa anade /ruta/a/mi_lenguaje/info.json /ruta/a/mi_lenguaje/keys.json /ruta/a/mi_lenguaje/values.json`


### Traducir un archivo

Para traducir un archivo, se utiliza el subcomando `traduce`. Este subcomando toma dos argumentos:

- `archivo`: la dirección del archivo a traducir
- `lenguaje`: el nombre del lenguaje en el que se desea traducir el archivo (que coincide con el nombre de la carpeta del lenguaje en `lenguajes/` y el cual fue colocado en `info.json`)

Ejemplo:

`lepoa traduce /ruta/a/mi_archivo.py python`

### Traducir un archivo al reves

Para traducir un archivo de forma opuesta, es decir, del lenguaje transpilado a su lenguaje de origen se utiliza el subcomando `reversa`. Este subcomando toma los mismo argumentos que su contraparte `traduce`:

- `archivo`: la dirección del archivo a traducir a su lenguaje origen
- `lenguaje`: el nombre del lenguaje en el que se desea traducir el archivo (que coincide con el nombre de la carpeta del lenguaje en `lenguajes/`)

Ejemplo:

`lepoa reversa /ruta/a/mi_archivo.espy python`

### Especificaciones
Algunas cosas que se deben aclarar para el correcto uso de lepoa son como deben de ser creados algunos archivos:
#### Info.json
este deberá contener:
- `nombre`: el nombre del lenguaje
- `extension-original`: la extension del lenguaje base ya existente
- `extension`: la nueva extension que se usará
- `version`: la version del lenguaje
- `autores`: el nombre de los autores del lenguaje
- `descripcion`: una descripcion del lenguaje

de tal forma que el archivo deberá de verse similar a esto:

```
{
  "nombre": "nombre",
  "extension-original":"rb",
  "extension": "esrb",
  "version": "1.0.0",
  "autores": "Hernandez Barreto Alan Daleth",
  "descrpcion": "ejemplo de descripcion"
}
```
### keys.json
Este json deberá contener las palabras clave del "nuevo lenguaje".

Deberá ser escrito de una forma como esta:

```
[
  "IMPRIME",
  "FIN SI",
  "SI"
]
```
### values.json
Este json deberá de contener las palabras clave del lenguaje original, las palabras deberán estar en el mismo orden que su version traducida(imprimir con print por ejemplo), de tal forma que queden en la misma linea

Este será escrito de la misma manera que su contraparte keys.json:

```
[
  "print",
  "end",
  "if"
]
```
## Contribución

Para contribuir a lepoa, sigue estos pasos:

1. Haz un fork de este repositorio
2. Crea una nueva rama (`git checkout -b mi-rama`)
3. Realiza tus cambios y haz commit (`git commit -am "Agregué una nueva funcionalidad"`)
4. Haz push a la rama (`git push origin mi-rama`)
5. Abre un pull request
