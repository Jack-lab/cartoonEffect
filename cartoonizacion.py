import cv2
import numpy as np
import os

"""verificar que la cadena de ruta represente un archivo válido antes de pasarlo a cv2.imread:"""

def read_img(path):
    """Dada una ruta a un archivo de imagen, devuelve un cv2 cv2 array str -> np.ndarray"""
    if os.path.isfile(path):
        return cv2.imread(path)
    else:
        raise ValueError('La ruta proporcionada no es un archivo válido: {}'.format(path))


path = 'foto7.jpeg'
img = read_img(path)
#img = cv2.imread("foto4.jpg")

#Bordes
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#Cartoonización
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
