const stripePublicKey = $('#spk').text().slice(1, -1);
const stripeClientSKey = $('#scsk').text().slice(1, -1);

var stripe = Stripe(stripePublicKey);

var elements = stripe.elements({
    fonts: [{
        fontFamily: 'Lato',
        cssSrc: 'https://fonts.googleapis.com/css2?family=Lato&display=swap',
    }]
});

const style = {
    base: {
        color: '#495057',
        fontFamily: '"Lato", serif',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#6c757d',
            fontStyle: 'italic',
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {'style': style});

card.mount('#card-element');

// Stripe Form Validation Feedback
card.addEventListener('change', function (event) {
    const cardErrors = document.getElementById('card-errors');
    if (event.error) {
        const html = `
            <p class="form-field-error">
            * <span>${event.error.message}</span>
            <p>
        `;
        $(cardErrors).html(html);
    } else {
        cardErrors.textContent = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    // prevent multiple submissions
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);

    stripe.confirmCardPayment(stripeClientSKey, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {

        if (result.error) {
            const cardErrors = document.getElementById('card-errors');
            const html = `
              <p class="form-field-error">
                * <span>${result.error.message}</span>
              <p>`
            $(cardErrors).html(html);
            // enable form modification on errors
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);

        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
