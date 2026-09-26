> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Issue Refunds

> Issue refunds to customers using Razorpay Dashboard and APIs.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

You can issue refunds to your customers using the Dashboard or APIs. Refunds are possible for `captured` payments only.

<Info>
  **Customer Looking for Refund**

  If you are a customer looking for a refund, know about [customer refunds](/docs/payments/customers/customer-refunds).
</Info>

## Full and Partial Refunds

Refunds can be made either in **full** or in **part**.

* **Full Refund**
  <br />You can refund the entire amount that you received in the payment.

* **Partial Refund**
  <br />You can refund part of the amount received in the payment. You can issue multiple, partial refunds as long as their sum does not exceed the captured amount.

A payment moves to the `refunded` state only when the entire amount is refunded to the customer. In case of partial refunds, the payment continues to remain in the `captured` state till the entire payment is refunded.

## Issue Refunds

### Issue Refunds Using Dashboard

To issue refunds:

1. Log in to the Dashboard.
2. Navigate to **Transactions** → **Payments**.
3. Select the payment for which a refund is requested. The payment should be in the `captured` state.
4. Scroll to the **Refund** section and click **Issue Refund**.
5. In the **amount** field, enter an amount lesser than the captured amount for issuing a partial refund. By default, the entire amount will be refunded.
6. Review the fees that will be levied for the refund to be processed instantly.
7. Click the **Issue Full Refund** or **Issue Partial Refund** button, depending on the amount to be refunded.

### Issue Refunds Using API

* To create a normal refund, use the [Create a Normal Refund API](/docs/api/refunds/create-normal).

### Related Information

* [About Refunds](/docs/pos/refunds)
* [Normal Refunds](/docs/pos/refunds/normal)
* [Refunds FAQs](/docs/pos/refunds/faqs)
