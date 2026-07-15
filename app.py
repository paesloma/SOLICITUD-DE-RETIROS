import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Generador de Correos de Retiro", page_icon="📦", layout="centered")

st.title("📦 Gestión de Retiros - Postventa")
st.subheader("Complete el formulario para estructurar el correo de retiro")

# --- FORMULARIO DE INGRESO ---
with st.form("formulario_retiro_tecnico"):
    st.write("### 👥 Configuración de Destinatarios")
    col_dest1, col_dest2 = st.columns(2)
    with col_dest1:
        destinatarios_base = st.text_input("Destinatarios (Para)", value="operaciones@empresa.com, finanzas@empresa.com")
    with col_dest2:
        cc_adicionales = st.text_input("En copia (CC)", placeholder="ejemplo@correo.com")

    st.write("---")
    st.write("### 📍 Datos de ORIGEN")
    col_ori1, col_ori2, col_ori3 = st.columns(3)
    with col_ori1:
        origen_ciudad = st.text_input("Ciudad (Origen)", value="")
    with col_ori2:
        origen_nombre = st.text_input("Nombre / Entidad (Origen)", value="")
    with col_ori3:
        origen_contacto = st.text_input("Contacto (Origen)", value="")
    
    col_ori4, col_ori5 = st.columns(2)
    with col_ori4:
        origen_direccion = st.text_input("Dirección (Origen)", value="")
    with col_ori5:
        origen_obs = st.text_input("Observaciones (Origen)", value="")

    st.write("---")
    st.write("### 🎯 Datos de DESTINO")
    col_des1, col_des2, col_des3 = st.columns(3)
    with col_des1:
        destino_ciudad = st.text_input("Ciudad (Destino)", value="CUENCA")
    with col_des2:
        destino_nombre = st.text_input("Nombre / Entidad (Destino)", value="SERVICIO TECNICO")
    with col_des3:
        destino_contacto = st.text_input("Contacto (Destino)", value="Servicio Técnico Motsur Henry Beltrán (07-4134673 ext. 20502)")
    
    col_des4, col_des5 = st.columns(2)
    with col_des4:
        destino_direccion = st.text_input("Dirección (Destino)", value="Gonzalo Diaz de Pineda y juan de Montoya, atrás del coral centro de la Av de las Américas")
    with col_des5:
        destino_obs = st.text_input("Observaciones (Destino)", value="REVISAR QUE EL ARTICULO NO SE ENCUENTRE CON GOLPES")

    # Botón de procesamiento
    procesar = st.form_submit_button("Generar Correo de Retiro")

# --- LÓGICA DE GENERACIÓN ---
if procesar:
    # 1. Construcción de Destinatarios
    destinatarios_finales = destinatarios_base
    if cc_adicionales:
        destinatarios_finales += f" | CC: {cc_adicionales}"

    # 2. Construcción de la Tabla de Texto Plano Alineada
    # Usamos formato de tabla Markdown clásica para que sea fácilmente legible y copiable
    tabla_correo = f"""
| | CIUDAD | NOMBRE | DIRECCION | CONTACTO | OBSERVACIONES |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ORIGEN** | {origen_ciudad if origen_ciudad else "-"} | {origen_nombre if origen_nombre else "-"} | {origen_direccion if origen_direccion else "-"} | {origen_contacto if origen_contacto else "-"} | {origen_obs if origen_obs else "-"} |
| **DESTINO** | {destino_ciudad if destino_ciudad else "-"} | {destino_nombre if destino_nombre else "-"} | {destino_direccion if destino_direccion else "-"} | {destino_contacto if destino_contacto else "-"} | {destino_obs if destino_obs else "-"} |
"""

    # 3. Construcción del Cuerpo del Mensaje Final
    cuerpo_mensaje = f"""Estimado ingeniero.

Su gentil ayuda con el siguiente retiro el articulo:

{tabla_correo}

Agradecido a la atención de la presente

Atentamente 
Ing. Pablo Lopez
Coordinador Postventa 
0995115782"""

    # --- SECCIÓN DE COPIADO ---
    st.success("✅ ¡Correo estructurado con éxito! Copia los bloques de abajo:")
    st.write("---")
    
    # Resultado 1: Destinatarios del correo
    st.write("### 👥 1. Destinatarios")
    st.code(destinatarios_finales, language="text")

    # Resultado 2: Cuerpo del mensaje completo
    st.write("### 📝 2. Cuerpo del Mensaje")
    st.code(cuerpo_mensaje, language="text")
