<script>

import Questions from './Questions.vue';


export default{
    data() {
        return {
            change: false,
            ajout: false,
            type: '',

            enonce: '',
            choix_un: '',
            choix_deux: '',
            reponse: '',
            score_total: 0,
            score_instant: 0,
            score_visible: false
        };
    },
    props: {
        questionnaire : Object
    },
    methods:{
        chgm_points : function($event) {
            
        },
        valide_questionnaire : function() {
            console.log(this.questionnaire)
            this.score_instant = this.score_total;
            this.score_visible = true;
        }
    },
    emits : [],
    components: { Questions }
}
</script>

<template>
    
    <!-- <p>{{ questionnaire }}</p> -->
    <li>
        <label >{{questionnaire.nom}}</label>
    </li>

    <Questions
        v-for="question of questionnaire.questions"
        :question="question"
        @points="chgm_points">
                <!-- @remove="supprItem", @update="modifItem" -->
    </Questions>
    <div v-if="score_visible == true">
        <p>Score : {{ score_instant }} / {{ questionnaire.questions }}</p>
    </div>
    <button  type="button" @click="valide_questionnaire">Valider</button>
</template>
