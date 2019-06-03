<template>
  <div>
    <topbar/>
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
            @click="fieldsForm(row.item, $event.target)">Show Fields
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
      <b-modal
        :id="formFields.id"
        :title="formFields.risk"
        ok-only
        centered
        :header-bg-variant="'info'"
        :footer-bg-variant="'info'">
        <b-form @reset="onReset" v-if="show">
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
      </b-modal>
    </b-container>
  </div>
</template>

<script>
  import Topbar from "./topbar";

  const typeUrl = '/api/risk_type/';
  const singleTypeUrl = '/api/single_risk_type/';

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
        show: false,
        fields: [
          {key: 'name', label: 'Type'},
          {key: 'field_names_', label: 'Fields'},
          {key: 'actions', label: 'Actions'}
        ],
        formFields: {id: 'risk-modal'}
      }
    },
    beforeMount() {
      this.$http.get(typeUrl).then((data) => {
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
      },
      fieldsForm(item, button) {
        this.$http.get(singleTypeUrl + '?risk_id=' + item.id).then((data) => {
          this.formFields = Object.assign(this.formFields, data.data);
          this.$root.$emit('bv::show::modal', this.formFields.id, button);
          this.show = true;
        }).catch(error => {
          this.formFields = {id: 'risk-modal'};
        })
      },
      onReset() {
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
