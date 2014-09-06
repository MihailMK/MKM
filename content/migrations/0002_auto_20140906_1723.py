# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contents',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='contents_text',
            new_name='content_text',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='contents_title',
            new_name='content_title',
        ),
    ]
