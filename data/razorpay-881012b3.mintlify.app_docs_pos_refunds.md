> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Refunds

> Initiate refunds using Razorpay POS Dashboard and APIs for your customers.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

There could be situations when customers request a refund of the payments made for the products or services purchased or availed on your website or app.

<Info>
  **Customer Looking for Refund**

  If you are a customer looking for a refund, know about [customer refunds](/docs/payments/customers/customer-refunds).
</Info>

## Refund Types

You can use [Normal Refunds](/docs/payments/refunds/normal) to refund payments to your customers. The amount is refunded within 5-7 working days.

## Dashboard Actions

You can perform the following actions on refunds from the Dashboard:

* [View Refunds](/docs/pos/refunds/view)
* [Issue Refunds](/docs/pos/refunds/issue)
* [View Settlement Details of a Refund](/docs/pos/refunds/view#view-settlement-details-of-a-refund)

## Refund States

Following are the various states of a refund:

| States      | Description                                                                                                                                                                                                                                                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created`   | This state indicates that the refund is initiated from Razorpay. This state will be displayed only on the Refunds API.                                                                                                                                               |
| `processed` | This is the final state of the refund.                                                                                                                                                                                                                               |
| `failed`    | A refund can attain the failed state in the following scenarios:<ul><li>Normal refunds are not possible for a payment that is more than 6 months old.</li><li>Instant refunds can sometimes fail because of the customer's account or bank-related issues.</li></ul> |

<Warning>
  **Watch Out!**

  Usually, Razorpay moves a refund to the `processed` state before receiving the ARN/RRN number from the Gateway. You can ensure that a refund moves to the `processed` state only after receiving confirmation from the Gateway by activating this feature on your account by raising a [support request](https://razorpay.com/support/#request).
</Warning>

## Handle Refund Chargeback

For the prevention of chargebacks, Razorpay only does **source refunds**. It means that money is refunded to the payment method that the customer used to make the payment. For example, if a credit card was used to make the payment, the refund is pushed to the same credit card. Similarly, in the case of UPI payments, the refund is pushed to the VPA used while making the payment.

If a chargeback is received for an instantly refunded payment, the processed refund will have a **UTR (Unique Transfer Reference)** in the callback. This UTR appears against the **ARN (Application Reference Number)** parameter in the Refund entity. The UTR serves as proof of refund completed between you and Razorpay.

Additionally, Razorpay passes the **RRN (Razorpay Reference Number)** of the payment in the Fund Transfer Request sent for the refund. This ties the instant refund back to the parent payment, thereby, serving as proof of the refund. This data can also be used as a defense against a future chargeback or arbitration case.

## Reports

Detailed insights can be gained using reports and real-time data on the Dashboard. These reports can then be used for accounting and recon purposes. Know more about [reports](/docs/payments/dashboard/reports).

Understand [how the Refund process works](/docs/payments/refunds/normal#how-normal-refunds-work).

### Related Information

* [Handle refund errors](/docs/pos/refunds/errors)
* [Refunds API](/docs/pos/refunds/apis)
* [Refunds FAQs](/docs/pos/refunds/faqs)
