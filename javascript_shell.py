from interpreter import *
from lexer import *
from parser_analyze import *


def run(input):
    # Generate tokens
    lexer = Lexer(input)
    tokens = lexer.tokens_list()

    # return tokens                             # Voir les tokens

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()

    # return ast.node, ast.error                # Voir l'ast

    # if ast.error:                             # Essai Gestion erreur
    #   return ast.error

    # Run program
    interpreter = Interpreter()
    result = interpreter.visit(ast.node)

    return result                               # Voir le résultat obtenu


while True:
    user_input = input('Javascript>')
    print(run(user_input))
