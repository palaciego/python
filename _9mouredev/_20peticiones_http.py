"""# #20 PETICIONES HTTP
> #### Dificultad: Difícil | Publicación: 13/05/24 | Corrección: 20/05/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**."""


import requests

"""
Ejercicio
"""

response = requests.get("https://google.com")
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error con código {response.status_code} al realizar la petición.")

"""
Extra
"""

pokemon = input("Introduce un nombre o número del Pokémon a buscar: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json()
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["height"])
    print("Tipo(s): ")
    for type in data["types"]:
        print(type["type"]["name"])
    print("Juegos:")
    for game in data["game_indices"]:
        print(game["version"]["name"])

    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("Cadena de evolución:")

            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)

            get_evolves(data["chain"])

        else:
            print(f"Error {response.status_code} obteniendo las evoluciones.")
    else:
        print(f"Error {response.status_code} obteniendo las evoluciones.")
else:
    print(f"Error {response.status_code}: Pokémon no encontrado")