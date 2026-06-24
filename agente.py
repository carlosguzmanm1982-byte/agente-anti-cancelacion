import ollama

from tools import (
    analizar_sentimiento,
    calcular_riesgo,
    buscar_cliente,
    propuesta_retencion
)


def responder(nombre_cliente, mensaje):

    # Buscar datos del cliente
    cliente = buscar_cliente(nombre_cliente)


    # Validar si existe
    if cliente == "Cliente no encontrado":
        return "No encontré información del cliente."


    # Analizar sentimiento
    sentimiento = analizar_sentimiento(mensaje)


    # Calcular riesgo
    riesgo = calcular_riesgo(
    cliente,
    sentimiento
    )


    # Obtener estrategia
    estrategia = propuesta_retencion(
    cliente,
    riesgo
    )


    prompt = f"""

Eres un Agente Anti-Cancelación.

Tu objetivo es reducir la cancelación del servicio.

Información del cliente:

Cliente:
{nombre_cliente}

Plan contratado:
{cliente['plan']}

Historial:
Fallas:
{cliente['fallas']}

Intermitencias:
{cliente['intermitencias']}

Problemas de facturación:
{cliente['facturacion']}


Análisis automático:

Sentimiento del cliente:
{sentimiento}

Nivel de riesgo:
{riesgo}

Estrategia recomendada:
{estrategia}


Mensaje del cliente:

{mensaje}


Instrucciones:

1. Responde con empatía.
2. No contradigas al cliente.
3. Reconoce su problema.
4. Explica una solución.
5. Propón una alternativa para evitar la cancelación.
6. Termina con una invitación a continuar.


"""


    respuesta = ollama.chat(
        model="gemma4:31b-cloud",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return {
    "respuesta": respuesta["message"]["content"],
    "sentimiento": sentimiento,
    "riesgo": riesgo,
    "estrategia": estrategia,
    "cliente": cliente
}