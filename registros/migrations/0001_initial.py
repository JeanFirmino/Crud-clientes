from django.db import migrations, models
from phone_field import PhoneField

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nascimento', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', PhoneField(max_length=11)),
                ('observacoes', models.TextField(null=True,blank=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
