hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
minutosAHora = (dura+min)//60
horaDeSalida = (hora + minutosAHora)%24
minutosDeSalida = (min+dura)%60

print("Hora de salida: ", str(horaDeSalida),":",str(minutosDeSalida))