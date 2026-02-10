import unicodedata # Para eliminar acentos de caracteres

# VARIABLES GLOBALES
nombres_txt_1 = []
nombres_txt_2 = []

# FUNCIONES
# Normaliza nombre: elimina acentos, convierte a minúsculas y ordena palabras
def normalizar_nombre(nombre_completo):
    # Convertir a minúsculas
    nombre_minusculas = nombre_completo.lower()
    
    # Eliminar acentos manteniendo letras base
    nombre_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', nombre_minusculas) if unicodedata.category(c) != 'Mn')
    
    # Separar en palabras, ordenar alfabéticamente y unir
    palabras = nombre_sin_acentos.split()
    
    palabras_ordenadas = sorted(palabras)
    
    nombre_ordenado = ' '.join(palabras_ordenadas)
    
    return nombre_ordenado

# Carga y normaliza nombres desde archivo .txt
def cargar_nombres_desde_archivo(ruta_archivo):
    nombres_cargados = []
    
    try:
        # Abrir archivo en modo lectura con codificación UTF-8
        with open(ruta_archivo, 'r', encoding = 'utf-8') as archivo:
            # Leer todas las líneas del archivo
            lineas_archivo = archivo.readlines()
        
        # Procesar cada línea: limpiar espacios y filtrar líneas vacías
        for linea in lineas_archivo:
            nombre_limpio = linea.strip()
            
            if nombre_limpio: # Verificar que la línea no esté vacía
                nombres_cargados.append(nombre_limpio)
    
    except FileNotFoundError:
        print("Archivo no encontrado")
        
        return []
    except Exception as e:
        print("Error al leer archivo")
        
        return []
    
    return nombres_cargados

# Compara dos listas de nombres y encuentra diferencias
def comparar_listas_nombres(lista_1, lista_2):
    # Normalizar nombres en ambas listas (sin acentos, minúsculas, ordenados)
    nombres_normalizados_1 = [normalizar_nombre(nombre) for nombre in lista_1]
    nombres_normalizados_2 = [normalizar_nombre(nombre) for nombre in lista_2]
    
    # Crear conjuntos para comparación eficiente
    conjunto_1 = set(nombres_normalizados_1)
    conjunto_2 = set(nombres_normalizados_2)
    
    # Encontrar nombres que están en lista_2 pero no en lista_1
    nombres_faltantes_en_1 = []
    
    for nombre_original, nombre_normalizado in zip(lista_2, nombres_normalizados_2):
        if nombre_normalizado not in conjunto_1:
            nombres_faltantes_en_1.append(nombre_original)
    
    # Encontrar nombres que están en lista_1 pero no en lista_2
    nombres_faltantes_en_2 = []
    
    for nombre_original, nombre_normalizado in zip(lista_1, nombres_normalizados_1):
        if nombre_normalizado not in conjunto_2:
            nombres_faltantes_en_2.append(nombre_original)
    
    return nombres_faltantes_en_1, nombres_faltantes_en_2

# BUCLE PRINCIPAL
while True:
    # CARGAR PRIMER ARCHIVO .TXT
    while True:
        ruta_txt_1 = input("Ingresa ruta del primer archivo .txt: ").strip('"\'')
        
        nombres_txt_1 = cargar_nombres_desde_archivo(ruta_txt_1)
        
        if nombres_txt_1:
            break # Archivo cargado exitosamente
        else:
            print("Archivo vacío o no válido\n")
    
    # CARGAR SEGUNDO ARCHIVO .TXT
    while True:
        ruta_txt_2 = input("Ingresa ruta del segundo archivo .txt: ").strip('"\'')
        
        nombres_txt_2 = cargar_nombres_desde_archivo(ruta_txt_2)
        
        if nombres_txt_2:
            break # Archivo cargado exitosamente
        else:
            print("Archivo vacío o no válido\n")
    
    # COMPARAR LISTAS
    faltantes_en_1, faltantes_en_2 = comparar_listas_nombres(nombres_txt_1, nombres_txt_2)
    
    # MOSTRAR RESULTADOS
    print("-" * 50)
    
    # Mostrar nombres que están en el segundo archivo pero no en el primero
    if faltantes_en_1:
        print("Nombres en el SEGUNDO archivo que NO están en el PRIMERO:")
        
        for indice, nombre in enumerate(faltantes_en_1, 1):
            print(f"{indice}. {nombre}")
    else:
        print("Todos los nombres del segundo archivo están en el primero")
    
    print("-" * 30)
    
    # Mostrar nombres que están en el primer archivo pero no en el segundo
    if faltantes_en_2:
        print("Nombres en el PRIMER archivo que NO están en el SEGUNDO:")
        
        for indice, nombre in enumerate(faltantes_en_2, 1):
            print(f"{indice}. {nombre}")
    else:
        print("Todos los nombres del primer archivo están en el segundo")
    
    print("-" * 50 + "\n")
    
    # PREGUNTAR SI CONTINUAR
    respuesta = input("¿Comparar otros archivos? (s/n): ").strip().lower()
    
    if respuesta != 's':
        break
