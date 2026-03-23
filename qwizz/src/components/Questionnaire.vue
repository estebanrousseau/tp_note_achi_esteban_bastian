<script>

import Questions from './Questions.vue';


export default{
    props: {
        questionnaire : Object
    },
    methods:{
        ajouter : function() { // Ajouter question

        },
        modifier : function() { // Modifier questionnaire
            // console.log(this.modification)
            this.$emit('modifier',{questionnaire: this.questionnaire});
        },
        supprimer : function() { // Supprimer questionnaire
            this.$emit('delete',{questionnaire: this.questionnaire});
        }
    },
    emits : ['post', 'modifier', 'delete']
}
</script>

<template>
    <li>
        <label>{{questionnaire.nom}}
        

            <button type="button" @click="modifier">Modifier</button>
            <button type="button" @click="supprimer">Supprimer</button>
        </label>
    </li>

    <Questions
        v-for="question of questionnaire"
        :todo="question">
                <!-- @remove="supprItem", @update="modifItem" -->
    </Questions>
</template>
