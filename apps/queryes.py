import django
import os
import datetime

from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag


#
#     obj = Entry.objects.filter(author__name__contains='alexander89')
#     print(f"----{obj}")
#
#     o = Entry.objects.get(id=1)
#
#     print(o)
#
#     o = Entry.objects.filter(author__email__contains='alexander89@gmail.com')
#     print(o)
#
#
#     o = Author.objects.all()
#     print(o)
#
# obj = Entry.objects.filter(author__authorprofile__city=None)
# print(obj)
#
#
# og= AuthorProfile.objects.filter(city=None)
# print(f"----{og}")

# print(Entry.objects.get(id__exact=4))
# print(Entry.objects.get(id=4))  # Аналогично exact
# print(Blog.objects.get(name__iexact="Путешествия по миру"))
# print(Blog.objects.filter(name__contains="Путешествия"))
# print(Entry.objects.filter(headline__contains='мод'))
# print(Entry.objects.filter(id__in=[1, 3, 4]))
# print(Entry.objects.filter(number_of_comments__in='123'))

# inner_qs = Blog.objects.filter(name__contains='Путешествия')
# print(inner_qs)
# entries = Entry.objects.filter(blog__in=inner_qs)
# print(entries)
#
#
# print(Entry.objects.filter(number_of_comments__gt=10))
# print(Entry.objects.filter(number_of_comments__gte=10))
# print(Entry.objects.filter(number_of_comments__lt=10))
# print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
# print(Entry.objects.filter(headline__lte="Зя"))
# print(Entry.objects.filter(headline__lte="Зя"))
# print(Entry.objects.filter(headline__startswith='Как'))
# print(Entry.objects.filter(headline__endswith='ния'))
# start_date = datetime.date(2023, 1, 1)
# end_date = datetime.date(2023, 12, 31)
# print(Entry.objects.filter(pub_date__range=(start_date, end_date)))
# print(Entry.objects.filter(pub_date__year=2023))
# # Вывести записи старше 2022 года
# print(Entry.objects.filter(pub_date__year__lt=2022))
# # Вывести все записи за февраль доступных годов, отобразить название, дату публикации, заголовок
# print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
# print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(pub_date__day__lte=15).values_list("author__name").distinct())
# print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(pub_date__day__lte=15).values("author__name").distinct())
# print(Entry.objects.filter(pub_date__date=datetime.date(2021, 6, 1)))
#
#

# print(AuthorProfile.objects.filter(city__isnull=True))
# print(AuthorProfile.objects.filter(city__isnull=False))
#

# print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))

# print(Author.objects.filter(email__iregex=r'\w+(@gmail.com|@mail.ru)'))
#
#
#
# all_obj = Blog.objects.all()
# print("Вывод всех значений в таблице Blog\n", all_obj)


# all_obj = Blog.objects.first()
# print("Вывод первого значения в таблице Blog\n", all_obj)
#

#
# all_obj = Blog.objects.all()
# obj_first = all_obj.first()
# print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
#        f"Все значения = {all_obj}")
#
#

#
# all_obj = Blog.objects.all()
# for idx, value in enumerate(all_obj):
#     print(f"idx = {idx}, value = {value}")
# print(all_obj[0])  # Получение 0-го элемента
# print(all_obj[2:4])  # Получение 2 и 3 элемента
# """Получение последнего элемента не осуществимо через обратный индекс
# all_obj[-1] - нельзя
# можно воспользоваться latest('<name_field>'), где <name_field> - имя колонки в БД.
#
# Почти все операции над БД не требуют предварительного получения всех элементов, постоянная запись Blog.objects.all()
# просто для примера.
# """
# print(all_obj.latest("id"))  # Получение последнего элемента
# print(Blog.objects.latest("id"))  # Одинаково работает
# #

# print(Blog.objects.exclude(id__gte=2))  # Вывод всех строк таблицы Blog кроме тех у которых значение id >= 2.
# #  <QuerySet [<Blog: Путешествия по миру>]>
#

