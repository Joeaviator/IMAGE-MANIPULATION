import cv2
import matplotlib as plt
image=cv2.imread("image.png")
#convert to RGB
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
#title
plt.title("Colorful Azul E190 in RGB format")
plt.show

