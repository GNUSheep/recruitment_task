from django.shortcuts import render, redirect
from .suffle_app import suffle

def index(request):
    if request.method == "POST" and request.FILES.get("inputed_file"):
        try:
            file_content = request.FILES["inputed_file"].read().decode("utf-8")
            request.session['file_content'] = suffle(file_content)
            return redirect('file_view')
        except UnicodeDecodeError:
            error = "Error while trying to read a file"
            request.session['file_content'] = error
            return redirect('file_view')
    return render(request, "index.html")

def file_view(request):
    error_msg = "Error while trying to read a file"
    
    file_content = request.session.get('file_content', error_msg)
    return render(request, "file_view.html", {"file_content": file_content, "is_file": file_content != error_msg})
