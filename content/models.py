# -*- coding: utf-8 -*-

from django.db import models


class Content (models.Model):
    content_title = models.CharField ( max_length = 150, blank = True, verbose_name = "Заголовок")
    content_text = models.TextField ( verbose_name = "Содержание" )


