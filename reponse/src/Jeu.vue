<script>

  import Questionnaire from './components/QuestionnaireJeu.vue';

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
      valideQuestionnaire: function($event) {
        console.log('Questionnaire validé avec', $event.nb_points, 'points');
      },
      part_edit() {
        this.$router.push('/edit');
      }

      
    },
    components: { Questionnaire }
  };
</script>

<template>
  <button type="submit" @click="part_edit">Edit</button>
  <router-link to="/"></router-link>
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>

       <Questionnaire
        v-for="questionnaire of questionnaires"
        :questionnaire="questionnaire"
        >
       </Questionnaire> 

    </ol>
    <div class="input-group">
      <!-- <input v-model="modification" placeholder="modifier un questionnaire" type="text" class="form-control"> -->
      
      <span class="input-group-btn">
        
      </span>
    </div>
  </div>
</template>
