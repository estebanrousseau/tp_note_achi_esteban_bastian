<script>

  import Questionnaire from './components/QuestionnaireEdit.vue';

  const API_BASE = 'http://localhost:5000';



let data = {
  modification : '',
  questionnaire_actuel: null
};


  export default {
    data() {
      return {
        questionnaires: [],
        title: 'Mes questionnaires',
        newQuestion: ''
      };
    },
    async created() {
      await this.fetchQuestionnaires();
    },
    methods: {
      async fetchQuestionnaires() {
        const url = `${API_BASE}/quizz/api/v1.0/questionnaires`;

        try {
          const response = await fetch(url);

          if (!response.ok) {
            throw new Error(`Statut de réponse : ${response.status}`);
          }

          const json = await response.json();
          this.questionnaires = json.global_questionnaire || [];

        } catch (error) {
          console.error(error);
        }
      },

      async addQuestionnaire() {
        const url = `${API_BASE}/quizz/api/v1.0/questionnaires`;
        let data = {
          nom: this.newQuestion,
          question: {},
          uri: `${API_BASE}/quizz/api/v1.0/questionnaires/${this.questionnaires.length + 1}`
        }
        this.questionnaires.push(data);
        const response = await fetch(url, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            });
      },

      removeQuestionnaire($event) {
        this.questionnaires = this.questionnaires.filter(q => q.uri !== $event.questionnaire.uri);
      },

      async modifierQuestionnaire($event) {
        if(this.modification != ""){
          const url = `${API_BASE}/quizz/api/v1.0/questionnaires`;
          let index = this.questionnaires.indexOf($event.questionnaire);

          let data = {
            nom: this.modification,
            question: this.questionnaires.at(index).question,
            uri: this.questionnaires.at(index).uri
          }

          this.questionnaires.at(index).nom = this.modification;

          const response = await fetch(`${url}/${index}`, {
                method: "PUT",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            });
        }
      },

      part_jeu() {
        this.$router.push('/');
      },

      chgm_questionnaire($event){
        this.questionnaire_actuel = $event.questionnaire
        console.log(this.questionnaire_actuel)
      }
    },
    components: { Questionnaire }
  };
</script>

<template>
  <button type="submit" @click="part_jeu">Jeu</button>
  <router-link to="/edit"></router-link>
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>

       <Questionnaire
        v-for="questionnaire of questionnaires"
        :questionnaire="questionnaire"
        @delete="removeQuestionnaire"
        @modifier="modifierQuestionnaire"
        @select_questionnaire="chgm_questionnaire"
        >
       </Questionnaire> 

    </ol>
    <div class="input-group">
      <!-- <input v-model="modification" placeholder="modifier un questionnaire" type="text" class="form-control"> -->
      <input v-model="newQuestion" @keyup.enter="addQuestionnaire" placeholder="Ajouter un questionnaire" type="text" class="form-control">
      <span class="input-group-btn">
        <button @click="addQuestionnaire" class="btn btn-default" type="button">Ajouter</button>
      </span>
    </div>
  </div>
</template>
