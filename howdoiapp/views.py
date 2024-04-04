from django.shortcuts import render
import howdoi

def howdoi_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        answer = howdoi.howdoi(query)
        return render(request, 'howdoiapp/howdoi.html', {'query': query, 'answer': answer})
    return render(request, 'howdoiapp/howdoi.html', {})
