> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Types

> Explore the RazorpayX Error Codes and know how to troubleshoot and understand them.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

RazorpayX aims to make all transactions successful for its customers. Even then, errors might still occur in the financial ecosystem due to intermittent communication and technical issues at multiple levels.

In RazorpayX, you can identify error codes at the `source` of the response, along with the `reason` for such errors. This will help in minimising the errors reducing the losses.

* [**API Error Codes**](#api-error-codes): These are returned to you when the API does not fire as expected.
* [**Contact Error Codes**](/docs/errors/x/contacts): These are returned when an error occurs during contact creation.
* [**Fund Account Error Codes**](/docs/errors/x/fund-account): These are returned when Fund Account creation fails.
* [**Payout Status Details**](/docs/errors/x/payout-status-details): These provide the reason for a payouts' state and the next steps to be taken. These are returned in the API response and webhook payloads and are available on the Dashboard.

<CardGroup cols={2}>
  <Card title="Advantages of Error Codes">
    Error codes can help you build your own logic and take further remedial action at your end, wherever possible. Deriving these insights can help your business to:

    * Map and analyse top failure reasons.
    * Identify the source of failure.
    * Narrow down and understand the cause of the failure (could be due to actions taken by your contact or external factors such as the beneficiary bank or network connectivity).
    * Identify the exact reason of the failure.
    * Handle actionable error codes.
    * Avoid possible integration errors.
  </Card>
</CardGroup>

## API Error Codes

API error codes are sent to you when an API cannot be fired. All successful Razorpay API responses return with HTTP Status code 200.

Razorpay Errors API identifies two types of errors:

* Business: Errors where merchant action is required.
* Internal: Technical errors at Razorpay's server.

In case of a failure, we return a JSON error response that contains the reason for the failure. You can use this response to make changes to the API request body and try to fire them again.

Check [API Error Reasons and Next Steps](#api-error-reasons-and-next-steps) to understand the reason and troubleshooting procedure.

### Sample Code for API Errors

API errors appear in the format shown below. You can refer to the [API errors troubleshooting steps](#api-error-reasons-and-next-steps) to resolve them.

<CardGroup cols={1}>
  <Card title="Sample Error Code">
    Here is an example of how an error code appears when an API does not fire.

    <CodeGroup>
      ```json Sample Error Response theme={null}
       {
         "error": {
         "code": "BAD_REQUEST_ERROR",
         "description": "The account number field is required",
         "source": "business",
         "step": "null",
         "reason": "input_validation_failed",
         "metadata": {},
         "field": "account_number"
         }
       }
      ```

      ```json Complete Error Response theme={null}
       {
         "id": "pout_00000000000001",
         "entity": "payout",
         "fund_account_id": "fa_00000000000001",
         "amount": 1000000,
         "currency": "INR",
         "notes": {
         "notes_key_1": "Tea, Earl Grey, Hot",
         "notes_key_2": "Tea, Earl Grey… decaf."
         },
         "fees": 0,
         "tax": 0,
         "status": "failed",
         "utr": null,
         "mode": "IMPS",
         "purpose": "refund",
         "reference_id": "Acme Transaction ID 12345",
         "narration": "Acme Corp Fund Transfer",
         "batch_id": null,
         "failure_reason": "IMPS is not enabled on Beneficiary Account",
         "created_at": 1545383037,
         "error": {
         "description": "IMPS is not enabled on beneficiary account, Retry with different mode",
         "source": "beneficiary_bank",
         "reason": "imps_not_allowed",
         "code": "NA",
         "step": "NA",
         "metadata": {}
         }
       }
      ```
    </CodeGroup>
  </Card>

  <Card title="Parameters">
    `code`
    : `string` Type of the error. For example, `BAD_REQUEST_ERROR`.

    `description`
    : `string` A description for the error. For example, `The id provided does not exist`.

    `source`
    : `string` Possible values:

    * `business`: Merchant action required.
    * `internal`: Technical error at Razorpay's server.

    `reason`
    : `string` The error reason. For example, `input_validation_failed`.

    `step`
    : `NA` Not applicable for API Error Codes, value displayed to maintain consistency of error object.

    `metadata`
    : `Null value` Not applicable for API Error Codes, value displayed to maintain consistency of error object.
  </Card>
</CardGroup>

### API Error Reasons and Next Steps

The below tables lists the API error reasons and the steps to fix them.

| Error Description                                                                           | Next Steps                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The requested URL was not found on the server.                                              | Occurs when wrong URL or HTTPS method is passed. Enter the correct URL as per the respective API request. Know more about [API gateway URLs](/docs/api/x#api-gateway-url). If the issue persists, [contact support](/docs/x/support). |
| Transactions from this IP are not allowed. Contact support for help.                        | Occurs when the API call is sent from an IP whose server/node is not allowlisted. Always [allowlist IPs](/docs/x/dashboard/allowlist-ip).                                                                                             |
| Different request body sent for the same Idempotency Header.                                | Occurs when the system receives a different payout request body for an existing idempotent header. Ensure that every payout body has a [unique idempotency header](/docs/api/x/payout-idempotency/make-request).                      |
| We are facing some trouble completing your request at the moment. Please try again shortly. | Occurs in exceptional cases when there is a server issue at Razorpay's end. Retry safely using an [idempotency request](/docs/api/x/payout-idempotency/make-request) or [contact support](/docs/x/support).                           |

## HTTP Errors

Given below is a list of HTTP error codes, reasons and next steps to fix them.

<CardGroup cols={1}>
  <Card title="HTTP Code 400: BAD_REQUEST_ERROR">
    * **Error Description**: Payout is not in pending state and cannot be approved or rejected.
    * **Source**: business
    * **Reason**: `payout_approval_not_allowed`
    * **Next Steps**: Payout approval is no longer required. No further action required.

    ```json Sample Error Response theme={null}
      {
        "error": {
          "code": "BAD_REQUEST_ERROR",
          "description": "Payout is not in pending state and cannot be approved or rejected",
          "source": "business",
          "step": "NA",
          "reason": "payout_approval_not_allowed",
          "metadata": {}
        }
      }
    ```
  </Card>

  <Card title="HTTP Code 401: BAD_REQUEST_AUTHENTICATION_ERROR">
    **The OAuth token used in the request was invalid or has expired**

    * **Source**: business
    * **Reason**: `authentication_failed`
    * **Next Steps**: Please check the OAuth token being used and retry again.

    ```json Sample Error Response theme={null}
    {
      "error": {
        "code": "BAD_REQUEST_ERROR",
        "description": "The OAuth token used in the request was invalid or has expired",
        "source": "business",
        "step": "NA",
        "reason": "authentication_failed",
        "metadata": {}
      }
    }
    ```

    **The OAuth token used does not have sufficient permissions for this request**

    * **Source**: business
    * **Reason**: `authentication_failed`
    * **Next Steps**: Please check the OAuth token being used and retry again.

    ```json Sample Error Response theme={null}
    {
      "error": {
        "code": "BAD_REQUEST_ERROR",
        "description": "The OAuth token used does not have sufficient permissions for this request",
        "source": "business",
        "step": "NA",
        "reason": "authentication_failed",
        "metadata": {}
      }
    }
    ```
  </Card>

  <Card title="HTTP Code 500: SERVER_ERROR">
    * **Error Description**: We are facing some trouble completing your request at the moment. Please try again shortly.
    * **Source**: internal
    * **Reason**: `server_error`
    * **Next Steps**: Retry the request using the same idempotency key and request body. See [Handling 5XX Errors](#handling-5xx-errors) for the recommended retry schedule.

    ```json Sample Error Response theme={null}
    {
      "error": {
        "code": "SERVER_ERROR",
        "description": "We are facing some trouble completing your request at the moment. Please try again shortly.",
        "source": "internal",
        "step": "NA",
        "reason": "server_error",
        "metadata": {}
      }
    }
    ```
  </Card>

  <Card title="HTTP Code 502: GATEWAY_ERROR">
    * **Error Description**: The request could not be completed due to an error at the payment gateway or downstream bank.
    * **Source**: internal
    * **Reason**: `gateway_error`
    * **Next Steps**: Retry the request using the same idempotency key and request body. See [Handling 5XX Errors](#handling-5xx-errors) for the recommended retry schedule.

    ```json Sample Error Response theme={null}
    {
      "error": {
        "code": "GATEWAY_ERROR",
        "description": "The request could not be completed due to an error at the payment gateway",
        "source": "internal",
        "step": "NA",
        "reason": "gateway_error",
        "metadata": {}
      }
    }
    ```
  </Card>

  <Card title="HTTP Code 503: SERVICE_UNAVAILABLE">
    * **Error Description**: The service is temporarily unavailable. This is usually a transient condition.
    * **Source**: internal
    * **Reason**: `service_unavailable`
    * **Next Steps**: Retry the request using the same idempotency key and request body. See [Handling 5XX Errors](#handling-5xx-errors) for the recommended retry schedule.

    ```json Sample Error Response theme={null}
    {
      "error": {
        "code": "SERVER_ERROR",
        "description": "The service is temporarily unavailable. Please try again shortly.",
        "source": "internal",
        "step": "NA",
        "reason": "service_unavailable",
        "metadata": {}
      }
    }
    ```
  </Card>
</CardGroup>

### Handling 5XX Errors

5xx errors occur when servers fail to connect, causing network issues during an ongoing payout process. The [idempotency feature](/docs/api/x/payout-idempotency/make-request) is specifically built to handle such network issues.

<Warning>
  **Critical: Retry rules for 5XX errors**

  When retrying after a 5XX error:

  * You **must** use the **same idempotency key** as the original request.
  * You **must** send the **same request body**. A different payload is rejected as a `BAD_REQUEST`.
  * You can safely retry within **7 calendar days** of the original request.

  Razorpay guarantees the payout will not be processed twice if it was already completed.
</Warning>

**Recommended retry schedule**

If you receive a 5XX error or a timeout, retry up to 3 times at the following intervals:

1. After **1 minute**
2. After **2 minutes**
3. After **5 minutes**

After 3 retries with no success, do not retry further. Wait at least 1 hour before marking the payout as failed.

### Reducing 5XX Errors

If the payout was created in the first request to the RazorpayX system using the same idempotency key, you get the created payout details along with the current [status](/docs/x/payouts/states-life-cycle#payout-states) in the response to the new request.

<Warning>
  **Watch Out!**

  The current status of the payout can be returned as `pending`, `processing`, or `failed`.
</Warning>

### Mark Failed Status of a Payout request with 5XX error

If a 5XX error is received on the request or a retried request:

1. After **5 minutes**, check the payout status using `reference_id` (the same value you passed in the original request) via the [Fetch all payouts API](/docs/api/x/payouts/fetch-all). Do this for up to **1 hour** from payout creation time, in case you do not receive a webhook.
2. If no status is returned after 1 hour, mark the payout as **failed**.

## Webhooks

We recommend you to enable webhooks so that you are alerted of the status updates in any process. By enabling alerts for errors, you can reduce the delay in troubleshooting.

* You can [Set Up Payout Webhooks](/docs/webhooks/setup-edit-payouts) to configure and receive instant notifications.
* They are sent whenever a specific [event](/docs/webhooks) occurs.
* When the configured events are triggered, we send an HTTP POST [payload](/docs/webhooks/payouts) in JSON to the webhook's configured URL.

### Related Information

* [Contact Error Codes](/docs/errors/x/contacts)
* [Fund Account Error Codes](/docs/errors/x/fund-account)
* [Payout Status Details](/docs/errors/x/payout-status-details)
