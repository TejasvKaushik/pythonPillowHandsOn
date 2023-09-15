from PIL import Image

#create new image by import
image = Image.open("images/pic.jpeg")

# #alt way to open an image 
# with Image.open("pic.jpeg") as image:
#     #show image
#     image.show()

#create a new image from scratch
image_blank = Image.new('RGBA', (1000, 600))

#show image
image.show()

#save image
# image.save("test_save.png")

print(image.size)
print(image.format)
print(image.mode)
print(image.filename)
print(image.info)
print(image.palette)
print(image.format_description)