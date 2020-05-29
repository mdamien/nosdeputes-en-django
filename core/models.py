# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alinea(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    texteloi_id = models.CharField(max_length=16, blank=True, null=True)
    article_loi_id = models.BigIntegerField(blank=True, null=True)
    numero = models.BigIntegerField(blank=True, null=True)
    texte = models.TextField(blank=True, null=True)
    ref_loi = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alinea'
        unique_together = (('texteloi_id', 'article_loi_id', 'numero'),)


class Amendement(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    legislature = models.BigIntegerField(blank=True, null=True)
    texteloi_id = models.CharField(max_length=16, blank=True, null=True)
    numero = models.CharField(max_length=8, blank=True, null=True)
    sous_amendement_de = models.CharField(max_length=8)
    rectif = models.BigIntegerField(blank=True, null=True)
    sujet = models.CharField(max_length=100, blank=True, null=True)
    sort = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    auteur_groupe_acronyme = models.CharField(max_length=16, blank=True, null=True)
    signataires = models.TextField(blank=True, null=True)
    texte = models.TextField(blank=True, null=True)
    expose = models.TextField(blank=True, null=True)
    content_md5 = models.CharField(max_length=36, blank=True, null=True)
    nb_multiples = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'amendement'
        unique_together = (('legislature', 'texteloi_id', 'numero', 'rectif'),)


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    titre = models.CharField(max_length=254, blank=True, null=True)
    corps = models.TextField(blank=True, null=True)
    user_corps = models.TextField(blank=True, null=True)
    categorie = models.CharField(max_length=128, blank=True, null=True)
    citoyen_id = models.BigIntegerField(blank=True, null=True)
    article_id = models.BigIntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleLoi(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    texteloi_id = models.CharField(max_length=16, blank=True, null=True)
    titre = models.CharField(max_length=16, blank=True, null=True)
    ordre = models.BigIntegerField(blank=True, null=True)
    precedent = models.CharField(max_length=16, blank=True, null=True)
    suivant = models.CharField(max_length=16, blank=True, null=True)
    expose = models.TextField(blank=True, null=True)
    titre_loi_id = models.BigIntegerField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_loi'
        unique_together = (('texteloi_id', 'titre'),)


class ArticleVersion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    titre = models.CharField(max_length=254, blank=True, null=True)
    corps = models.TextField(blank=True, null=True)
    user_corps = models.TextField(blank=True, null=True)
    categorie = models.CharField(max_length=128, blank=True, null=True)
    citoyen_id = models.BigIntegerField(blank=True, null=True)
    article_id = models.BigIntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'article_version'
        unique_together = (('id', 'version'),)


class Intervention(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    nb_mots = models.BigIntegerField(blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=36, blank=True, null=True)
    intervention = models.TextField(blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    source = models.CharField(max_length=128, blank=True, null=True)
    seance_id = models.BigIntegerField(blank=True, null=True)
    section_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    personnalite_id = models.BigIntegerField(blank=True, null=True)
    parlementaire_id = models.BigIntegerField(blank=True, null=True)
    parlementaire_groupe_acronyme = models.CharField(max_length=16, blank=True, null=True)
    fonction = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'intervention'


class Organisme(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(unique=True, max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organisme'


class Parlementaire(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    nom_de_famille = models.CharField(max_length=255, blank=True, null=True)
    sexe = models.CharField(max_length=255, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=255, blank=True, null=True)
    nom_circo = models.CharField(max_length=255, blank=True, null=True)
    num_circo = models.BigIntegerField(blank=True, null=True)
    sites_web = models.TextField(blank=True, null=True)
    debut_mandat = models.DateField(blank=True, null=True)
    fin_mandat = models.DateField(blank=True, null=True)
    place_hemicycle = models.BigIntegerField(blank=True, null=True)
    url_an = models.CharField(unique=True, max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    autoflip = models.IntegerField(blank=True, null=True)
    id_an = models.BigIntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    groupe_acronyme = models.CharField(max_length=8, blank=True, null=True)
    adresses = models.TextField(blank=True, null=True)
    suppleant_de_id = models.BigIntegerField(blank=True, null=True)
    anciens_mandats = models.TextField(blank=True, null=True)
    autres_mandats = models.TextField(blank=True, null=True)
    anciens_autres_mandats = models.TextField(blank=True, null=True)
    mails = models.TextField(blank=True, null=True)
    top = models.TextField(blank=True, null=True)
    villes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    url_ancien_cpc = models.TextField()
    url_nouveau_cpc = models.TextField()

    class Meta:
        managed = False
        db_table = 'parlementaire'


class ParlementaireAmendement(models.Model):
    id = models.BigAutoField(primary_key=True)
    parlementaire_id = models.BigIntegerField(blank=True, null=True)
    parlementaire_groupe_acronyme = models.CharField(max_length=16, blank=True, null=True)
    amendement_id = models.CharField(max_length=36, blank=True, null=True)
    numero_signataire = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parlementaire_amendement'


class ParlementaireOrganisme(models.Model):
    fonction = models.TextField(blank=True, null=True)
    importance = models.BigIntegerField(blank=True, null=True)
    debut_fonction = models.DateField(blank=True, null=True)
    organisme_id = models.BigIntegerField(primary_key=True)
    parlementaire_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'parlementaire_organisme'
        unique_together = (('organisme_id', 'parlementaire_id'),)


class ParlementairePhoto(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parlementaire_photo'


class ParlementaireTexteloi(models.Model):
    id = models.BigAutoField(primary_key=True)
    parlementaire_id = models.BigIntegerField(blank=True, null=True)
    parlementaire_groupe_acronyme = models.CharField(max_length=16, blank=True, null=True)
    texteloi_id = models.CharField(max_length=16, blank=True, null=True)
    importance = models.BigIntegerField(blank=True, null=True)
    fonction = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parlementaire_texteloi'


class Personnalite(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    nom_de_famille = models.CharField(max_length=255, blank=True, null=True)
    sexe = models.CharField(max_length=255, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personnalite'


class Presence(models.Model):
    id = models.BigAutoField(primary_key=True)
    parlementaire_id = models.BigIntegerField(blank=True, null=True)
    parlementaire_groupe_acronyme = models.CharField(max_length=16, blank=True, null=True)
    seance_id = models.BigIntegerField(blank=True, null=True)
    nb_preuves = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'presence'


class PreuvePresence(models.Model):
    id = models.BigAutoField(primary_key=True)
    presence_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'preuve_presence'


class QuestionEcrite(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    source = models.CharField(unique=True, max_length=255, blank=True, null=True)
    legislature = models.BigIntegerField(blank=True, null=True)
    numero = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    date_cloture = models.DateField(blank=True, null=True)
    ministere = models.TextField(blank=True, null=True)
    themes = models.TextField(blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    reponse = models.TextField(blank=True, null=True)
    motif_retrait = models.TextField(blank=True, null=True)
    content_md5 = models.CharField(max_length=36, blank=True, null=True)
    parlementaire_id = models.BigIntegerField(blank=True, null=True)
    parlementaire_groupe_acronyme = models.CharField(max_length=16, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'question_ecrite'
        unique_together = (('legislature', 'numero'),)


class Seance(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    numero_semaine = models.BigIntegerField(blank=True, null=True)
    annee = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    moment = models.CharField(max_length=255, blank=True, null=True)
    organisme_id = models.BigIntegerField(blank=True, null=True)
    tagged = models.IntegerField(blank=True, null=True)
    session = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'seance'
        unique_together = (('organisme_id', 'date', 'moment'),)


class Section(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=36, blank=True, null=True)
    titre = models.TextField(blank=True, null=True)
    titre_complet = models.TextField(blank=True, null=True)
    section_id = models.BigIntegerField(blank=True, null=True)
    min_date = models.CharField(max_length=15, blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    nb_interventions = models.BigIntegerField(blank=True, null=True)
    id_dossier_an = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'section'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    is_triple = models.IntegerField(blank=True, null=True)
    triple_namespace = models.CharField(max_length=100, blank=True, null=True)
    triple_key = models.CharField(max_length=100, blank=True, null=True)
    triple_value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class Tagging(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag_id = models.BigIntegerField()
    taggable_model = models.CharField(max_length=30, blank=True, null=True)
    taggable_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tagging'


class Texteloi(models.Model):
    id = models.CharField(unique=True, max_length=16, blank=True, primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    legislature = models.BigIntegerField(blank=True, null=True)
    numero = models.BigIntegerField(blank=True, null=True)
    annexe = models.CharField(max_length=12, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    type_details = models.TextField(blank=True, null=True)
    categorie = models.CharField(max_length=128, blank=True, null=True)
    id_dossier_an = models.CharField(max_length=255, blank=True, null=True)
    titre = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    source = models.CharField(unique=True, max_length=128, blank=True, null=True)
    organisme_id = models.BigIntegerField(blank=True, null=True)
    signataires = models.TextField(blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'texteloi'
        unique_together = (('numero', 'annexe'),)


class TitreLoi(models.Model):
    id = models.BigAutoField(primary_key=True)
    nb_commentaires = models.BigIntegerField(blank=True, null=True)
    texteloi_id = models.CharField(max_length=16, blank=True, null=True)
    chapitre = models.CharField(max_length=8, blank=True, null=True)
    section = models.CharField(max_length=8, blank=True, null=True)
    titre = models.TextField(blank=True, null=True)
    expose = models.TextField(blank=True, null=True)
    parlementaire_id = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    source = models.CharField(unique=True, max_length=128, blank=True, null=True)
    nb_articles = models.BigIntegerField(blank=True, null=True)
    titre_loi_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'titre_loi'


class VariableGlobale(models.Model):
    id = models.BigAutoField(primary_key=True)
    champ = models.CharField(max_length=32, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'variable_globale'
