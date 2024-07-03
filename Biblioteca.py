print("Bienvedido a la Biblioteca virtual nxa")

import csv
archivo_con_datos = "Biblioteca.csv"

def cargar_datos():
    try:
        with open(archivo_con_datos, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open(archivo_con_datos, 'w', newline='') as file:
        headers = ['titulo','autor', 'genero']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(datos)

def agregar_libros(titulo, autor, genero):
    datos = cargar_datos()
    datos.append({
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
       
    })
    guardar_datos(datos)

def actualizar_libros(index, titulo, autor, genero):
    datos = cargar_datos()
    if 0 <= index < len(datos):
        datos[index] = {
            'titulo': titulo,
             'autor': autor,
             'genero': genero,
        }
        guardar_datos(datos)
    else:
        print("Índice invalido.")

def eliminar_libro (index):
    datos = cargar_datos()
    if 0 <= index < len(datos):
        del datos[index]
        guardar_datos(datos)
    else:
        print("Índice .")
#aki lo k falta 

def main():
    while True:
        print("\nBienvenido al registro de gastos personales")
        print("1. Agregar libro")
        print("2. Actualizar libro")
        print("3. Eliminar libro")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            genero = input("Ingrese el genero del libro: ")
            agregar_libros(titulo, autor, genero)

        
        elif opcion == '2':
            index = int(input("Ingrese el luibro que va a actualizar: "))
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            genero= input("Ingrese el genero del libro: ")
            actualizar_libros(index, titulo, autor, genero)
        
        elif opcion == '3':
            index = int(input("Ingrese el libro a eliminar: "))
            eliminar_libro(index)
        
        
        elif opcion == '4':
          print("Gracias por utilizar la biblioteca virtual. ¡Hasta luego!")
          break
        
    else:
      print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
 
"""if __name__ == "__main__":
    main()"""

        
        
        
       
      
