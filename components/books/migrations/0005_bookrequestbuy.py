# Generated by Django 3.0.5 on 2020-04-13 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200412_1620'),
        ('books', '0004_bookreadstatus_is_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequestBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_url', models.URLField()),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('0', 'waiting'), ('1', 'approved'), ('2', 'bought')], default='0', max_length=56)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookCategory')),
            ],
        ),
    ]
