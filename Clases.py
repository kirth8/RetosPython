print("========================================================================")
print("CLASES Y OBJETOS - RETO 1")
print("Crear una clase Usuario y usarla")
print("========================================================================")

class user:
    def __init__(self, name, lastname, correo, activo):
        self.name = name
        self.lastname = lastname
        self.correo = correo
        self.activo = activo

    def userGet(self):
        print("=============================")
        print("Nombre: ", self.name)
        print("Apellido: ", self.lastname)
        print("Correo: ", self.correo)
        print("Activo: ", self.activo)
        print("=============================")


obj1 = user("Pepo", "Pereira", "pepo@gmail.com", True)
obj2 = user("Andrea", "Pirlo", "andreapirlo@gmail.com", False)

obj1.userGet()
obj2.userGet()