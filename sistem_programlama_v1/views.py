from django.shortcuts import render

# Create your views here.
def faculty_list(request):
    return render(request, 'sistem_programlama_v1/faculty_list.html', {})