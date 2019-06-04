<template>
  <b-modal
    :id="formFields.id"
    :title="formFields.risk"
    ok-only
    centered
    :header-bg-variant="'info'"
    :footer-bg-variant="'info'">
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
  </b-modal>
</template>

<script>
  export default {
    props: {
      formFields: Object
    }
  }
</script>
