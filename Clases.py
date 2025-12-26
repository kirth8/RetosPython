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

    def psudoDiccionario(seft):
        return {
            "nombre": seft.name,
            "Apellido": seft.lastname,
            "Correo Electronico": seft.correo,
        }

    @staticmethod
    def from_dict(data):
        return user(data["nombre"], data["Apellido"])


obj1 = user("Pepo", "Pereira", "pepo@gmail.com", True)
obj2 = user("Andrea", "Pirlo", "andreapirlo@gmail.com", False)
obj3 = user("Gordo", "Sheo", "sheo@gmail.com", True)
obj4 = user("Hanie", "Ballena", "hanie@gmail.com", True)

obj1.userGet()
obj2.userGet()
obj3.userGet()
obj4.userGet()

usuarios = [obj1, obj2, obj3, obj4]

print("Lista de usuarios:")
cont = 0
for user in usuarios:
    cont +=1
    print(f"{cont}. {user.name} {user.lastname}")

for user in usuarios:
    print(user.psudoDiccionario())


