from django.views import generic

from admin_panel import models
from register import models as reg_models, views


class UserProfileView(generic.DetailView):
    model = reg_models.User
    context_object_name = 'user'
    template_name = 'personal_cabinet/profile/view.html'

    def get_object(self, queryset=None):
        user_id = self.request.user.pk
        return self.model.objects.get(pk=user_id)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['flat_list'] = models.Flat.objects.filter(owner=self.get_object())
        return context
