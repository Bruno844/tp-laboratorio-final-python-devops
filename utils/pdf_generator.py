from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generar_pdf_informe(biblioteca, nombre_archivo: str = "reporte_biblioteca.pdf"):
    """Genera un informe PDF estilizado del estado del sistema de la biblioteca."""
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story = []
    styles = getSampleStyleSheet()

    # Estilos
    titulo_style = ParagraphStyle('TituloStyle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#1E3A8A'), spaceAfter=12)
    subtitulo_style = ParagraphStyle('SubTituloStyle', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#2563EB'), spaceAfter=8)
    normal_style = styles['Normal']

    # Encabezado
    story.append(Paragraph(f"📚 Reporte General - {biblioteca.nombre}", titulo_style))
    story.append(Paragraph("Resumen del estado del catálogo, usuarios y préstamos activos.", normal_style))
    story.append(Spacer(1, 15))

    # Sección 1: Materiales
    story.append(Paragraph("📖 Catálogo de Materiales", subtitulo_style))
    data_mat = [["ID", "Título", "Autor / Detalle", "Tipo", "Estado"]]
    for m in biblioteca.materiales:
        tipo = "Libro" if hasattr(m, 'num_paginas') else "Revista"
        estado = "Disponible" if m.disponible else "Prestado"
        data_mat.append([m.id_material, m.titulo[:25], m.autor[:20], tipo, estado])

    t_mat = Table(data_mat, colWidths=[60, 180, 140, 70, 70])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F3F4F6')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#D1D5DB'))
    ]))
    story.append(t_mat)
    story.append(Spacer(1, 20))

    # Sección 2: Usuarios
    story.append(Paragraph("👥 Registro de Usuarios", subtitulo_style))
    data_usr = [["ID", "Nombre", "Email", "Tipo", "Préstamos Activos"]]
    for u in biblioteca.usuarios:
        tipo = "VIP" if hasattr(u, 'codigo_membresia') else "Estándar"
        data_usr.append([u.id_usuario, u.nombre, u.email, tipo, f"{len(u.materiales_prestados)}/{u.limite_prestamos()}"])

    t_usr = Table(data_usr, colWidths=[60, 140, 170, 70, 80])
    t_usr.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563EB')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#EFF6FF')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BFDBFE'))
    ]))
    story.append(t_usr)

    doc.build(story)
    return nombre_archivo
