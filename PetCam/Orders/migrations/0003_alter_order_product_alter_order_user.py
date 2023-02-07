# Generated by Django 4.1.5 on 2023-01-31 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_alter_product_category'),
        ('Users', '0002_alter_user_address_alter_user_name_and_more'),
        ('Orders', '0002_rename_user_order_user_remove_order_number_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user', verbose_name='Nombre de usuario'),
        ),
    ]