<template>
  <div>
    <base-modal
      :id="formFields.id"
      :title="formFields.title"
      :submit="true"
      v-on:do-submit="submitForm">
      <b-form v-if="formFields.show">
        <b-form-group label="Risk Type">
          <b-form-input
            type="text"
            v-model="riskType">
          </b-form-input>
        </b-form-group>
        <p v-if="error" style="color: red">{{ error }}</p>
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
        riskType: '',
        error: ''
      }
    },

    methods: {
      submitForm(event) {
        if (!this.riskType) {
          this.error = 'This field is required';
          event.preventDefault();
          return false;
        }

        this.$http.post(this.apiUrl, {name: this.riskType}).then(() => {
          this.showToast('success', 'Risk type created successfully', 'Success');
          this.$emit('refresh-table');
        }).catch(err => {
          this.showError(err);
        });

        this.formFields.show = false;
        this.riskType = '';
        this.error = '';
      }
    }
  }
</script>
