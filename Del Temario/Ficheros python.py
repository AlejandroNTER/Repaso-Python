line1= "Es mi primera linea"
line2= "Es mi segunda linea"
line3= "Es mi tercera linea"
line4= "¡Es el final del fichero!"

fichero1= open("primerfichero.txt","a", encoding="utf-8")
fichero1.write(line1)

with open("segundofichero.txt","r",encoding="utf-8") as fichero2:
    #fichero2.writelines([line2,line3,line4])
    for line in fichero2:
        fichero1.write(line)
    fichero2.close()

fichero1.close()