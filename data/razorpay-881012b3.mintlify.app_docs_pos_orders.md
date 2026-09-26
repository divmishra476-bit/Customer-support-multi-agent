> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Orders

> All about Razorpay Orders, their states and Razorpay Dashboard actions.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Order is an important step of the payment life cycle at Razorpay. When a customer clicks the pay button, an order is created with a unique identifier. This contains details such as the transaction amount and currency. The order id secures the payment request and one cannot tamper with the order amount. Pass this order id to the Razorpay Checkout.

### Advantages

* Single successful payment bound to an order. Prevents multiple payments.
* Quick and easy query in the database. Combines multiple payment attempts for a single order.

## Order States

Following are the various states of an order:

| Status      | Description                                                                                                                                                                                                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created`   | When a new order is created, it is in the `created`  state. It stays in this state until payment is attempted on it.                                                                                                                                                        |
| `attempted` | An order moves from `created` to `attempted` state when payment is first attempted on it. It remains in the `attempted` state until a payment associated with that order is captured.                                                                                       |
| `paid`      | After the payment is captured successfully, the order moves to the `paid` state. No further payment requests are allowed once the order moves to the `paid` state. The order continues to be in the `paid` state even if the payment associated with the order is refunded. |

<Warning>
  **Watch Out!**

  If an order is in an `attempted` state with the associated payment id in the `authorized` state, initiating another payment using the same order id is not allowed.
</Warning>

## Order and Payment Flows

Following is a pictorial representation of how order and payment flows are closely related:

<img class="click-zoom" src="https://razorpay.com/docs/build/browser/assets/images/orders-payment-flow.jpg" alt="Pictorial representation of Order and Payment Flow" width="800" />

## Dashboard Actions

Perform the following actions using the Dashboard:

* [View orders](/docs/pos/orders/dashboard#view-order-details)
* [View reports related to orders](/docs/pos/orders/dashboard#reports)
