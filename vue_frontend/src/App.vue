<template>
  <div id="app" class="small-container">
    <h1>Items Grouper</h1>
    <input-text-area @divide-groups="divideToGroupsByBackend"/>
    <item-groups-table :groups="groups"/>  
  </div>
</template>

<script>
  import InputTextArea from '@/components/InputTextArea.vue'
  import ItemGroupsTable from '@/components/ItemGroupsTable.vue'
  export default {
    name: 'app',
    methods: {
    async divideToGroupsByBackend(text) {
  try {
      const text_array = text.split(','); 
      const response = await fetch('http://127.0.0.1:5000/stringGroup', {
      method: 'POST',
      body: JSON.stringify(text_array),
      headers: { 'Content-type': 'application/json; charset=UTF-8' },
    })
    const groupsInResponse = await response.json();
    this.groups = Object.assign({}, groupsInResponse);
    console.log('llllllllll');
    console.log(groupsInResponse);
    console.log(this.groups);
  } catch (error) {
    console.error(error)
  }
},
    },
    components: {
      InputTextArea,
      ItemGroupsTable,
    },
    data() {
    return {
      groups:{},
    }
  },
  }
</script>

<style>
button {
  background: #009435;
  border: 1px solid #009435;
}

.small-container {
  max-width: 680px;
}
</style>