# # Пример для get
# try:
#     Blog.objects.get(id=1, name="Путешествия по миру")
#     print("True")
# except Blog.DoesNotExist:
#     print("Не существует")
# # Пример для filter
# print(Blog.objects.filter(id=1, name="Путешествия по миру").exists())


# print(Blog.objects.count())  # Можно ко всей таблице
# print(Blog.objects.filter(id__gte=2).count())  # Можно к запросу
#
# all_data = Blog.objects.all()
# filtred_data = all_data.filter(id__gte=2)
# print(filtred_data.count())  # Можно к частным запросам
#

# filtered_data = Blog.objects.filter(id__gte=2)
# print(filtered_data.order_by("id"))  # упорядочивание по возрастанию по полю id
# print(filtered_data.order_by("-id"))  # упорядочивание по уменьшению по полю id
# print(filtered_data.order_by("-name", "id"))  # упорядочивание по двум параметрам, сначала по первому на уменьшение,
# # затем второе на увеличение. Можно упорядочивание провести по сколь угодно параметрам.
#


# from django.db.models import Count
# # Запрос, аннотирующий количество статей для каждого блога,
# # при этом добавляется новая колонка number_of_entries для вывода
# entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
# print(entry)

# from django.db.models import Count
# blogs = Blog.objects.alias(number_of_entries=Count('entries')).filter(number_of_entries__gt=4)
# print(blogs)
#


# count_authors = Entry.objects.aggregate(
#         count_authors=Count('author', distinct=True)
#     )
# print(count_authors)  # {'count_authors': 12}
#
#
# entries_with_tags_count = Entry.objects.annotate(
#     tag_count=Count('tags')).values('id', 'tag_count')
# print(entries_with_tags_count)
#
#
# entries_with_tags_count = Entry.objects.annotate(
#     tag_count=Count('body_text')).values('author_id', 'tag_count')
# print(entries_with_tags_count)
#

#
# from django.db.models import Sum
#
# # Вычислить общее число комментариев в БД
# calc_rating = Entry.objects.aggregate(
#     sum_comments=Sum('number_of_comments')
# )
# print(calc_rating)  # {'sum_comments': 134}


# filtered_data = Blog.objects.filter(id__gte=2).order_by("id")
# print(filtered_data)  # упорядочивание по возрастанию по полю id
#
#
# print(filtered_data.reverse())
#
# filtered_data = Blog.objects.filter(id__gte=2).order_by("id")
# print(filtered_data)
# print(filtered_data.reverse())
#

# print(Entry.objects.order_by('author', 'pub_date').distinct('author', 'pub_date'))
#
#

# Обычный запрос
# print(Blog.objects.filter(name__startswith='Фитнес'))
# # <QuerySet [<Blog: Фитнес и здоровый образ жизни>]>
#
# print(Blog.objects.filter(name__startswith='Фитнес').values())

# jb = Author.objects.values_list('id', 'name', 'email')
# for i in jb:
#     print(i)
# print(Blog.objects.values_list())

# blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру')
# blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения')
# blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни')
# result_qs = blog_a_entries.union(blog_b_entries, blog_c_entries)
# print(result_qs)


# print(Entry.objects.filter(blog__name__in=['Путешествия по миру', 'Кулинарные искушения', 'Фитнес и здоровый образ жизни']))



# from django.db import connection
#
# print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
# """
# Число запросов =  0  Запросы =  []
# """
# entry = Entry.objects.get(id=5)
# print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
# """
# Число запросов =  1  Запросы =  [...]
# """
# blog = entry.blog
# print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
# """
# Число запросов =  2  Запросы =  [...,...]
# """
# print('Результат запроса = ', blog)
# """
# Результат запроса =  Путешествия по миру
# """
# result = ModelA.objects.select_related('modelb', 'modelb__modelc', 'modelb__modelc__modeld').get(id=1)








