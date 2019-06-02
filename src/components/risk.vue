<template>
  <div>
    <topbar></topbar>
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
        :items="items"
        :fields="fields"
        :filter="filter"
        @filtered="onFiltered"
        :current-page="currentPage"
        :per-page="perPage">
        <template slot="actions" slot-scope="row">
          <b-button variant="warning">Edit</b-button>
          <b-button variant="success">Add Fields</b-button>
          <b-button variant="info">Show Fields</b-button>
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
      <b-modal :id="field-modal">
        <b-form></b-form>
      </b-modal>
    </b-container>
  </div>
</template>

<script>
  import Topbar from "./topbar";

  const typeUrl = '/api/risk_type/';

  export default {
    components: {
      Topbar
    },
    name: 'risk',
    data() {
      return {
        items: [],
        filter: null,
        currentPage: 1,
        totalRows: 1,
        perPage: 10,
        pageOptions: [1, 5, 10, 15],
        fields: [
          {key: 'name', label: 'Type'},
          {key: 'field_names_', label: 'Fields'},
          {key: 'actions', label: 'Actions'}
        ]
      }
    },
    beforeMount() {
      let promise = this.$http.get(typeUrl);
      return promise.then((data) => {
        this.items = data.data.results;
      }).catch(error => {
        this.items = [];
      })
    },
    mounted() {
      this.totalRows = this.items.length;
    },
    methods: {
      onFiltered(filteredItems) {
        this.currentPage = 1;
        this.totalRows = filteredItems.length;
      }
    }
  }
</script>

<style>
  li {
    display: inline-block;
    margin: 0 0;
  }
</style>
