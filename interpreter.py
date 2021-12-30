import tokenJS
from number import *

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.tok.value)

    def visit_BinOpNode(self, node):
        left = self.visit(node.left_node)
        right = self.visit(node.right_node)

        if node.op_tok.type == tokenJS.T_PLUS:
            result = left.add(right)
        elif node.op_tok.type == tokenJS.T_MINUS:
            result = left.sub(right)
        elif node.op_tok.type == tokenJS.T_MUL:
            result = left.mul(right)
        elif node.op_tok.type == tokenJS.T_DIV:
            result = left.div(right)
        else:
            result = 0
        return result

    def visit_UnaryOpNode(self, node):
        nb = self.visit(node.node)
        if node.op_tok.type == tokenJS.T_MINUS:
            nb = nb.mul(Number(-1))
        return nb
