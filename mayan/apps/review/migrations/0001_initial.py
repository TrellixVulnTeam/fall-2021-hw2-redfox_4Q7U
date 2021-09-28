# Generated by Django 2.2.23 on 2021-09-28 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documents', '0075_delete_duplicateddocumentold'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='firstname')),
                ('last_name', models.CharField(max_length=255, verbose_name='lastname')),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='GPA')),
                ('GRE', models.IntegerField()),
                ('GMAT', models.IntegerField()),
                ('comments', models.TextField(verbose_name='Text')),
                ('submit_date', models.DateTimeField(verbose_name='submit_date')),
                ('personal_statement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='documents.Document', verbose_name='Document')),
                ('reviewer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
