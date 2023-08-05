# Generated by Django 4.1.5 on 2023-02-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasis_certs', '0002_rename_certificates_certificate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': 'Certificate', 'verbose_name_plural': 'Certificates'},
        ),
        migrations.AlterField(
            model_name='certificate',
            name='footer_text',
            field=models.CharField(blank=True, help_text='Text that is located in the footer of the certificate', max_length=150, verbose_name='Footer text'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='key',
            field=models.CharField(help_text='Key that identifies the certificate for its execution', max_length=20, verbose_name='Key to call back'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='legend',
            field=models.TextField(help_text='Text that goes inside the body of the certificate', verbose_name='Certificate text'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='name',
            field=models.CharField(help_text='Name that appears as the title of the certificate', max_length=80, verbose_name='Certificate name'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='query_text',
            field=models.TextField(help_text='Text used to execute the query', verbose_name='Query text'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='template',
            field=models.CharField(help_text='Template used to generate the certificate', max_length=150, verbose_name='Template to use'),
        ),
    ]
