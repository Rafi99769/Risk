<template>
  <b-modal
    :id="id"
    :title="title"
    centered
    ok-only
    :ok-title="submit ? 'Submit' : 'Close'"
    ok-variant="dark"
    @ok="okPressed"
    header-bg-variant="info"
    footer-bg-variant="info"
    content-class="border-0"
    header-class="top-radius-0"
    footer-class="bottom-radius-0">
    <slot/>
  </b-modal>
</template>

<script>
  export default {
    name: 'base-modal',

    props: {
      id: String,
      title: String,
      submit: Boolean
    },

    methods: {
      okPressed() {
        if (this.submit)
          this.$emit('do-submit');
        else
          this.$emit('reset-form');
      }
    }
  }
</script>
