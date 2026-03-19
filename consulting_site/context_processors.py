from django.conf import settings

def settings_context(request):
    """Add settings to template context"""
    return {
        'settings': settings,
    }