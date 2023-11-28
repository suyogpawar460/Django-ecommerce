# Generated by Django 4.1.12 on 2023-10-29 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('MH', 'Maharashtra'), ('MP', 'Madhya Pradesh'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HP', 'Himachal Pradesh'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('TS', 'Telangana'), ('TL', 'Tamilnadu'), ('PB', 'Punjab'), ('HR', 'Haryana'), ('MZ', 'Mizoram'), ('AS', 'Asam'), ('MG', 'Meghalaya'), ('CG', 'Chhattisgarh'), ('DL', 'Delhi'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('MN', 'Manipur'), ('NL', 'Nagaland'), ('SK', 'Sikkim'), ('TR', 'Tripura'), ('PY', 'Pondicherry'), ('OR', 'Orisa'), ('RJ', 'Rajasthan'), ('WB', 'West Bengal'), ('BR', 'Bihar')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]