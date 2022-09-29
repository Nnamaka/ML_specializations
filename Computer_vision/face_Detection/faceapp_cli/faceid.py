# dependencies
# import cv2 as cv
# import tensorflow as tf
# from layers import L1Dist
# import numpy as np
import argparse

my_parser = argparse.ArgumentParser(description='face recognition CLI')

my_parser.add_argument('ID', metavar='id', type=str, help='starts verification')

args = my_parser.parse_args()

if ( args.ID == 'start'):
    print("The program seems ok!")

# if __name__ == '__main__':
#     pass