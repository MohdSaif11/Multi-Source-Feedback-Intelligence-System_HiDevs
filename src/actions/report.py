from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(filename, insights):
    doc = SimpleDocTemplate(filename)
    elements = []
    
    for insight in insights:
        elements.append(Paragraph(insight))
    
    doc.build(elements)
