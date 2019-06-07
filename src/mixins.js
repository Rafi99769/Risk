export const mixins = {
  methods: {
    showToast(variant = null, msg) {
      this.$bvToast.toast(msg, {
        toaster: 'b-toaster-top-center',
        variant: variant,
        solid: true,
        toastClass: 'm-t-15'
      });
    }
  }
};
