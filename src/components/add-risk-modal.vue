<template>
  <div>
    <base-modal
      :id="formFields.id"
      :title="formFields.title"
      :submit="true"
      v-on:do-submit="submitForm">
      <b-form v-if="formFields.show" @submit="submitForm">
        <b-form-group label="Risk Type">
          <b-form-input
            type="text"
            v-model="riskType">
          </b-form-input>
        </b-form-group>
      </b-form>
    </base-modal>
  </div>
</template>

<script>
  import BaseModal from "./base-modal";
  import {mixins} from "../mixins.js";

  export default {
    name: 'add-risk-modal',

    mixins: [mixins],

    components: {
      BaseModal
    },

    props: {
      formFields: Object,
      apiUrl: String
    },

    data() {
      return {
        riskType: ''
      }
    },

    methods: {
      submitForm() {
        if (this.riskType) {
          this.$http.post(this.apiUrl, {name: this.riskType}).then(() => {
            this.showToast('success', 'Risk Created Successfully');
            this.$emit('refresh-table');
          }).catch(err => {
            this.showToast('danger', err);
          });
        }

        this.formFields.show = false;
        this.riskType = '';
      }
    }
  }
</script>
