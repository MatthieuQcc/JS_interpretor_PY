from tokenJS import *
from node import *
from parser_result import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        res = self.expr()
        if res.error:
            return res.failure("Invalid syntax error")
        return res

    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (T_PLUS, T_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(tok, factor))

        elif tok.type in (T_INT, T_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(tok))

        elif tok.type == L_PAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_tok.type == R_PAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure("Expected ')'")

        return res.failure("Expected int or float")

    def term(self):
        return self.bin_op(self.factor, (T_MUL, T_DIV))

    def expr(self):
        return self.bin_op(self.term, (T_MINUS, T_PLUS))

    def bin_op(self, func, ops):
        res = ParseResult()
        left = res.register(func())
        if res.error:
            return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.advance())
            right = res.register(func())
            if res.error:
                return res
            left = BinOpNode(left, op_tok, right)

        return res.success(left)
