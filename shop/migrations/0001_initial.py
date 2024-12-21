# Generated by Django 5.1.3 on 2024-12-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('25 ml', '25 ml'), ('50 ml', '50 ml'), ('75 ml', '75 ml')], default='25 ml', max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=24.0, editable=False, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
    ]
