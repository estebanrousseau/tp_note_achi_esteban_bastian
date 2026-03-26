<script>

  import Questionnaire from './components/Questionnaire.vue';

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

      addQuestionnaire() {
        this.questionnaires.push({
          nom: this.newQuestion,
          question: {},
          uri: `${API_BASE}/quizz/api/v1.0/questionnaires/${this.questionnaires.length + 1}`
        });
      },

      removeQuestionnaire($event) {
        this.questionnaires = this.questionnaires.filter(q => q.uri !== $event.questionnaire.uri);
      },

      modifierQuestionnaire($event) {
        // console.log($event.questionnaire);
        // console.log($event.modification)
        if(this.modification != ""){
        let index = this.questionnaires.indexOf($event.questionnaire);
        this.questionnaires.at(index).nom = this.modification;
        }
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
      <input v-model="modification" placeholder="modifier un questionnaire" type="text" class="form-control">
      <input v-model="newQuestion" @keyup.enter="addQuestionnaire" placeholder="Ajouter un questionnaire" type="text" class="form-control">
      <span class="input-group-btn">
        <button @click="addQuestionnaire" class="btn btn-default" type="button">Ajouter</button>
      </span>
    </div>
  </div>
</template>
