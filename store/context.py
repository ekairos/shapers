import re
from .models import Category


def in_store(request):
    """
    Returns values from Store app used in other apps templates
    Add this file to template context processors in /shapers/settings.py
    """

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'is_in_store': bool(re.search("^/store/", request.path))
    }
    return context
