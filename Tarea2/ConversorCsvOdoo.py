# Función para generar el XML de Odoo a partir de un archivo CSV
def generar_xml_desde_csv(csv_filename):
    # Abrimos el archivo CSV
    with open(csv_filename, 'r', encoding='utf-8') as archivo_csv:
        # Leemos las líneas del archivo CSV
        lineas = archivo_csv.readlines()

    # Variable para almacenar el XML generado
    xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<data>'

    # Iteramos sobre cada línea (después de la cabecera)
    for idx, linea in enumerate(lineas[1:], start=1):  # Comienza desde la línea 1, omitiendo el encabezado
        # Limpiamos la línea de saltos de línea y dividimos los campos por coma
        campos = linea.strip().split(',')

        # Asignamos los valores de cada columna a las variables correspondientes
        nombre = campos[0]
        director = campos[1]
        actores = campos[2]
        fecha_lanzamiento = campos[3]
        pais = campos[4]
        duracion = campos[5]
        calificacion = campos[6]
        archivo_imagen = campos[7]

        # Procesamos los actores: se espera que los actores estén separados por guiones (-)
        actores_lista = actores.split('-')
        actores_refs = [f"ref('{actor}')" for actor in actores_lista]  # Generamos las referencias de actores

        # Generamos un ID único para cada película (en este caso, simplemente usamos el índice del bucle)
        id_pelicula = f"film_{idx}"

        # Creamos el XML para esta película.
        xml_output += f"""
<record id="{id_pelicula}" model="videoclub.peliculas">
  <field name="name">{nombre}</field>
  <field name="director" ref="{director}" />
  <field name="actors" eval="[(6,0,[{', '.join(actores_refs)}])]" />
  <field name="release">{fecha_lanzamiento}</field>
  <field name="country">{pais}</field>
  <field name="duration">{duracion}</field>
  <field name="rating">{calificacion}</field>
  <field file="{archivo_imagen}" name="cover" type="base64" />
</record>
"""

    # Cerramos el contenedor raíz
    xml_output += "\n</data>"

    return xml_output

# Nombre del archivo CSV
csv_filename = 'pelicula.csv'

# Llamamos a la función y obtenemos el XML generado
xml_resultado = generar_xml_desde_csv(csv_filename)

# Guardamos el resultado en un archivo XML
with open('peliculas.xml', 'w', encoding='utf-8') as archivo_xml:
    archivo_xml.write(xml_resultado)

print("XML generado exitosamente y guardado como 'peliculas.xml'")
