<template>
  <div>
    <base-modal
      :id="formFields.id"
      :title="formFields.title"
      :submit="true"
      v-on:do-submit="submitForm">
      <div class="panel panel-default"
           v-for="(field, index) in riskFields">
        <div class="text-right ml-lg-5">
        <span style="cursor: pointer"
              @click="deleteField(index)">×</span>
        </div>
        <div class="panel-body">
          <b-form v-if="formFields.show"
                  :key="index"
                  class="mb-2"
                  inline>
            <label>Field</label>
            <b-form-input
              v-model="field.name"
              type="text"
              class="ml-sm-2 mb-2 w-90">
            </b-form-input>
            <label>Type
              <b-form-select
                v-model="field.type"
                :options="fieldChoices"
                class="ml-sm-2 mr-sm-2">
              </b-form-select>
            </label>
            <label v-if="field.type === 'enum'">Choices</label>
            <b-form-select
              v-if="field.type === 'enum'"
              :options="field.choices"
              class="ml-sm-2 mr-sm-2 w-40">
            </b-form-select>
            <b-button v-if="field.type === 'enum'"
                      variant="success"
                      size="sm"
                      @click="addChoice(index)"
                      v-b-modal.choice-modal>Add
            </b-button>
          </b-form>
        </div>
      </div>
      <b-row class="mt-1">
        <b-col md="4" offset="4" class="text-center">
          <b-button
            variant="primary"
            size="sm"
            @click="addField">Add More
          </b-button>
        </b-col>
      </b-row>
    </base-modal>

    <base-modal
      id="choice-modal"
      title="Add Choice"
      :submit="true"
      v-on:do-submit="submitChoice">
      <b-form-group label="Choice">
        <b-form-input
          type="text"
          v-model="choice.value">
        </b-form-input>
      </b-form-group>
    </base-modal>
  </div>
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
      apiUrl: String,
      riskId: String
    },

    data() {
      return {
        riskFields: [
          {
            name: '',
            type: '',
            choices: []
          }
        ],
        fieldChoices: [
          {value: 'text', text: 'Text'},
          {value: 'number', text: 'Number'},
          {value: 'enum', text: 'Enum'},
          {value: 'date', text: 'Date'}
        ],
        choice: {
          index: null,
          value: ''
        }
      }
    },

    mounted() {
      this.$root.$on('bv::modal::hide', (event, modalId) => {
        if (modalId === this.formFields.id)
          this.resetRiskFields();
        else
          this.resetChoice();
      });
    },

    methods: {
      submitForm() {
        this.$http.post(this.apiUrl, {
          risk_id: this.riskId,
          risk_fields: this.riskFields
        }).then(() => {
          this.showToast('success', 'Risk field created successfully', 'Success');
          this.$emit('refresh-table');
        }).catch(err => {
          this.showError(err);
        });

        this.formFields.show = false;
      },

      addField() {
        this.riskFields.push({
          name: '',
          type: '',
          choices: []
        });
      },

      addChoice(index) {
        this.choice.index = index;
      },

      submitChoice() {
        this.riskFields[this.choice.index].choices.push(this.choice.value);
      },

      deleteField(index) {
        this.riskFields.splice(index, 1);
      },

      resetRiskFields() {
        this.riskFields = [
          {
            name: '',
            type: '',
            choices: []
          }
        ];
      },

      resetChoice() {
        this.choice = {
          index: null,
          value: ''
        }
      }
    }
  }
</script>
