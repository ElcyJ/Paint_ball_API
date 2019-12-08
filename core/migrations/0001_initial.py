# Generated by Django 2.2.7 on 2019-12-08 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('ammunition', models.IntegerField()),
                ('range', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('localization_x', models.IntegerField()),
                ('localization_y', models.IntegerField()),
                ('gun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players_with_gun', to='core.Gun')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('A', 'Azul'), ('V', 'Vermelho')], max_length=1)),
                ('quant_players', models.IntegerField()),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='core.Map')),
            ],
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('U', 'UP'), ('D', 'Down'), ('R', 'Right'), ('L', 'Left')], max_length=1)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shots', to='core.Player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players_in_team', to='core.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
    ]
