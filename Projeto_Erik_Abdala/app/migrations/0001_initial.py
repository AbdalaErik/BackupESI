# Generated by Django 4.2.7 on 2023-11-06 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Fisico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=300)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=50)),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('enunciado', models.CharField(max_length=500)),
                ('alternativa_a', models.CharField(max_length=300)),
                ('alternativa_b', models.CharField(max_length=300)),
                ('alternativa_c', models.CharField(max_length=300)),
                ('alternativa_d', models.CharField(max_length=300)),
                ('alternativa_e', models.CharField(max_length=300)),
                ('alternativa_correta', models.CharField(max_length=300)),
                ('alternativa_submetida', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=300)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questao')),
            ],
        ),
        migrations.CreateModel(
            name='Subarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=300)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=500)),
                ('subarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subarea')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionarioRespondido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_realizacao', models.DateField()),
                ('numero_acertos', models.PositiveIntegerField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questionario')),
            ],
        ),
        migrations.CreateModel(
            name='Invencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('ano', models.DateField()),
                ('area', models.ManyToManyField(to='app.area')),
                ('fisico', models.ManyToManyField(to='app.fisico')),
            ],
        ),
    ]
