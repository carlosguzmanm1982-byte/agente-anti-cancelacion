# =================================
# BASE DE DATOS FICTICIA
# =================================

clientes = {

    "nestor velastegui": {"plan": 350, "fallas": 41, "intermitencias": 6, "facturacion": 8},
    "elian leguizamon": {"plan": 800, "fallas": 48, "intermitencias": 20, "facturacion": 10},
    "yusmari zaldivar": {"plan": 850, "fallas": 25, "intermitencias": 19, "facturacion": 8},
    "zaira almodovar": {"plan": 400, "fallas": 41, "intermitencias": 3, "facturacion": 9},
    "antonella velastegui": {"plan": 450, "fallas": 30, "intermitencias": 16, "facturacion": 11},
    "antonella archundia": {"plan": 500, "fallas": 4, "intermitencias": 7, "facturacion": 10},
    "tadeo montealegre": {"plan": 200, "fallas": 37, "intermitencias": 13, "facturacion": 12},
    "jhoneisy villalobos": {"plan": 600, "fallas": 9, "intermitencias": 19, "facturacion": 3},
    "juliana echenique": {"plan": 200, "fallas": 2, "intermitencias": 15, "facturacion": 5},
    "valeska mendieta": {"plan": 900, "fallas": 5, "intermitencias": 16, "facturacion": 4},
    "romina paniagua": {"plan": 750, "fallas": 3, "intermitencias": 13, "facturacion": 9},
    "juliana villalobos": {"plan": 600, "fallas": 10, "intermitencias": 17, "facturacion": 4},
    "valeska paniagua": {"plan": 650, "fallas": 22, "intermitencias": 12, "facturacion": 4},
    "dante baquedano": {"plan": 150, "fallas": 28, "intermitencias": 4, "facturacion": 5},
    "antonella baquedano": {"plan": 550, "fallas": 31, "intermitencias": 17, "facturacion": 5},
    "dante zaldivar": {"plan": 450, "fallas": 2, "intermitencias": 12, "facturacion": 11},
    "sandro velastegui": {"plan": 550, "fallas": 40, "intermitencias": 14, "facturacion": 2},
    "yusmari villalobos": {"plan": 450, "fallas": 28, "intermitencias": 19, "facturacion": 10},
    "adriel velastegui": {"plan": 150, "fallas": 2, "intermitencias": 14, "facturacion": 2},
    "zaira archundia": {"plan": 750, "fallas": 50, "intermitencias": 14, "facturacion": 7},
    "tadeo baquedano": {"plan": 550, "fallas": 14, "intermitencias": 1, "facturacion": 2},
    "aitana almodovar": {"plan": 550, "fallas": 12, "intermitencias": 9, "facturacion": 2},
    "valentina paniagua": {"plan": 350, "fallas": 50, "intermitencias": 11, "facturacion": 8},
    "ciro carpio": {"plan": 650, "fallas": 48, "intermitencias": 10, "facturacion": 12},
    "ciro montealegre": {"plan": 400, "fallas": 5, "intermitencias": 13, "facturacion": 6},
    "jhoneisy olavarria": {"plan": 50, "fallas": 40, "intermitencias": 17, "facturacion": 12},
    "nestor perez": {"plan": 750, "fallas": 37, "intermitencias": 6, "facturacion": 15},
    "romina rebolledo": {"plan": 900, "fallas": 20, "intermitencias": 7, "facturacion": 14},
    "dante mendieta": {"plan": 950, "fallas": 15, "intermitencias": 19, "facturacion": 14},
    "luca villalobos": {"plan": 400, "fallas": 14, "intermitencias": 12, "facturacion": 5},
    "antonella montealegre": {"plan": 750, "fallas": 10, "intermitencias": 5, "facturacion": 9},
    "adriel villalobos": {"plan": 700, "fallas": 44, "intermitencias": 6, "facturacion": 13},
    "fausto baquedano": {"plan": 750, "fallas": 23, "intermitencias": 3, "facturacion": 7},
    "nestor villalobos": {"plan": 150, "fallas": 50, "intermitencias": 4, "facturacion": 4},
    "aitana leguizamon": {"plan": 550, "fallas": 49, "intermitencias": 2, "facturacion": 15},
    "aitana olavarria": {"plan": 700, "fallas": 6, "intermitencias": 5, "facturacion": 12},
    "valentina carpio": {"plan": 600, "fallas": 28, "intermitencias": 1, "facturacion": 14},
    "sandro mendieta": {"plan": 550, "fallas": 44, "intermitencias": 18, "facturacion": 14},
    "tadeo perez": {"plan": 550, "fallas": 8, "intermitencias": 2, "facturacion": 8},
    "fausto mendieta": {"plan": 800, "fallas": 9, "intermitencias": 6, "facturacion": 14},
    "valentina baquedano": {"plan": 400, "fallas": 21, "intermitencias": 19, "facturacion": 14},
    "nestor montealegre": {"plan": 450, "fallas": 31, "intermitencias": 3, "facturacion": 11},
    "juliana perez": {"plan": 750, "fallas": 23, "intermitencias": 11, "facturacion": 9},
    "valeska archundia": {"plan": 950, "fallas": 31, "intermitencias": 3, "facturacion": 9},
    "juliana archundia": {"plan": 450, "fallas": 7, "intermitencias": 5, "facturacion": 11},
    "zaira echenique": {"plan": 1000, "fallas": 48, "intermitencias": 20, "facturacion": 8},
    "yusmari perez": {"plan": 250, "fallas": 2, "intermitencias": 17, "facturacion": 14},
    "elian rebolledo": {"plan": 250, "fallas": 24, "intermitencias": 12, "facturacion": 14},
    "jhoneisy perez": {"plan": 600, "fallas": 36, "intermitencias": 19, "facturacion": 3},
    "ciro leguizamon": {"plan": 300, "fallas": 18, "intermitencias": 13, "facturacion": 10}

}

