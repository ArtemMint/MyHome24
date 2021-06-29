import random

from rest_framework import views
from rest_framework.response import Response
from functools import reduce

from admin_panel import utils, models


class StatisticView(views.APIView):

    def get(self, request):
        statistic = utils.get_short_statistic()
        return Response(statistic)


class StatisticChartView(views.APIView):
    invoice_model = models.Invoice
    transaction_model = models.AccountTransaction

    def get(self, request):
        months = [
            i for i in range(1, 13)
        ]
        #TODO add invoice statistic
        invoice_in_total = [
            random.randrange(100, 15000)
            for _ in range(0, 12)
        ]
        invoice_out_total = [
            random.randrange(100, 15000)
            for _ in range(0, 12)
        ]
        transaction_in_total = []
        transaction_indebtedness_total = []

        for month in months:
            transactions_in = self.transaction_model.objects.filter(
                created_date__month=month,
                created_date__year=utils.get_current_year(),
                type='Приход',
            )
            transactions_indebtedness = self.transaction_model.objects.filter(
                created_date__month=month,
                created_date__year=utils.get_current_year(),
                type='Расход',
            )

            if transactions_indebtedness:
                total = 0
                for el in transactions_indebtedness:
                    total += abs(el.total)
                transaction_indebtedness_total.append(total)
            else:
                transaction_indebtedness_total.append(0)

            if transactions_in:
                total = 0
                for el in transactions_in:
                    total += el.total
                transaction_in_total.append(total)
            else:
                transaction_in_total.append(0)

        labels = [
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь",
        ]

        statistic = {
            'labels': labels,
            'invoice_in_total': invoice_in_total,
            'invoice_out_total': invoice_out_total,
            'transaction_in_total': transaction_in_total,
            'transaction_indebtedness_total': transaction_indebtedness_total,
        }
        return Response(statistic)
