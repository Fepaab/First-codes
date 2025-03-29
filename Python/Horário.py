import datetime
    
now = datetime.datetime.now()

YEAR        = datetime.date.today().year     # the current year
MONTH       = datetime.date.today().month    # the current month
DATE        = datetime.date.today().day      # the current day
HOUR        = datetime.datetime.now().hour   # the current hour
MINUTE      = datetime.datetime.now().minute # the current minute
SECONDS     = datetime.datetime.now().second #the current second

if HOUR < 12:
    saudacao = "Bom dia"
elif 12 <= HOUR < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa Noite"

print(f"{saudacao}, gostaria de saber o horário com mais precisão?")

x = input("Sim/Não: ").strip().upper()
if x in["SIM", "SI", "S"]:
    print(f"Data: {DATE} : {MONTH} : {YEAR}")
    print("Hora: ",HOUR,":",MINUTE,":",SECONDS)
else :
    print(f"Ok então, {saudacao}.")