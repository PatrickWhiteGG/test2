import cv2
lena = cv2.imread("lena.bmp")
cv2.imshow("demo1",lena)
cv2.imshow("demo2",lena)
cv2.waitKey()
cv2.destroyAllWindows()
# 就是一次銷毀全部視窗