> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Errors

> Check the errors returned in the API responses from Razorpay.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
  <span>🇲🇾 Malaysia</span>
  <span>🇸🇬 Singapore</span>
  <span>🇺🇸 United States</span>
</div>

Razorpay APIs, when fired, can have either a successful response or a failure response. All successful Razorpay API responses return with HTTP Status code 200. In case of failure, a JSON error response is returned with the relevant error parameters.

This error response helps to:

* Map and analyse top failure reasons.
* Identify the source of failure. It can be due to customer action or external factors (Razorpay, Gateway, Bank or Network).
* Identify the payment step and the exact failure reason. Display valid responses and provide meaningful next steps to your customers.

## Error Structure

The error response contains `code`, `description`, `field`, `source`, `step`, `reason` and `metadata` parameters that help diagnose and solve the error.

### Sample Code

In this sample code, see the `description`, `source`, `step` and `reason`, indicating that the API failed due to authentication failure for incorrect OTP.

You can notify your customer and ask them to retry the payment with the correct OTP at Razorpay Checkout.

```json Sample Error Response theme={null}
{
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "description": "Authentication failed due to incorrect otp",
    "field": null,
    "source": "customer",
    "step": "payment_authentication",
    "reason": "invalid_otp",
    "metadata": {
      "payment_id": "pay_EDNBKIP31Y4jl8",
      "order_id": "order_DBJKIP31Y4jl8"
    }
  }
}
```

### Response Parameters

`error`
: `object` The error object.

`code`
: `string` Type of the error.

`description`
: `string` Descriptive text about the error.

`field`
: `string` Name of the parameter in the API request that caused the error.

`source`
: `string` The point of failure in the specific operation (payment in this case). Check the [card](/docs/errors/payments/payment-methods-error-parameters#cards), [netbanking](/docs/errors/payments/payment-methods-error-parameters#netbanking), [wallets](/docs/errors/payments/payment-methods-error-parameters#wallet), [UPI Intent](/docs/errors/payments/payment-methods-error-parameters#intent-flow), [Cardless EMI](/docs/errors/payments/payment-methods-error-parameters#cardless-emi) and [Emandate](/docs/errors/payments/payment-methods-error-parameters#emandate) sections to know about the possible values for each method.

`step`
: `string` The stage where the transaction failure occurred. The stages can vary depending on the payment method used to complete the transaction. Check the [card](/docs/errors/payments/payment-methods-error-parameters#cards), [netbanking](/docs/errors/payments/payment-methods-error-parameters#netbanking), [wallets](/docs/errors/payments/payment-methods-error-parameters#wallet), [UPI Intent](/docs/errors/payments/payment-methods-error-parameters#intent-flow), [Cardless EMI](/docs/errors/payments/payment-methods-error-parameters#cardless-emi) and [Emandate](/docs/errors/payments/payment-methods-error-parameters#emandate) sections to know about the possible values for each method.

`reason`
: `string` The exact error reason. It can be handled programmatically.

`metadata`
: `object` Contains additional information about the request.

`payment_id`
: `string` Unique identifier of the payment.

`order_id`
: `string` Unique identifier of the order associated with the payment.

### Related Information

* [Understand Razorpay APIs](/docs/api/understand)
* [API Authentication](/docs/api/authentication)
* [Sandbox Setup](/docs/api/sandbox-setup)
* [Pagination](/docs/api/understand#pagination)
* [Best Practices](/docs/api/best-practices)
* [Glossary](/docs/api/glossary)
