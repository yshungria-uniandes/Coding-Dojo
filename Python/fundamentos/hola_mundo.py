# Crea un nuevo archivo Python llamado hola_mundo.py

# Escribe el código para imprimir una cadena literal que diga “Hola, mundo” (#1)
print("Hola, mundo")
# Ejecuta el archivo

# Almacena tu nombre en una variable y luego úsala para imprimir la cadena “¡Hola, {{tu nombre}}!” usando una coma en la función print (#2a)
nombre = "Yojan"
# Ejecuta el archivo

# Almacena tu nombre en una variable y luego úsala para imprimir la cadena “¡Hola, {{tu nombre}}!” usando un + en la función print (#2b)
nombre = "Yojan"
print("¡Hola, " + nombre + "!")
# Ejecuta el archivo

# Almacena tu número favorito en una variable y luego úsala para imprimir la cadena “¡Hola, {{num}}!” usando una coma en la función print (#3a)
numero_favorito = 7
print("¡Hola, ",  str(numero_favorito), "!")
# Ejecuta el archivo

# Almacena tu número favorito en una variable y luego úsala para imprimir la cadena “¡Hola, {{num}}!” usando un + en la función print (#3b)
numero_favorito = 7
print("¡Hola, " + str(numero_favorito) + "!")
# Ejecuta el archivo

# BONUS NINJA: descubre cómo resolver el error de arriba, sin cambiar el signo + a una coma
print("¡Hola, " + str(numero_favorito) + "!")

# Almacena dos de tus comidas favoritas en variables y luego úsalas para imprimir la cadena “Amo comer {{comida_uno}} y {{comida_dos}}.” con el método format (#4a)
comida_uno = "Pasta"
comida_dos = "Pizza"
print("Amo comer {} y {}.".format(comida_uno, comida_dos))
# Ejecuta el archivo

# Almacena dos de tus comidas favoritas en variables y luego úsalas para imprimir la cadena “Amo comer {{comida_uno}} y {{comida_dos}}.” con cadenas “f” (#4b)
f"Amo comer {comida_uno} y {comida_dos}."
# Ejecuta el archivo

# BONUS NINJA: Toma unos minutos para jugar con otros métodos de cadena ¡para saber qué hay allá afuera!
nombre = "Yojan"
nombre.lower()
nombre.upper()
nombre.title()
nombre.count("o")
nombre.find("o")
nombre.replace("Y", "J")
nombre.isalpha()
nombre.isdigit()
nombre.isalnum()
nombre.isspace()
nombre.startswith("Y")
nombre.endswith("n")
nombre.split("o")
nombre.join("o")
nombre.strip()
nombre.lstrip()
nombre.rstrip()
nombre.center(20, "-")
nombre.ljust(20, "-")
nombre.rjust(20, "-")
nombre.encode()
nombre.encode("utf-8")
nombre.encode("utf-16")
nombre.encode("utf-32")
nombre.encode("ascii")
nombre.encode("latin-1")
nombre.encode("cp1252")
nombre.encode("cp850")
nombre.encode("cp437")
nombre.partition("o")
nombre.rpartition("o")
nombre.rfind("o")
nombre.rindex("o")
nombre.swapcase()
nombre.translate("o")
nombre.zfill(10)
nombre.casefold()
nombre.expandtabs(10)