from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render

from url.models import Url


@require_http_methods(['GET'])
def short_url_view(request, short_url_id):
    try:
        url = Url.objects.get(short_url_id=short_url_id)
    except Url.DoesNotExist:
        return render(request, "404.html")
    return redirect(url.orginal_url)
