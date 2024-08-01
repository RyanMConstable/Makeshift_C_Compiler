import argparse
#The lexers goal is to read in a source file and produce a list of tokens

parser = argparse.ArgumentParser(description='Lexer for the makeshift C Compiler')
parser.add_argument('filepath', metavar='P', type=str, help="A source file path for the compiler")

args = parser.parse_args()

file = args.filepath

#Attempt to open the file
try:
    f = open(file, "r")
    curTok = ""
    tokList = []
    while True:
        tok = f.read(1)
        if not tok:
            break
        if tok == "{" or tok == "}" or tok == "(" or tok == ")" or tok == " " or tok == ";":
            if curTok != "":
                tokList.append(curTok)
            if tok != " " and tok != '':
                tokList.append(tok)
            curTok = ""
        else:
            curTok += tok
    #print(tokList)
except Exception as e:
    print("ERROR: " + e)
