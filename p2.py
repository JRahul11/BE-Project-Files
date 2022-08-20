# from PIL import Image
# import imagehash
# hash0 = imagehash.average_hash(Image.open('gfg.html.png')) 
# print(hash0)
# hash1 = imagehash.average_hash(Image.open('javat.html.png')) 
# print(hash1)
# cutoff = 2  # maximum bits that could be different between the hashes. 

# if hash0 - hash1 < cutoff:
#   print('images are similar')
# else:
#   print('images are not similar')

from PIL import Image

from pixelmatch.contrib.PIL import pixelmatch
 
# Cropped image of above dimension
# (It will not change original image)
# im1 = img_a.crop((left, top, right, bottom))
# im1 = img_a.crop((0, 0, 0, 0))
# im1.show()


left = 150
top = 60
right = 510
bottom = 425

img_a = Image.open("am1.bin.png")
img_b = Image.open("am2.bin.png")

im1 = img_a.crop((left, top, right, bottom))
im2 = img_b.crop((left, top, right, bottom))
img_diff = Image.new("RGBA", im1.size)

mismatch = pixelmatch(im1, im2, img_diff, includeAA=True)
print(mismatch)

img_diff.save("diff.png")
