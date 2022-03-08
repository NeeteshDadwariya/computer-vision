import numpy as np
import cv2


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=100, color=(0, 255, 0), thickness=-1)


is_drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, param):
    global is_drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        is_drawing = True
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), thickness=5, color=(0, 255, 0))
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        #cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), thickness=-1, color=(0, 255, 0))


cv2.namedWindow('my_drawing')
# cv2.setMouseCallback('my_drawing', draw_circle)
cv2.setMouseCallback('my_drawing', draw_rectangle)

img = np.zeros((512, 512, 3))

while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
