X = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = X//86400
segundos_restantes = X%86400
horas = segundos_restantes//3600
segundos_restantes = segundos_restantes%3600
minutos = segundos_restantes//60
segundos = segundos_restantes%60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
