import date_functions
import mail_functions
import custom_messages

#List of the description of work, for example, "Reminder to check service x on server Linux y.", it would, "verify_service_x_server_y".
work_descriptions = ['work_description01', 'work_description02', 'work_description03'] 

#List of the clients, ou recepients, use this thinking in your business(name of client) or service infrastructure(name of service ou server). 
list_of_recipient = ['client01', 'client02', 'client03']

#List of the emails sent to the execution queue. This recept dictionarys of emails to send.
work_queue = []

#Verifiy the day of month as a condition, you could also use another function from the date_functions.py file.
if date_functions.day_of_month() == 1:
    for recipient in range(0, len(list_of_recipient)):
        work_queue.append({'recipient': list_of_recipient[recipient], 'work_description': work_descriptions[0]})
elif date_functions.day_of_month() == 7:
    for recipient in range(0, len(list_of_recipient)):
        work_queue.append({'recipient': list_of_recipient[recipient], 'work_description': work_descriptions[1]})
elif date_functions.day_of_month() == 21:
    for recipient in range(0, len(list_of_recipient)):
        work_queue.append({'recipient': list_of_recipient[recipient], 'work_description': work_descriptions[2]})


#Execute queue work and send e-mail:
for email in range(0, len(work_queue)):
    mail_functions.send_mail(work_queue[email], work_queue[email])
