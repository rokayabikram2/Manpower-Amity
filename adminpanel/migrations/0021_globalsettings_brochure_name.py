# Generated by Django 4.2.4 on 2023-08-15 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0020_alter_navigation_page_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='brochure_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
