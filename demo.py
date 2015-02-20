from ascii_converter import convert
import argparse

parser = argparse.ArgumentParser(description='Convert an image to an ASCII art image.')
parser.add_argument('filename', metavar='FILENAME')

args = parser.parse_args()

try:
    convert(args.filename, N=5000, write=True)
except FileNotFoundError:
    print("Error: \"" + args.filename + "\" could not be found.")