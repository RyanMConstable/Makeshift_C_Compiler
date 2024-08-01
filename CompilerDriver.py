#This drive must allow a path to a C source file as its only argument

#If the command succeeds then it will create a file with the same name, minus the extension in the same directory
#Otherwise it will have a nonzero exit code with no file generated

#Should support --lex directs to run to the lexer but stop before parsing
#--parse runds lexer and parser but stops before assembly
#--codegen performs lexing parsing and assembly generation but not code emission
#All of these should return a 0 exit code if success, and produce no output files
#Extra: add -S option to direct the compiler to emit and assembly file but not to assemble or link it