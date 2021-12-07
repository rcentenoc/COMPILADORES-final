file = open("codigo.s", 'w')

def generador_assambler(x,y):
  file.write(".data\n")
  crear_variable(x)
  file.write("\n.text\nmain:\n")
  generar_variable(y)

def crear_variable(x):
  for i in x:
    file.write("\tvar_"+ str(i) + ": .word 0:1\n")


def generar_variable(y):
  var(y[0][0][1])
  var2(y[0][2][1])
  generar_suma()


def var(y):
  file.write("\tli $a0, " + str(y) + "\n")
  file.write ("\tsw $a0, 0($sp)\n")
  file.write ("\taddiu $sp, $sp-4\n")

def var2(y):
  file.write("\tli $a0, "+ str(y) +"\n")


def generar_suma():
  file.write("\tlw $t1, 4($sp)\n\tadd $a0, $t1, $a0\n\taddiu $sp, $sp, 4\n")



def fin():
  file.write("jr $ra")
  file.close()


