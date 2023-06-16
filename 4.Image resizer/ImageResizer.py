import cv2

src = cv2.imread(r"4.Image resizer/nice-image.png")

scale_percent_string= input('''Enter how much of the real image's percentage do 
you want in the new image:     ''')
scale_percent= int(scale_percent_string)

width = int(src.shape[1]*(scale_percent/100))
Height= int(src.shape[0]*(scale_percent/100))

dsize = (width,Height)

output = cv2.resize(src,dsize)

cv2.imwrite("new-image.png",output)
cv2.imshow("new-image.png",output)



cv2.waitKey(0)
