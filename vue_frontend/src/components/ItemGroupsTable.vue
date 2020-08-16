<template>
  <div id="item-group-table">
    <table>
      <thead>
        <tr>
          <th><h2>groups</h2></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(items, key) in groups" :key="key">
          <td><h3>{{ key }}</h3></td>
          <td>  
             <li v-for='text in items' :key="text">
             {{text}}
             </li>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'item-group-table',
    data() {
     return {
    }
},
    props: {
        groups: Object,
    },
    methods: {
  editMode(id) {
    this.editing = id
  },
}
  }
</script>

<style scoped></style>