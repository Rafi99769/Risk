<template>
  <base-modal
    :id="formFields.id"
    :title="formFields.risk"
    v-on:reset-form="resetForm">
    <b-form v-if="formFields.show">
      <b-form-group v-for="field in formFields.fields"
                    :key="field.id"
                    :label="field.field">
        <b-form-input v-if="field.type === 'text'"
                      type="text">
        </b-form-input>
        <b-form-input v-else-if="field.type === 'number'"
                      type="number">
        </b-form-input>
        <b-form-input v-else-if="field.type === 'date'"
                      type="date">
        </b-form-input>
        <b-form-select v-else-if="field.type === 'enum'"
                       :options="field.choices">
        </b-form-select>
      </b-form-group>
    </b-form>
  </base-modal>
</template>

<script>
  import BaseModal from "./base-modal";

  export default {
    name: 'show-risk-field-modal',

    components: {BaseModal},

    props: {
      formFields: Object
    },

    methods: {
      resetForm() {
        this.formFields.show = false;
      }
    }
  }
</script>

<style>
  .bottom-radius-0 {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }

  .top-radius-0 {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
</style>
