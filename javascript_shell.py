from lexer import *

def run(text):
    lexer = Lexer(text)
    tokens = lexer.tokens_list()
    return tokens

while True:
    user_input = input('javascript>')
    print(run(user_input))