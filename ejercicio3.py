print ("ingrese cantidad de respuestas correctas")
rc = int (input ("rc: "))

print ("ingrese cantidad de respuestas incorrectas")
ri = int (input ("ri: "))

print ("ingrese cantidad de respuestas en blanco")
rb = int (input ("rb; "))

pcr = rc * 3
pri = ri * -1
prb = rb * 0

pf = pcr + pri + prb

print (" el puntaje final es de" , pf )




