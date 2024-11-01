from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Provincia(models.Model):
    provincia_id = models.AutoField(db_column='PROVINCIA_ID', primary_key=True)  # Field name made lowercase.
    provincia_nombre = models.CharField(db_column='PROVINCIA_NOMBRE', max_length=50)  # Field name made lowercase.
    region_id = models.IntegerField(db_column='REGION_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    region_id = models.AutoField(db_column='REGION_ID', primary_key=True)  # Field name made lowercase.
    region_nombre = models.CharField(db_column='REGION_NOMBRE', max_length=50)  # Field name made lowercase.
    region_codigo = models.CharField(db_column='REGION_CODIGO', max_length=4)  # Field name made lowercase.
    region_iso3166_2_cl = models.CharField(db_column='REGION_ISO3166_2_CL', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Comuna(models.Model):
    comuna_id = models.AutoField(db_column='COMUNA_ID', primary_key=True)  # Field name made lowercase.
    comuna_nombre = models.CharField(db_column='COMUNA_NOMBRE', max_length=50)  # Field name made lowercase.
    provincia_id = models.IntegerField(db_column='PROVINCIA_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comuna'


class Detalle(models.Model):
    detalle_id = models.AutoField(db_column='DETALLE_ID', primary_key=True)  # Field name made lowercase.
    comuna_id = models.IntegerField(db_column='COMUNA_ID')  # Field name made lowercase.
    poblacion = models.CharField(db_column='POBLACION', max_length=500)  # Field name made lowercase.
    codigo_postal = models.IntegerField(db_column='CODIGO_POSTAL')  # Field name made lowercase.
    informacion = models.CharField(db_column='INFORMACION', max_length=500)  # Field name made lowercase.
    alcalde = models.CharField(db_column='ALCALDE', max_length=50)  # Field name made lowercase.
    imagen = models.ImageField(db_column='IMAGES', upload_to='detalle/', blank=True, null=True)  # Almacena la imagen en /media/detalle/


    class Meta:
        managed = False
        db_table = 'detalle'

