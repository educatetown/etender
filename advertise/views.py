from django.shortcuts import render
from .forms import AdvertisingForm


def advertising_clients(request):
    form = AdvertisingForm()

    if request.method == "POST":
        form = AdvertisingForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'thankyou.html')

        else:
            print("Error form INVALID!")

    return render(request, 'advertise/advertising_clients.html', {'form': form})


