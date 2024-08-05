#!/usr/bin/env python3

import argparse
import subprocess
import os
import Lexer

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
parser.add_argument('--lex', dest='lex', action="store_true", help='Run lexer')
parser.add_argument('--parser', action="store_true", help="Run lexer, and the parser")
parser.add_argument('--codegen', action="store_true", help="Run lexer, parser, and assembler")
parser.add_argument('-S', action="store_true", help="Emit assembly file but don't assemble or link it")
parser.add_argument('-V', action="store_true", help="Print out result of each stage of compiler (verbose)")

args = parser.parse_args()


file = args.filepath
idx1 = file.rindex(".")
idx2 = file.rindex("/")
filename = file[idx2+1:idx1]

lex = args.lex
parser = args.parser
codegen = args.codegen
emitAssembly = args.S
verbose = args.V


#Create a pattern matching for each command

#The following command preprocesses the source file
# "gcc -E -P input_file -o preprocessed_file" this should generate a .i extension
#Delete when done
subprocess.run(["gcc", "-E", "-P", file, "-o", filename + ".i"])

if lex:
    toks = Lexer.main(filename + ".i")
    if verbose:
        print("Tokens Created by Lexer:")
        print(toks)
    if toks == 1:
        exit(1)
    
os.remove("./" + filename + ".i")


#Compile the preprocessed source file and output an assembly file
#Skip this step because we don't have a compiler yet (generate a .s file)
#Delete when done

#Assemble and link the assembly file to produce an executable using
# "gcc assembly_file -o output_file" (generate a .o file)
#Leave generated
#subprocess.run(["gcc", filename + ".s", "-o", filename + ".o"])