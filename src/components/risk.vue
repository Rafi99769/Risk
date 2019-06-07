<template>
  <div>
    <top-bar/>

    <b-container fluid>
      <b-row>
        <b-col md="4" class="my-1">
          <b-form-group>
            <b-input-group>
              <b-form-input v-model="filter" placeholder="Search Type"></b-form-input>
              <b-input-group-append>
                <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
              </b-input-group-append>
            </b-input-group>
          </b-form-group>
        </b-col>
        <b-col md="4" offset="4" class="my-1">
          <b-form-group label-cols-sm="3" label="Rows" class="mb-0">
            <b-form-select v-model="perPage" :options="pageOptions"></b-form-select>
          </b-form-group>
        </b-col>
      </b-row>
      <b-table
        show-empty
        stacked="md"
        striped
        hover
        :id="id"
        :items="items"
        :fields="fields"
        :filter="filter"
        @filtered="onFiltered"
        :current-page="currentPage"
        :per-page="perPage">
        <template slot="actions" slot-scope="row">
          <b-button
            size="sm"
            variant="warning">Edit
          </b-button>
          <b-button
            size="sm"
            variant="success">Add Fields
          </b-button>
          <b-button
            size="sm"
            variant="info"
            @click="showFieldsForm(row.item, $event.target)">Show Fields
          </b-button>
        </template>
      </b-table>
      <b-row>
        <b-col md="6" class="my-1">
          <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            class="my-0">
          </b-pagination>
        </b-col>
      </b-row>
      <b-row>
        <b-col md="3" offset="9" class="my-1">
          <b-button
            pill
            variant="primary"
            @click="addRiskForm($event.target)">Add Risk
          </b-button>
        </b-col>
      </b-row>

      <show-risk-field-modal :form-fields="showFieldsFormContent"/>

      <add-risk-modal :form-fields="addRiskFormContent" :api-url="typeUrl"
                      v-on:refresh-table="refreshTable"/>
    </b-container>
  </div>
</template>

<script>
  import TopBar from "./topbar";
  import ShowRiskFieldModal from "./show-risk-field-modal";
  import AddRiskModal from "./add-risk-modal";

  const typeUrl = '/api/risk_type/';
  const singleTypeUrl = '/api/single_risk_type/';

  export default {
    name: 'risk',

    components: {
      AddRiskModal,
      TopBar,
      ShowRiskFieldModal
    },

    data() {
      return {
        id: 'risk-table',
        items: [],
        filter: null,
        currentPage: 1,
        totalRows: 1,
        perPage: 5,
        pageOptions: [1, 5, 10, 15],
        fields: [
          {key: 'name', label: 'Type'},
          {key: 'field_names_', label: 'Fields'},
          {key: 'actions', label: 'Actions', thStyle: {'width': '35%'}}
        ],
        showFieldsFormContent: {id: 'show-field-modal', show: false},
        addRiskFormContent: {id: 'add-risk-modal', show: false},
        typeUrl: typeUrl
      }
    },

    mounted() {
      this.loadData();
    },

    methods: {
      loadData() {
        this.$http.get(typeUrl).then((data) => {
          this.items = data.data;
          this.currentPage = 1;
          this.totalRows = this.items.length;
        }).catch(() => {
          this.items = [];
        })
      },

      refreshTable() {
        this.loadData();
      },

      onFiltered(filteredItems) {
        this.currentPage = 1;
        this.totalRows = filteredItems.length;
      },

      resetShowFieldsFormContent() {
        this.showFieldsFormContent = {id: 'show-field-modal', show: false};
      },

      showFieldsForm(item, button) {
        this.resetShowFieldsFormContent();

        this.$http.get(singleTypeUrl + '?risk_id=' + item.id).then((data) => {
          this.showFieldsFormContent = Object.assign(this.showFieldsFormContent, data.data);
          this.$root.$emit('bv::show::modal', this.showFieldsFormContent.id, button);
          this.showFieldsFormContent.show = true;
        });
      },

      resetAddRiskFormContent() {
        this.addRiskFormContent = {id: 'add-risk-modal', show: false, title: 'Add Risk'};
      },

      addRiskForm(button) {
        this.resetAddRiskFormContent();
        this.$root.$emit('bv::show::modal', this.addRiskFormContent.id, button);
        this.addRiskFormContent.show = true;
      }
    }
  }
</script>
