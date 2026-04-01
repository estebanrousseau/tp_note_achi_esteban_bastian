<script>

export default{
    data() {
        return {
            points: '',
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
        envois_points() {
            if(this.ouverte()){
                if(this.reponse == this.question.champ_reponse){
                    this.$emit('points',{question: this.question, points: 1});
                    console.log("Bonne rep ouverte")
                }
                else{
                    this.$emit('points',{question: this.question, points: 0});
                    console.log("Mauvaise rep ouverte")
                }
            }
            if(this.choix_multiple()){
                if(this.reponse == this.question.reponse){
                    this.$emit('points',{question: this.question, points: 1});
                    console.log("Bonne rep choix multiple")
                }
                else{
                    this.$emit('points',{question: this.question, points: 0});
                    console.log("Mauvaise rep choix multiple")
                }
            }
        },
        poepoe() {
            console.log(this.reponse)
        }
    },
    emits : ['points']
}
</script>

<template>
    <div>
        <label>{{ question.enonce }}<br></label>
        <div v-if="ouverte()">
            <input v-model="reponse" type="text" placeholder="Reponse"></input>
        </div>

        <div v-if="choix_multiple()">
            <div>
                <label for="choix_un">{{ question.choix_un }}
                    <input v-model="reponse" type="radio" value="1">
                </label>
            </div>

            <div>
                <label for="choix_deux">{{ question.choix_deux }}
                    <input v-model="reponse" type="radio" value="2">
                </label>
            </div>
        </div>
        <button @click="envois_points" type="button">Valider le question</button>
    </div>
</template>