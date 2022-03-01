import cv2
lena = cv2.imread("photo\lena.bmp",1)
print(lena)

# cv2.imread(filename , flags=None )

# filename : 要輸入的是圖片檔案名稱

# flags : 指定「彩色」「黑白」「Alpha合成」的方式來讀取圖片

# 彩色 : 為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel
# 黑白 : 是以灰階的格式來讀取圖片
# Alpha合成 : 是讀取圖片中所有的 channels，包含透明度的 channel

# 分別是("lena.bmp",1)，("lena.bmp",0)，("lena.bmp",-1)

# 或者是("lena.bmp",cv2.IMREAD_COLOR)，("lena.bmp",cv2.IMREAD_GRAYSCALE)，("lena.bmp",cv2.IMREAD_UNCHANGED)

# flags還有很多參數可以使用，EX: cv2.IMREAD_ANYDEPTH，cv2.IMREAD_ANYCOLOR....... 