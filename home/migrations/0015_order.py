# Generated by Django 3.0.2 on 2020-05-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_feedbacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('orderDate', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=255)),
                ('vendor_username', models.CharField(max_length=255)),
                ('ordered_items', models.CharField(max_length=5000)),
                ('grandTotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('zipCode', models.CharField(max_length=10)),
                ('phoneNo', models.IntegerField()),
                ('paymentMode', models.CharField(max_length=10)),
            ],
        ),
    ]
