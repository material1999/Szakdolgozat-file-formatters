import glob
import os

def main():

    for file in glob.glob("simulation/*.csv"):
        src = file
        dst = src.replace("_1000", "")
        os.rename(src, dst)

if __name__ == '__main__':
	main()