print("Clientes cargados:", len(clientes))


# =================================
# TOOL 1
# Buscar cliente
# =================================

def buscar_cliente(nombre):

    nombre = nombre.lower()

    if nombre in clientes:
        return clientes[nombre]

    return "Cliente no encontrado"



# =====================================
# TOOL: Analizar sentimiento
# =====================================

def analizar_sentimiento(texto):

    texto = texto.lower()


    palabras_negativas = [
        "cancelar",
        "quiero irme",
        "molesto",
        "enojado",
        "fastidiado",
        "problema",
        "falla",
        "fallando",
        "lento",
        "malo",
        "pésimo",
        "queja",
        "inconforme",
        "cansado",
        "decepcionado"
    ]


    palabras_positivas = [
        "gracias",
        "excelente",
        "bueno",
        "conforme",
        "satisfecho",
        "feliz"
    ]


    negativos = 0
    positivos = 0


    for palabra in palabras_negativas:
        if palabra in texto:
            negativos += 1


    for palabra in palabras_positivas:
        if palabra in texto:
            positivos += 1


    if negativos >= 2:
        return "negativo"

    elif positivos > negativos:
        return "positivo"

    else:
        return "neutral"




# =====================================
# TOOL: Calcular riesgo
# =====================================

def calcular_riesgo(cliente, sentimiento="neutral"):


    puntos = 0


    # Fallas técnicas
    if cliente["fallas"] >= 40:
        puntos += 40

    elif cliente["fallas"] >= 20:
        puntos += 25


    # Intermitencias
    if cliente["intermitencias"] >= 15:
        puntos += 30

    elif cliente["intermitencias"] >= 8:
        puntos += 15


    # Facturación
    if cliente["facturacion"] >= 10:
        puntos += 25

    elif cliente["facturacion"] >= 5:
        puntos += 15


    # Sentimiento
    if sentimiento == "negativo":
        puntos += 20



    if puntos >= 70:
        return "ALTO"

    elif puntos >= 40:
        return "MEDIO"

    else:
        return "BAJO"




# =====================================
# TOOL: Propuesta de retención
# =====================================

def propuesta_retencion(cliente, riesgo):


    problemas = []


    if cliente["fallas"] >= 30:
        problemas.append("problemas técnicos")


    if cliente["intermitencias"] >= 10:
        problemas.append("inestabilidad del servicio")


    if cliente["facturacion"] >= 8:
        problemas.append("revisión de facturación")



    if riesgo == "ALTO":

        return (
            "Cliente en riesgo alto. "
            "Aplicar atención prioritaria, "
            "revisión técnica urgente y beneficio de retención. "
            "Motivos detectados: "
            + ", ".join(problemas)
        )


    elif riesgo == "MEDIO":

        return (
            "Cliente con riesgo moderado. "
            "Ofrecer seguimiento técnico y optimización del plan. "
            "Motivos: "
            + ", ".join(problemas)
        )


    else:

        return (
            "Cliente estable. "
            "Ofrecer beneficios adicionales para mantener satisfacción."
        )