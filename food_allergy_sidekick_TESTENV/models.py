# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class KeyValueStore(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    idmeal = models.IntegerField(db_column='idMeal', blank=True, null=True)  # Field name made lowercase.
    strmeal = models.TextField(db_column='strMeal', blank=True, null=True)  # Field name made lowercase.
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True, default='recipe_images/food_icon.jpg')
    strcategory = models.TextField(db_column='strCategory', blank=True, null=True)  # Field name made lowercase.
    strarea = models.TextField(db_column='strArea', blank=True, null=True)  # Field name made lowercase.
    strinstructions = models.TextField(db_column='strInstructions', blank=True, null=True)  # Field name made lowercase.
    strmealthumb = models.TextField(db_column='strMealThumb', blank=True, null=True)  # Field name made lowercase.
    strtags = models.TextField(db_column='strTags', blank=True, null=True)  # Field name made lowercase.
    stryoutube = models.TextField(db_column='strYoutube', blank=True, null=True)  # Field name made lowercase.
    stringredient1 = models.TextField(db_column='strIngredient1', blank=True, null=True)  # Field name made lowercase.
    stringredient2 = models.TextField(db_column='strIngredient2', blank=True, null=True)  # Field name made lowercase.
    stringredient3 = models.TextField(db_column='strIngredient3', blank=True, null=True)  # Field name made lowercase.
    stringredient4 = models.TextField(db_column='strIngredient4', blank=True, null=True)  # Field name made lowercase.
    stringredient5 = models.TextField(db_column='strIngredient5', blank=True, null=True)  # Field name made lowercase.
    stringredient6 = models.TextField(db_column='strIngredient6', blank=True, null=True)  # Field name made lowercase.
    stringredient7 = models.TextField(db_column='strIngredient7', blank=True, null=True)  # Field name made lowercase.
    stringredient8 = models.TextField(db_column='strIngredient8', blank=True, null=True)  # Field name made lowercase.
    stringredient9 = models.TextField(db_column='strIngredient9', blank=True, null=True)  # Field name made lowercase.
    stringredient10 = models.TextField(db_column='strIngredient10', blank=True, null=True)  # Field name made lowercase.
    stringredient11 = models.TextField(db_column='strIngredient11', blank=True, null=True)  # Field name made lowercase.
    stringredient12 = models.TextField(db_column='strIngredient12', blank=True, null=True)  # Field name made lowercase.
    stringredient13 = models.TextField(db_column='strIngredient13', blank=True, null=True)  # Field name made lowercase.
    stringredient14 = models.TextField(db_column='strIngredient14', blank=True, null=True)  # Field name made lowercase.
    stringredient15 = models.TextField(db_column='strIngredient15', blank=True, null=True)  # Field name made lowercase.
    stringredient16 = models.TextField(db_column='strIngredient16', blank=True, null=True)  # Field name made lowercase.
    stringredient17 = models.TextField(db_column='strIngredient17', blank=True, null=True)  # Field name made lowercase.
    stringredient18 = models.TextField(db_column='strIngredient18', blank=True, null=True)  # Field name made lowercase.
    stringredient19 = models.TextField(db_column='strIngredient19', blank=True, null=True)  # Field name made lowercase.
    stringredient20 = models.TextField(db_column='strIngredient20', blank=True, null=True)  # Field name made lowercase.
    strmeasure1 = models.TextField(db_column='strMeasure1', blank=True, null=True)  # Field name made lowercase.
    strmeasure2 = models.TextField(db_column='strMeasure2', blank=True, null=True)  # Field name made lowercase.
    strmeasure3 = models.TextField(db_column='strMeasure3', blank=True, null=True)  # Field name made lowercase.
    strmeasure4 = models.TextField(db_column='strMeasure4', blank=True, null=True)  # Field name made lowercase.
    strmeasure5 = models.TextField(db_column='strMeasure5', blank=True, null=True)  # Field name made lowercase.
    strmeasure6 = models.TextField(db_column='strMeasure6', blank=True, null=True)  # Field name made lowercase.
    strmeasure7 = models.TextField(db_column='strMeasure7', blank=True, null=True)  # Field name made lowercase.
    strmeasure8 = models.TextField(db_column='strMeasure8', blank=True, null=True)  # Field name made lowercase.
    strmeasure9 = models.TextField(db_column='strMeasure9', blank=True, null=True)  # Field name made lowercase.
    strmeasure10 = models.TextField(db_column='strMeasure10', blank=True, null=True)  # Field name made lowercase.
    strmeasure11 = models.TextField(db_column='strMeasure11', blank=True, null=True)  # Field name made lowercase.
    strmeasure12 = models.TextField(db_column='strMeasure12', blank=True, null=True)  # Field name made lowercase.
    strmeasure13 = models.TextField(db_column='strMeasure13', blank=True, null=True)  # Field name made lowercase.
    strmeasure14 = models.TextField(db_column='strMeasure14', blank=True, null=True)  # Field name made lowercase.
    strmeasure15 = models.TextField(db_column='strMeasure15', blank=True, null=True)  # Field name made lowercase.
    strmeasure16 = models.TextField(db_column='strMeasure16', blank=True, null=True)  # Field name made lowercase.
    strmeasure17 = models.TextField(db_column='strMeasure17', blank=True, null=True)  # Field name made lowercase.
    strmeasure18 = models.TextField(db_column='strMeasure18', blank=True, null=True)  # Field name made lowercase.
    strmeasure19 = models.TextField(db_column='strMeasure19', blank=True, null=True)  # Field name made lowercase.
    strmeasure20 = models.TextField(db_column='strMeasure20', blank=True, null=True)  # Field name made lowercase.
    strsource = models.TextField(db_column='strSource', blank=True, null=True)  # Field name made lowercase.
    ingredients = models.TextField(blank=True, null=True)
    measurements = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'key_value_store'


class ProfilesUserprofile(models.Model):
    allergies = models.CharField(max_length=123)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'profiles_userprofile'


class RecipesRecipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recipes_recipe'
