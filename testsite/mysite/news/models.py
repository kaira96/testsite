from django.db import models


###################################36
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование') #varchar 255
    content = models.TextField(blank=True, verbose_name='Контент') #не обяз к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') #значение поля меняться не будет
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')  #когда в последнее время менялась запись
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True) #будет создан файл картинки с годом месяцем и днем создания
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано',)
    # ##########################################38
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=1)
    # ##########################################39
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    ##########################################45
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    #########################################47
    def my_func(self):
        return 'Hello from model'


    ###################################20
    def __str__(self):
        return self.title  # Возвращает строковое состояние объекта

    ###################################29
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


###################################37
class Category(models.Model):
    title = models.CharField(max_length=155, db_index=True, verbose_name='Наименование категории')

    ###################################43
    def __str__(self):
        return self.title  # Возвращает строковое состояние объекта

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']



# ###################################34
# class News(models.Model):
#     title = models.CharField(max_length=150, verbose_name='Наименование') #varchar 255
#     content = models.TextField(blank=True, verbose_name='Контент') #не обяз к заполнению
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') #значение поля меняться не будет
#     update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')  #когда в последнее время менялась запись
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото') #будет создан файл картинки с годом месяцем и днем создания
#     is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

# ###################################15
# class News(models.Model):
#     title = models.CharField(max_length=150) #varchar 255
#     content = models.TextField(blank=True) #не обяз к заполнению
#     created_at = models.DateTimeField(auto_now_add=True) #значение поля меняться не будет
#     update_at = models.DateTimeField(auto_now=True)  #когда в последнее время менялась запись
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d') #будет создан файл картинки с годом месяцем и днем создания
#     is_published = models.BooleanField(default=True)


