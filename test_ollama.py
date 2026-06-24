import ollama

respuesta = ollama.chat(
    model="gemma4:31b-cloud",
    messages=[
        {
            "role": "user",
            "content": "Dime en una frase qué es inteligencia artificial"
        }
    ]
)

print(respuesta["message"]["content"])