import sys
import os
# Ajoute le dossier racine du projet au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from schemas.schemas import User
from db.connexion import SessionLocal
from db.crud import create_user

db = SessionLocal()
datas = [
  {
    "email": "attoisse.mohamed@isi.com",
    "nom": "attoisse",
    "prenom": "mohamed",
    "classe": "MLOps 2025"
  },
  {
    "email": "amina.kone@isi.com",
    "nom": "Kone",
    "prenom": "Amina",
    "classe": "MLOps 2025"
  },
  {
    "email": "jean.toure@isi.com",
    "nom": "Toure",
    "prenom": "Jean",
    "classe": "MLOps 2025"
  },
  {
    "email": "fatou.ndiaye@isi.com",
    "nom": "Ndiaye",
    "prenom": "Fatou",
    "classe": "MLOps 2025"
  },
  {
    "email": "moussa.sall@isi.com",
    "nom": "Sall",
    "prenom": "Moussa",
    "classe": "MLOps 2025"
  },
  {
    "email": "khalil.diop@isi.com",
    "nom": "Diop",
    "prenom": "Khalil",
    "classe": "MLOps 2025"
  },
  {
    "email": "sophie.faye@isi.com",
    "nom": "Faye",
    "prenom": "Sophie",
    "classe": "MLOps 2025"
  },
  {
    "email": "cheikh.ba@isi.com",
    "nom": "Ba",
    "prenom": "Cheikh",
    "classe": "MLOps 2025"
  },
  {
    "email": "yasmin.sene@isi.com",
    "nom": "Sene",
    "prenom": "Yasmin",
    "classe": "MLOps 2025"
  },
  {
    "email": "ibrahima.sy@isi.com",
    "nom": "Sy",
    "prenom": "Ibrahima",
    "classe": "MLOps 2025"
  }
]

for data in datas: 
   user = User(**data)
   result = create_user(db, user)
   print(User.from_orm(result).dict())
db.close()  # N'oubliez pas de fermer la session