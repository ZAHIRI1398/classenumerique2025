from app import app
from extensions import db, bcrypt
from models import User, Exercise, Question, Choice, TextHole, HighlightWord, Course, Class

with app.app_context():
    # Créer ou trouver l'admin
    admin = User.query.filter_by(email='admin@example.com').first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@example.com',
            role='teacher'
        )
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()

    # Créer une classe et un cours pour les exercices
    class_ = Class.query.filter_by(name='Classe Démo').first()
    if not class_:
        class_ = Class(name='Classe Démo', description='Classe de démonstration', teacher_id=admin.id)
        db.session.add(class_)
        db.session.commit()

    course = Course.query.filter_by(title='Cours Démo', class_id=class_.id).first()
    if not course:
        course = Course(title='Cours Démo', class_id=class_.id)
        db.session.add(course)
        db.session.commit()

    # --- Exercice QCM ---
    qcm = Exercise.query.filter_by(title='QCM Exemple').first()
    if not qcm:
        qcm = Exercise(
            title='QCM Exemple',
            description='Un exemple de QCM avec 2 questions.',
            exercise_type='QCM',
            points=10,
            subject='Français',
            level='CM2',
            created_by=admin.id,
            course_id=course.id
        )
        db.session.add(qcm)
        db.session.commit()
        # Questions & choix
        q1 = Question(text='Quelle est la capitale de la France ?', exercise_id=qcm.id)
        db.session.add(q1)
        db.session.flush()
        db.session.add_all([
            Choice(text='Paris', is_correct=True, question_id=q1.id),
            Choice(text='Lyon', is_correct=False, question_id=q1.id),
            Choice(text='Marseille', is_correct=False, question_id=q1.id),
        ])
        q2 = Question(text='Combien font 2 + 2 ?', exercise_id=qcm.id)
        db.session.add(q2)
        db.session.flush()
        db.session.add_all([
            Choice(text='3', is_correct=False, question_id=q2.id),
            Choice(text='4', is_correct=True, question_id=q2.id),
            Choice(text='5', is_correct=False, question_id=q2.id),
        ])
        db.session.commit()

    # --- Exercice Texte à trous ---
    th = Exercise.query.filter_by(title='Texte à trous Exemple').first()
    if not th:
        th = Exercise(
            title='Texte à trous Exemple',
            description='Complétez les trous.',
            exercise_type='text_holes',
            points=10,
            subject='Mathématiques',
            level='CM1',
            created_by=admin.id,
            course_id=course.id
        )
        db.session.add(th)
        db.session.commit()
        db.session.add_all([
            TextHole(text_before='La capitale de l’Espagne est', correct_answer='Madrid', text_after='.', exercise_id=th.id),
            TextHole(text_before='Le carré de 3 est', correct_answer='9', text_after='.', exercise_id=th.id)
        ])
        db.session.commit()

    # --- Exercice Mot à souligner ---
    hw = Exercise.query.filter_by(title='Mot à souligner Exemple').first()
    if not hw:
        hw = Exercise(
            title='Mot à souligner Exemple',
            description='Soulignez les mots demandés dans la phrase.',
            exercise_type='highlight_word',
            points=10,
            subject='Français',
            level='CM2',
            created_by=admin.id,
            course_id=course.id
        )
        db.session.add(hw)
        db.session.commit()
        sentence = "Le chat noir saute sur le mur blanc."
        words = "chat,noir,blanc"
        highlight = HighlightWord(sentence=sentence, words_to_highlight=words, exercise_id=hw.id)
        db.session.add(highlight)
        db.session.commit()

print('Exemples d\'exercices créés pour admin@example.com (mot de passe : admin)')
