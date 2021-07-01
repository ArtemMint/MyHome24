from django.views import generic
from django.shortcuts import render


class ListFilteringView(generic.View):
    model = None
    search_form = None
    template_name = None

    def __init__(self, *args, **kwargs):
        """
        Initialization filter with list of model`s objects
        and counter with number of objects
        """
        super().__init__(*args, **kwargs)
        self.filter = None
        self.counter = None

    def get(self, request, pk: int = None):
        """
        GET method that collect
        """
        self.filter = self.search_form(
            request.GET,
            queryset=self.get_queryset(),
        )
        self.counter = self.get_queryset().count()
        return self.render_to_response()

    def get_queryset(self):
        try:
            queryset = self.model.objects.all()
        except ValueError:
            queryset = []
        return queryset

    def get_context_data(self):
        context = {
            'filter': self.filter,
            'number': self.counter,
        }
        return context

    def get_template_name(self):
        try:
            template_name = self.template_name
        except:
            print('You should implement template_name variable in class.')
            return None
        return template_name

    def render_to_response(self):
        return render(
            request=self.request,
            template_name=self.get_template_name(),
            context=self.get_context_data(),
        )
