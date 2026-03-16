from .app import db

class Question(db.Model):
    __tablename__ = 'Question'
    no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enonce = db.Column(db.String(255))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("Questionnaire.id"))
    type = db.Column(db.String(120))

    __mapper_args__ = {
        "polymorphic_identity": "Question",
        "polymorphic_on": type,
    }

    def __init__(self, enonce, questionnaire_id):
        self.enonce = enonce
        self.questionnaire_id = questionnaire_id

    def __repr__(self):
        return f"{self.to_json()}"
    
    def to_json(self):
        return {"no" : self.no, "enonce" : self.enonce}
    
class QuestionOuverte(Question):
    __tablename__ = 'QuestionOuverte'
    no = db.Column(db.Integer, db.ForeignKey('Question.no'), primary_key=True)
    enonce = db.Column(db.String(255))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("Questionnaire.id"))
    champ_reponse = db.Column(db.String(255))

    __mapper_args__ = {
        "polymorphic_identity": "QuestionOuverte",
    }

    def __init__(self, enonce, questionnaire_id):
        self.enonce = enonce
        self.questionnaire_id = questionnaire_id
        self.champ_reponse = ""

    def __repr__(self):
        return f"{self.to_json()}"
    
    def to_json(self):
        return {"no" : self.no, "enonce" : self.enonce, "champ_reponse" : self.champ_reponse}
    
class QuestionChoixMultiple(Question):
    __tablename__ = 'QuestionChoixMultiple'
    no = db.Column(db.Integer, db.ForeignKey('Question.no'), primary_key=True)
    enonce = db.Column(db.String(255))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey("Questionnaire.id"))
    choix_un = db.Column(db.String(120))
    choix_deux = db.Column(db.String(120))
    reponse = db.Column(db.Integer)

    __mapper_args__ = {
        "polymorphic_identity": "QuestionChoixMultiple",
    }

    def __init__(self, enonce, questionnaire_id, choix_un, choix_deux, reponse):
        self.enonce = enonce
        self.questionnaire_id = questionnaire_id
        self.choix_un = choix_un
        self.choix_deux = choix_deux
        self.reponse = reponse

    def __repr__(self):
        return f"{self.to_json()}"
    
    def to_json(self):
        return {"no" : self.no, "enonce" : self.enonce, "choix_un" : self.choix_un, "choix_deux" : self.choix_deux, "reponse" : self.reponse}

class Questionnaire(db.Model):
    __tablename__ = 'Questionnaire'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(255))
    question = db.relationship("Question", backref = db.backref("Questionnaire", lazy = "select"), uselist = True)

    def __init__(self, nom, question):
        self.nom = nom
        self.question = question

    def __repr__(self):
        return f"{self.id}, {self.nom}, {self.question}"

    def creer_question_ouverte(self, enonce):
        newQuestion = QuestionOuverte(enonce = enonce, questionnaire_id = self.id)
        db.session.add(newQuestion)
        db.session.commit()
        self.question.append(newQuestion)
        db.session.commit()
        return newQuestion
    
    def creer_question_choix_multiple(self, enonce, choix_un, choix_deux, reponse):
        newQuestion = QuestionChoixMultiple(enonce = enonce, questionnaire_id = self.id, choix_un = choix_un, choix_deux = choix_deux, reponse = reponse)
        db.session.add(newQuestion)
        db.session.commit()
        self.question.append(newQuestion)
        db.session.commit()
        return newQuestion
    
    def get_questions(self):
        lesQuestions = Question.query.all()
        questions = []
        for question in lesQuestions:
            if question.questionnaire_id == self.id:
                questions.append(question)
        return questions
    
    def modif_enonce(self, no, nouvel_enonce):
        question = Question.query.get(no)
        question.enonce = nouvel_enonce
        db.session.commit()
        return question
    
    def modif_question_ouverte(self, no, new_reponse):
        question = Question.query.get(no)
        question.champ_reponse = new_reponse
        db.session.commit()
        return question

    def modif_question_choix_multiple(self, no, new_choix_un, new_choix_deux, new_reponse):
        question = Question.query.get(no)
        question.choix_un = new_choix_un
        question.choix_deux = new_choix_deux
        question.reponse = new_reponse
        db.session.commit()
        return question
    
    def delete_question_by_no(self, no):
        question = Question.query.get(no)
        if question != None:
            db.session.delete(question)
            db.session.commit()

    def get_question_by_no(self, no):
        lesQuestions = self.get_questions
        for question in lesQuestions():
            if question.no == no:
                return question
        return None
    
    def list_to_json(self, list):
        les_questions = {}
        if list != None:
            for ques in list:
                if "questions" not in les_questions:
                    les_questions["questions"] = [(ques.to_json())]
                else:
                    les_questions["questions"].append(ques.to_json())
        return les_questions

    def to_json(self):
        json = {"nom" : self.nom, "id" : self.id}
        json.update(self.list_to_json(self.question))
        return json
    
def get_questionaire_by_id(id):
    questionnaire = Questionnaire.query.get(id)
    return questionnaire

def cree_questionnaire(nom):
    newQuestionnaire = Questionnaire(nom = nom, question = [])
    db.session.add(newQuestionnaire)
    db.session.commit()
    return newQuestionnaire

def modif_questionnaire(id, nouveau_nom):
    questionnaire = Questionnaire.query.get(id)
    questionnaire.nom = nouveau_nom
    db.session.commit()
    return questionnaire

def delete_questionnaire_by_id(id):
    global_questionnaire = Questionnaire.query.all()
    if len(global_questionnaire) > 0:
        questionnaire = global_questionnaire[id-1]
        db.session.delete(questionnaire)
        db.session.commit()
