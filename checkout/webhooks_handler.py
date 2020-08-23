from django.http import HttpResponse


class StripeWhHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event_default(self, event):
        """Default Stripe webhook events handler method"""

        print("Default Handler", f'{event["type"]}')
        return HttpResponse(
            content=f'Stripe webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle Stripe successful payment intents"""

        payment_intent = event.data.object
        print('INTENT SUCCESS', f'{event["type"]}', payment_intent)

        return HttpResponse(
            content=f'Stripe Webhook received: '
                    f'{event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """Handle Stripe payment intent failures"""

        print('INTENT FAILED', f'{event["type"]}')
        return HttpResponse(
            content=f'Stripe Webhook Failure received: {event["type"]}',
            status=200)
