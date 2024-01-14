# Generated by Django 4.2 on 2023-05-29 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Города',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Citizenships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='гражданство')),
            ],
            options={
                'verbose_name': 'Гражданство',
                'verbose_name_plural': 'Гражданство',
            },
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='статус')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('salary', models.CharField(max_length=200, verbose_name='оплата')),
                ('responsibilities', models.TextField(default='', verbose_name='Обязанности')),
                ('requirements', models.TextField(default='', verbose_name='Требования')),
                ('conditions', models.TextField(default='', verbose_name='Условия')),
            ],
            options={
                'verbose_name': 'Вакансии',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, null=True, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('custom_citizenship', models.CharField(blank=True, max_length=20, null=True, verbose_name='Другое гражданство')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Время создания')),
                ('status_date', models.DateTimeField(blank=True, null=True, verbose_name='Время смены статуса')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметка')),
                ('citizenship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.citizenships', verbose_name='Гражданство')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.cities', verbose_name='Город')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainpage.statuses', verbose_name='Статус')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.vacancies', verbose_name='Вакансия')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
            },
        ),
        migrations.CreateModel(
            name='CitiesVacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainpage.cities', verbose_name='Город')),
                ('vacancy', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainpage.vacancies', verbose_name='Вакансия')),
            ],
            options={
                'verbose_name': 'Города и вакансии',
                'verbose_name_plural': 'Города и вакансии',
                'unique_together': {('city', 'vacancy')},
            },
        ),
    ]