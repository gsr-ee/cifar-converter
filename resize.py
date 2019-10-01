from argparse import ArgumentParser
from PIL import Image
import os

#Script for resizing the images inside the directories to the dimension 32x32x3

def main(args):
	path=args.path
	dir=os.listdir(args.path)
	new_width  = 32
	new_height = 32
	print('Resizing the images: %d x %d' %(new_width,new_height))
	for i in range(len(dir)):
		files=os.listdir(os.path.join(path,dir[i]))
		for j in range(len(files)):
			img = Image.open(os.path.join(path,dir[i],files[j]))# image extension *.png,*.jpg
			img = img.resize((new_width, new_height), Image.ANTIALIAS)
			os.remove(os.path.join(path,dir[i],files[j]))
			img.save(os.path.join(path,dir[i],files[j])) # format may what u want ,*.png,*jpg,*.gif
	print("All done!")

if __name__ == "__main__":
	parser = ArgumentParser(
        description="Convert any image to 32x32 size.")
	parser.add_argument('-path', '--path', type=str,
        help="Specify the path to the datapath that contains the images.")
	args = parser.parse_args()
	main(args)



