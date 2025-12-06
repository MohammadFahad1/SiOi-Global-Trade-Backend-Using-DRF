from django.shortcuts import redirect

def api_root(request):
    return redirect('api-root')