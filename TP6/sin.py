import ply.yacc as yacc
from lex import tokens, literals

def p_global(p):
    """
    S : Exp
    """
    print(f"Valor da expressão: {p[1]}")

def p_exp_add(p):
    """
    Exp : Exp ADD Termo
    """
    p[0] = p[1] + p[3]

def p_exp_sub(p):
    """
    Exp : Exp SUB Termo
    """
    p[0] = p[1] - p[3]

def p_exp_term(p): 
    """
    Exp : Termo
    """
    p[0] = int(p[1])
    
def p_term_mult(p):
    """
    Termo : Termo MULT Factor
    """
    p[0] = p[1]*p[3]

def p_term_factor(p):
    """
    Termo : Factor
    """
    p[0] = p[1]

def p_factor_num(p):
    """
    Factor : NUM
    """
    p[0] = int(p[1])

def p_factor_group(p):
    """
    Factor : '(' Exp ')'
    """
    p[0] = p[2]

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

parser = yacc.yacc()

import sys
for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print("Frase válida: ", linha)
    else:
        print("Frase inválida... Corrija e tente novamente!\n")