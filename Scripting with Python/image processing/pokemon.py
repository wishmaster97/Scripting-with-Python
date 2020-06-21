from PIL import Image, ImageFilter
img = Image.open("./pokedox/pickachu.jpg")
print(img)
print(img.format)
print(img.size)
#print(dir(img))

filImg = img.filter(ImageFilter.BLUR)
filImg.save("blur.png", "png")
filImg.save("blur2.jpg", "jpeg")

#convert image in grey

filImg2 = img.convert('L')
filImg2.save("grey.png", "png")
#filImg2.show()

#rotate Image
rotate_img = filImg2.rotate(90)
#rotate_img.save("roatate90.png", "png")
#rotate_img.show()

#resize an image

resize_img = filImg2.resize((300, 300))
#resize_img.show()

#convert into RGB
filImg3 = img.convert('RGB')
filImg3.save("RGB.png", "png")


#cropping a image

box_dim = (200, 200, 300, 300)
crop_img = filImg.crop(box_dim)
#crop_img.show()


#resizing image while keeping its aspect ratio
astro_img = Image.open("./astro.jpg")
astro_img.thumbnail((400,200))
astro_img.show()