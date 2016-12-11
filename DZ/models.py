from django.db import models
from users.models import User

# Create your models here.
class Tovar(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    image = models.ImageField(upload_to='image', verbose_name='Картинка')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    cout = models.IntegerField(verbose_name='Цена')
    user = models.ForeignKey(User, verbose_name='Продавец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return '{0}: {1} {2} {3}'.format(self.user, self.name, self.created_at, self.cout)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def zakaz_on(self, name):
        """
        Подписан ли на пользователя
        """
        return Tovar.objects.filter(id=self.pk, subscribes=name).exists()