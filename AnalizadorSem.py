from Ll1 import AnalizadorSin, coordenadas, tabla_principal,valores,id_base,id_quechua
from assembler import generador_assambler,fin

symbol_table = []
variables_asambler= []
vars_assambler=[]

class Symbol:
  def __init__(self, token, linea, lexema = None, valor = None):
    self.valor = valor
    self.token = token
    self.lexema = lexema
    self.linea = linea 
    self.nodo_padre = None
    self.id = id

def acoplador(variables_asambler,vars_assambler):
  respuesta=AnalizadorSin()
  Recorrer_nodos(respuesta)
  generador_assambler(variables_asambler,vars_assambler)

def add_Symbol(nodo):
  if find_symbol(nodo.lexema):
    print( '\n► ERROR: En la linea ',nodo.linea,', la variable ',nodo.lexema, ' ya fue inicializada.')
    print(nodo.valor[1][0])
    return
  else:
    tipo=verificar(nodo.valor)
    for i in nodo.valor:
      if i[0] == 'id':
        if find_symbol(i[1]) == False:
          print('\n► ERROR: En la linea ',nodo.linea,',' ,i[1],' es una variable sin definir.')
          return
      # if i[1]=="+"or i[1]=="-"or i[1]== "*"or i[1]=="/":
    if tipo == False:
      print('\n► ERROR: En la linea ',nodo.valor,' la operacion es invalida.')
      return
    elif tipo != nodo.token:
      print('\n► ERROR: En la linea ',nodo.valor,' error de sintaxis.')
      return
    # elif (nodo.valor[1][1]=='+' or nodo.valor[1][1]=='-' or nodo.valor[1][1]=='*' or nodo.valor[1][1]=='/'):
    #   print('es ',nodo.valor[1][1])       
# " de la línea ", i.valor, "
    symbol_table.append(nodo)
    variables_asambler.append(nodo.lexema)
  print(' TIPO                         [RESULTADO]')
  print('   ↓                                ↓')

  for i in symbol_table:
    print(i.token," → " ,i.lexema, " fue inicializada y definida con exito en la línea", i.linea,".")
    print("SCOPE ► ID:",i.lexema,"|| token:",i.valor[0][0],"|| lexema:",i.valor[0][1],"|| token:",i.valor[1][0],"|| lexema:",i.valor[1][1],"|| token:",i.valor[2][0],"|| lexema:",i.valor[2][1],".\n")
  print('-----------------------------------------------------------------------') 
  print(i.linea) 
  
def find_symbol(param):
  for i in symbol_table:
    if i.lexema == param:
      return i
    else:
      return False
  symbol_table.reverse()
  return 

def Recorrer_nodos(param):
  stack_temporal=[]
  stack_auxiliar=[]
  stack_temporal.append(param)
  estado = False
  estado_recursivo = False
  posicion = 0
  while (len(stack_temporal)): 
    Actual = stack_temporal[0]
    if Actual.token == 'VARIABLES':
      estado = True
    if Actual.token.islower() and estado == True and estado_recursivo == False :
      if posicion == 0:
        nuevo = Symbol(Actual.lexema,Actual.linea)
        posicion +=1
      elif posicion == 1:
        nuevo.lexema=Actual.lexema
        posicion +=1
      elif posicion == 2:
        posicion +=1
      elif posicion == 3 and Actual.lexema != ';':
        VAR = [Actual.token, Actual.lexema]
        stack_auxiliar.append(VAR)
      else:
        stack_auxiliar.remove(['ε', ' '])
        nuevo.valor=stack_auxiliar
        nuevo.nodo_padre = tabla_principal[0][0]
        nuevo.id = tabla_principal[0][1]
        vars_assambler.append(stack_auxiliar)
        stack_auxiliar = []
        estado = False        
        add_Symbol(nuevo)
        posicion = 0
    if Actual.token == 'VARIABLE_FORMA_FOR':
      estado_recursivo = True
    if Actual.token.islower() and estado_recursivo == True and estado == False:
      if posicion == 0:
        nuevo = Symbol(Actual.lexema,Actual.linea)
        posicion += 1
      elif posicion == 1:
        nuevo.lexema=Actual.lexema
        posicion += 1
      elif posicion == 2:
        posicion += 1
      elif posicion == 3 and Actual.lexema != ',':
        VAR = [Actual.token, Actual.lexema]
        stack_auxiliar.append(VAR)
      else:
        nuevo.valor=stack_auxiliar
        tabla_principal.reverse()
        nuevo.nodo_padre = tabla_principal[0][0]
        nuevo.id = tabla_principal[0][1]
        estado_recursivo = False        
        add_Symbol(nuevo)
    referido = False
    if Actual.token in coordenadas:
      PadreElegido = Actual.token
      PadreElegidoId = Actual.valor
      referido = True
    if Actual.lexema == '{' or Actual.lexema == '(': 
      if referido == True:
        tabla_principal.append([PadreElegido, PadreElegidoId])
        referido = False
    if Actual.lexema == '}':
      tabla_principal.pop()
      referido = False
    stack_temporal.pop(0)
    for i in range(len(Actual.nodo_hijo)-1,-1,-1): 
        stack_temporal.insert(0,Actual.nodo_hijo[i])
        # print(stack_temporal)    

def verificar(lista):
  if lista[0][0] == 'id': 
    tipo = find_symbol(lista[0][1])
  else:
    tipo = valores[lista[0][0]]
  for i in range(len(lista)):
    if lista[i][0] == 'id':      
      if find_symbol(lista[i][1]) in id_quechua:
        if tipo != find_symbol(lista[i][1]):
          return False
    elif [lista[i][0]] in id_base:
      if tipo != valores[lista[i][0]]:
        return False
  return tipo


if __name__=='__main__':
  acoplador(variables_asambler,vars_assambler)
  print ("variables: ", variables_asambler)
  print("vars: ", vars_assambler)
  fin()
  # print(symbol_table)
