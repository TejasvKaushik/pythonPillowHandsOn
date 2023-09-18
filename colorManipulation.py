from PIL import Image

#image import
image = Image.open("images/earth.jpg")

#################################
# Analyzing picture information #
#################################

# print(image.getpixel((0, 0))) #returns the RGB value of the pixel at (0, 0)

print(image.getcolors(maxcolors = image.size[0] * image.size[1])) #returns a list of tuples containing the RGB value and the number of times it occurs in the image