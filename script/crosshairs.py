#!/usr/bin/env python
import cv2

img = cv2.imread('./test.png')
Nx = img.shape[0]
Ny = img.shape[1]
color = (0, 255, 0)
img = cv2.line(img, (0, Nx/2), (Ny-1, Nx/2), color, 1)
img = cv2.line(img, (Ny/2, 0), (Ny/2, Nx-1), color, 1)
wname = 'window'
cv2.startWindowThread()
cv2.namedWindow(wname)
cv2.imshow(wname, img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
