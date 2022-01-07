import qrcode
img = qrcode.make("https://www.github.com/Snigdha667/Python-Projects")
img.save("My_Github_Account.jpg")
import cv2
d= cv2.QRCodeDetector()
retval, points, straight_qrcode = d.detectAndDecode(cv2.imread("My_Github_Account.jpg"))
print(retval)