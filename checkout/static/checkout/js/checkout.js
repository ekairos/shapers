const stripePublicKey = $('#spk').text().slice(1, -1);

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
    const cardError = document.getElementById('card-errors');
    if (event.error) {
        const html = `
            <p class="form-field-error">
            * <span>${event.error.message}</span>
            <p>
        `;
        $(cardError).html(html);
    } else {
        cardError.textContent = '';
    }
});
