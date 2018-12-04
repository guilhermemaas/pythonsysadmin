def custom_message(work_description):
    """Custom body and title. Use to send emails, call this on workQueue if necessary.
    Use the conditions to determinate a custom message to return, delete this, or comment, case you dont use.
    """
    message = {}
    if work_description == 'work_description01':
        message['title'] = f'Custom title message - example {work_description}.\n'
        message['body'] = f'Custom body message - example {work_description}.'
    elif work_description == 'work_description01':
        message['title'] = f'Custom title message - example {work_description}.\n'
        message['body'] = f'Custom body message - example {work_description}.'
    elif work_description == 'work_description01':
        message['title'] = f'Custom title message - example {work_description}.\n'
        message['body'] = f'Custom body message - example {work_description}.'

    return message
