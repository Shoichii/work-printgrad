from django.shortcuts import render, redirect
from django.http import JsonResponse
from .form import FillForm
import json
import urllib.parse
import urllib.request
from django.urls import reverse
import datetime

# Create your views here.

def index(request):
    # form_calc = Calculator()
    fill_form = FillForm()
    return render(request, 'mainpage/mainpage.html', {'fill_form': fill_form})

# def calculator(request):
#     data = json.loads(request.body)
#     city_id = data.get('city_id')
#     vacancy_id = data.get('vacancy_id')
#     field = data.get('field')
    
#     if field == 'vacancy':
#         cities = Cities.objects.filter(citiesvacancies__vacancy_id=vacancy_id).values_list('id', flat=True)
#         cities_list = list(cities)
#         city = Cities.objects.get(id=cities_list[0])
        
        
#         vacancies = Vacancies.objects.filter(citiesvacancies__city_id=cities_list[0]).values_list('id', flat=True)
#         vacancies_list = list(vacancies)
#         vacancies_name_list = Vacancies.objects.filter(id__in=vacancies_list).values_list('name', flat=True)
#         vacancies_name_list = list(vacancies_name_list)
#         vacancy_db = Vacancies.objects.get(id=vacancy_id) 
#         name = vacancy_db.name
#         salary = vacancy_db.salary
#         responsibilities = vacancy_db.responsibilities
#         requirements = vacancy_db.requirements.replace('\r', '\\n\\')
#         conditions = vacancy_db.conditions
        
#         return JsonResponse({
#         'status': 'not city',
#         'city': str(city),
#         'vacancies': vacancies_name_list,
#         'vacancies_ids': vacancies_list,
#         'name': name,
#         'salary': salary,
#         'responsibilities': responsibilities,
#         'requirements' : requirements,
#         'conditions' : conditions
#         })
#     elif field == 'city':
#         if city_id == '':
#             vacancies = Vacancies.objects.all()
#             vacancies_name_list = [vacancy.name for vacancy in vacancies]
#             vacancies_ids = [vacancy.id for vacancy in vacancies]
#             return JsonResponse({
#                 'status': 'not vacancy',
#                 'vacancies': vacancies_name_list,
#                 'vacancies_ids': vacancies_ids,
#                 'city_is_not_selected' : True
#             })
        
#         city = Cities.objects.get(id=city_id)
        
        
#         vacancies = Vacancies.objects.filter(citiesvacancies__city_id=city).values_list('id', flat=True)
#         vacancies_list = list(vacancies)
#         vacancies_name_list = Vacancies.objects.filter(id__in=vacancies_list).values_list('name', flat=True)
#         vacancies_name_list = list(vacancies_name_list)
#         vacancy_db = Vacancies.objects.get(id=vacancies_list[0]) 
#         name = vacancy_db.name
#         salary = vacancy_db.salary
#         responsibilities = vacancy_db.responsibilities
#         requirements = vacancy_db.requirements.replace('\r', '\\n\\')
#         conditions = vacancy_db.conditions
            
#         return JsonResponse({
#         'status': 'not vacancy',
#         'city': str(city),
#         'vacancies': vacancies_name_list,
#         'vacancies_ids': vacancies_list,
#         'name': name,
#         'salary': salary,
#         'responsibilities': responsibilities,
#         'requirements' : requirements,
#         'conditions' : conditions
#         })
        
def form_data(request):
    form = FillForm(request.POST, request.FILES) 
    if form.is_valid():
        candidate = form.save()
        candidate_id = candidate.id
    # отправка сообщения в телеграм 
    candidate_url = reverse('admin:mainpage_candidate_change', args=[candidate_id])
    chat_id = '-1001825541211'
    bot_token = '6032602050:AAENsuZ8Mpo1JCQwbL2K1cJV6zYVt0T9HHw'
    message = '❗️❗️❗️Новый отклик\n'
    last_name = request.POST.get('last_name')
    first_name = request.POST.get('name')
    surname = request.POST.get('surname')
    message += f'{last_name} {first_name} {surname}\n'
    message += request.POST.get('phone')
    message += f'\nhttps://работа-принтград.рф/{candidate_url}'
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = urllib.parse.urlencode({'chat_id': chat_id, 'text': message}).encode('utf-8')
    response = urllib.request.urlopen(url, data).read()
    response_json = json.loads(response.decode('utf-8'))
    
        
    request.session['form_was_send'] = True
    return redirect('form_was_send')

def form_was_send(request):
    if 'form_was_send' in request.session:
        del request.session['form_was_send']
        return render(request, 'mainpage/form_was_send.html')
    return redirect('main')