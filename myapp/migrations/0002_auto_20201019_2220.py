from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='urlid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userfeedback',
            name='userid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
