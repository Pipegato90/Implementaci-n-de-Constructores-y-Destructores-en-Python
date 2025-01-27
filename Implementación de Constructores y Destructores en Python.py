# Definición de la clase Recurso
class Recurso:
    def __init__(self, nombre):
        """
        Constructor de la clase Recurso.
        Inicializa el recurso con un nombre y simula la apertura del recurso.
        """
        self.nombre = nombre
        print(f"Recurso '{self.nombre}' creado y listo para usar.")

    def usar_recurso(self):
        """
        Método para simular el uso del recurso.
        """
        print(f"Usando el recurso '{self.nombre}'...")

    def __del__(self):
        """
        Destructor de la clase Recurso.
        Se llama automáticamente cuando el objeto es eliminado.
        Simula la liberación o cierre del recurso.
        """
        print(f"Recurso '{self.nombre}' liberado y cerrado correctamente.")


# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre):
        """
        Constructor de la clase Usuario.
        Inicializa un usuario con un nombre y un recurso asignado.
        """
        self.nombre = nombre
        self.recurso_asignado = None
        print(f"Usuario '{self.nombre}' creado.")

    def asignar_recurso(self, recurso):
        """
        Método para asignar un recurso al usuario.
        """
        self.recurso_asignado = recurso
        print(f"Recurso '{recurso.nombre}' asignado al usuario '{self.nombre}'.")

    def usar_recurso(self):
        """
        Método para que el usuario use el recurso asignado.
        """
        if self.recurso_asignado:
            print(f"Usuario '{self.nombre}' está usando el recurso '{self.recurso_asignado.nombre}'.")
            self.recurso_asignado.usar_recurso()
        else:
            print(f"Usuario '{self.nombre}' no tiene ningún recurso asignado.")

    def __del__(self):
        """
        Destructor de la clase Usuario.
        Se llama automáticamente cuando el objeto es eliminado.
        Libera el recurso asignado al usuario.
        """
        if self.recurso_asignado:
            print(f"Usuario '{self.nombre}' está liberando el recurso '{self.recurso_asignado.nombre}'.")
            del self.recurso_asignado
        print(f"Usuario '{self.nombre}' eliminado.")


# Ejemplo de uso del programa
if __name__ == "__main__":
    # Crear un recurso
    archivo = Recurso("Archivo1.txt")

    # Crear un usuario y asignarle el recurso
    usuario = Usuario("Juan")
    usuario.asignar_recurso(archivo)

    # Usar el recurso
    usuario.usar_recurso()

    # Eliminar el usuario (el destructor se llama automáticamente)
    del usuario

    # El recurso también se libera automáticamente cuando el usuario es eliminado