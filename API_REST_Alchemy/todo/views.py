from flask import jsonify, abort, make_response, request, url_for
from .app import app
from .models import Questionnaire, get_questionaire_by_id, cree_questionnaire, modif_questionnaire, delete_questionnaire_by_id

# ============================================ GET ============================================
# --------------------------------------- Questionnaire ---------------------------------------
@app.route('/quizz/api/v1.0/questionnaires', methods = ['GET'])
def get_questionnaires():
    global_questionnaire = Questionnaire.query.all()
    public_questionnaire = []
    for questionnaire in global_questionnaire:
        public_questionnaire.append(make_public_questionnaire(questionnaire.to_json()))
    return jsonify({'global_questionnaire' : public_questionnaire})

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>', methods = ['GET'])
def get_questionnaire(questionnaire_id):
    questionnaire = get_questionaire_by_id(questionnaire_id)
    if questionnaire != None :
        return jsonify({'questionnaire' : make_public_questionnaire(questionnaire.to_json())})
    abort(404)

# ----------------------------------------- Question ------------------------------------------
@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions', methods = ['GET'])
def get_questions(questionnaire_id):
    questionnaire = get_questionaire_by_id(questionnaire_id)
    lesQuestions = questionnaire.get_questions()
    public_question = []
    for question in lesQuestions:
        public_question.append(make_public_question(questionnaire_id, question.to_json()))
    return jsonify({f"global_question_questionnaire_{questionnaire_id}" : public_question})

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:question_id>', methods = ['GET'])
def get_question(questionnaire_id, question_id):
    questionnaire = get_questionaire_by_id(questionnaire_id)
    question = questionnaire.get_question_by_no(question_id)
    if question != None :
        return jsonify({'question' : make_public_question(questionnaire_id, question.to_json())})
    abort(404)

# ------------------------------------------- Make --------------------------------------------
def make_public_questionnaire(questionnaire):
    new_questionnaire = {}
    for field in questionnaire:
        if field == 'id':
            new_questionnaire['uri'] = url_for('get_questionnaire', questionnaire_id = questionnaire['id'],
                _external = True)
        else:
            new_questionnaire[field] = questionnaire[field]
    return new_questionnaire

def make_public_question(questionnaire_id, question):
    new_question = {}
    for field in question:
        if field == 'no':
            new_question['uri'] = url_for('get_question', questionnaire_id = questionnaire_id, question_id = question['no'],
                _external = True)
        else:
            new_question[field] = question[field]
    return new_question

# ============================================ POST ============================================
@app.route('/quizz/api/v1.0/questionnaires', methods = ['POST'])
def create_questionnaire():
    # vérification des données reçues
    if not request.json or not 'nom' in request.json:
        abort(400)
    # ajout d'un nouveau questionaire
    newQuestionnaire = cree_questionnaire(request.json['nom']) # id = new_id, nom = request.json['nom']
    # questionnaire = get_questionaire_by_id(newQuestionnaire.id)
    # retour de la nouvelle tâche avec son uri 201 indique qu’une ressource a été créée
    return jsonify({'task' : make_public_questionnaire(newQuestionnaire.to_json())}), 201

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions', methods = ['POST'])
def create_question(questionnaire_id):
    questionnaire = get_questionaire_by_id(questionnaire_id)
    lesQuestions = questionnaire.get_questions()
    # vérification des données reçues
    if not request.json or not 'enonce' in request.json:
        abort(400)
    if not 'choix_un' in request.json and not 'choix_deux' in request.json and not 'reponse' in request.json:
        question = questionnaire.creer_question_ouverte(request.json['enonce'])
    else:
        question = questionnaire.creer_question_choix_multiple(request.json['enonce'], request.json['choix_un'], request.json['choix_deux'], request.json['reponse'])
        print(question.type)
    # retour de la nouvelle tâche avec son uri 201 indique qu’une ressource a été créée
    return jsonify({'task' : make_public_question(questionnaire_id, question.to_json())}), 201

# ============================================ PUT ============================================
@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>', methods = ['PUT'])
def update_questionnaire(questionnaire_id):
    global_questionnaire = Questionnaire.query.all()
    # Recherche de la tâche à modifier avec son id
    questionnaire = None
    for questionnairei in global_questionnaire:
        if questionnairei.id == questionnaire_id:
            questionnaire = questionnairei
            break
    # la tâche avec cette id n’existe pas
    if questionnaire is None:
        abort(404)
    # la requête n’est pas au format json
    if not request.json:
        abort(400)
    # Verification des types
    if 'nom' in request.json and not isinstance(request.json['nom'], str):
        abort(400)
    # modification des champs de la tâche
    questionnaire = modif_questionnaire(questionnaire.id, request.json['nom'])

    # retour de la tâche modifiée
    return jsonify({'task' : make_public_questionnaire(questionnaire.to_json())})

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:question_id>', methods = ['PUT'])
def update_question(questionnaire_id, question_id):
    questionnaire = get_questionaire_by_id(questionnaire_id)
    lesQuestions = questionnaire.get_questions()
    # Recherche de la tâche à modifier avec son id
    question = None
    for questioni in lesQuestions:
        if questioni.no == question_id:
            question = questioni
            break
    # la tâche avec cette id n’existe pas
    if question is None:
        abort(404)
    # la requête n’est pas au format json
    if not request.json:
        abort(400)
    # Verification des types
    if 'enonce' in request.json and not isinstance(request.json['enonce'], str):
        abort(400)
    # modification des champs de la tâche
    if 'enonce' in request.json:
        question = questionnaire.modif_enonce(question.no, request.json['enonce'])
    if question.type == "QuestionOuverte":
        if 'champ_reponse' in request.json:
            question = questionnaire.modif_question_ouverte(question.no, request.json['champ_reponse'])
    elif question.type == "QuestionChoixMultiple":
        if 'choix_un' in request.json and 'choix_deux' in request.json and 'reponse' in request.json :
            question = questionnaire.modif_question_choix_multiple(question.no, request.json['choix_un'], request.json['choix_deux'], request.json['reponse'])

    # retour de la tâche modifiée
    return jsonify({'task' : make_public_question(questionnaire_id, question.to_json())})

# ============================================ DELETE ============================================
@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>', methods = ['DELETE'])
def delete_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    # # la t â che avec cette id n ’ existe pas
    if questionnaire is None:
        abort(404)
    delete_questionnaire_by_id(questionnaire_id)
    # global_questionnaire.remove(questionnaire)
    return jsonify({"result": True})

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:question_id>', methods = ['DELETE'])
def delete_question(questionnaire_id, question_id):
    questionnaire = get_questionaire_by_id(questionnaire_id)
    question = questionnaire.get_question_by_no(question_id)
    # la t â che avec cette id n ’ existe pas
    if question is None:
        abort(404)
    questionnaire.delete_question_by_no(question_id)
    # lesQuestions.remove(question)
    return jsonify({"result": True})

# ============================================ ERROR ============================================
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error' : 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error' : 'Bad request'}), 400)
