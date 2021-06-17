import datetime


def get_current_date():
    return datetime.datetime.now().strftime('%m/%d/%y')


def generate_number(model):
    date = datetime.datetime.now().strftime('%d%m%y')
    if model.objects.count() > 0:
        initial_len = '00000'
        number = int(model.objects.all().count()) + 1
        initial_len = initial_len[0:(5 - (int(len(str(number)))))]
        number = f'{date}{initial_len}{number}'
    else:
        number = f'{date}00001'
    return number
