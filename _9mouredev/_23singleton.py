"""# #23 PATRONES DE DISEÑO: SINGLETON
> #### Dificultad: Media | Publicación: 03/06/24 | Corrección: 10/06/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**."""


"""
Ejercicio
"""


class Singleton:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

print(singleton1 is singleton2)

"""
Extra
"""


class UserSession:

    _instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email}"

    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None


session1 = UserSession()
print(session1.get_user())
session1.set_user(1, "mouredev", "Brais Moure", "mouredev@gmail.com")
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session3.get_user())