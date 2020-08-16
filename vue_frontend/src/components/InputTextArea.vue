<template>
  <div id="input-text-area">
   <form @submit.prevent="handleSubmit">
  <label>add strings seperated by ','</label>

  <textarea v-model="message" placeholder="a_bbbb,a_cccc,b_aaaa,b_cccc,c_aaaa,c_bbbb"></textarea>
  <button>divide into groups</button>
   </form>
  </div>
</template>

<script>
  export default {
    name: 'input-text-area',
    data() {
      return {
            message: "",
      }
    },
    methods: {
    handleSubmit() {
      this.$emit('divide-groups', this.message.trim());
      console.log(this.message.trim());
    }
  },
  }
</script>

<style scoped>
   form {
    margin-bottom: 2rem;
  }

  [class*='-message'] {
    font-weight: 500;
  }

  .error-message {
    color: #d33c40;
  }

  .success-message {
    color: #32a95d;
  }
</style>
