from django.db import models

# Create your models here.
class Banner(models.Model):
    """轮播图"""
    title = models.CharField('标题', max_length=50)
    is_active = models.BooleanField('是否是active', default=False)
    """
    link_url = models.URLField('图片链接', max_length=100)
        idx = models.IntegerField('索引')
    """

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'