import argparse
#The lexers goal is to read in a source file and produce a list of tokens

parser = argparse.ArgumentParser(description='Lexer for the makeshift C Compiler')
parser.add_argument('filepath', metavar='P', type=str, help="A source file path for the compiler")

args = parser.parse_args()

file = args.filepath

#Attempt to open the file
try:
    f = open(file, "r")
    print(f.read())
except Exception as e:
    print(e)
