from interpreter import *
from lexer import *
from jsparser import *


def run(input):
    # Generate tokens
    lexer = Lexer(input)
    tokens = lexer.tokens_list()

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()

    # Run program
    interpreter = Interpreter()
    result = interpreter.visit(ast)

    # return ast         # Voir l'ast

    return result  # Voir le résultat obtenu


while True:
    user_input = input('Javascript>')
    print(run(user_input))
