> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Commission for Payment Products

> Check how you can earn Partner commissions and how the commission is calculated for Payments products.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
  <span>🇲🇾 Malaysia</span>
</div>

You can become a Razorpay Partner, offer your customers a complete suite of payment and payout solutions and get rewarded for it in the form of commissions. You can earn commissions by charging an additional fee in the invoice raised on the customer, either as a flat amount or a percentage of the transaction value.

## How it Works

Let us assume you are **Acme Corporation**, an ERP solution provider for colleges, and have partnered with Razorpay. You work with various colleges, who use your ERP and allow students to make fee payments online using Razorpay Payment Gateway.

In Razorpay terminology, you are the Partner, the college is the Sub-merchant (affiliate account) and the college student is the customer. Acme Corporation can charge a service fee to ABC College. The ABC College can charge this service fee to the students. This service fee is the commission received by Acme Corporation.

| Partner            | Merchant      | Customer                 |
| ------------------ | ------------- | ------------------------ |
| `Acme Corporation` | `ABC College` | `Saurav Kumar` (Student) |

## Commission Calculation

By default, the commission is offered as a percentage of the transaction value. If you have a use case for a flat-rate commission model, contact our [Partnerships team](mailto:partnerships@razorpay.com).

### Commission Charged as a Percentage Transaction Value

*(Say 0.1%)*

Let us assume that the term fee is ₹10000. The following charges apply:

| Term Fees <br /><br />(A) | Payment Gateway Fee <br /><br />(B) | Service Fee <br />(Percentage of Transaction Value) <br />(C) | GST<br /><br /><br />(D) | Total Amount <br /><br />(A)+(B)+(C)+(D) |
| ------------------------- | ----------------------------------- | ------------------------------------------------------------- | ------------------------ | ---------------------------------------- |
| ₹10000                    | 10000\*2% = ₹200                    | 10000\*0.1% = ₹10                                             | (200+10)\*18% = ₹37.8    | **₹10247.8**                             |

### Commission as a Flat Rate

*(Say ₹10)*

Let us assume that the term fee is ₹10000. The following charges apply:

| Term Fees <br /><br />(A) | Payment Gateway Fee <br /><br />(B) | Service Fee <br />(Flat) <br />(C) | GST <br /><br />(D)    | Total Amount <br /><br />(A)+(B)+(C)+(D) |
| ------------------------- | ----------------------------------- | ---------------------------------- | ---------------------- | ---------------------------------------- |
| ₹10000                    | 10000\*2% = ₹200                    | ₹10                                | (200+100)\*18% = ₹37.8 | **₹10247.8**                             |

## Refunds Post Commission Payouts

In cases, where there is a refund after the commission has been paid out, it is entered as a negative commission in your account in the corresponding cycle. No commission is paid out for refund cases.

### Related Information

* [Commission Settlement Process](/docs/partners/commissions/settlement-process)
* [Commission Reports and Auto-generated Invoices](/docs/partners/commissions/reports-invoices)
* [Partners](/docs/partners)
