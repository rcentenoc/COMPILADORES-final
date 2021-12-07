from AnalizadorLex import capturador_tokens
from Graficador import Imprimir_arbol, Verificador
import pandas as pd

nuevo_nodo = []
indices = []
class nodo_detalle:
    def __init__(self,tipo=[],lexem=[],linea=[],poslex=[]):
        self.type=tipo
        self.poslex=poslex
        self.lexem=lexem
        self.line=linea

class nodo: 
    def __init__(self, token_list , valor, padre):
      self.nodo_hijo = []
      self.valor = valor 
      self.token = token_list[0] 
      self.lexema = token_list[1]
      self.linea = token_list [2]
      self.padre = padre 
      self.estado = False 
      self.terminal = False
    
    def insertarNodo(self, estructura , identificador): 
      stack_temporal=[]
      stack_temporal.append(self)
      while (len(stack_temporal)): 
          Actual = stack_temporal[0]
          if len(Actual.nodo_hijo) == 0 and Actual.terminal == False:
            Actual.nodo_hijo.append(nodo(estructura, identificador, self.token))
            return
          stack_temporal.pop(0)
          cont = 0
          for i in range(len(Actual.nodo_hijo)-1,-1,-1):
              stack_temporal.insert(0,Actual.nodo_hijo[i])
              if Actual.nodo_hijo[i].estado == True:
                cont =+ 1
          if cont == 0 and Actual.terminal == False:
            Actual.nodo_hijo.append(nodo(estructura, identificador, self.token))
            return

    def actualizarNodo(self): 
      stack_temporal=[]
      stack_temporal.append(self)
      while (len(stack_temporal)): 
          Actual = stack_temporal[0]
          if Actual.estado == True:
            Actual.terminal = True
          if Actual.estado == False:
            Actual.estado = True
            return
          stack_temporal.pop(0)
          for i in range(len(Actual.nodo_hijo)-1,-1,-1): 
              stack_temporal.insert(0,Actual.nodo_hijo[i]) 

def AnalizadorSin():
  # Stack_begin = capturador_tokens('Ejemplos/ejemplo_funcion.txt') 
  Stack_begin = capturador_tokens('ejemplo_funcion.txt') 
  Stack= "S"
  df = pd.read_csv('Gramática/GRAMMAR.csv', index_col=0) 
  Stack_temporal=["$"] 
  Stack_input = Stack_begin[0][0]
  identificador = 1 
  nodo_base = nodo(['S', ' ', 0, 0], identificador, ' ')
  nodo_base.estado = True
  # print(Stack_begin)
  for i in Stack_begin:
    i = nodo_detalle(Stack_begin[0][0],Stack_begin[0][1],Stack_begin[0][2],Stack_begin[0][3])
    # print(i.type +" , " + str(i.lexem) + " , " + str(i.line))
  while (df.at[Stack,Stack_input]) == (df.at[Stack,Stack_input]):
    Action = (df.at[Stack,Stack_input]).split(" ",2)
    # print(Action) # ['S', '::=', 'PROGRAM $'].....['PROGRAM', '::=', 'FUNCS PRINC']....etc
    Action = (Action.pop()).split()
    if Action[0] != 'ε':
      Action_list=[]
      for i in range(len(Action)):
        Tok = Action.pop()
        Action_list.append(Tok)
        Stack_temporal.append(Tok)
      Action_list.reverse()
      for i in Action_list:
        identificador += 1
        if i.islower():
          nodos_visitados = []
          for j in Stack_begin:
            if j[0] == i and j not in nodos_visitados:
              nodo_base.insertarNodo(j, identificador)
              break
        else:
          nodo_base.insertarNodo([i, ' ', 0, 0], identificador)
    else:
      identificador += 1
      nodo_base.insertarNodo([Action[0], ' ', 0, 0],identificador)
      nodo_base.actualizarNodo()
    Stack= Stack_temporal.pop()
    nodo_base.actualizarNodo()
    while Stack== Stack_input:
      Stack_begin.pop(0)
      if len(Stack_begin) == 0:
        break
      nodo_base.actualizarNodo()
      Stack= Stack_temporal.pop()
      Stack_input = Stack_begin[0][0]
    if len(Stack_begin) == 0: 
      break
    if Stack.islower():
      break
  # print('aqui')
  # print(nodo_base.lexema)
  # print(nodo_base.token)
  # print(nodo_base.valor)
  # print('------------')
  array_aux=[]
  array_aux = nodo_base

  if Verificador(Stack_begin):
    Imprimir_arbol(nodo_base)
    return nodo_base
  return 

coordenadas = ['FUNC_INIT', 'INICIO', 'IF_INIT', 'LOOP_WHILE', 'ELIF_INIT', 'LOOP_FOR']
tabla_principal = [['Global', 0]]
valores = {'number' : 'hun', 'texto' : 'chaq', 'char' : 'huk', 'true' : 'chiqa', 'false' : 'mana_chiqa' }
id_base = ['number', 'texto', 'char', 'true' ,'false']
id_quechua = ['hun', 'chaq', 'huk', 'chiqa','mana_chiqa']

if __name__=="__main__":
  AnalizadorSin()