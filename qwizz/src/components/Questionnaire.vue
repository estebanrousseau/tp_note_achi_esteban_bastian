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
            reponse: ''
        };
    },
    props: {
        questionnaire : Object
    },
    methods:{
        ajouter : function() { // Ajouter question
            if(this.type == 1){
                this.questionnaire.questions.push({
                    enonce: this.enonce,
                    champ_reponse: this.reponse,
                    no: 1,
                });
                this.enonce = ''
                this.reponse = ''
            }
            if(this.type == 2){
                this.questionnaire["questions"].push({
                    enonce: this.enonce,
                    choix_un: this.choix_un,
                    choix_deux: this.choix_deux,
                    no: 1,
                    reponse: this.reponse,
                });
                this.enonce = ''
                this.choix_un = ''
                this.choix_deux = ''
                this.reponse = ''
            }
            this.type = ''
            this.btn_ajout_clic()
        },
        modifier : function() { // Modifier questionnaire
            // console.log(this.modification)
            this.$emit('modifier',{questionnaire: this.questionnaire});
        },
        supprimer : function() { // Supprimer questionnaire
            this.$emit('delete',{questionnaire: this.questionnaire});
        },
        removeQuestion($event) {
            this.questionnaire.questions = this.questionnaire.questions.filter((questions) => questions != $event.question);
        },
        btn_edit_clic : function() {
            this.change = true
        },
        btn_save_clic : function() {
            this.change = false
        },
        btn_ajout_clic : function() {
            if (this.ajout == false)
                this.ajout = true
            else
                this.ajout = false
        }

    },
    emits : ['post', 'modifier', 'delete', 'select_questionnaire'],
    components: { Questions }
}
</script>

<template>
    <!-- <p>{{ questionnaire }}</p> -->
    <li>
        <label v-if="change == false">{{questionnaire.nom}}</label>
        <input 
            v-else-if="change == true"
            v-model="questionnaire.nom" 
            placeholder="Nom du questionnaire" 
            type="text">

        <br v-if="ajout">
        <label v-if="ajout"><strong>1</strong> (Question ouverte) ou <strong>2</strong> (Question a choix multiple)</label>
        <input 
            v-if="ajout"
            v-model="this.type" 
            placeholder="Type de question" 
            type="text">


        <input 
            v-if="ajout && type == 1 | type == 2"
            v-model="this.enonce" 
            placeholder="Enonce" 
            type="text">
        <input 
            v-if="ajout && type == 2"
            v-model="this.choix_un" 
            placeholder="Choix un" 
            type="text">
        <input 
            v-if="ajout && type == 2"
            v-model="this.choix_deux" 
            placeholder="Choix deux" 
            type="text">
        <label v-if="ajout && type == 2">Choix de reponse : 1 ou 2</label>
        <input 
            v-if="ajout && type == 1 | type == 2"
            v-model="this.reponse" 
            placeholder="Reponse" 
            type="text">

        <button v-if="!(ajout)" type="button" @click="btn_ajout_clic">Nouvelle question</button>
        <button v-if="ajout" type="button" @click="ajouter">Ajouter</button>
        <button v-if="change == false" type="button" @click="btn_edit_clic">Modifier</button>
        <button v-if="change == true" type="button" @click="btn_save_clic">Enregistrer</button>
        <button type="button" @click="supprimer">Supprimer</button>
    </li>

    <Questions
        v-for="question of questionnaire.questions"
        :question="question"
        @delete="removeQuestion">
                <!-- @remove="supprItem", @update="modifItem" -->
    </Questions>
</template>
