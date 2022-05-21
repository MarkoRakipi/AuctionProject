# Generated by Django 4.0.4 on 2022-05-18 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_rename_product_id_auction_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='buy_now_price',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='start_price',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_time', models.DateTimeField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.auction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
