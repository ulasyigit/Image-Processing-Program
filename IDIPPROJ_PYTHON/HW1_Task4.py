from PIL import Image, ImageFilter

image = Image.open('messi.jpg')
image.show()
image.save('messi.png')

# image information

print(image.filename)
print(image.format)
print(image.mode)
print(image.size)

# filters

blurred_image = image.filter(ImageFilter.BLUR)
contoured_image = image.filter(ImageFilter.CONTOUR)
blurred_image.show()
contoured_image.show()

blurred_image.save("blurred.png")
contoured_image.save("contoured.png")

# transpose

transposed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
transposed_image.save("transposed.png")
transposed_image.show()

# resize

size = (450, 150)
resized_image = image.resize(size)
resized_image.save("resized.png")
resized_image.show()
