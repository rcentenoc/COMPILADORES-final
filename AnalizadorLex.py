import ply.lex as lex
import sys

reservadas = { 
  'uma' : 'main',
  'ari' : 'if',
  'shuc' : 'else',
  'pacha' : 'while',
  'haykaq' : 'for',
  'tukuchay' : 'break',
  'chaya' : 'return',
  'chiqa' : 'true',
  'mana_chiqa' : 'false',
  'kala' : 'null',
  'e' : 'and',
  'o' : 'or',
  'mana' : 'not',
  'hun' : 'integer',
  'huk' : 'character',
  'chaq' : 'string',
  'yuyay' : 'boolean',
  'manamunay' : 'void',
  'quy' : 'input',
  'uyariy' : 'output'
}

tokens = ('comment_init', 'comment_fin', 'id', 'char', 'number',
'oper_suma', 'oper_dif', 'oper_div', 'oper_mult', 'oper_asign',
'oper_mod', 'oper_mayor', 'oper_menor', 'oper_identico',
'oper_diferente', 'oper_neg', 'oper_mayorigu', 'oper_menorigu',
'par_init', 'par_fin', 'key_init', 'key_fin', 'corch_init',
'corch_fin', 'comma', 'texto', 'break_line') + tuple(reservadas.values())

t_comment_init = r'\|\|\:'
t_comment_fin = r'\:\|\|'
t_oper_identico = r'=='
t_oper_mayorigu = r'>='
t_oper_menorigu = r'<='
t_oper_diferente = r'\!=' 
t_oper_suma = r'\+'
t_oper_dif = r'-'
t_oper_mult = r'\*'
t_oper_div = r'/'
t_par_init = r'\('
t_par_fin = r'\)'
t_oper_asign = r'='
t_oper_mod = r'%'
t_oper_mayor = r'>'
t_oper_menor = r'<'
t_oper_neg = r'\!'
t_key_init = r'{'
t_key_fin = r'}'
t_corch_init = r'\['
t_corch_fin = r'\]'
t_comma = r','
t_break_line = r'\;'

entrada = []
token_type = []
token_value = []
token_line = []
token_salida = []


def t_texto(t):
  r'"([^\\"]|\\")*"'
  t.type = reservadas.get(t.value,'texto')   
  return t

def t_char(t):
     r'\|([^\\"]|\\")\|'
     t.type = reservadas.get(t.value,'char')   
     return t

def t_id(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'id')   
     return t

def t_number(t):
  r'\d+'
  t.value = int(t.value) 
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
  print("Illegal character ’ %s’" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

def capturador_tokens(file):
  token_list=list()
  print(token_list)
  f = open(file, "r")
  data = f.read()
  lexer.input(data)
  while True:
    tok = lexer.token()
    if not tok:
      break 
    token_list.append([tok.type,tok.value, tok.lineno, tok.lexpos])
    # token_type.append(tok.type)
    # token_value.append(tok.value)
    # token_line.append(tok.lineno)
  token_list.append([ '$', None, None, None ])
  return token_list

if __name__ == "__main__":
    token_list = capturador_tokens("ejemplo_funcion.txt")
    for tok in token_list:
        print( str(tok[0]) + ' ', end='')
        print()
    print("\n     #----------- ANALIZADOR DE token_list -----------#\n")
    print("\n#----------- [ tipo , lexema , linea , posicion del lexema ] -----------#\n")
    print(token_list)
    # print("\n")
    # print(token_list[0])
    # print(token_list[1])
    # print(len(token_list))
    # print(token_list[0][0])
    # print(token_list[0][1])
    # print(token_list[0][2])
    # print(token_list[0][3])
    
    # print(token_type)
    # print("\n")
    # print(token_value)
    # print("\n")
    # print(token_line)
