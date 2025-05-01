from models import db, Exercise, DragDropElement, DragDropZone, Course
from app import app

# Example data: assumes a course with id=1 exists
with app.app_context():
    # Create an example drag-and-drop exercise
    exercise = Exercise(
        title="Associer les animaux à leurs habitats",
        description="Faites glisser chaque animal dans la zone correspondant à son habitat.",
        exercise_type="drag_drop",
        solution="Lion->Savane; Pingouin->Banquise; Chameau->Désert",
        course_id=1,  # Change as needed
        points=5,
        max_attempts=3,
        difficulty="Facile",
        created_by=1  # Change as needed
    )
    db.session.add(exercise)
    db.session.flush()  # Get exercise.id

    # Create drag-drop elements
    lion = DragDropElement(label="Lion", image_path=None, exercise_id=exercise.id)
    pingouin = DragDropElement(label="Pingouin", image_path=None, exercise_id=exercise.id)
    chameau = DragDropElement(label="Chameau", image_path=None, exercise_id=exercise.id)
    db.session.add_all([lion, pingouin, chameau])
    db.session.flush()

    # Create drag-drop zones (coordinates are for example only)
    zone1 = DragDropZone(x=10, y=20, width=20, height=20, correct_element_id=lion.id, exercise_id=exercise.id)
    zone2 = DragDropZone(x=40, y=20, width=20, height=20, correct_element_id=pingouin.id, exercise_id=exercise.id)
    zone3 = DragDropZone(x=70, y=20, width=20, height=20, correct_element_id=chameau.id, exercise_id=exercise.id)
    db.session.add_all([zone1, zone2, zone3])

    db.session.commit()
    print("Exemple d'exercice drag & drop créé avec succès !")
