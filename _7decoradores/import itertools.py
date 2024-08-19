import itertools

# count: Genera una secuencia infinita que empieza en 10 y se incrementa de 2 en 2
print("count:")
for i in itertools.count(10, 2):
    print(i)
    if i >= 20:
        break

# cycle: Itera infinitamente sobre la secuencia proporcionada
print("\ncycle:")
counter = 0
for item in itertools.cycle('ABC'):
    print(item)
    counter += 1
    if counter >= 6:
        break

# chain: Une múltiples iteradores en uno solo
print("\nchain:")
for item in itertools.chain('ABC', 'DEF'):
    print(item)

# combinations: Genera todas las combinaciones posibles de una longitud especificada
print("\ncombinations:")
for combo in itertools.combinations('ABCD', 2):
    print(combo)

# permutations: Genera todas las permutaciones posibles de una longitud especificada
print("\npermutations:")
for perm in itertools.permutations('ABC', 2):
    print(perm)

from collections import deque, Counter, OrderedDict, defaultdict, namedtuple

# deque: Cola de doble extremo
print("\ndeque:")
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)

# Counter: Cuenta elementos en una secuencia
print("\nCounter:")
c = Counter('abracadabra')
print(c)

# OrderedDict: Diccionario que mantiene el orden de inserción
print("\nOrderedDict:")
od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3
print(od)

# defaultdict: Diccionario con un valor por defecto para claves inexistentes
print("\ndefaultdict:")
dd = defaultdict(int)
dd['one'] += 1
dd['two'] += 2
print(dd)

# namedtuple: Crea tuplas con nombre
print("\nnamedtuple:")
Point = namedtuple('Point', 'x y')
p = Point(10, 20)
print(p)
print(p.x, p.y)

import operator

# add: Suma dos números
print("add:")
result = operator.add(5, 3)
print(result)

# mul: Multiplica dos números
print("\nmul:")
result = operator.mul(5, 3)
print(result)

# itemgetter: Obtiene el valor de un índice específico en una secuencia
print("\nitemgetter:")
getter = operator.itemgetter(1)
sequence = [1, 2, 3]
print(getter(sequence))

# attrgetter: Obtiene el valor de un atributo específico en un objeto
print("\nattrgetter:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 30)
getter = operator.attrgetter('name')
print(getter(person))

from contextlib import contextmanager, closing, suppress
from urllib.request import urlopen

# contextmanager: Define un gestor de contexto
print("\ncontextmanager:")
@contextmanager
def simple_context_manager():
    print("Entering")
    yield
    print("Exiting")

with simple_context_manager():
    print("Inside")

# closing: Asegura que un recurso se cierre al finalizar
print("\nclosing:")
with closing(urlopen('http://www.python.org')) as page:
    print(page.status)

# suppress: Suprime excepciones específicas
print("\nsuppress:")
with suppress(FileNotFoundError):
    open('nonexistentfile.txt')
    print("File not found error suppressed")

from functools import lru_cache, partial, reduce, wraps

# lru_cache: Memoriza resultados de una función
print("\nlru_cache:")
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# partial: Crea una nueva función con argumentos parcialmente aplicados
print("\npartial:")
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))

# reduce: Aplica una función de manera acumulativa a los elementos de una secuencia
print("\nreduce:")
result = reduce(operator.add, [1, 2, 3, 4])
print(result)

# wraps: Copia metadatos de una función a otra
print("\nwraps:")
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Calling function")
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

import math

# sqrt: Calcula la raíz cuadrada de un número
print("\nsqrt:")
print(math.sqrt(16))

# factorial: Calcula el factorial de un número
print("\nfactorial:")
print(math.factorial(5))

# gcd: Calcula el máximo común divisor de dos números
print("\ngcd:")
print(math.gcd(48, 18))

# log: Calcula el logaritmo natural de un número
print("\nlog:")
print(math.log(10))

import datetime

# date: Representa una fecha
print("\ndate:")
today = datetime.date.today()
print(today)

# time: Representa un tiempo
print("\ntime:")
now = datetime.datetime.now().time()
print(now)

# datetime: Representa una combinación de fecha y tiempo
print("\ndatetime:")
now = datetime.datetime.now()
print(now)

# timedelta: Representa una duración
print("\ntimedelta:")
delta = datetime.timedelta(days=5)
print(now + delta)

import datetime

# date: Representa una fecha
print("\ndate:")
today = datetime.date.today()
print(today)

# time: Representa un tiempo
print("\ntime:")
now = datetime.datetime.now().time()
print(now)

# datetime: Representa una combinación de fecha y tiempo
print("\ndatetime:")
now = datetime.datetime.now()
print(now)

# timedelta: Representa una duración
print("\ntimedelta:")
delta = datetime.timedelta(days=5)
print(now + delta)

import re

# match: Busca una coincidencia al inicio de la cadena
print("\nmatch:")
match = re.match(r'\d+', '123abc')
print(match.group())

# search: Busca una coincidencia en toda la cadena
print("\nsearch:")
search = re.search(r'\d+', 'abc123')
print(search.group())

# findall: Encuentra todas las coincidencias en la cadena
print("\nfindall:")
findall = re.findall(r'\d+', 'abc123def456')
print(findall)

# sub: Reemplaza coincidencias en la cadena
print("\nsub:")
sub = re.sub(r'\d+', 'X', 'abc123def456')
print(sub)

import json

# load: Carga datos desde un archivo JSON
print("\nload:")
json_str = '{"name": "Alice", "age": 25}'
data = json.loads(json_str)
print(data)

# loads: Carga datos desde una cadena JSON
print("\nloads:")
json_str = '{"name": "Alice", "age": 25}'
data = json.loads(json_str)
print(data)

# dump: Escribe datos a un archivo JSON
print("\ndump:")
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
print(json_str)

# dumps: Convierte datos a una cadena JSON
print("\ndumps:")
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
print(json_str)

import os

# listdir: Lista archivos en el directorio actual
print("\nlistdir:")
print(os.listdir('.'))

# mkdir: Crea un directorio
print("\nmkdir:")
os.mkdir('test_dir')
print('Directory created')

# remove: Elimina un archivo
print("\nremove:")
with open('test_file.txt', 'w') as f:
    f.write('test')
os.remove('test_file.txt')
print('File removed')

# path: Manipula rutas de archivos
print("\npath:")
print(os.path.join('dir', 'file.txt'))

import sys

# argv: Argumentos pasados al script desde la línea de comandos
print("\nargv:")
print(sys.argv)

# exit: Finaliza la ejecución del programa
print("\nexit:")
# sys.exit("Exiting program")

# path: Rutas de búsqueda de módulos
print("\npath:")
print(sys.path)

# stdout: Salida estándar
print("\nstdout:")
sys.stdout.write("Hello, stdout!\n")

import logging

# basicConfig: Configura el registro básico
print("\nbasicConfig:")
logging.basicConfig(level=logging.INFO)
logging.info('Este es un mensaje informativo')

# getLogger: Obtiene un logger
print("\ngetLogger:")
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)
logger.debug('Este es un mensaje de depuración')

# info: Registra un mensaje informativo
print("\ninfo:")
logger.info('Este es un mensaje informativo')

# error: Registra un mensaje de error
print("\nerror:")
logger.error('Este es un mensaje de error')
