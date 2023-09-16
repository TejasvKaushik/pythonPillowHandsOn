from PIL import Image, ImageEnhance, ImageOps

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

# applying multiple enhancements
enhancer = ImageEnhance.Sharpness(image)
enhancedImage = enhancer.enhance(5)
# enhancer = ImageEnhance.Brightness(enhancedImage)
# enhancedImage = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancedImage)
enhancedImage = enhancer.enhance(2)
enhancer = ImageEnhance.Color(enhancedImage)
enhancedImage = enhancer.enhance(0)

#showing the image
# enhancedImageColor.show()
# enhancedImageContrast.show()
# enhancedImageBrightness.show()
# enhancedImageSharpness.show()
enhancedImage.show()
