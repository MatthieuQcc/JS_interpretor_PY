from lexer import *
from jsparser import *


def run(input):
    # Generate tokens
    lexer = Lexer(input)
    tokens = lexer.tokens_list()

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()

    return ast


while True:
    user_input = input('Javascript>')
    print(run(user_input))
