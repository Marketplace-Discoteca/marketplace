# Generated by Django 5.1.1 on 2024-10-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nombre_cliente',
            field=models.CharField(default='asa', max_length=50),
            preserve_default=False,
        ),
    ]