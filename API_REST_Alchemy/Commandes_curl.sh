# ================= Questionnaire =================
# GET
curl -i http://localhost:5000/quizz/api/v1.0/questionnaires
curl -i http://localhost:5000/quizz/api/v1.0/questionnaires/1

# POST
curl -i -H "Content-Type: application/json" -X POST -d '{"nom":"Faits Divers"}' http://localhost:5000/quizz/api/v1.0/questionnaires

# PUT
curl -i -H "Content-Type: application/json" -X PUT -d '{"nom":"Litterature"}' http://localhost:5000/quizz/api/v1.0/questionnaires/3

# DELETE
curl -i -X DELETE http://localhost:5000/quizz/api/v1.0/questionnaires/3

# ================= Question =================
# GET
curl -i http://localhost:5000/quizz/api/v1.0/questionnaires/1/questions
curl -i http://localhost:5000/quizz/api/v1.0/questionnaires/1/questions/1

# POST
# ----------------- Question Ouvertes -----------------
curl -i -H "Content-Type: application/json" -X POST -d '{"enonce":"Bonjour ?"}' http://localhost:5000/quizz/api/v1.0/questionnaires/1/questions
# ----------------- Question Choix Multiple -----------------
curl -i -H "Content-Type: application/json" -X POST -d '{"enonce":"Bonjour ?", "choix_un":"Dodo", "choix_deux":"Pas dodo", "reponse":1}' http://localhost:5000/quizz/api/v1.0/questionnaires/2/questions

# PUT
# ----------------- Enonce -----------------
curl -i -H "Content-Type: application/json" -X PUT -d '{"enonce":"Hello ?"}' http://localhost:5000/quizz/api/v1.0/questionnaires/1/questions/1
# ----------------- Question Ouvertes -----------------
curl -i -H "Content-Type: application/json" -X PUT -d '{"champ_reponse":"Fromage"}' http://localhost:5000/quizz/api/v1.0/questionnaires/1/questions/1
# ----------------- Question Choix Multiple -----------------
curl -i -H "Content-Type: application/json" -X PUT -d '{"choix_un":"Miam", "choix_deux":"MiamMiam", "reponse":2}' http://localhost:5000/quizz/api/v1.0/questionnaires/1/questions/2

# DELETE
curl -i -X DELETE http://localhost:5000/quizz/api/v1.0/questionnaires/1/questions/4

