# nosdeputes-en-django
Petit projet pour le fun

Pour l'installation:
```pip install django phpserialize  mysqlclient```

Pour ingérer les données de NS/ND:

```
mysql -u cpc -ppassword --default-character-set=utf8 -e "CREATE DATABASE cpc_ns"
mysql -u cpc -ppassword --default-character-set=utf8 cpc_ns < ~/Téléchargements/nossenateurs.fr_donnees.sql
```