import datetime
from functools import reduce

from admin_panel import models


# decorator function
def get_round_result(func):
    def rounded(*args, **kwargs):
        result = func
        return round(result, 2)
    return rounded


def get_short_statistic():
    transaction_balance, account_indebtedness = 0.00, 0.00
    try:
        accounts = models.Account.get_accounts_list().filter()
    except models.Account.DoesNotExist:
        accounts = []

    try:
        account_balance = models.AccountTransaction.get_balance()
    except models.AccountTransaction.DoesNotExist:
        account_balance = []

    if accounts:
        for account in accounts:
            transaction_balance = reduce(
                lambda x, y: x + y if account.balance() >= 0 else x - y,
                [
                    account.balance()
                    for account in accounts
                ]
            )
            account_indebtedness = reduce(
                lambda x, y: x + y,
                [
                    account.balance()
                    if account.balance() < 0 else 0
                    for account in accounts
                ]
            )

    return {
        'transaction_balance': transaction_balance,
        'account_balance': account_balance,
        'account_indebtedness': account_indebtedness,
    }


def get_current_date():
    return datetime.datetime.now().strftime('%m/%d/%y')


def get_current_year():
    return datetime.datetime.now().year


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
