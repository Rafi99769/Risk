<template>
  <div id="app">
    <risk></risk>
  </div>
</template>

<script>
  import Risk from "./components/risk"

  export default {
    components: {Risk},
    name: 'app'
  }
</script>

<style lang="scss">
  #app {
    text-align: center;
  }

  .m-t-15 {
    margin-top: 15%;
  }

  .w-90 {
    width: 90% !important;
  }

  .w-40 {
    width: 40% !important;
  }
</style>
