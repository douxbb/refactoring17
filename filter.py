import numpy as np
from PIL import Image


class GreyImage:
    def __init__(self, pix_array, pix_size=10, gradation=5):
        self.image = np.array(pix_array)
        self.size = pix_size        
        self.grad = 255 // gradation
        self.width = len(self.image)
        self.height = len(self.image[0])

    def get_grey_image(self):        
        for x in range(0, self.width, self.size):
            for y in range(0, self.height, self.size):                
                    self.image[x:x + self.size, y:y + self.size] = self.get_middle_color(x, y)
        return Image.fromarray(self.image)    
    def get_middle_color(self, x, y):
        return int(self.image[x:x + self.size, y:y + self.size].sum() / 3 // self.size ** 2 // self.grad * self.grad)



orig_img = Image.open("img2.jpg")
arr = GreyImage(orig_img, pix_size=int(input()), gradation=int(input())).get_grey_image()
arr.save('res.jpg')
