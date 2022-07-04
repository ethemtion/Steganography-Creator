import cv2
import numpy as np

class Main:
    def __init__(self) -> None:
        pass

    def conv2binary(self,text):
        if type(text) == str:
            return ''.join([ format(ord(i), "08b") for i in text ])
        elif type(text) == bytes or type(text) == np.ndarray:
            return [ format(i, "08b") for i in text ]
        elif type(text) == int or type(text) == np.uint8:
            return format(text, "08b")
        else:
            raise TypeError("Input type not supported")
            
    
    def encode(self,text,img):
        #img = cv2.imread(imgP)
        binary_text = self.conv2binary(text)
        text_len = len(text)
        data_idx = 0
        
        for values in img:
            for pixel in values:
            # convert RGB values to binary format
                r, g, b = self.conv2binary(pixel)
                # modify the least significant bit only if there is still data to store
                if data_idx < text_len:
                    # hide the data into least significant bit of red pixel
                    pixel[0] = int(r[:-1] + binary_text[data_idx], 2)
                    data_idx = data_idx + 1
                if data_idx < text_len:
                    # hide the data into least significant bit of green pixel
                    pixel[1] = int(g[:-1] + binary_text[data_idx], 2)
                    data_idx = data_idx + 1
                if data_idx < text_len:
                    # hide the data into least significant bit of  blue pixel
                    pixel[2] = int(b[:-1] + binary_text[data_idx], 2)
                    data_idx += 1
                # if data is encoded, just break out of the loop
                if data_idx >= text_len:
                    break
        cv2.imwrite("encoded_img.jpg", img)

    def decode(self,img):
        binary_txt = ""
        for values in img:
            for pixel in values:
                r, g, b = self.conv2binary(pixel) #convert the red,green and blue values into binary format
                binary_txt += r[-1] #extracting data from the least significant bit of red pixel
                binary_txt += g[-1] #extracting data from the least significant bit of red pixel
                binary_txt += b[-1] #extracting data from the least significant bit of red pixel
        # split by 8-bits
        # for i in range(0, len(binary_txt), 8):
        #     all_bytes = binary_txt[i: i+8]
        
        # # convert from bits to characters
        # decoded_txt = ""
        # for byte in all_bytes:
        #     decoded_txt += byte
        #     if decoded_txt[-5:] == "#####": #check if we have reached the delimeter which is "#####"
        #         break
        # #print(decoded_data
        return binary_txt #remove the delimeter to show the original hidden message