<script>

import TodoItem from './components/Questionnaire.vue';

let data = {
  todos: [{ text: 'Faire les courses', checked: true, id:1 }, { text: 'Apprendre REST', checked: false, id:2 }],
  title: 'Mes tâches',
  newItem: ''
  // newText: ''
};

export default {

  data() {
    return data;
  },
  methods: {
    addItem: function () {
      let text = this.newItem.trim();
      if (text) {
        if(this.todos.length == 0){
          this.todos.push({
            text: text,
            checked: false,
            id: 1
          });
        }
        else{
          this.todos.push({
            text: text,
            checked: false,
            id: this.todos[this.todos.length -1].id + 1 ?? 1
          });
        }
        this.newItem = '';
      }
    },
    supprItem($event){
      let obj = this.todos.indexOf($event.task);
      this.todos.splice(obj, 1);
    },
    modifItem($event){
      
    }
  },
  components: { TodoItem }
}
</script>

<template>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <h2>{{ title }}</h2>
  <ol>
  <TodoItem
    v-for="item of todos"
    :todo="item"
    :key="item.id"
    @remove="supprItem"
    @update="modifItem">
  </TodoItem>
  </ol>
  <div class="input-group">
    <input v-model="newItem" 
     @keyup.enter="addItem" 
     placeholder="Ajouter une tache à la liste" 
    type="text"
    class="form-control">
    <span class="input-group-btn">
      <button @click="addItem" 
      class="btn btn-default" 
      type="button">Ajouter</button>
    </span>
  </div>
</template>