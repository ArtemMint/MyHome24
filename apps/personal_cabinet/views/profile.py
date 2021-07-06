from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages

from admin_panel import models
from register import models as reg_models, forms, views


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


class UpdateUserProfileView(generic.View):
    model = reg_models.User
    form_class = forms.UpdateUserForm
    context_object_name = 'user_form'
    success_url = 'personal_cabinet:user_profile'
    template_name = 'personal_cabinet/profile/update.html'

    def get_object(self, queryset=None):
        user_id = self.request.user.pk
        return self.model.objects.get(pk=user_id)

    def get(self, request):
        form = forms.UpdateUserForm(
            instance=self.get_object(),
        )
        return self.render_template(form)

    def post(self, request):
        form = forms.UpdateUserForm(
            self.request.POST or None,
            self.request.FILES,
            instance=self.get_object(),
        )
        if form.is_valid():
            user = form.save(commit=False)
            raw_password1 = form.cleaned_data['password1']
            raw_password2 = form.cleaned_data['password2']
            if raw_password1:
                if raw_password1 == raw_password2:
                    user.set_password(raw_password1)
                    user.save()
                    messages.success(self.request, 'Ваш профиль обновлен!')
                    return redirect(self.success_url)
                else:
                    messages.success(self.request, 'Пароли не совпадают!')
            else:
                user.save()
                messages.success(self.request, 'Ваш профиль обновлен!')
                return redirect('personal_cabinet:user_profile')
        else:
            messages.success(self.request, 'Ошибка обновление!')
        return self.render_template(form)

    def render_template(self, form):
        return render(
            self.request,
            self.template_name,
            {
                'user_form': form,
            }
        )
