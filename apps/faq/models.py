from django.db import models

# Create your models here.
class FAQ(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Короткое описание",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"

class Questions(models.Model):
    faq = models.ForeignKey(
        FAQ, on_delete=models.CASCADE,
        related_name="faq",
        verbose_name="Часто задаваемый вопрос"
    )
    question = models.CharField(
        max_length=300,
        verbose_name="вопрос"
    )
    answer = models.TextField(
        verbose_name="ответ на вопрос"
    )

    def __str__(self):
        return f"{self.faq.title} - {self.question}"
    
    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"