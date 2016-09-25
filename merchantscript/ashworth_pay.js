// require jquery for the mvp scope. might go full js for lightweight or react for fancy.
// Add jquery and this script to your page, add id="ashworthpay" to the element where you want the payment form.

$( document ).ready(function() {

    formSetup();

    function formSetup() {
        var form_html = '<form id="ashworth-pay-form"><input type="number" name="cardnumber" placeholder="card number" id="card-number">' +
        '<input type="number" name="month" placeholder="expiry month">' +
        '<input type="number" name="year" placeholder="expiry year">' +
        '<input type="number" name="ccv" placeholder="card ccv"></form>' +
        '<input type="submit" id="ashworth-send"></form>'

        var hook = $('#ashworthpay');

        if(!hook.length) {
            console.log('WARNING! no element found to hook the payment form to.');
        } else {
            hook.append(form_html);
            $('#ashworth-send').click(sendData);
        }
    }

    function sendData(){
        var cardNumber = $("#card-number");
        var value = 73.74;
        var currency = 'GBP';

        $.post();
    }


});
