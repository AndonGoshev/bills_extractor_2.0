import time

def extensions():
    return ['pdf', 'txt']


def total_attempts_reached():
    print('Total amount of attempts reached! Please try again later!')
    time.sleep(3)
    exit()


def company_name_constraint():
    return ['yettel']


def extension_error():
    print(f'The software does not support this type of a file! You can only use {", ".join(extensions())}')
    time.sleep(3)
    exit()

