> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Settlements - Dashboard Actions

> View settlement details, check the settlements break-up, enable settlements on hold and view reports from the Razorpay Dashboard.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

You can use the Dashboard to perform the following actions:

* [View Settlements](#view-settlements-using-dashboard)
* [Settlements Break-Up Description](#settlements-break-up-description)
* [View Settelement Timeline](#view-settlement-timeline-on-dashboard)
* [Enable Settlements Places on Hold](#enable-settlements-placed-on-hold)
* [View Reports](#reports)

## View Settlements Using Dashboard

You can view details of settlements made to you from the Dashboard.

To view settlement details:

1. Log in to the Dashboard.
2. Navigate to **Settlements**.
3. Click on the **details** of the settlement ID that you wish to refer.

### Settlements Break-Up Description

The following screenshot displays the settlement break-up:

<img src="https://razorpay.com/docs/build/browser/assets/images/settlements-2.jpg" alt="Settlement break-up description image" width="400" />

A settlement has the following components:

`Payment`
: The total payment amount that is being settled before deductions.

`Adjustment`
: Adjustments to transactions, if any.

`Tax`
: Tax deducted on the payment.

`Fee`
: Fees deducted by Razorpay for the transactions.

`Transfer`
: Transfers made if any, Transfers are payouts made to your [linked accounts](/docs/payments/route/linked-account).

Linked accounts are accounts created for third-party sellers by you after onboarding them onto the Razorpay platform.

`Refunds`
: Refunds made if any, are refunds you have issued to your customer.

<AccordionGroup>
  <Accordion title="Example">
    In this example, the amount settled to your account = Payment - Adjustment - Tax - Fee - Transfer + Refunds

    | Transaction Details                  | Amount(₹) |
    | ------------------------------------ | --------- |
    | Payment                              | 50.00     |
    | Refunds                              | 10.00     |
    | Tax                                  | 2.88      |
    | Fee                                  | 16.00     |
    | Total amount settled in your account | 20.94     |
  </Accordion>
</AccordionGroup>

<AccordionGroup>
  <Accordion title="Example: Gross Settelements and Deductions Calculations">
    Following is an example of gross settlements and deductions calculations of your settlement:

    <img src="https://razorpay.com/docs/build/browser/assets/images/settlement-components-view.jpg" alt="settlement components detail view" width="800" />

    The gross settlements and deductions calculations only apply to merchants on the prepaid model.
  </Accordion>
</AccordionGroup>

## View Settlement Timeline on Dashboard

You can view the settlement timeline to check when the settlement for a particular payment will be credited.

To view the settlement timeline:

1. Log in to the Dashboard.
2. Navigate to **Settlements**.
3. Click on the **details** of the settlement ID for which you want to view the timeline.
4. You will be able to see the settlement timeline for that particular settlement ID.
   <img src="https://razorpay.com/docs/build/browser/assets/images/pos-settlement-details.jpg" alt="POS settlement details" width="800" />

## Enable Settlements Placed On Hold

Your settlement can be placed on hold if we detect some risk with your payments or with your Razorpay account. You are notified about this on your Dashboard.

Contact the [support team](https://razorpay.com/support) to enable settlements that are placed on hold.

<img src="https://razorpay.com/docs/build/browser/assets/images/settlements-risk-soh-notice.jpg" alt="Settlements placed on hold" width="800" />

To enable settlements when they are put on hold:

1. Log in to the Dashboard.
2. Navigate to **Home**.
3. Click **Resolve** on the notification as shown above..

## Reports

Detailed insights can be gained using reports and real-time data on the Dashboard. These reports can then be used for accounting and reconciliation purposes. Know more about [reports.](/docs/pos/dashboard/reports)

### Related Information

* [About Settlements](/docs/pos/settlements)
* [Settlement FAQs](/docs/pos/settlements/faqs)
