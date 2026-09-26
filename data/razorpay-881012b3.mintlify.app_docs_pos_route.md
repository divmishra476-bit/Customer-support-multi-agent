> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Route

> Use Razorpay Route to split payments between third parties and manage settlements, refunds and reconciliation by creating Linked Accounts.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Razorpay Route allows you to split payments between third parties, sellers or bank accounts. Using Route, you can easily manage settlements, refunds, reconciliation and make vendor payments. It is helpful for businesses that disburse payments in a `one-to-many` model.

## Features

Using Razorpay Route, you can:

* Add and manage Linked Accounts.
* Split payments and transfer funds to multiple Linked Accounts.
* Reverse transferred funds and manage customer refunds with automated reversals.
* Manage Linked Account settlements.
* Move from manual and file-based reconciliation to an entirely API-driven one and more.

<img class="click-zoom" src="https://razorpay.com/docs/build/browser/assets/images/route-route_what_we_offer.jpg" alt="What We Offer" width="970" />

## Advantages

<AccordionGroup>
  <Accordion title="Instant Transfers">
    Razorpay Route facilitates instant transfers, ensuring recipients receive their payments promptly. This benefits businesses and individuals relying on timely payments for their operations or financial needs.
  </Accordion>

  <Accordion title="Multiple Payment Transfers">
    Razorpay Route splits payments into various portions, allowing for seamless funds transfer to different parties involved in a transaction. This is particularly useful in marketplaces, where sellers, service providers, and platform owners receive their respective shares.
  </Accordion>

  <Accordion title="Easy Integration">
    You can easily integrate Razorpay Route within the existing payment system and platform. Its API-driven approach allows businesses to seamlessly incorporate Razorpay Route into their systems by enhancing payment capabilities without significant disruptions.
  </Accordion>

  <Accordion title="Transparent Reporting and Settlements">
    Razorpay provides comprehensive reporting and analytics, allowing us to track transactions, transfers, and settlements.
  </Accordion>
</AccordionGroup>

## How Route Works

Given below is the funds flow in Route:

<img class="click-zoom" src="https://razorpay.com/docs/build/browser/assets/images/route_flow.gif" alt="Route Flow" width="970" />

1. The customer makes a purchase on your site.
2. You can choose to do any one of the following:
   * Initiate transfer of funds to Linked Accounts.
   * Defer the transfer from being settled.
   * Define a time until which the transfer settlement should be delayed.
3. Razorpay settles funds to the Linked Account and sends a webhook payload to you.

## Prerequisites

You should add Linked Accounts using [Dashboard](/docs/payments/route/linked-account#add-and-manage-linked-accounts).

## Get Started

To get started with Route:

1. Log in to the Dashboard and click **Route** under **PAYMENT PRODUCTS**.
2. After login, you should add linked accounts to start using Route. Refer to the [Linked Accounts](/docs/payments/route/linked-account) page for more information.
3. Once linked accounts are added, you can then start creating transfers to those accounts. Refer to the [Transfer Funds to Linked Accounts](/docs/payments/route/transfer-funds-to-linked-accounts) page for more information.

Know more about [Route](/docs/payments/route) and the [Dashboard actions](/docs/payments/route/batch-upload).

### Related information

[Route Use Cases](/docs/payments/route/use-cases)
