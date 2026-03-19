<script>

// import Questions from './components/Questions.vue';

let data = {
    reponse: ''
};

export default{
    data() {
        return data;
    },
    props: {
        question : Object
    },
    methods:{
        ouverte : function() {
            if(this.question.length == 3)
                return true
            return false
        },
        choix_multiple : function() {
            if(this.question.length == 5)
                return true
            return false
        },
        modifier : function() { // Modifier question

        },
        supprimer : function() { // Supprimer question

        }
    },
    emits : ['put', 'delete']
}
</script>

<template>
    <div>
        <label>{{ question.enonce }}</label>
        <div v-if="ouverte">
            <input 
                v-model="reponse" 
                placeholder="Ajouter une tache à la liste" 
                type="text">
        </div>

        <div v-if="choix_multiple">
            <input 
                v-model="reponse" 
                type="radio">
        </div>
        <button type="button" @click="modifier">Modifier</button>
        <button type="button" @click="supprimer">Supprimer</button>
    </div>
    <li>
        <label>{{ questionnaire.nom }}

        </label>
    </li>

    <Questions
        v-for="question of questionnaire"
        :todo="question">
                <!-- @remove="supprItem", @update="modifItem" -->
    </Questions>
</template>