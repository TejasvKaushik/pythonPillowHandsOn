from PIL import Image, ImageEnhance, ImageFilter

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

# ---------------------------------------------------------------------------------------------

#applying filters

#basic filters
blurredImage = image.filter(ImageFilter.BLUR)
contouredImage = image.filter(ImageFilter.CONTOUR)
detailImage = image.filter(ImageFilter.DETAIL)
edgeEnhanceImage = image.filter(ImageFilter.EDGE_ENHANCE)
edgeEnhanceMoreImage = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
embossImage = image.filter(ImageFilter.EMBOSS)
findEdgesImage = image.filter(ImageFilter.FIND_EDGES)
sharpenedImage = image.filter(ImageFilter.SHARPEN)
smoothImage = image.filter(ImageFilter.SMOOTH)
smoothMoreImage = image.filter(ImageFilter.SMOOTH_MORE)

#rank filters
imageFilterMin = image.filter(ImageFilter.MinFilter(size = 3))
imageFilterMedian = image.filter(ImageFilter.MedianFilter(size = 3))
imageFilterMax = image.filter(ImageFilter.MaxFilter(size = 3))

#multiband filters
imageBoxBlur = image.filter(ImageFilter.BoxBlur(20)) 
imageGaussianBlur = image.filter(ImageFilter.GaussianBlur(4))
imageUnsharpMask = image.filter(ImageFilter.UnsharpMask(radius=20, percent=150, threshold=3))

#showing the image
imageUnsharpMask.show()