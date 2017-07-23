# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juliannaspizzaapp', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juliannaspizzaapp.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='juliannaspizzaapp.Order')),
            ],
        ),
    ]