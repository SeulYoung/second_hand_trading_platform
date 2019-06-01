# Generated by Django 2.2.1 on 2019-06-01 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chatter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.Buyer', to_field='buyer_id')),
                ('chatter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.CustomerService', to_field='customerService_id')),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chatter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.Buyer', to_field='buyer_id')),
                ('chatter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.Seller', to_field='seller_id')),
            ],
        ),
    ]
