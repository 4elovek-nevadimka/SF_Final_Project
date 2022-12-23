from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from final_project import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user(sender, instance, created, **kwargs):
    role_group = {'CL': 'Client', 'SC': 'Service company', 'MN': 'Manager'}
    if created:
        try:
            group = Group.objects.get(name=role_group.get(instance.role))
            instance.groups.add(group)
        except Group.DoesNotExist:
            pass
