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

    # Reemplazo de celdas vacías por espacios para evitar que la tabla se deforme
    o_ciud = origen_ciudad if origen_ciudad else "&nbsp;"
    o_nomb = origen_nombre if origen_nombre else "&nbsp;"
    o_dire = origen_direccion if origen_direccion else "&nbsp;"
    o_cont = origen_contacto if origen_contacto else "&nbsp;"
    o_obse = origen_obs if origen_obs else "&nbsp;"

    d_ciud = destino_ciudad if destino_ciudad else "&nbsp;"
    d_nomb = destino_nombre if destino_nombre else "&nbsp;"
    d_dire = destino_direccion if destino_direccion else "&nbsp;"
    d_cont = destino_contacto if destino_contacto else "&nbsp;"
    d_obse = destino_obs if destino_obs else "&nbsp;"

    # 2. Construcción de la Tabla en HTML Limpio y Compatible con Outlook/Gmail
    tabla_html = f'''
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; font-size: 11pt; border: 1px solid #cccccc; margin: 15px 0;">
    <thead>
        <tr style="background-color: #f2f2f2; text-align: left;">
            <th style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; width: 10%;"></th>
            <th style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; width: 15%;">CIUDAD</th>
            <th style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; width: 15%;">NOMBRE</th>
            <th style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; width: 25%;">DIRECCIÓN</th>
            <th style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; width: 20%;">CONTACTO</th>
            <th style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; width: 15%;">OBSERVACIONES</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; background-color: #f9f9f9;">ORIGEN</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{o_ciud}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{o_nomb}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{o_dire}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{o_cont}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{o_obse}</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cccccc; font-weight: bold; background-color: #f9f9f9;">DESTINO</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{d_ciud}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{d_nomb}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{d_dire}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{d_cont}</td>
            <td style="padding: 8px; border: 1px solid #cccccc;">{d_obse}</td>
        </tr>
    </tbody>
</table>
'''

    # --- SECCIÓN DE RESULTADOS ---
    st.success("✅ ¡Correo generado! Selecciona el texto de abajo directamente con tu cursor para copiarlo:")
    st.write("---")
    
    # Destinatarios (Se mantienen en cuadro de código por facilidad de copia rápida)
    st.write("### 👥 1. Destinatarios")
    st.code(destinatarios_finales, language="text")

    # Cuerpo del Mensaje y Tabla en formato HTML nativo
    st.write("### 📝 2. Cuerpo del Mensaje (Selecciona y copia todo este bloque)")
    
    # Contenedor visual para copiar de forma limpia
    st.markdown(
        f"""
        <div style="background-color: #ffffff; padding: 20px; border: 1px solid #dddddd; border-radius: 5px; color: #000000; font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.5;">
            Estimado ingeniero.<br><br>
            Su gentil ayuda con el siguiente retiro el articulo:<br>
            {tabla_html}
            <br>
            Agradecido a la atención de la presente<br><br>
            Atentamente<br>
            <b>Ing. Pablo Lopez</b><br>
            Coordinador Postventa<br>
            0995115782
        </div>
        """, 
        unsafe_allow_html=True
    )
