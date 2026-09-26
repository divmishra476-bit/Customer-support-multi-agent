> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscribe to Webhooks

> Setup and manage webhooks for your client application from the Razorpay Dashboard.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Webhooks allow you to build or set up integrations that subscribe to certain Razorpay events on merchant resources. When one of those events is triggered, we send an HTTP POST payload in JSON to a specific URL.

Webhooks can be configured and managed independently for each application you create on your Dashboard, thereby giving you greater control over your notifications.

Know more about [Razorpay Webhooks](/docs/webhooks).

## Set Up Webhooks

Managing webhooks for individual applications follows the same procedure as managing account webhooks.

<Info>
  **Handy Tips**

  If you are just starting off and have not created an application yet, refer the [create application section](/docs/partners/technology-partners/onboard-businesses/integrate-oauth/integration-steps#1-create-an-application) to create an app.
</Info>

To set up webhooks:

1. Log in to the Dashboard.
2. Navigate to **Applications**.
3. On a created application, click **Manage Webhook**.
   <img src="https://razorpay.com/docs/build/browser/assets/images/oauth_test_7.jpg" alt="Manage Webhook" width="475" />
4. Enter the **Webhook URL** where you will receive the webhook payload when the event is triggered.
   <img src="https://razorpay.com/docs/build/browser/assets/images/oauth_test_8.jpg" alt="Edit Webhook" width="475" />
5. Create a new **Secret**. This field is optional.

<Info>
  **Handy Tips**

  The **Secret** can be used to validate that the webhook is from Razorpay, thus it should not be exposed publicly. On the UI, the **Secret** will not be shown after creation. You can leave the **Secret** blank to leave it unedited.
</Info>

6. Select the event(s) you want to activate the webhook for from the list of available events.
7. Click **Save** to enable the webhook.

To validate your webhook signature, refer the [Validation section](/docs/webhooks/validate-test#validate-webhooks).

<Info>
  **Handy Tips**

  Use the Test mode on the Dashboard to test webhooks.
</Info>

## Webhook Retries

The webhook responses must return a status code in the range 2XX within a window of 5 seconds. If we receive response codes other than this or if the request times out, it is considered a failure.

On failure, a webhook is retried at progressive intervals of time.
