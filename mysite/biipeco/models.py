from django.db import models

class Intro(models.Model):
    title = models.CharField('Основная надпись', max_length=100)
    text = models.CharField('Дополнительная нажпись', max_length=140)
    btn_p = models.CharField('Первая кнопка', max_length=20)
    btn_w = models.CharField('Вторая кнопка', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Первая секция'
        verbose_name_plural = 'Первая секция'

class We(models.Model):
    text1 = models.CharField('Первая надпись', max_length=30)
    text2 = models.CharField('вторая надпись', max_length=30)
    text3 = models.CharField('Третья надпись', max_length=30)
    text4 = models.CharField('Четвертая надпись', max_length=30)

    def __str__(self):
        return 'Преимущества'

    class Meta:
        verbose_name = 'Почему мы'
        verbose_name_plural = 'Почему мы'

class Service(models.Model):
    text = models.CharField('Надпись', max_length=30)
    price = models.CharField('вторая надпись', max_length=20)
    img = models.FileField(upload_to='img/main/%Y/%m/%d/')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервис'

class Problems(models.Model):
    text1 = models.CharField('Первая надпись', max_length=40)
    text2 = models.CharField('вторая надпись', max_length=150)
    img = models.FileField(upload_to='img/main/%Y/%m/%d/')


    def __str__(self):
        return 'Проблемы'

    class Meta:
        verbose_name = 'Проблемы'
        verbose_name_plural = 'Проблемы'

class Needs(models.Model):
    text1 = models.CharField('Первая надпись', max_length=40)
    text2 = models.CharField('вторая надпись', max_length=60)
    btn_w = models.CharField('Кнопка', max_length=20)


    def __str__(self):
        return 'Не уверены?'

    class Meta:
        verbose_name = 'Не уверены?'
        verbose_name_plural = 'Не уверены?'

class Person(models.Model):
    name = models.CharField('Имя', max_length=15)
    email = models.CharField('Почта', max_length=200)
    whatsapp = models.CharField('Whatsapp', max_length=200)
    telegram = models.CharField('Telegram', max_length=200)
    img = models.FileField(upload_to='img/main/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Specializations(models.Model):
    person = models.DecimalField(max_digits=1, decimal_places=0)
    name = models.CharField('Специализация', max_length=70)

    def __str__(self):
        return 'Специализация'

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализация'

class Talks(models.Model):
    img = models.FileField(upload_to='img/main/%Y/%m/%d/')

    def __str__(self):
        return 'Отзыв'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Menu(models.Model):
    email = models.CharField('Почта', max_length=200)
    whatsapp = models.CharField('Whatsapp', max_length=200)
    telegram = models.CharField('Telegram', max_length=200)
    phone1 = models.CharField('Телефон для страницы', max_length=20)
    phone1_link = models.CharField('Телефон для ссылки (в формате +79000000000)', max_length=20)
    phone2 = models.CharField('Телефон', max_length=20)
    phone2_link = models.CharField('Телефон для ссылки (в формате +79000000000)', max_length=20)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Maps(models.Model):
    img = models.FileField(upload_to='img/main/%Y/%m/%d/')
    name = models.CharField('Регион', max_length=25)
    price = models.CharField('Цена', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class Licenses(models.Model):
    img = models.FileField(upload_to='img/main/%Y/%m/%d/')

    def __str__(self):
        return 'Лицензия'

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'