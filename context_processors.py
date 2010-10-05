from django.conf import settings

def settings_context(request):
    base_url = 'http%s://%s' % ('s' if request.is_secure() else '',
                                request.get_host())

    return {
        'site_name': settings.SITE_NAME,
        'site_description': settings.SITE_DESCRIPTION,
        'site_authors': settings.SITE_AUTHORS,
        'site_base_url': base_url,
        'google_analytics_id': getattr(settings, 'GOOGLE_ANALYTICS_ID', None),
    }
