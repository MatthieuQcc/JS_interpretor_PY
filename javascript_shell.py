from lexer import *

def run(input):
    lexer = Lexer(input)
    tokens = lexer.tokens_list()
    return tokens

while True:
    user_input = input('javascript>')
    print(run(user_input))

    
