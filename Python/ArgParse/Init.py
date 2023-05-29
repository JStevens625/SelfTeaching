#!/usr/bin/python3

import argparse
import math

parser = argparse.ArgumentParser(description="Calculate the volume of a cylinder")

parser.add_argument('radius',type=int, help="Define the radius of cylinder")
parser.add_argument('height',type=int, help="Define the height of cylinder")

args = parser.parse_args()

def cylinder_volume(radius,height):
    volume = (math.pi) * (radius**2) * (height)
    return volume

if __name__ == '__main__':
    print (cylinder_volume(args.radius,args.height))