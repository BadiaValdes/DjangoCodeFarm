from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from .models import Marca

class MyFirstPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    def print(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)
        elements = []
        flow_obj = []

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        marca = Marca.objects.all()
        header = []
        head = []

        head.append('#')
        head.append('Nombre')
        elements.append(head)
        count = 1
        header.append(Paragraph('Mis marcas', styles['Heading1']))

        for marc in marca:
            data = []
            data.append(count)
            data.append(marc.nombre)
            count+=1
            elements.append(data)


        style = TableStyle(
            [('LINEABOVE', (0, 0), (-1, 0), 0.25, colors.black), ('LINEABOVE', (0, 1), (-1, -1), 0.25, colors.black), ('GRID',(0,0),(-1,-1),0.5,colors.black),
             ('LINEBELOW', (0, -1), (-1, -1), 0.25, colors.black), ('ALIGN', (1, 1), (-1, -1), 'RIGHT')])


        t = Table(elements)

        t.setStyle(style)

        flow_obj.append(t)

        general=[]
        general.append(header)

        doc.build(flow_obj)

        pdf = buffer.getvalue()
        buffer.close()
        return pdf