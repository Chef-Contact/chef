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
        upload_to="settings/",
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
    become_button_text = models.CharField(
        max_length = 50,
        verbose_name = 'Текст для button become'
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
    work_button_text = models.CharField(
        max_length = 50,
        verbose_name = 'Текст для button work'
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
    host_button_text = models.CharField(
        max_length = 50,
        verbose_name = 'Текст для button recommend'
    )
    benefist_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка benefist'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = "Настройки Главной страницы"


class Become(models.Model):
    # parent_become = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_become', blank=True,
    #                                   null=True)
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
        upload_to='become/',
        verbose_name='Фото',
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Познакомьтесь с другими культурами "


class BecomeActive(models.Model):
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
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
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Познакомьтесь с другими культурами Active"


class Gellary(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name = 'Заголовка'
    )
    image = models.ImageField(
        upload_to='gellary/',
        verbose_name = 'Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='Галлерия'


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
        verbose_name_plural = "Найдите идеальную еду "



class PerfectActive(models.Model):
    foreign = models.ForeignKey(Perfect, on_delete=models.CASCADE)
    title = models.CharField(
          verbose_name='Заголовка', 
          max_length=155,
          blank=True, null=True
          )
    image = models.ImageField(
        upload_to='perfect/', 
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
    forein = models.ForeignKey(Become, on_delete=models.CASCADE)
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
        verbose_name="Иконку"
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
        upload_to="settings/",
        verbose_name='Фото'
    )
    locations = models.CharField(
        max_length=100,
        verbose_name='Локация'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Рекомендуемые хосты'


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
        upload_to='settings/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'ВСТРЕЧАТЬ НОВЫХ ЛЮДЕЙ'


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
        upload_to='settings/',
        verbose_name='Фото'
    )
    button_text = models.CharField(
        max_length = 50,
        verbose_name = 'Текст для кнопки'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'ВСТРЕЧАТЬ НОВЫХ ЛЮДЕЙ Active'


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
        upload_to='settings/',
        verbose_name='Фото'
    )
    color = models.CharField(
        choices=COLOR,
        max_length=100,
        verbose_name="Цвет"
    )
    button_text = models.CharField(
        max_length = 50,
        verbose_name = 'Текст для кнопки'
    )

    def __str__(self):
        return f"{self.title} - {self.context[:20]}"

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Преимущества домашней еды'


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
        return self.last_name

    class Meta:
        verbose_name = ""
        verbose_name_plural = 'Контакты'


class Policies(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    descriptions = RichTextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Политика'


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
        verbose_name = ''
        verbose_name_plural = 'Конфедициально'


class About(models.Model):
    title_banner = models.CharField(
        max_length=155,
        verbose_name='Заголовка баннера'
    )

    description_banner = models.CharField(
        max_length=155,
        verbose_name='Описание баннера'
    )
    image_banner = models.ImageField(
        upload_to='background_images/',
        verbose_name='Изображение баннера',
        blank=True, null=True,
    )
    title_about = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    title_about2 = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    title_about3 = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description_about = models.CharField(
        max_length=155,
        verbose_name='Описание баннера'
    )
    description_about2 = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description_about3 = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name = "Настройка о нас"
        verbose_name_plural = "Настройки о нас"


class TrustSafety(models.Model):
    title_banner = models.CharField(
        max_length=155,
        verbose_name='Заголовок баннера'
    )
    description_banner = models.TextField(
        verbose_name='Описание баннера'
    )
    background_image = models.ImageField(
        upload_to='background_images/',
        verbose_name='Изображение баннера'
    )
    insurance_title = models.CharField(
        max_length=155,
        verbose_name='Заголовок Insurance'
    )
    insurance_description = models.TextField(
        verbose_name='Описание Insurance'
    )

    def __str__(self):
        return self.title_banner

    class Meta:
        verbose_name = 'Доверие и Безопасность'
        verbose_name_plural = 'Доверие и Безопасность'


class TrustSafetyObjects(models.Model):
    trustsafety = models.ForeignKey(
        TrustSafety, on_delete=models.CASCADE,
        related_name='trust_trustsafety',
        verbose_name='Объект Trust'
    )
    icon_image = models.ImageField(
        upload_to='icons/',
        verbose_name='Иконка элемента'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок элемента'
    )
    description = models.TextField(
        verbose_name='Описание элемента'
    )

    class Meta:
        verbose_name = 'Доверие и Безопасность'
        verbose_name_plural = 'Доверие и Безопасность'


class InsuranceObjects(models.Model):
    trustsafety = models.ForeignKey(
        TrustSafety, on_delete=models.CASCADE,
        related_name='insurance_trustsafety',
        verbose_name='Объект Insurance'
    )
    question = models.CharField(
        max_length=155,
        verbose_name='Вопрос Insurance'
    )
    answer = models.TextField(
        verbose_name='Ответ Insurance'
    )

    class Meta:
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurance'


class Rules(models.Model):
    main_image = models.ImageField(
        upload_to='rules_image_main/',
        verbose_name='Главная фотография',
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image1 = models.ImageField(
        upload_to='image_rules1/',
        verbose_name='Фотография 1'
    )
    flag1 = models.ImageField(
        upload_to='flag_rules1/',
        verbose_name='Фото флага1'
    )
    image2 = models.ImageField(
        upload_to='image_rules2/',
        verbose_name='Фотография 2'
    )
    flag2 = models.ImageField(
        upload_to='flag_rules2/',
        verbose_name='Фото флага2'
    )
    lottery_rule = RichTextField(
        verbose_name='Правило'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'



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


