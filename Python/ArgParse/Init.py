#!/usr/bin/python3

import argparse
import math

parser = argparse.ArgumentParser(description="Calculate the volume of a cylinder")

parser.add_argument('-r','--radius',type=int, metavar='', required=True, help="Define the radius of cylinder")
parser.add_argument('-H','--height',type=int, metavar='', required=True, help="Define the height of cylinder")

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Print Quiet')
group.add_argument('-v', '--verbose', action='store_true', help='Print Verbose')

args = parser.parse_args()

def cylinder_volume(radius,height):
    volume = (math.pi) * (radius**2) * (height)
    return volume

if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(f"Volume of a Cylinder with radius {args.radius} and height {args.height} is {volume}")
    else: print(f"Volume of Cylinder is {volume}")