from django.views import generic

from register import models, views


class UserProfileView(generic.DetailView):
    model = models.User
    context_object_name = 'user'
    template_name = 'personal_cabinet/profile/view.html'

    def get_object(self, queryset=None):
        user_id = self.request.user.pk
        return self.model.objects.get(pk=user_id)
