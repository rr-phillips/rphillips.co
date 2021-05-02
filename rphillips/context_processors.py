from .settings import BASE_DIR, STATIC_ROOT

def baseProcessor(request):
    context = {
        'base_template': BASE_DIR / 'templates/static_pages/index.html',
        'base_dir': BASE_DIR,
        'static_dir': STATIC_ROOT
    }
    return context