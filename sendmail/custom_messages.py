def custom_message01(title_word, body_word, work_description):
    """Custom body and title. Use to send emails, call this on workQueue if necessary.
    Add new methods like this, case you need to give many custom messages more.
    Use the conditions to determinate a custom message to return, delete this, or comment, case you dont use.
    """
    message = {}
    if work_description == 1:
        message['title'] = f'Custom title message - {title_word} example {work_description}.\n'
        message['body'] = f'Custom body message {body_word} example {work_description}.'
    elif work_description == 2:
        message['title'] = f'Custom title message - {title_word} example {work_description}.\n'
        message['body'] = f'Custom body message {body_word} example {work_description}.'
    elif work_description == 3:
        message['title'] = f'Custom title message - {title_word} example. {work_description}\n'
        message['body'] = f'Custom body message {body_word} example {work_description}.'

    return message


#method_2, for example, without conditions.
#def custom_message02(title_word, body_word, work_description):
#    message = {}
#    message['title'] = f'Custom title message - {title_word} example {work_description}.\n'
#    message['body'] = f'Custom body message {body_word} example {work_description}.'
#
#    return message
