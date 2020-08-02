from PIL import Image , ImageEnhance , ImageFilter
import os
"""
img1 = Image.open("pic1.jpg") # here we open the image

img1.save("pic1.pdf") # in this method we can change the type of the file to png,pdf and many more

# to open the image we use
img1.show()

# to change the size of the image it will also reduce the space
Max_size =(250,250)
img1.thumbnail(Max_size)
img1.save("img1.jpg")


# if we want to change  hundreds of file type 
for i in os.listdir():
        if i.endswith(".jpg"):
                img1 = Image.open(i)
                filename,extention = os.path.splitext(i)
                img1.save(f"{filename}.png")


# if we want to change 100 of file size than

for i in os.listdir():
        if i.endswith(".jpg"):
                img1 = Image.open(i)
                Max_size =(250,250)
                img1.thumbnail(Max_size)
                img1.save(f"{i}")



# to increse the sharpness of the image we use ImageEnhancer
img1 = Image.open("pic1.jpg")

enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(5).save("new.jpg")
# 0 __ blurry
# 1 _ orignal
# 2  shapness increse
# 3 _ sharpness more increse
# and so on

# to increse the sharpness of the image
img1 = Image.open("pic1.jpg")

enhancer = ImageEnhance.Color(img1)
enhancer.enhance(2).save("new.jpg")
# 0 for black and white
# 1 color increse

# to increse the brightness of the image

img1 = Image.open("pic1.jpg")

enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.5).save("new.jpg")
# 0 == for black
# 1 == increase

# to increse the contrast of the image

img1 = Image.open("pic1.jpg")

enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.5).save("new.jpg")

"""

# to blur the file

img1 = Image.open("pic1.jpg")
img1.filter(ImageFilter.GaussianBlur()).save('new.png')








