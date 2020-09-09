# Generated by Django 3.0.2 on 2020-08-05 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='evidencijagospodarstva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('katastar', models.CharField(max_length=120)),
                ('naselje', models.CharField(max_length=50)),
                ('povrsina', models.IntegerField()),
                ('naziv_gosp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='podaci_radnje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vrstaradnje', models.CharField(max_length=120)),
                ('katcest', models.CharField(max_length=120)),
                ('datum', models.DateField()),
                ('evidencijagospodarstva_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EOlive.evidencijagospodarstva')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='spricanje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazivtek', models.CharField(max_length=120)),
                ('kolicina', models.DecimalField(decimal_places=2, max_digits=10)),
                ('katcest', models.CharField(max_length=120)),
                ('datums', models.DateField()),
                ('podaci_radnje_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EOlive.podaci_radnje')),
            ],
        ),
        migrations.CreateModel(
            name='prihranjivanje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazivprihrane', models.CharField(max_length=120)),
                ('kolicinap', models.DecimalField(decimal_places=2, max_digits=10)),
                ('katcest', models.CharField(max_length=120)),
                ('datump', models.DateField()),
                ('podaci_radnje_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EOlive.podaci_radnje')),
            ],
        ),
        migrations.AddField(
            model_name='evidencijagospodarstva',
            name='User_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='berba',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vrstamaslina', models.CharField(max_length=120)),
                ('datumb', models.DateField()),
                ('katcest', models.CharField(max_length=120)),
                ('kolicinaubrano', models.DecimalField(decimal_places=2, max_digits=10)),
                ('doprinosulja', models.DecimalField(decimal_places=2, max_digits=10)),
                ('evidencijagospodarstva_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EOlive.evidencijagospodarstva')),
            ],
        ),
    ]
