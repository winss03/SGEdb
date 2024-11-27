# Definir la clase Persona
class Persona:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"


# Definir la clase Contacto, que hereda de Persona
class Contacto(Persona):
    def __init__(self, nombre, apellido, email, telefono, direccion):
        super().__init__(nombre, apellido, email)
        self.telefono = telefono
        self.direccion = direccion
    
    def __str__(self):
        return f"{super().__str__()} - Teléfono: {self.telefono}, Dirección: {self.direccion}"


# Definir la clase Agenda
class Agenda:
    def __init__(self):
        self.contactos = []

    def alta_contacto(self, nombre, apellido, email, telefono, direccion):
        """Añadir un contacto a la agenda."""
        for contacto in self.contactos:
            if contacto.email == email:
                print(f"Ya existe un contacto con el email: {email}")
                return
        nuevo_contacto = Contacto(nombre, apellido, email, telefono, direccion)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nuevo_contacto.nombre} añadido exitosamente.")
    
    def baja_contacto(self, email):
        """Eliminar un contacto de la agenda por su email."""
        for contacto in self.contactos:
            if contacto.email == email:
                self.contactos.remove(contacto)
                print(f"Contacto {contacto.nombre} eliminado exitosamente.")
                return
        print("Contacto no encontrado.")
    
    def modificar_contacto(self, email, nuevo_telefono=None, nueva_direccion=None):
        """Modificar los detalles de un contacto."""
        for contacto in self.contactos:
            if contacto.email == email:
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                if nueva_direccion:
                    contacto.direccion = nueva_direccion
                print(f"Contacto {contacto.nombre} modificado exitosamente.")
                return
        print("Contacto no encontrado.")
    
    def listado_contactos(self, archivo_html="listado_contactos.html"):
        """Generar un archivo HTML con la lista de contactos."""
        if not self.contactos:
            with open(archivo_html, 'w', encoding='utf-8') as f:
                f.write("<html><body><h1>No hay contactos en la agenda.</h1></body></html>")
            return
        
        html = "<html><body><h1>Listado de Contactos</h1><table border='1'><tr><th>Nombre</th><th>Email</th><th>Teléfono</th><th>Dirección</th></tr>"
        for contacto in self.contactos:
            html += f"<tr><td>{contacto.nombre} {contacto.apellido}</td><td>{contacto.email}</td><td>{contacto.telefono}</td><td>{contacto.direccion}</td></tr>"
        html += "</table></body></html>"

        with open(archivo_html, 'w') as f:
            f.write(html)
        print(f"Listado de contactos guardado en {archivo_html}.")
    
    def buscar_contacto(self, nombre):
        """Buscar un contacto por nombre."""
        encontrados = [contacto for contacto in self.contactos if nombre.lower() in contacto.nombre.lower()]
        if encontrados:
            for contacto in encontrados:
                print(contacto)
        else:
            print("No se encontraron contactos con ese nombre.")


# Crear instancia de la agenda y agregar contactos de ejemplo
agenda = Agenda()

# Añadir algunos contactos de ejemplo
agenda.alta_contacto("Juan", "Pérez", "juan.perez@email.com", "555-1234", "Calle Falsa 123")
agenda.alta_contacto("Ana", "Gómez", "ana.gomez@email.com", "555-5678", "Avenida Real 456")
agenda.alta_contacto("Carlos", "López", "carlos.lopez@email.com", "555-8765", "Calle Luna 789")
agenda.alta_contacto("Laura", "Martínez", "laura.martinez@email.com", "555-0000", "Calle Sol 101")
agenda.alta_contacto("Pedro", "Sánchez", "pedro.sanchez@email.com", "555-4321", "Calle Agua 202")


# Función para mostrar el menú y procesar las opciones
def mostrar_menu():
    while True:
        print("\n--- MENÚ AGENDA DE CONTACTOS ---")
        print("1. Alta de contacto")
        print("2. Baja de contacto")
        print("3. Modificación de contacto")
        print("4. Listado de contactos")
        print("5. Buscar contacto")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            agenda.alta_contacto(nombre, apellido, email, telefono, direccion)
        
        elif opcion == '2':
            email = input("Ingrese el email del contacto a eliminar: ")
            agenda.baja_contacto(email)
        
        elif opcion == '3':
            email = input("Ingrese el email del contacto a modificar: ")
            nuevo_telefono = input("Nuevo teléfono (deje en blanco para no modificar): ")
            nueva_direccion = input("Nueva dirección (deje en blanco para no modificar): ")
            agenda.modificar_contacto(email, nuevo_telefono if nuevo_telefono else None, nueva_direccion if nueva_direccion else None)
        
        elif opcion == '4':
            archivo_html = input("Ingrese el nombre del archivo HTML (por defecto: listado_contactos.html): ")
            if not archivo_html:
                archivo_html = "listado_contactos.html"
            agenda.listado_contactos(archivo_html)
        
        elif opcion == '5':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            agenda.buscar_contacto(nombre)
        
        elif opcion == '6':
            print("Saliendo de la agenda.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")


# Llamar a la función para mostrar el menú
mostrar_menu()
