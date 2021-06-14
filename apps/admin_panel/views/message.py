from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required

from admin_panel import models
from admin_panel import forms


@login_required(login_url='/admin/site/login')
def message_list_view(request):
    return render(
        request,
        'admin_panel/messages/index.html',
        {
            'messages_list': models.Message.get_messages_list(),
        }
    )


@login_required(login_url='/admin/site/login')
def message_create_view(request):
    message_form = forms.MessageForm()
    if request.POST:
        message_form = forms.MessageForm(
            request.POST,
        )
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.sender = request.user.email
            message.save()
            messages.success(request, 'Сообщение отправлено!')
            return redirect('admin_panel:message_list')
        else:
            messages.warning(request, 'Ошибка отправки!')
    return render(
        request,
        'admin_panel/messages/create.html',
        {
            'form': message_form,
        }
    )


class MessageDetailView(generic.DetailView):
    model = models.Message
    template_name = 'admin_panel/messages/detail.html'
    context_object_name = 'message'
