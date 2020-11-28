from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import V_item
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.
@xframe_options_exempt
def vault_shelf(request):
    shelf = V_item.objects.order_by('stocked_date')

    context = {
        "shelf": shelf
    }
    return render(request, 'vault/vault_shelf.html', context)


def loginUser(request):
    error = None
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user == None:
            error = "Username or password is incorrect"
        else:
            login(request, user)
            return redirect('Vault:vault_shelf')

    return render(request, 'users/login.html', {'error': error})



@login_required
def upload_file(request):
    form = request.POST
    description = form['description']
    my_file = request.FILES['my_file']
    stocked_date = timezone.now() 
    model = V_item(stocked_date=stocked_date, my_file=my_file, description=description)
    model.save()
    return redirect('Vault:vault_shelf')

@xframe_options_exempt
def s_item(request, item_id):
    item = V_item.objects.get(pk=item_id)

    context = {
        "item": item
    }    
    return render(request, 'vault/vault_shelf.html', context)