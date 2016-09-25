// require jquery for the mvp scope. might go full js for lightweight or react for fancy.
// Add jquery and this script to your page, add id="ashworthpay" to the element where you want the payment form.

$( document ).ready(function() {

    hook = $('.ashworthpay');
    if(!hook.length) {
        console.log('WARNING! no element found to hook the payment form to.');
    } else {
        // stuff.
    }

});
