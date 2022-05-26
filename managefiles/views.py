from django.shortcuts import render


def manage_files(request):
    return render(request, 'managefiles/managefiles.html')
