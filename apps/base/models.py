from django.db import models
from ckeditor.fields import RichTextField
from apps.base.contants import COLOR, ICONS, ICON

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовка"
    )
    descriptions = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to="settings",
        verbose_name="Фото"
    )
    become_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка become '
    )
    become_descriptions = models.TextField(
        max_length=300,
        verbose_name='Описание  become'
    )
    find_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка find'
    )
    find_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание find'
    )
    work_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка work'
    )
    work_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание work'
    )
    work_context = models.CharField(
        max_length=255,
        verbose_name='Описание work - 2'
    )
    download_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка download'
    )
    download_descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание download'
    )
    host_title = models.CharField(
        max_length=155,
        verbose_name="Заголовка host"
    )
    benefist_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка benefist'
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural="Настройки Главной страницы"


class Become(models.Model):
    parent_become = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_become', blank=True, null=True)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка',
        blank=True, null=True
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='become',
        verbose_name='Фото',
        blank=True, null=True
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=""
        verbose_name_plural="Познакомьтесь с другими культурами "

class BecomeActive(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка',
        blank=True, null=True
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='become',
        verbose_name='Фото',
        blank=True, null=True
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=""
        verbose_name_plural="Познакомьтесь с другими культурами Active"


class Perfect(models.Model):
    title = models.CharField(
          verbose_name='Заголовка', 
          max_length=155
          )
    image = models.ImageField(
        upload_to='perfect/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Найдите идеальную еду"
        verbose_name_plural = "Найдите идеальную еду"


class PerfectActive(models.Model):
    foreign = models.ForeignKey(Perfect, on_delete=models.CASCADE)
    title = models.CharField(
          verbose_name='Заголовка', 
          max_length=155,
          blank=True, null=True
          )
    image = models.ImageField(
        upload_to='perfect', 
        verbose_name='Фото',
        blank=True, null=True
    )
    title_price = models.CharField(
        max_length=155,
        verbose_name='Заголовка цены'
    )
    context_price = models.CharField(
        max_length=155,
        verbose_name='Описание цены'
    )
    title_price2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка цены 2'
    )
    context_price2 = models.CharField(
        max_length=155,
        verbose_name='цены 2'
    )

    def __str__(self):
        return self.title_price

    class Meta:
        verbose_name = "Найдите идеальную еду Active"
        verbose_name_plural = "Найдите идеальную еду Active"


class Work(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE )
    title = models.CharField( 
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=255, 
        verbose_name='Описание'
    )
    icon = models.CharField(
        choices=ICONS,
        max_length=100,
        verbose_name = "Иконку"
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Как это работает"
        verbose_name_plural = "Как это работает"


class Featured(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to="settings",
        verbose_name='Фото'
    )
    locations = models.CharField(
        max_length=100,
        verbose_name='Локация'
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='Рекомендуемые хосты'



class Cooking(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=200,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='ВСТРЕЧАТЬ НОВЫХ ЛЮДЕЙ'

class CookingActive(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=200,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='ВСТРЕЧАТЬ НОВЫХ ЛЮДЕЙ  Active'


class Benefist(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=200,
        verbose_name='Описание заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    color = models.CharField(
        choices=COLOR,
        max_length=100,
        verbose_name = "Цвет"
    )

    def __str__(self):
        return f"{self.title} - {self.context[:20]}"

    class Meta:
        verbose_name=''
        verbose_name_plural='Преимущества домашней еды'



###############################################
class Contact(models.Model):
    last_name = models.CharField(
        max_length=155,
        verbose_name='ФИО'
    )
    email = models.CharField(
        max_length=155,
        verbose_name="Адрес электронной почты"
    )
    number = models.CharField(
        max_length=75,
        verbose_name='Номер телефона'
    )
    message = models.CharField(
        max_length=355,
        verbose_name='Сообщение'
    )

    def __str__(self):
        return  self.last_name

    class Meta:
        verbose_name = ""
        verbose_name_plural='Контакты'



class Policies(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    descriptions = RichTextField(
        verbose_name = "Описание"
    )

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='Политика'


class Privacy(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=''
        verbose_name_plural='Конфедициально'


##############################################################33
class Hospitaly(models.Model):
    title = models.CharField(
        max_length = 155,
        verbose_name = 'Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='hospitaly',
        verbose_name='Фото'
    )
    quests_title = models.CharField(
        max_length = 155,
        verbose_name = 'Заголовка GUESTS '
    )
    quests_all = RichTextField(
        verbose_name = 'Описание 2'
    )
    quests_all2 = RichTextField(
        verbose_name = 'Описание 3'
    )
    quests_all3 = RichTextField(
        verbose_name = 'Описание 4'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='ГОСТЕПРИИМСТВО'

#############################################

class Specefic(models.Model):
    title = models.CharField(
        max_length = 155,
        verbose_name = 'Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='specefic',
        verbose_name = 'Фото'
    )
    title_about_diets = models.CharField(
        max_length = 100,
        verbose_name ='Заголовка О ДИЕТАХ'
    ) 
    center = models.CharField(
        max_length = 155,
        verbose_name ='Центр'
    )
    title_diets = RichTextField(
        verbose_name = 'Заголовка diets '
    )
    title_allergens = RichTextField(
        verbose_name = 'Заголовка allergens '
    )
    title_filters = RichTextField(
        verbose_name = 'Заголовка filters '
    )
    title_offered = RichTextField(
        verbose_name = 'Заголовка offered '
    )
    title_list = RichTextField(
        verbose_name = 'Заголовка list '
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='ОСОБЫЕ ОГРАНИЧЕНИЯ В ДИЕТЕ'

###############################################################
class Howitworks(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to="howitworks/"
    )
    title2 = models.CharField(
        max_length = 155,
        verbose_name = 'Заголовка WORK'
    )
    title3 = models.CharField(
        max_length=155,
        verbose_name='Заголовка 3'
    )
    title4 = models.CharField(
        max_length=155,
        verbose_name='Заголовка 4'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Настройки всего Howitworks'

class HowitworksObject(models.Model):
    foreing = models.ForeignKey(Howitworks, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to="howitworks/"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Объект Howitworks'

class GuestsHosts(models.Model):
    foreing = models.ForeignKey(Howitworks, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    icon = models.CharField(
        choices=ICON,
        max_length=100,
        verbose_name='Иконка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Объект Howitworks 2'