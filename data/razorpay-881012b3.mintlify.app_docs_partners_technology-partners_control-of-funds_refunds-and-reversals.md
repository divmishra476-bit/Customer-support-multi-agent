> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Refunds and Reversals

> Process refunds and reversals using APIs. Refund the base transaction amount and reverse platform and third-party fees.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

You can create refunds and reversals in 2 cases:

* **The base transaction amount is refunded** <br />
  You can refund the base transaction amount with or without reversing the platform and third-party fees.

* **The platform and third-party fees are reversed** <br />
  You can reverse the platform and third-party fees with or without refunding the base transaction amount.

### Create Refund Without Reversals

To create refunds without reversals, you can process [Normal Refunds](/docs/api/refunds/create-normal) or [Instant Refunds](/docs/api/refunds/create-instant) using our APIs. Know more about [Instant Refunds](/docs/payments/refunds/instant).

### Create Refund With Reversals

Sub-merchants can process refunds from their Dashboards. Alternatively, you (the Platform) can process refunds on behalf of sub-merchants. If you are processing the refund, you can specify whether the platform fees should also be refunded or not using the [Refund Payments and Reverse Transfer from a Linked Account](/docs/api/payments/route) API.

### Create Reversals Only for Platform or Third-Party Fees

Every platform fee or third-party fee is linked with a Transfer. To reverse the platform or third-party fees, use the [Reverse a Transfer API](/docs/api/payments/route/reverse-a-transfer).

## Related Information

* [Set up Platform and Third-Party Accounts](/docs/partners/technology-partners/control-of-funds/set-up-accounts)
* [Process Platform and Third-Party Fees](/docs/partners/technology-partners/control-of-funds/process-fees)
