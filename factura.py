from PIL import Image, ImageFont, ImageDraw 
import numpy as np

def obtener_factura(nombre, ident, cel, email, dir, fecha, descr, des1, val1, des2, val2, des3, val3, des4, val4, total, idd=1):

    def agregar_linea(A, number=1062, lineas=3):
        A = list(A)
        B = ''
        for i in range(len(A)):
            ancho3 = image_editable.textsize(''.join(A[:i]), font=title_font)[0]
            if ancho3>number:
                B = ''.join(A[:i])
                break
        if B != '':
            B = B + "\n" + agregar_linea(''.join(A[i:]), number=number)
        if B=='':
            B = B + ''.join(A)
        if len(B.split("\n"))>lineas:
            B = '\n'.join(B.split("\n")[:3])+"..."
        return B 

    to_money = lambda x: '${:,.1f}'.format(x).replace(",", "@").replace(".", ",").replace("@", ".") if x>=0 else x

    def des_valor(des1, val1, x, y,z):
        title_font = ImageFont.truetype('Zag Regular.otf', 50)
        TEXTO1 = agregar_linea(des1, number=600, lineas=0)
        image_editable.text((x,z), TEXTO1.split("\n")[0].split("...")[0], (100,100,100), font=title_font, fontsize=10)
        if val1=="0":
            return
        try: 
            val1 = float(val1)
            val1 = to_money(val1)
        except:
            val1
        image_editable.text((y,z), val1, (100,100,100), font=title_font, fontsize=10)

    #Imagen
    my_image = Image.open("Factura.png")
    ancho, alto = my_image.size
    image_editable = ImageDraw.Draw(my_image)

    # Escribiendo nombre
    title_font = ImageFont.truetype('Zag Regular.otf', 70)
    ancho2 = image_editable.textsize(nombre, font=title_font)[0]
    numero1 = (ancho-ancho2-250)/2
    image_editable.text((numero1, 602), nombre, (100,100,100), font=title_font, fontsize=25)

    # Numero
    title_font = ImageFont.truetype('Zag Bold.otf', 55)
    zeros = np.zeros(8-len(list(str(idd))), dtype=int)
    numeross = ''.join([str(I) for I in zeros])
    texto = "N°"+numeross+str(idd)
    image_editable.text((800, 50), texto, (100,100,100), font=title_font, fontsize=25)

    # Informacion de pago
    title_font = ImageFont.truetype('Zag Regular.otf', 60)
    descr=agregar_linea(descr, number=1045)
    ancho3 = image_editable.textsize(descr, font=title_font)[0]
    numero2 = (ancho-ancho3-220)/2
    image_editable.text((numero2+20, 955), descr, (100,100,100), font=title_font, fontsize=25)

    # Fecha
    title_font = ImageFont.truetype('Zag Regular.otf', 60)
    ancho4 = image_editable.textsize(fecha, font=title_font)[0]
    numero3 = (ancho-ancho4-250)/2
    image_editable.text((numero3, 1180), fecha, (100,100,100), font=title_font, fontsize=25)

    # iNFORMACION Y DESCRIPCIONES
    title_font = ImageFont.truetype('Zag Regular.otf', 40)
    image_editable.text((330, 690), ident, (100,100,100), font=title_font, fontsize=10)
    image_editable.text((260, 735), cel, (100,100,100), font=title_font, fontsize=10)
    image_editable.text((230, 780), email.lower(), (100,100,100), font=title_font, fontsize=10)
    image_editable.text((260, 825), dir, (100,100,100), font=title_font, fontsize=10)

    des_valor(des1, val1, 100, 870, 1360)
    des_valor(des2, val2, 100, 870, 1420)
    des_valor(des3, val3, 100, 870, 1480)
    des_valor(des4, val4, 100, 870, 1540)

    # TOtal
    title_font = ImageFont.truetype('Zag Bold.otf', 55)
    try: 
        total = float(total)
        total = to_money(total)
    except:
        total
    image_editable.text((865,1650), total, (100,100,100), font=title_font)

    my_image.save("result.png")

    return my_image