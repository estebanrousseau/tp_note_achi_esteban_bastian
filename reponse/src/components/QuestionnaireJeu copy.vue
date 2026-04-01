<script>

import Questions from './QuestionsJeu.vue';

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
            score_visible: false,
            questionPoints: {}
        };
    },
    props: {
        questionnaire : Object
    },
    computed: {
        totalQuestions() {
            return Array.isArray(this.questionnaire?.questions)
                ? this.questionnaire.questions.length
                : 0;
        },
        totalPossiblePoints() {
            if (!Array.isArray(this.questionnaire?.questions)) {
                return 0;
            }
            return this.questionnaire.questions.reduce((sum, question) => {
                return sum + (Number(question.points) || 1);
            }, 0);
        }
    },
    methods:{
        chgm_points : function($event) {
            if (!$event) {
                return;
            }

            const question = $event.question ?? ($event[0] ?? null);
            const points = $event.points ?? ($event[1] ?? $event.score ?? null);
            if (!question || points === null || points === undefined) {
                return;
            }

            const key = question.id ?? question.enonce ?? JSON.stringify(question);
            const value = Number(points) || 0;
            this.questionPoints[key] = value;
            this.score_total = Object.values(this.questionPoints).reduce(
                (sum, current) => sum + (Number(current) || 0),
                0
            );
        },
        valide_questionnaire : function() {
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
        <p>Score : {{ score_instant }} / {{ totalPossiblePoints }}</p>
    </div>
    <button type="button" @click="valide_questionnaire">Valider le questionnaire</button>
</template>
