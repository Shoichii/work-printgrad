from django.db import models
import datetime


# Create your models here.

# class Cities(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Город')
    
#     class Meta:
#         verbose_name = 'Города'
#         verbose_name_plural = 'Города'
    
#     def __str__(self):
#         return self.name
    
# class Vacancies(models.Model):
#     name = models.CharField(max_length=200, verbose_name='название')
#     salary = models.CharField(max_length=200, verbose_name='оплата')
#     responsibilities = models.TextField(default='', verbose_name='Обязанности')
#     requirements = models.TextField(default='', verbose_name='Требования')
#     conditions = models.TextField(default='', verbose_name='Условия')
    
#     class Meta:
#         verbose_name = 'Вакансии'
#         verbose_name_plural = 'Вакансии'
    
#     def __str__(self):
#         return self.name
    
# class CitiesVacancies(models.Model):
#     city = models.ForeignKey(Cities, on_delete=models.CASCADE, default=None, verbose_name='Город')
#     vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE, default=None, verbose_name='Вакансия')
    
#     class Meta:
#         unique_together = ('city', 'vacancy')
#         verbose_name = 'Города и вакансии'
#         verbose_name_plural = 'Города и вакансии'
    
#     def __str__(self):
#         return f"{self.city} - {self.vacancy}"
    
    
class Citizenships(models.Model):
    name = models.CharField(max_length=100, verbose_name='гражданство')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Гражданство'
        verbose_name_plural = 'Гражданство'
        
class Statuses(models.Model):
    name = models.CharField(max_length=120, verbose_name='статус')
    
    def __str__(self):
        return self.name
    
    
# class Sources(models.Model):
#     name = models.CharField(max_length=120, verbose_name='Откуда узнали')
    
#     def __str__(self):
#         return self.name
    
    
class Candidate(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    # surname = models.CharField(max_length=50,verbose_name='Отчество',null=True)
    # last_name = models.CharField(max_length=50,verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='День рождения')
    citizenship = models.ForeignKey(Citizenships,on_delete=models.CASCADE,verbose_name='Гражданство', null=True, blank=True)
    custom_citizenship = models.CharField(max_length=20, verbose_name='Другое гражданство', null=True, blank=True)
    # city = models.ForeignKey(Cities,on_delete=models.CASCADE,verbose_name='Город')
    # vacancy = models.ForeignKey(Vacancies,on_delete=models.CASCADE,verbose_name='Вакансия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    resume_link = models.TextField(verbose_name='Ссылка на резюме', null=True, blank=True)
    resume_file = models.FileField(verbose_name='Резюме', upload_to='files/', null=True, blank=True)
    # sources = models.ForeignKey(Sources,on_delete=models.CASCADE, verbose_name='Откуда узнали', null=True, blank=True)
    status = models.ForeignKey(Statuses, verbose_name='Статус', on_delete=models.CASCADE, default=1)
    start_date = models.DateTimeField(blank=True,null=True, verbose_name='Время создания')
    status_date = models.DateTimeField(blank=True,null=True,verbose_name='Время смены статуса')
    note = models.TextField(blank=True,null=True, verbose_name='Заметка')
    
    
    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
    
    
    def __str__(self):
        return f'Кандидат ({self.pk})'
    
    def save(self, *args, **kwargs):
        time_format = "%Y-%m-%d %H:%M"
        current_time = datetime.datetime.now()
        time_str = current_time.strftime(time_format)
        if self.pk is not None:
            old_user = Candidate.objects.get(pk=self.pk)
            if old_user.status != self.status:
                self.status_date = time_str
        else:
            self.start_date = time_str
        super(Candidate, self).save(*args, **kwargs)
        
    