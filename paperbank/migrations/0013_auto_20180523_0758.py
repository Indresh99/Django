# Generated by Django 2.0.3 on 2018-05-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperbank', '0012_strings_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='cse1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_name', models.CharField(max_length=250)),
                ('cse_link_mid', models.CharField(max_length=250)),
                ('cse_link_end', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='cse',
        ),
        migrations.RemoveField(
            model_name='bca',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='biotech',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='civil',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='electronics',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='it',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='mech',
            name='semester',
        ),
    ]
