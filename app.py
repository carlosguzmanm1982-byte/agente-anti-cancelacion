import streamlit as st
from agente import responder


st.set_page_config(
    page_title="Agente Anti-Cancelación",
    page_icon="🤖"
)


st.title("🤖 Agente Anti-Cancelación")

st.write(
    "Sistema inteligente para detectar intención de cancelación "
    "y proponer estrategias de retención."
)


cliente = st.text_input(
    "Nombre del cliente"
)


mensaje = st.text_area(
    "Mensaje del cliente",
    placeholder="Ejemplo: quiero cancelar porque estoy molesto..."
)


if st.button("Analizar conversación"):

    if cliente and mensaje:

        with st.spinner(
            "Analizando cliente y generando estrategia..."
        ):

            resultado = responder(
                cliente.lower(),
                mensaje
            )


        st.success("Análisis completado")

        st.subheader("📊 Análisis del cliente")


        datos = resultado["cliente"]


        st.write(
            "👤 Cliente:",
            cliente
        )


        st.write(
            "📡 Plan contratado:",
            datos["plan"]
        )


        st.write(
            "🔧 Fallas registradas:",
            datos["fallas"]
        )


        st.write(
            "📶 Intermitencias:",
            datos["intermitencias"]
        )


        st.write(
            "💳 Problemas de facturación:",
            datos["facturacion"]
        )


        st.write(
            "😊 Sentimiento detectado:",
            resultado["sentimiento"]
        )


        st.write(
            "⚠️ Riesgo de cancelación:",
            resultado["riesgo"]
        )


        st.write(
            "🎯 Estrategia recomendada:",
            resultado["estrategia"]
        )


        st.subheader("🤖 Respuesta del agente")

        st.write(
            resultado["respuesta"]
        )


    else:

        st.warning(
            "Ingrese nombre del cliente y mensaje"
        )