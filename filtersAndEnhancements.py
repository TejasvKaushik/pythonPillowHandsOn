from PIL import Image, ImageEnhance

image = Image.open("images/earth.jpg")

#creating an enhancer object
colorEnhancer = ImageEnhance.Color(image) #this takes care of the vibrance of the image
contrastEnhancer = ImageEnhance.Contrast(image) #this takes care of the contrast of the image
brightnessEnhancer = ImageEnhance.Brightness(image) #this takes care of the brightness of the image
sharpnessEnhancer = ImageEnhance.Sharpness(image) #this takes care of the sharpness of the image

#applying the enhancement
enhancedImageColor = colorEnhancer.enhance(0)
enhancedImageContrast = contrastEnhancer.enhance(2)
enhancedImageBrightness = brightnessEnhancer.enhance(2)
enhancedImageSharpness = sharpnessEnhancer.enhance(5)

#showing the image
# enhancedImageColor.show()
# enhancedImageContrast.show()
# enhancedImageBrightness.show()
enhancedImageSharpness.show()
