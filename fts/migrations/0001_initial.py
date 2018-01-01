# Generated by Django 2.0 on 2018-01-04 13:47

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('content', models.TextField()),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='article',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='fts_article_search__53d8fa_gin'),
        ),
    ]
