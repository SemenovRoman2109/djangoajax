from django.shortcuts import render
from .models import *
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
def show_book(request):
    context = {
        "books":Book.objects.all()  
    }
    # если отправлен ajax запрос
    if request.method == 'POST':
        # получаем даные из Input 
        filter_text = request.POST.get('filter-text')
        # Фильтруем книги с модели Book по имени
        books = Book.objects.filter(name__icontains = filter_text)
        # Создаем словарь "данные книг"
        data = {
            'html_books_list': render_to_string( "bookpartial.html",{ #рендерим html файл в строку
                'books': books,# передаем список книг
                'filter_text': filter_text# передаем ключевое слово
            })
        }
        # Возвращаем ответ Json к данных книг
        return JsonResponse(data)
    return render(request, 'book_list.html', context)
    
    