import qrcode as qr
import cv2 as cv


link = input("Enter the link that you want to generate the qr code for: ")
name = input("Enter the Name You'd like the file to have: ")


img = qr.make(link)
img.save(f"{name}.jpg")


image = cv.imread(f'{name}.jpg')
cv.imshow('image window', image)
cv.waitKey(0)
cv.destroyAllWindows()

print("file has been generated")