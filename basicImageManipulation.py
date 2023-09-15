from PIL import Image, ImageColor

image = Image.open("images/lz1.jpg")

#rotate image
image_rotate = image.rotate(60, expand=True, fillcolor=ImageColor.getcolor("red", "RGB"))

# ------------------------------------------------------------------------------------------#

#crop image
image_crop = image.crop((0, 0, 500, 845))

# ------------------------------------------------------------------------------------------#

#flip image
imageFlipHorizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
imageFlipVertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
imageTranspose = image.transpose(Image.Transpose.TRANSPOSE)

# ------------------------------------------------------------------------------------------#

#resize image
imageResize = image.resize((1000, 1920)) #this ruins the aspect ratio
##better way to resize
scaleFactor = 2
newSize = (image.size[0] // scaleFactor, image.size[1] // scaleFactor)
imageResizeBetter = image.resize(newSize)

# ------------------------------------------------------------------------------------------#

#show image
imageResizeBetter.show()
