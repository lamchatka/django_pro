from django.shortcuts import render
from .forms import NewUserForm

def register(request):
    form = NewUserForm() # создали экземпляр класса-формы
    context = {
        "form": form
    }
    return render(request, "users/register.html", context=context)
