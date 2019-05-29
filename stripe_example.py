try:
  import stripe
  stripe.api_key = "sk_test_5D6yzdOiPWgciMYeF8YwwCXs"

  for customer in stripe.Customer.list(limit=3):
    print(customer['description'], '###### Cards #####', end='\n')
    for card in customer.sources.list(object='card'):
      print(card, end='\n')

except stripe.error.CardError as e:
  # Since it's a decline, stripe.error.CardError will be caught
  body = e.json_body
  err  = body.get('error', {})

  print("Status is: %s" % e.http_status)
  print("Type is: %s" % err.get('type'))
  print("Code is: %s" % err.get('code'))
  # param is '' in this case
  print("Param is: %s" % err.get('param'))
  print("Message is: %s" % err.get('message'))
except stripe.error.RateLimitError as e:
  # Too many requests made to the API too quickly
  body = e.json_body
  err = body.get('error', {})

  print("Status is: %s" % e.http_status)
  print("Type is: %s" % err.get('type'))
  print("Code is: %s" % err.get('code'))
  # param is '' in this case
  print("Param is: %s" % err.get('param'))
  print("Message is: %s" % err.get('message'))
except stripe.error.InvalidRequestError as e:
  # Invalid parameters were supplied to Stripe's API
  body = e.json_body
  err = body.get('error', {})

  print("Status is: %s" % e.http_status)
  print("Type is: %s" % err.get('type'))
  print("Code is: %s" % err.get('code'))
  # param is '' in this case
  print("Param is: %s" % err.get('param'))
  print("Message is: %s" % err.get('message'))
except stripe.error.AuthenticationError as e:
  # Authentication with Stripe's API failed
  # (maybe you changed API keys recently)
  body = e.json_body
  err = body.get('error', {})

  print("Status is: %s" % e.http_status)
  print("Type is: %s" % err.get('type'))
  print("Code is: %s" % err.get('code'))
  # param is '' in this case
  print("Param is: %s" % err.get('param'))
  print("Message is: %s" % err.get('message'))
except stripe.error.APIConnectionError as e:
  # Network communication with Stripe failed
  body = e.json_body
  err = body.get('error', {})

  print("Status is: %s" % e.http_status)
  print("Type is: %s" % err.get('type'))
  print("Code is: %s" % err.get('code'))
  # param is '' in this case
  print("Param is: %s" % err.get('param'))
  print("Message is: %s" % err.get('message'))
except stripe.error.StripeError as e:
  # Display a very generic error to the user, and maybe send
  # yourself an email
  body = e.json_body
  err = body.get('error', {})

  print("Status is: %s" % e.http_status)
  print("Type is: %s" % err.get('type'))
  print("Code is: %s" % err.get('code'))
  # param is '' in this case
  print("Param is: %s" % err.get('param'))
  print("Message is: %s" % err.get('message'))
except Exception as e:
  # Something else happened, completely unrelated to Stripe
  print("Status is: %s" % e.http_status)

