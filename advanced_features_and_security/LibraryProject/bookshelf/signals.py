from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(Book)

    permissions = {
        "can_view": "Can view book",
        "can_create": "Can create book",
        "can_edit": "Can edit book",
        "can_delete": "Can delete book",
    }

    for codename, name in permissions.items():
        Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

    group_permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in group_permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            permission = Permission.objects.get(codename=perm)
            group.permissions.add(permission)
