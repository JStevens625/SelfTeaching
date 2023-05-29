#!/usr/bin/python3

import argparse
import math

parser = argparse.ArgumentParser(description="")

args = parser.parse_args()

def cylinder_volume(radius,height):
    volume = (math.pi) * (radius**2) * (height)
    return volume

if __name__ == '__main__':
    print (cylinder_volume(2,4))