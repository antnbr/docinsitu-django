from django.shortcuts import render

# initial view
def render_view(request):
    return render(request, 'render/render_view.html', {})
