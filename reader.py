
import numpy as np

class Dataset():
    def __init__(self, path):
        self.bytestream=open(path+'/dataset-images.bin', mode="rb")
        self.bytelabels = open(path + '/dataset-labels.bin', mode="rb")
        self.height=32
        self.width=32
        self.depth=3

    def read(self, index):
        image_bytes=self.height*self.width*self.depth

        self.bytestream.seek(image_bytes,0)
        self.bytelabels.seek(index,0)

        byte_buffer = np.frombuffer(self.bytestream.read(image_bytes), dtype=np.uint8)
        reshaped_array = np.reshape(byte_buffer, [self.depth, self.width, self.height])
        bytes_image = np.transpose(reshaped_array, [2, 1, 0])

        byte_label =  np.frombuffer(self.bytelabels.read(1), dtype=np.uint8)

        return bytes_image,byte_label

    def close(self):
        self.bytestream.close()
        self.bytelabels.close()

data=Dataset(path='models')



