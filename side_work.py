from PIL import Image

im1 = Image.open("Image/mumbai coast.jpg")
im2 = Image.open("Image/nebula-mountain.jpg")
im3 = Image.open("Image/supernova.jpg")

pdf1_filename = "reader.pdf"


image1 = im1.convert('RGB')
image2 = im2.convert('RGB')
image3 = im3.convert('RGB')

im_list = [image1,image2,image3]

image1.save(pdf1_filename,save_all=True,append_images=im_list)


#im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
