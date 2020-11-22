from .settings import BASE_DIR

def baseProcessor(request):
    context = {
        'base_template': BASE_DIR / 'templates/base_template.html'
    }
    return context