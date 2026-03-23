<script>

  import Questionnaire from './components/Questionnaire.vue';

  const API_BASE = 'http://localhost:5000';

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
        if($event.change != ""){
        let index = this.questionnaires.indexOf($event.questionnaire);
        this.questionnaires.at(index).nom = $event.modif;
      }
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
        >
       </Questionnaire> 

    </ol>
    <div class="input-group">
      <input v-model="newQuestion" @keyup.enter="addQuestionnaire" placeholder="Ajouter une question" type="text" class="form-control">
      <span class="input-group-btn">
        <button @click="addQuestionnaire" class="btn btn-default" type="button">Ajouter</button>
      </span>
    </div>
  </div>
</template>
