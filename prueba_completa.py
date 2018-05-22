import lexer_rules
import parser_rules

from  ply.lex import lex
from  ply.yacc import  yacc

text= open("prueba.txt").read()
#text = "((2 + 14) / (2)) * 3"
lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
expression = parser.parse(text, lexer)
print (expression)
"""
result = expression.evaluate()
print result
"""
