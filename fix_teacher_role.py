# Script pour corriger le rôle de l'utilisateur connecté (mettre 'teacher')
from flask import Flask
from extensions import db
from models import User

app = Flask(__name__)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'classe_numerique.db')
if not os.path.exists(db_path):
    raise FileNotFoundError(f"La base de données n'existe pas : {db_path}")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    user = User.query.filter_by(email='admin@example.com').first()
    if user:
        user.role = 'teacher'
        db.session.commit()
        print(f"Le rôle de {user.username} a été mis à jour en 'teacher'.")
    else:
        print("Utilisateur introuvable. Modifiez l'email dans le script si nécessaire.")
