import datetime
    
now = datetime.datetime.now()

YEAR        = datetime.date.today().year     # the current year
MONTH       = datetime.date.today().month    # the current month
DATE        = datetime.date.today().day      # the current day
HOUR        = datetime.datetime.now().hour   # the current hour
MINUTE      = datetime.datetime.now().minute # the current minute
SECONDS     = datetime.datetime.now().second #the current second

if HOUR == 0:
    hour_12 = 12
    ampm = "A.M."
elif HOUR < 12:
    hour_12 = HOUR
    ampm = "A.M."
elif HOUR == 12:
    hour_12 = 12
    ampm = "P.M."
else: 
    hour_12 = HOUR - 12
    ampm = "P.M."

if HOUR < 12:
    saudacao = "Bom dia"
elif HOUR < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

print(f"{saudacao}, gostária de saber a Música tocando no momento?")

x = input("Sim/Não: ").strip().upper()
if x in["SIM", "SI", "S"]:
    print(f'Now Playing: "{HOUR} {ampm}"')
else :
    print (f'Alias, podemos te dar o Horário com mais Precisão, gostaria de saber?')
    y = input("Sim/Não: ").strip().upper()
    if y in["SIM", "SI", "S"]:
        print(f"Data: {DATE:02d}/{MONTH:02d}/{YEAR}")
        print(f"Hora: {hour_12:02d}:{MINUTE:02d}:{SECONDS:02d} {ampm}")
