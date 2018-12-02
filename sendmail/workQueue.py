import dateTimeFunctions
import mailFunctions
import customMessages

list_of_works = []
list_of_works.append()

if dia_do_mes() == 1:
    for cliente in range(0, len(clientes)): 
        enviar_email((email_corpo(1, clientes[cliente])))
elif dia_do_mes() == 7:
    for cliente in range(0, len(clientes)):
        enviar_email((email_corpo(2, clientes[cliente])))
elif dia_do_mes() == 28:
    for cliente in range(0, len(clientes)):
        enviar_email((email_corpo(3, clientes[cliente])))