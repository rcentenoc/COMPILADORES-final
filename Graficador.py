import graphviz
#-------------------------- LIBRERIAS
def Verificador(stack_input): 
  if len(stack_input) == 0:
    print ("\n------------- PERTENECE AL LENGUAJE -------------\n")
    return True
  else:
    print ("\n------------- NO PERTENECE AL LENGUAJE -------------\n")
    return False 

def Imprimir_arbol(Input):
  Imprimir_arbol_token(Input)
  Imprimir_arbol_lexema(Input)
  Imprimir_arbol_lineas(Input)
  Imprimir_arbol_semantico(Input)

def Imprimir_arbol_token(input): 
  Arbol = graphviz.Digraph("Arbol", filename="Trees/TreeTOKEN.gv")
  Arbol_de_nodos = []
  Arbol_de_nodos.append(input)
  # print(Arbol_de_nodos)
  # print('-------------')
  while (len(Arbol_de_nodos)):
    Actual = Arbol_de_nodos[0]
    # Arbol.node(str(Actual.valor)+'\n'+str(Actual.token)+'\n'+str(Actual.lexema)+'\n'+str(Actual.linea)) #str(Actual.lexema), str(Actual.linea)
    Arbol.node(str(Actual.valor),str(Actual.token)) #str(Actual.lexema), str(Actual.linea)
    Arbol_de_nodos.pop(0)
    for i in range(len(Actual.nodo_hijo)): 
      Arbol_de_nodos.insert(0,Actual.nodo_hijo[i])
      if Actual.nodo_hijo[i].token.islower():
        # Arbol.node((str(Actual.nodo_hijo[i].token)+'\n'+str(Actual.nodo_hijo[i].lexema)+'\n'+str(Actual.nodo_hijo[i].linea)), color="navy", shape= "egg", style= "bold") 
        Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].token), color="navy", shape= "egg", style= "bold") 
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      else:
        # Arbol.node((str(Actual.nodo_hijo[i].token)+'\n'+str(Actual.nodo_hijo[i].lexema)+'\n'+str(Actual.nodo_hijo[i].linea)), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].token), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      Arbol.edge(str(Actual.valor),str(Actual.nodo_hijo[i].valor))
  Arbol.view()

def Imprimir_arbol_lexema(input): 
  Arbol = graphviz.Digraph("Arbol", filename="Trees/TreeLEXEM.gv")
  Arbol_de_nodos = []
  Arbol_de_nodos.append(input)
  # print(Arbol_de_nodos)
  # print('-------------')
  while (len(Arbol_de_nodos)):
    Actual = Arbol_de_nodos[0]
    if Actual.token.islower():
      Arbol.node(str(Actual.valor), str(Actual.lexema))
    else:
      Arbol.node(str(Actual.valor), str(Actual.token))
    # Arbol.node(str(Actual.valor),str(Actual.lexema)) #str(Actual.lexema), str(Actual.linea)
    # print(Actual.valor)
    Arbol_de_nodos.pop(0)
    for i in range(len(Actual.nodo_hijo)): 
      Arbol_de_nodos.insert(0,Actual.nodo_hijo[i])
      if Actual.nodo_hijo[i].token.islower():
        # Arbol.node((str(Actual.nodo_hijo[i].token)+'\n'+str(Actual.nodo_hijo[i].lexema)+'\n'+str(Actual.nodo_hijo[i].linea)), color="navy", shape= "egg", style= "bold") 
        Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].lexema), color="navy", shape= "egg", style= "bold") 
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      else:
        # Arbol.node((str(Actual.nodo_hijo[i].token)+'\n'+str(Actual.nodo_hijo[i].lexema)+'\n'+str(Actual.nodo_hijo[i].linea)), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].lexema), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      Arbol.edge(str(Actual.valor),str(Actual.nodo_hijo[i].valor))
  Arbol.view()

def Imprimir_arbol_lineas(input): 
  Arbol = graphviz.Digraph("Arbol", filename="Trees/TreeLINE.gv")
  Arbol_de_nodos = []
  Arbol_de_nodos.append(input)
  # print(Arbol_de_nodos)
  # print('-------------')
  while (len(Arbol_de_nodos)):
    Actual = Arbol_de_nodos[0]
    if Actual.token.islower():
      Arbol.node(str(Actual.valor), str(Actual.linea))
    else:
      Arbol.node(str(Actual.valor), str(Actual.token))
    # Arbol.node(str(Actual.valor),str(Actual.lexema)) #str(Actual.lexema), str(Actual.linea)
    # print(Actual.valor)
    Arbol_de_nodos.pop(0)
    for i in range(len(Actual.nodo_hijo)): 
      Arbol_de_nodos.insert(0,Actual.nodo_hijo[i])
      if Actual.nodo_hijo[i].token.islower():
        # Arbol.node((str(Actual.nodo_hijo[i].token)+'\n'+str(Actual.nodo_hijo[i].lexema)+'\n'+str(Actual.nodo_hijo[i].linea)), color="navy", shape= "egg", style= "bold") 
        Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].linea), color="navy", shape= "egg", style= "bold") 
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      else:
        # Arbol.node((str(Actual.nodo_hijo[i].token)+'\n'+str(Actual.nodo_hijo[i].lexema)+'\n'+str(Actual.nodo_hijo[i].linea)), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].lexema), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      Arbol.edge(str(Actual.valor),str(Actual.nodo_hijo[i].valor))
  Arbol.view()

def Imprimir_arbol_semantico(input): 
  Arbol = graphviz.Digraph("Arbol", filename="Trees/TreeSEMANT.gv")
  Arbol_de_nodos = []
  Arbol_de_nodos.append(input)
  while (len(Arbol_de_nodos)):
    Actual = Arbol_de_nodos[0]
    Arbol.node(str(Actual.valor)+'\n'+str(Actual.token)+'\n'+str(Actual.lexema)+'\n'+str(Actual.linea))
    # Arbol.node(str(Actual.valor),str(Actual.lexema)) #str(Actual.lexema), str(Actual.linea)
    # print(Actual.valor)
    Arbol_de_nodos.pop(0)
    for i in range(len(Actual.nodo_hijo)): 
      Arbol_de_nodos.insert(0,Actual.nodo_hijo[i])
      if Actual.nodo_hijo[i].token.islower():
        Arbol.node(str(Actual.nodo_hijo[i].valor)+'\nSimbolo: '+(str(Actual.nodo_hijo[i].token)+'\nLexema: '+str(Actual.nodo_hijo[i].lexema)+'\nLinea: '+str(Actual.nodo_hijo[i].linea)), color="navy", shape= "egg", style= "bold") 
        # Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].linea), color="navy", shape= "egg", style= "bold") 
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      else:
        Arbol.node(str(Actual.nodo_hijo[i].valor)+'\nSimbolo: '+(str(Actual.nodo_hijo[i].token)+'\nLexema: '+str(Actual.nodo_hijo[i].lexema)+'\nLinea: '+str(Actual.nodo_hijo[i].linea)), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        # Arbol.node(str(Actual.nodo_hijo[i].valor), str(Actual.nodo_hijo[i].lexema), color="crimson", shape= "house", style= "filled", fillcolor= "palegreen")      
        # str(Actual.nodo_hijo[i].lexema), str(Actual.nodo_hijo[i].linea),
      Arbol.edge(str(Actual.valor),str(Actual.nodo_hijo[i].valor))
  Arbol.view()
