export const mixins = {
  methods: {
    upperFirstChar(msg) {
      return msg[0].toUpperCase() + msg.substring(1);
    },

    showToast(variant = null, msg, title) {
      this.$bvToast.toast(msg, {
        title: title,
        toaster: 'b-toaster-top-center',
        variant: variant,
        solid: true,
        toastClass: 'm-t-15'
      });
    },

    showError(error) {
      let responseData = error.response.data, msg = '';
      Object.keys(responseData).some(key => {
        msg = Array.isArray(responseData[key]) ? responseData[key][0] : responseData[key];
        return msg !== '';
      });
      this.showToast('danger', this.upperFirstChar(msg), 'Error');
    }
  }
};
