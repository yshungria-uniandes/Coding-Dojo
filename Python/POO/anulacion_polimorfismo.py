class Padre:
    def method_a(self):
        print("invocando método_a PADRE")
class Hijo(Padre):
    def method_a(self):
        print("invocando método_a HIJO")
papá = Padre()
hijo = Hijo()
papá.method_a()
hijo.method_a() # Nota que esto anula el método Padre



# utilizaremos la clase Persona para demostrar polimorfismo
# en el que varias clases heredan de la misma clase pero se comportan de diferentes maneras
class Persona:
  def pagar_cuenta(self):
      raise NotImplementedError
# Millonario hereda de Persona
class Millonario(Persona):
  def pagar_cuenta(self):
      print("Aquí tienes. Quédate con el cambio.")
# Estudiante de posgrado también hereda de la clase Persona
class EstudiantePosgrado(Persona):
  def pagar_cuenta(self):
      print("¿Puedo deberle diez dólares o lavar los platos?")

# Según este ejemplo, un millonario y un estudiante de posgrado son Personas. Sin embargo, cuando se trata de pagar una cuenta, la forma en que actúan es bastante diferente. Este patrón es útil cuando sabes que cada subclase de una clase principal debe definir un comportamiento específico en un método y no quieres definir un comportamiento predeterminado en la clase principal (de ahí la implementación virtual pura en la principal). 

yojan = Millonario()

estudiante = EstudiantePosgrado()

yojan.pagar_cuenta()

estudiante.pagar_cuenta()