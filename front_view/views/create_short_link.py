from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from url.models import Url


@login_required(login_url='/login/')
@require_http_methods(['GET', "POST"])
def create_short_link(request):
    if request.method == 'GET':
        return render(request, 'create_short_link.html')
    elif request.method == 'POST':
        orginal_url = request.POST['orginal_url']

        try:
            url = Url.objects.create(
                creator=request.user, orginal_url=orginal_url)
        except:
            context = {'msg': "PLEASE ENTER VALID URL"}
            return render(request, 'create_short_link.html', context)

        base_url = str(request.build_absolute_uri()).split(
            "/create-short-link")[0]

        context = {
            "msg": f"THIS IS YOUR SHORT URL: {base_url}/{url.short_url_id}"}
        return render(request, 'create_short_link.html', context)
