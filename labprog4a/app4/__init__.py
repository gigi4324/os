import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectReg',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('ptitle', models.CharField(max_length=30)),
                ('planguage', models.CharField(max_length=30)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='studCourseRegApp.student'
                )),
            ],
        ),
    ]
