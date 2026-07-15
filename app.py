import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Generador de Correos de Retiro", page_icon="💰", layout="centered")

st.title("💰 Gestión de Procesos de Retiros")
st.subheader("Complete el formulario para generar el correo de notificación")

# --- FORMULARIO DE INGRESO ---
with st.form("formulario_retiro"):
    st.write("### Datos del Cliente y Retiro")
    
    col1, col2 = st.columns(2)
    with col1:
        nombre_cliente = st.text_input("Nombre Completo del Cliente", placeholder="Ej. Juan Pérez")
        identificacion = st.text_input("Documento de Identidad", placeholder="Ej. 1712345678")
    with col2:
        monto = st.number_input("Monto a Retirar ($)", min_value=0.0, step=10.0, format="%.2f")
        motivo = st.selectbox("Motivo del Retiro", [
            "Cierre de Cuenta",
            "Retiro Parcial de Fondos",
            "Excedente de Garantía",
            "Error en Depósito / Devolución"
        ])

    st.write("### Detalles Bancarios de Destino")
    col3, col4, col5 = st.columns(3)
    with col3:
        banco = st.text_input("Institución Financiera / Banco", placeholder="Ej. Banco Pichincha")
    with col4:
        tipo_cuenta = st.selectbox("Tipo de Cuenta", ["Ahorros", "Corriente"])
    with col5:
        numero_cuenta = st.text_input("Número de Cuenta")

    st.write("### Configuración de Destinatarios")
    # Destinatarios predefinidos según el flujo administrativo
    destinatarios_base = ["operaciones@empresa.com", "finanzas@empresa.com"]
    add_jefatura = st.checkbox("Incluir a Jefatura de Operaciones (jefatura.ops@empresa.com)", value=True)
    emails_adicionales = st.text_input("Correos adicionales (separados por coma)", placeholder="ejemplo@correo.com, otro@correo.com")

    # Botón de procesamiento del formulario
    procesar = st.form_submit_button("Generar Datos de Copiado")

# --- LÓGICA DE GENERACIÓN ---
if procesar:
    if not nombre_cliente or not identificacion or not numero_cuenta or not banco:
        st.error("⚠️ Por favor, complete todos los campos obligatorios antes de continuar.")
    else:
        # 1. Construcción de Destinatarios
        lista_emails = destinatarios_base.copy()
        if add_jefatura:
            lista_emails.append("jefatura.ops@empresa.com")
        if emails_adicionales:
            # Limpiar espacios en blanco y filtrar vacíos
            adicionales = [email.strip() for email in emails_adicionales.split(",") if email.strip()]
            lista_emails.extend(adicionales)
        
        destinatarios_finales = "; ".join(lista_emails)

        # 2. Construcción del Cuerpo del Mensaje
        cuerpo_mensaje = f"""Estimado Equipo de Finanzas,

Se ha solicitado formalmente el proceso de retiro con los siguientes detalles adjuntos para su respectiva validación y transferencia:

--- DATOS DE LA SOLICITUD ---
• Beneficiario: {nombre_cliente}
• Identificación: {identificacion}
• Motivo: {motivo}
• Valor a Transferir: ${monto:,.2f}

--- DATOS DE TRANSFERENCIA ---
• Banco: {banco}
• Tipo de Cuenta: {tipo_cuenta}
• Número de Cuenta: {numero_cuenta}

Quedo atento a la confirmación de la transferencia para notificar al usuario.

Saludos cordiales,"""

        # --- SECCIÓN DE COPIADO ---
        st.success("✅ ¡Datos generados con éxito! Utilice el botón de la esquina derecha de cada recuadro para copiar rápidamente.")
        st.write("---")
        
        # Resultado 1: Destinatarios del correo
        st.write("### 👥 1. Destinatarios del Correo (Para / CC)")
        st.code(destinatarios_finales, language="text")

        # Resultado 2: Cuerpo del mensaje
        st.write("### 📝 2. Cuerpo del Mensaje")
        st.code(cuerpo_mensaje, language="text")
