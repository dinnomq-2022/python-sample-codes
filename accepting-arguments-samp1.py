import argparse

parser = argparse.ArgumentParser(description='This print the name of my goat')
parser.add_argument('-c', '--color', metavar='color', required=True
                    ,choices={'white','silver','gold','brown'}, help='search valid colors')

args = parser.parse_args()
print(args.color)
