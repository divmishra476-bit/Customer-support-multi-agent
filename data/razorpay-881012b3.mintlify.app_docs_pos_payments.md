> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Payments

> Check payments, the various payment states and Razorpay Dashboard actions. Understand late authorisations.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

You can accept live payments using the Razorpay Payment Gateway once your Razorpay account has been activated.

## Payment Life Cycle

Following are the various states of a payment:

| States       | Description                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created`    | This is the first state.  The customer has provided the payment details, which are sent to Razorpay. The payment has not been processed yet.                                                                                                                                                                                                                                        |
| `authorized` | The payment state changes to `authorized` when the bank successfully authenticates the customer's payment details. The money is deducted from the customer’s account by Razorpay. The amount is settled to your account after the payment is manually or automatically captured.  Payment in this state is auto-refunded to the customer if not captured within 3 days of creation. |
| `captured`   | When the payment status is changed to `captured`, the payment is verified as complete by Razorpay. The amount is settled to your account as per the settlement schedule.                                                                                                                                                                                                            |
| `refunded`   | You can refund the payments that have been successfully captured at your end. The amount is reversed to the customer's account.                                                                                                                                                                                                                                                     |
| `failed`     | An unsuccessful payment attempt is marked as `failed`, and the customer will have to retry the payment. Any amount debited will be refunded into customers account in 5-7 working days.                                                                                                                                                                                             |

The following state diagram depicts the flow of money through the various payment states:

<img src="https://razorpay.com/docs/build/browser/assets/images/payment-capture-payment-states.jpg" class="click-zoom" alt="Different stages of Payments Life Cycle" width="800" />

## Dashboard Actions

You can perform the following actions on payments from the Dashboard:

* [Issue a refund for a payment](/docs/pos/refunds/issue)
* [View details of a payment](/docs/pos/payments/dashboard#view-payment-details)
* [View settlement details of a payment](/docs/pos/settlements/dashboard#view-settlements-using-dashboard)
