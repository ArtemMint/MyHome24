from django.dispatch import receiver
from django.db.models.signals import post_save
from register.models import User


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    """User

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
        created ([type]): [description]
    """
    if created:
        full_name = f'{instance.first_name} {instance.last_name} {instance.middle_name}'
        User.objects.filter(pk=instance.pk).update(full_name=full_name)


@receiver(post_save, sender=User)
def update_client(sender, instance, **kwargs):
    """update User

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
    """
    full_name = f'{instance.first_name} {instance.last_name} {instance.middle_name}'
    User.objects.filter(pk=instance.pk).update(full_name=full_name)
