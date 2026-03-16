from .app import app, db
from .models import cree_questionnaire, delete_questionnaire_by_id, modif_questionnaire

@app.cli.command()
def syncdb():
    db.drop_all()
    db.create_all()
    qz1 = cree_questionnaire('Maths')
    qz2 = cree_questionnaire('Histoire')

    qz1.creer_question_ouverte("Coucou ?")
    qz1.creer_question_choix_multiple("Ca va ?", "Oui", "Non", 1)

    qz2.creer_question_choix_multiple("Lincoln ?", "Mort", "Vivant", 2)

