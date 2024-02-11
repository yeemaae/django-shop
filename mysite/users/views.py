from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm, MyUserForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:index')
    form = NewUserForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)


@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image)
        profile.save()
    return render(request, "users/profile.html")


class MyLoginView(LoginView):
    form_class = MyUserForm
    redirect_authenticated_user = True


def seller_profile(request, id):
    seller = User.objects.get(id=id)

    context = {"seller": seller}

    return render(request, 'users/sellerprofile.html', context)
