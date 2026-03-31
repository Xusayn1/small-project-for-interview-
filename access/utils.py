from .models import AccessRule


def check_permission(user, element_name, action):
    if not user:
        return False

    try:
        rule = AccessRule.objects.get(
            role=user.role,
            element__name=element_name
        )
    except AccessRule.DoesNotExist:
        return False

    return getattr(rule, f"can_{action}", False)
