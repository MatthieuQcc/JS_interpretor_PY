## TOKENS

# Definition of constants for the different Token types and

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

T_INT = 'INT'
T_FLOAT = 'FLOAT'
T_PLUS = 'PLUS'
T_MINUS = 'MINUS'
T_DIV = 'DIV'
T_MUL = 'MUL'
L_PAREN = 'L_PAREN'
R_PAREN = 'R_PAREN'

class Token:    
    def __init__(self, new_type, new_value = None) -> None:
        self.value = new_value
        self.type = new_type
    
    def __repr__(self) -> str:
        if self.value: 
            return f'{self.type} : {self.value}'
        else: 
            return f'{self.type}'


