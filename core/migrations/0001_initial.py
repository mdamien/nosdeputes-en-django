# Generated by Django 3.0.6 on 2020-05-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alinea',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('texteloi_id', models.CharField(blank=True, max_length=16, null=True)),
                ('article_loi_id', models.BigIntegerField(blank=True, null=True)),
                ('numero', models.BigIntegerField(blank=True, null=True)),
                ('texte', models.TextField(blank=True, null=True)),
                ('ref_loi', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'alinea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Amendement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('legislature', models.BigIntegerField(blank=True, null=True)),
                ('texteloi_id', models.CharField(blank=True, max_length=16, null=True)),
                ('numero', models.CharField(blank=True, max_length=8, null=True)),
                ('sous_amendement_de', models.CharField(max_length=8)),
                ('rectif', models.BigIntegerField(blank=True, null=True)),
                ('sujet', models.CharField(blank=True, max_length=100, null=True)),
                ('sort', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('auteur_groupe_acronyme', models.CharField(blank=True, max_length=16, null=True)),
                ('signataires', models.TextField(blank=True, null=True)),
                ('texte', models.TextField(blank=True, null=True)),
                ('expose', models.TextField(blank=True, null=True)),
                ('content_md5', models.CharField(blank=True, max_length=36, null=True)),
                ('nb_multiples', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'amendement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('titre', models.CharField(blank=True, max_length=254, null=True)),
                ('corps', models.TextField(blank=True, null=True)),
                ('user_corps', models.TextField(blank=True, null=True)),
                ('categorie', models.CharField(blank=True, max_length=128, null=True)),
                ('citoyen_id', models.BigIntegerField(blank=True, null=True)),
                ('article_id', models.BigIntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('object_id', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('version', models.BigIntegerField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleLoi',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('texteloi_id', models.CharField(blank=True, max_length=16, null=True)),
                ('titre', models.CharField(blank=True, max_length=16, null=True)),
                ('ordre', models.BigIntegerField(blank=True, null=True)),
                ('precedent', models.CharField(blank=True, max_length=16, null=True)),
                ('suivant', models.CharField(blank=True, max_length=16, null=True)),
                ('expose', models.TextField(blank=True, null=True)),
                ('titre_loi_id', models.BigIntegerField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'article_loi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleVersion',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('titre', models.CharField(blank=True, max_length=254, null=True)),
                ('corps', models.TextField(blank=True, null=True)),
                ('user_corps', models.TextField(blank=True, null=True)),
                ('categorie', models.CharField(blank=True, max_length=128, null=True)),
                ('citoyen_id', models.BigIntegerField(blank=True, null=True)),
                ('article_id', models.BigIntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('object_id', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('version', models.BigIntegerField()),
            ],
            options={
                'db_table': 'article_version',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('nb_mots', models.BigIntegerField(blank=True, null=True)),
                ('md5', models.CharField(blank=True, max_length=36, null=True, unique=True)),
                ('intervention', models.TextField(blank=True, null=True)),
                ('timestamp', models.BigIntegerField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=128, null=True)),
                ('seance_id', models.BigIntegerField(blank=True, null=True)),
                ('section_id', models.BigIntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('personnalite_id', models.BigIntegerField(blank=True, null=True)),
                ('parlementaire_id', models.BigIntegerField(blank=True, null=True)),
                ('parlementaire_groupe_acronyme', models.CharField(blank=True, max_length=16, null=True)),
                ('fonction', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'intervention',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'organisme',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parlementaire',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_de_famille', models.CharField(blank=True, max_length=255, null=True)),
                ('sexe', models.CharField(blank=True, max_length=255, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('lieu_naissance', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_circo', models.CharField(blank=True, max_length=255, null=True)),
                ('num_circo', models.BigIntegerField(blank=True, null=True)),
                ('sites_web', models.TextField(blank=True, null=True)),
                ('debut_mandat', models.DateField(blank=True, null=True)),
                ('fin_mandat', models.DateField(blank=True, null=True)),
                ('place_hemicycle', models.BigIntegerField(blank=True, null=True)),
                ('url_an', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('autoflip', models.IntegerField(blank=True, null=True)),
                ('id_an', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('groupe_acronyme', models.CharField(blank=True, max_length=8, null=True)),
                ('adresses', models.TextField(blank=True, null=True)),
                ('suppleant_de_id', models.BigIntegerField(blank=True, null=True)),
                ('anciens_mandats', models.TextField(blank=True, null=True)),
                ('autres_mandats', models.TextField(blank=True, null=True)),
                ('anciens_autres_mandats', models.TextField(blank=True, null=True)),
                ('mails', models.TextField(blank=True, null=True)),
                ('top', models.TextField(blank=True, null=True)),
                ('villes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('url_ancien_cpc', models.TextField()),
                ('url_nouveau_cpc', models.TextField()),
            ],
            options={
                'db_table': 'parlementaire',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParlementaireAmendement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('parlementaire_id', models.BigIntegerField(blank=True, null=True)),
                ('parlementaire_groupe_acronyme', models.CharField(blank=True, max_length=16, null=True)),
                ('amendement_id', models.CharField(blank=True, max_length=36, null=True)),
                ('numero_signataire', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'parlementaire_amendement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParlementaireOrganisme',
            fields=[
                ('fonction', models.TextField(blank=True, null=True)),
                ('importance', models.BigIntegerField(blank=True, null=True)),
                ('debut_fonction', models.DateField(blank=True, null=True)),
                ('organisme_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('parlementaire_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'parlementaire_organisme',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParlementairePhoto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parlementaire_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParlementaireTexteloi',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('parlementaire_id', models.BigIntegerField(blank=True, null=True)),
                ('parlementaire_groupe_acronyme', models.CharField(blank=True, max_length=16, null=True)),
                ('texteloi_id', models.CharField(blank=True, max_length=16, null=True)),
                ('importance', models.BigIntegerField(blank=True, null=True)),
                ('fonction', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'parlementaire_texteloi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personnalite',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_de_famille', models.CharField(blank=True, max_length=255, null=True)),
                ('sexe', models.CharField(blank=True, max_length=255, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('lieu_naissance', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'personnalite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('parlementaire_id', models.BigIntegerField(blank=True, null=True)),
                ('parlementaire_groupe_acronyme', models.CharField(blank=True, max_length=16, null=True)),
                ('seance_id', models.BigIntegerField(blank=True, null=True)),
                ('nb_preuves', models.BigIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'presence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PreuvePresence',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('presence_id', models.BigIntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'preuve_presence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionEcrite',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('legislature', models.BigIntegerField(blank=True, null=True)),
                ('numero', models.BigIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('date_cloture', models.DateField(blank=True, null=True)),
                ('ministere', models.TextField(blank=True, null=True)),
                ('themes', models.TextField(blank=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('reponse', models.TextField(blank=True, null=True)),
                ('motif_retrait', models.TextField(blank=True, null=True)),
                ('content_md5', models.CharField(blank=True, max_length=36, null=True)),
                ('parlementaire_id', models.BigIntegerField(blank=True, null=True)),
                ('parlementaire_groupe_acronyme', models.CharField(blank=True, max_length=16, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'question_ecrite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('numero_semaine', models.BigIntegerField(blank=True, null=True)),
                ('annee', models.BigIntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('moment', models.CharField(blank=True, max_length=255, null=True)),
                ('organisme_id', models.BigIntegerField(blank=True, null=True)),
                ('tagged', models.IntegerField(blank=True, null=True)),
                ('session', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'seance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('md5', models.CharField(blank=True, max_length=36, null=True, unique=True)),
                ('titre', models.TextField(blank=True, null=True)),
                ('titre_complet', models.TextField(blank=True, null=True)),
                ('section_id', models.BigIntegerField(blank=True, null=True)),
                ('min_date', models.CharField(blank=True, max_length=15, null=True)),
                ('max_date', models.DateField(blank=True, null=True)),
                ('timestamp', models.BigIntegerField(blank=True, null=True)),
                ('nb_interventions', models.BigIntegerField(blank=True, null=True)),
                ('id_dossier_an', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'section',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_triple', models.IntegerField(blank=True, null=True)),
                ('triple_namespace', models.CharField(blank=True, max_length=100, null=True)),
                ('triple_key', models.CharField(blank=True, max_length=100, null=True)),
                ('triple_value', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tagging',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tag_id', models.BigIntegerField()),
                ('taggable_model', models.CharField(blank=True, max_length=30, null=True)),
                ('taggable_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tagging',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Texteloi',
            fields=[
                ('id', models.CharField(blank=True, max_length=16, primary_key=True, serialize=False, unique=True)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('legislature', models.BigIntegerField(blank=True, null=True)),
                ('numero', models.BigIntegerField(blank=True, null=True)),
                ('annexe', models.CharField(blank=True, max_length=12, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('type_details', models.TextField(blank=True, null=True)),
                ('categorie', models.CharField(blank=True, max_length=128, null=True)),
                ('id_dossier_an', models.CharField(blank=True, max_length=255, null=True)),
                ('titre', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('organisme_id', models.BigIntegerField(blank=True, null=True)),
                ('signataires', models.TextField(blank=True, null=True)),
                ('contenu', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'texteloi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TitreLoi',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nb_commentaires', models.BigIntegerField(blank=True, null=True)),
                ('texteloi_id', models.CharField(blank=True, max_length=16, null=True)),
                ('chapitre', models.CharField(blank=True, max_length=8, null=True)),
                ('section', models.CharField(blank=True, max_length=8, null=True)),
                ('titre', models.TextField(blank=True, null=True)),
                ('expose', models.TextField(blank=True, null=True)),
                ('parlementaire_id', models.BigIntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('nb_articles', models.BigIntegerField(blank=True, null=True)),
                ('titre_loi_id', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'titre_loi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VariableGlobale',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('champ', models.CharField(blank=True, max_length=32, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'variable_globale',
                'managed': False,
            },
        ),
    ]
