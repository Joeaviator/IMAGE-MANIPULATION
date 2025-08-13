import cv2
import matplotlib as plt
image=cv2.imread("image.png")
#convert to RGB
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
#title
plt.title("Colorful Azul E190 in RGB format")
plt.show()
#Convert to grayscale
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray)
#title
plt.title(" Azul E190 in Grayscale format")
plt.show()
#Rotate the image
(h,w)=image.shape[:2]
center=(w//2)
m=cv2.getRotationMatrix2D(center,180,1.0)
rotated=cv2.warpAffine(m,(w,h))
rotated_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.title("Roteted image")
plt.show()

