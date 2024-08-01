import argparse
#This drive must allow a path to a C source file as its only argument

#If the command succeeds then it will create a file with the same name, minus the extension in the same directory
#Otherwise it will have a nonzero exit code with no file generated

#Should support --lex directs to run to the lexer but stop before parsing
#--parse runds lexer and parser but stops before assembly
#--codegen performs lexing parsing and assembly generation but not code emission
#All of these should return a 0 exit code if success, and produce no output files
#Extra: add -S option to direct the compiler to emit and assembly file but not to assemble or link it

parser = argparse.ArgumentParser(description='Wrapper for homemade C compiler')
parser.add_argument('filepath', metavar='P', type=str, help="A source file path for the compiler")
parser.add_argument('--lex', dest='lex', help='Run lexer')
parser.add_argument('--parser', help="Run lexer, and the parser")
parser.add_argument('--codegen', help="Run lexer, parser, and assembler")
parser.add_argument('-S', help="Emit assembly file but don't assemble or link it")

args = parser.parse_args()
#print(args.filepath)