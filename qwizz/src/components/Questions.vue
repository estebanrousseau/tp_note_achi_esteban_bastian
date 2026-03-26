<script>

// import Questions from './components/Questions.vue';

export default{
    data() {
        return {
            change: false,
            reponse: ''
        };
    },
    props: {
        question : Object
    },
    methods:{
        ouverte : function() {
            if(Object.keys(this.question).length == 3)
                return true
            return false
        },
        choix_multiple : function() {
            if(Object.keys(this.question).length == 5)
                return true
            return false
        },
        btn_edit_clic : function() {
            this.change = true
        },
        btn_save_clic : function() {
            this.change = false
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
    <!-- <p>{{ question }}</p> -->
    <!-- <p>{{ ouverte() }}</p> -->
    <!-- <p>{{ choix_multiple() }}</p> -->
    <!-- <p>{{ Object.keys(question).length }}</p> -->
    <div>
        <div v-if="ouverte()">
            <div v-if="change == false">
                <label>{{ question.enonce }}<br></label>
                <label>{{ question.champ_reponse }}</label>
            </div>
            <div v-else-if="change == true">
                <input 
                    v-model="question.enonce" 
                    placeholder="Enonce" 
                    type="text"><br>
                <input 
                    v-model="question.champ_reponse" 
                    placeholder="Reponse" 
                    type="text">
            </div>
        </div>

        <div v-if="choix_multiple()">
            <div v-if="change == false">
                <label>{{ question.enonce }}<br></label>
                <label>Choix 1 :{{ question.choix_un }}<br></label>
                <label>Choix 2 :{{ question.choix_deux }}<br></label>
                <label>Reponse :{{ question.reponse }}</label>
            </div>
            <div v-else-if="change == true">
                <input 
                    v-model="question.enonce" 
                    placeholder="Enonce" 
                    type="text"><br>
                <input 
                    v-model="question.choix_un" 
                    placeholder="Choix un" 
                    type="text">
                <input 
                    v-model="question.choix_deux" 
                    placeholder="Choix deux" 
                    type="text"><br>
                <input 
                    v-model="question.reponse" 
                    placeholder="Reponse" 
                    type="number"
                    min="1"
                    max="2">
            </div>
        </div>
        <button v-if="change == false" type="button" @click="btn_edit_clic">Modifier</button>
        <button v-if="change == true" type="button" @click="btn_save_clic">Enregistrer</button>
        <button type="button" @click="supprimer">Supprimer</button>
    </div>
    <!-- <li>
        <label>{{ questionnaire.nom }}

        </label>
    </li>

    <Questions
        v-for="question of questionnaire"
        :todo="question">
                 @remove="supprItem", @update="modifItem"
    </Questions> -->
</template>