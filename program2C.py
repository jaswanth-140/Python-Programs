import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image=mpimg.imread('image.jpg')
plt.imshow(image)
plt.axis("off")
plt.title("Loaded image")
plt.show()