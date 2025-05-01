from app import app, db
from models import User, Class

with app.app_context():
    teacher = User.query.filter_by(email='admin@example.com').first()
    if not teacher:
        print("Aucun enseignant trouvé avec l'email admin@example.com")
    else:
        # Créer une classe de test si aucune n'existe
        if not Class.query.filter_by(name='Classe Test').first():
            test_class = Class(name='Classe Test', description='Classe de démonstration', teacher_id=teacher.id)
            db.session.add(test_class)
            db.session.commit()
            print('Classe Test ajoutée pour l\'enseignant.')
        else:
            print('Classe Test existe déjà.')
