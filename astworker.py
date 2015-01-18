from ast import *
from decimal import Decimal
import ast_utils

class RewriteNum(NodeTransformer):

    def __init__(self, src):
        self.src = src
        super(RewriteNum, self).__init__()

    def visit_Num(self, node):
        new = parse("Decimal('%s')" % node.n, mode="eval")
        return copy_location(new.body, node)

def compile_calc(src, filename="<input>", mode='single'):
    code = ast_utils.parse_source(src, mode=mode)
    node = RewriteNum(src).visit(code)
    fix_missing_locations(node)
    return compile(node, filename, mode)
