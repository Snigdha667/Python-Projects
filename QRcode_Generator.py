import qrcode
img = qrcode.make("https://www.github.com/Snigdha667/Python-Projects/commit/0864a394932049e7b0bb6dc5c04d20ab8f99ce10")
img.save("My_Github_Account.jpg")
import cv2
d= cv2.QRCodeDetector()
retval, points, straight_qrcode = d.detectAndDecode(cv2.imread("My_Github_Account.jpg"))
print(retval)
