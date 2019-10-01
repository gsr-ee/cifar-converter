from PIL import Image
import os
from array import *
from argparse import ArgumentParser

#Scripts for converting the images into binary files

def main(args):

    path=os.path.join(args.path,args.prefix)

    data = array('B')
    labels = array('B')
	
    print('Reading the images to convert into binary format ...')

    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.JPG'):

                im = Image.open(os.path.join(dirname, filename))
                pix = im.load()
                #print(os.path.join(dirname, filename))

                # store the class name from look at path
                class_name = int(os.path.join(dirname).split('/')[-1])
                #print(class_name)

                # create array of bytes to hold stuff

                # first append the class_name byte
                labels.append(class_name)

                # then write the rows
                # Extract RGB from pixels and append
                # note: first we get red channel, then green then blue
                # note: no delimeters, just append for all images in the set
                for color in range(0, 3):
                    for x in range(0, 32):
                        for y in range(0, 32):
                            data.append(pix[x, y][color])

############################################
# write all to binary, all set for cifar10!!#
############################################
    print('Done!')
    print('Converting the images into a binary format ...')
    if not (os.path.exists('models')):
        os.mkdir('models')

    print('Converting the images into a binary format ...')
    output_file = open('models/%s-images.bin' %args.prefix, 'wb')
    data.tofile(output_file)
    output_file.close()
    print('Done!')

    print('Converting the labels into a binary format ...')
    output_file = open('models/%s-labels.bin' %args.prefix, 'wb')
    labels.tofile(output_file)
    output_file.close()
    print('All done!')

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Convert any image to binary file.")
    parser.add_argument('-path', '--path', type=str,
                        help="Specify the path to the datapath that contains the images.")
    parser.add_argument('-prefix', '--prefix', type=str,
                        help="Specify the type of the dataset, i.e, train or test.", choices=['train','test'])
    args = parser.parse_args()
    main(args)
