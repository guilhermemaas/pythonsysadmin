def custom_message01(title, body, reason):
    """Custom body and title. Use to send emails, call this on workQueue if necessary.
    Add new methods like this, case you need to give many custom messages more.
    Use the conditions to determinate a custom message to return, delete this, or comment, case you dont use.
    """
    message = {}
    if reason == 1:
        message['title'] = f'Custom title message - {title} example {reason}.\n'
        message['body'] = f'Custom body message {body} example {reason}.'
    elif reason == 2:
        message['title'] = f'Custom title message - {title} example {reason}.\n'
        message['body'] = f'Custom body message {body} example. {reason}'
    elif reason == 3:
        message['title'] = f'Custom title message - {title} example. {reason}\n'
        message['body'] = f'Custom body message {body} example. {reason}'

    return message


"""
#method_2, for example.
def custom_message01(title, body, reason):
    message = {}
    if reason == 1:
        message['title'] = f'Custom title message - {title} example {reason}.\n'
        message['body'] = f'Custom body message {body} example {reason}.'
    elif reason == 2:
        message['title'] = f'Custom title message - {title} example {reason}.\n'
        message['body'] = f'Custom body message {body} example. {reason}'
    elif reason == 3:
        message['title'] = f'Custom title message - {title} example. {reason}\n'
        message['body'] = f'Custom body message {body} example. {reason}'

    return message
"""