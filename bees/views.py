from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import Contactform

def homepage(request):
    return render(request, 'homepage.html')

def chi_siamo(request):
    return render(request, 'chi_siamo.html')

def contatti(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            try:
                nome = str(form.cleaned_data["nome"]) + " " + str(form.cleaned_data["cognome"])
                indirizzo = str(form.cleaned_data["email"])
                sbjt = nome + " send you a message via Addabees"
                text = "message from: " + indirizzo + "\n\n" + "text:" + "\n" + str(form.cleaned_data["messaggio"])
                send_mail(
                    subject=sbjt,
                    message=text,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["m.maggio88@gmail.com"],
                    fail_silently=False
                )
                form = Contactform()
                messages.add_message(request, messages.SUCCESS, "Il tuo messaggio è stato inviato correttamente. Grazie!")
                return render(request, 'contatti.html', {"form" : form})
            except Exception as e:
                return render(request, "550.html")
    else:
        form = Contactform()

    context = {"form" : form}
    return render(request, 'contatti.html', context)

def il_miele(request):
    return render(request, 'il_miele.html')

def gallery(request):
    with open('bees/static/piante.md', 'r') as f:
        content=f.read()
    context = {"content" : content}
    return render(request, 'gallery.html', context)

    
