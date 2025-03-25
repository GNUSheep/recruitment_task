from django.shortcuts import render
from .checker import is_valid

# Create your views here.
def index(request):
    pesel = ""
    msg = ""
    
    if "text_box" in request.POST:
        pesel = request.POST['text_box']
        pesel = pesel.strip()
        (is_ok, birth_date_or_err, gender) = is_valid(pesel)

        if is_ok:
            msg = f"PESEL is correct, date of birth: {birth_date_or_err} and gender: {gender}"
        else:
            msg = birth_date_or_err

    return render(request, "index.html", {"pesel": pesel, "msg": msg})
