# Generated by Django 5.1.2 on 2024-10-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('comuna_id', models.AutoField(db_column='COMUNA_ID', primary_key=True, serialize=False)),
                ('comuna_nombre', models.CharField(db_column='COMUNA_NOMBRE', max_length=50)),
                ('provincia_id', models.IntegerField(db_column='PROVINCIA_ID')),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('detalle_id', models.AutoField(db_column='DETALLE_ID', primary_key=True, serialize=False)),
                ('comuna_id', models.IntegerField(db_column='COMUNA_ID')),
                ('poblacion', models.CharField(db_column='POBLACION', max_length=500)),
                ('codigo_postal', models.IntegerField(db_column='CODIGO_POSTAL')),
                ('informacion', models.CharField(db_column='INFORMACION', max_length=500)),
                ('alcalde', models.CharField(db_column='ALCALDE', max_length=50)),
            ],
            options={
                'db_table': 'detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('provincia_id', models.AutoField(db_column='PROVINCIA_ID', primary_key=True, serialize=False)),
                ('provincia_nombre', models.CharField(db_column='PROVINCIA_NOMBRE', max_length=50)),
                ('region_id', models.IntegerField(db_column='REGION_ID')),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(db_column='REGION_ID', primary_key=True, serialize=False)),
                ('region_nombre', models.CharField(db_column='REGION_NOMBRE', max_length=50)),
                ('region_codigo', models.CharField(db_column='REGION_CODIGO', max_length=4)),
                ('region_iso3166_2_cl', models.CharField(db_column='REGION_ISO3166_2_CL', max_length=5)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
    ]
