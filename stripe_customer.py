# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = 'pk_test_51KYbhzBWScTJy5yL9lIkeozFzkNSrQ5boYNcqnrtnqnodpyJ7nUCOGTZvCPrianCfhlWIITUIiF68tmxnbQtSVKN00J14pRpSy'
stripe.Customer.create(description = "My First Test Customer")


stripe.PaymentIntent.create(
    customer = '{{USER_ID}}',
    currency = "usd",
    amount = 2000,
    payment_method_types = ["card"],
    setup_future_usage = "on_session",
)