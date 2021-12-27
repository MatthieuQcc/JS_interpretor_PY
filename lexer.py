## LEXER

from tokenJS import *

class Lexer:
    def __init__(self, new_text : str) -> None:
        self.text = new_text
        self.current_pos = 0
        self.current_char = None
        self.next()

    def next(self):
        # we advance to the next char in the input
        if self.current_pos < len(self.text):
            self.current_char = self.text[self.current_pos]
        else: 
            self.current_char = None
        self.current_pos += 1
    
    def create_number(self):
        my_number = ""
        is_float = False
        while (self.current_char in DIGITS) | (self.current_char == '.'):
            if self.current_char == '.':
                if is_float:
                    break
                is_float = True
                my_number += '.'
            else:
                my_number += self.current_char
            self.next()

        if is_float:
            return Token(T_FLOAT, float(my_number))
        else:
            return Token(T_INT, int(my_number))

    def tokens_list(self):
        tok = []
        while self.current_char != None:
            # we ignore spaces and tabs for now
            if self.current_char == ' ' or self.current_char == '\t':
                self.next()
            elif self.current_char == '+':
                tok.append(Token(T_PLUS))
                self.next()
            elif self.current_char == '-':
                tok.append(Token(T_MINUS))
                self.next()
            elif self.current_char == '*':
                tok.append(Token(T_MUL))
                self.next()
            elif self.current_char == '/':
                tok.append(Token(T_DIV))
                self.next()
            elif self.current_char == '(':
                tok.append(Token(L_PAREN))
                self.next()
            elif self.current_char == ')':
                tok.append(Token(R_PAREN))
                self.next()
            elif self.current_char in DIGITS:
                tok.append(self.create_number())
                #self.next()
            else:
                return("ERROR WRONG CHAR")
        return tok
