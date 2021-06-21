import datetime
from functools import reduce

from admin_panel import models


def get_short_statistic():
    accounts = models.Account.get_accounts_list().filter()

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
    account_balance = models.AccountTransaction.get_balance()

    return {
        'transaction_balance': round(transaction_balance, 2),
        'account_balance': round(account_balance, 2),
        'account_indebtedness': round(account_indebtedness, 2)
    }


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
