> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Onboarding Status

> Track your sub-merchant's onboarding status through webhooks.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

You can [subscribe to webhook events](/docs/partners/technology-partners/onboard-businesses/integrate-oauth/subscribe-to-webhooks) to receive real-time notifications about a merchant's account activation status. Using this information, you can:

* Nudge your sub-merchants to complete their onboarding and get payments enabled.
* Know when a sub-merchant's account is activated to manage their payments.

## Available Webhook Events

| Webhook Event                 | Description                                                                         | Payload                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `account.activated`           | Triggered when an account is successfully activated and ready for use.              | [Sample Payload](/docs/webhooks/partners/activated#account-activated)                     |
| `account.under_review`        | Triggered when an account is under review for verification or compliance checks.    | [Sample Payload](/docs/webhooks/partners/under-review#account-under-review)               |
| `account.needs_clarification` | Triggered when additional information is required to complete account verification. | [Sample Payload](/docs/webhooks/partners/needs-clarification#account-needs-clarification) |
| `account.suspended`           | Triggered when an account is disabled due to policy or compliance violations.       | [Sample Payload](/docs/webhooks/partners/suspended#account-suspended)                     |
| `account.rejected`            | Triggered when an account application is declined and cannot be activated.          | [Sample Payload](/docs/webhooks/partners/rejected#account-rejected)                       |
