<template>
  <base-modal
    :id="formFields.id"
    :title="formFields.title"
    :submit="true"
    v-on:do-submit="submitForm">
    <b-form v-if="formFields.show" v-for="(field, index) in riskFields" :key="index">
      <b-form-group label="Field">
        <b-form-input
          v-model="field.name"
          type="text">
        </b-form-input>
      </b-form-group>
      <b-form-group label="Type">
        <b-form-select
          v-model="field.type"
          :options="fieldChoices">
        </b-form-select>
      </b-form-group>
    </b-form>
  </base-modal>
</template>

<script>
  import BaseModal from "./base-modal";
  import {mixins} from "../mixins.js";

  export default {
    components: {BaseModal},

    mixins: [mixins],

    name: 'add-fields-modal',

    props: {
      formFields: Object,
      apiUrl: String
    },

    data() {
      return {
        riskFields: [
          {
            name: '',
            type: ''
          }
        ],
        fieldChoices: [
          {value: 'text', text: 'Text'},
          {value: 'number', text: 'Number'},
          {value: 'enum', text: 'Enum'},
          {value: 'date', text: 'Date'}
        ]
      }
    },

    methods: {
      submitForm() {
        this.formFields.show= false;
      }
    }
  }
</script>
