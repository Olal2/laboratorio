import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Lector de archivos", layout='wide')
st.header('Subir archivos CSV o Excel')
archivos = st.file_uploader("Sube uno o más archivos:", type=["csv", "xlsx"], accept_multiple_files=True)

for archivo in archivos:
    nombre = archivo.name
    st.subheader(f"Archivo: {nombre}")
    try:
        if nombre.endswith('.csv'):
            df = pd.read_csv(archivo)
        elif nombre.endswith('.xlsx'):
            df = pd.read_excel(archivo)
        else:
            st.warning(f"Formato no soportado: {nombre}")
            continue

        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error al leer {nombre}: {e}")

#PBI
st.header("Visualizador de Power BI")
tipo_pbi = st.radio("¿Cómo deseas mostrar el archivo de Power BI?", ["Enlace público", "Archivo HTML exportado"])
if tipo_pbi == "Enlace público":
    url = st.text_input("Pega aquí el enlace público del informe de Power BI")
    if url:
        components.iframe(url, height=600, scrolling=True)
elif tipo_pbi == "Archivo HTML exportado":
    archivo_html = st.file_uploader("Sube el archivo HTML exportado de Power BI", type=["html"])
    if archivo_html is not None:
        html_content = archivo_html.read().decode("utf-8")
        components.html(html_content, height=700, scrolling=True)