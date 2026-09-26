> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Payout Status Details

> Know the status of your payouts using the Payout Status Details API.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Payout Status details are returned when a payout is created and moves to another state.

<Warning>
  **Watch Out!**

  The `failure_reason`, `queueing_details` and `cancellation_details` fields along with the error object would be deprecated from the API response. Please move to Payout status details to understand the status of your payout.
</Warning>

## About Status Details

Status details are sent as part of the fetch payout API response and webhook payloads. You can also check the status details on the [dashboard](/docs/x/payouts/status-details). It provides additional details about each payout status including intermediate status like `pending`, `processing`, `queued` and terminal states like `reversed` and `failed`. The details will include payout clearance SLA and why payout is in `processing` state. A payout update webhook is fired every time an attribute in status details changes.

You can check status details of a payout to know why it is in the `processing` state. It maybe due to:

* [Deemed Success](https://razorpay.com/blog/business-banking/payout-processing-imps-upi-transactions-deemed-success-npci/)
* NEFT/RTGS off hours
* Partner bank or beneficiary bank issues
* Other bank or server issues

You can use this information to keep your beneficiaries informed.

<Info>
  **Handy Tips**

  * The status details object in the payouts' API response gives details about the exact reason for a payout state and the next steps to be taken. Please share this information with your developers.
  * You can subscribe to daily reports to receive a detailed document on the status, reason for status and SLA for the payouts in `processing state`. [Raise a support ticket](/docs/x/support) from the Dashboard, with a list of recipient email IDs. We will enable the function for you in 3 working days.
</Info>

## Status Details API Response

Below is the sample status details response that appears as part of the status details object.

### Sample Code

<CodeGroup>
  ```json Sample Status Details Response Code theme={null}
  {
    "status_details": {
      "description": "IMPS is not enabled on beneficiary account, Retry with different mode",
      "source": "beneficiary_bank",
      "reason": "imps_not_allowed",
    }
  }
  ```

  ```json Complete Status Details Response Code theme={null}
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
    "created_at": 1545383037,
    "status_details": {
      "description": "IMPS is not enabled on beneficiary account, Retry with different mode",
      "source": "beneficiary_bank",
      "reason": "imps_not_allowed",
    }
  }
  ```
</CodeGroup>

`description`
: `string` A description for the error. For example, `IMPS is not enabled on beneficiary account, Retry with different mode`.

`source`
: `string` Possible values:

* `gateway`: Technical error at Razorpay partner bank.
* `beneficiary_bank`: Technical error at beneficiary bank.
* `business`: Merchant action required.
* `internal`: Technical error at Razorpay's server.

`reason`
: `string` The error reason. For example, `imps_not_allowed`.

All the reasons for any payout state appear at the [source parameter](#sample-code) of the code. The error reason, source, description and steps to be taken for various payout statuses are given below.

### Status: reversed/failed

<div className="error-code-cards">
  <CardGroup cols={2}>
    <Card title="bank_account_closed" icon="building-columns">
      * **Description**: Payout failed as the beneficiary account is closed. Please contact the beneficiary bank.
      * **Source**: beneficiary\_bank
      * **Next Steps**: NA
    </Card>

    <Card title="bank_account_frozen" icon="lock">
      * **Description**: Payout failed as beneficiary account is frozen. Please contact the beneficiary bank.
      * **Source**: beneficiary\_bank
      * **Next Steps**: NA
    </Card>

    <Card title="bank_account_invalid" icon="building-columns">
      * **Description**: Payout failed due to invalid beneficiary account details.
      * **Source**: beneficiary\_bank
      * **Next Steps**: NA
    </Card>

    <Card title="beneficiary_account_dormant" icon="lock">
      * **Description**: Payout failed as beneficiary account is dormat. Please contact the beneficiary bank.
      * **Source**: beneficiary\_bank
      * **Next Steps**: NA
    </Card>

    <Card title="beneficiary_bank_failure" icon="building-columns">
      * **Description**: Payout failed at the beneficiary bank due to a technical issue. Please retry after 30 min.
      * **Source**: beneficiary\_bank
      * **Next Steps**: Retry
    </Card>

    <Card title="beneficiary_bank_offline" icon="building-columns">
      * **Description**: Beneficiary bank systems are offline. Please retry after 30 min.
      * **Source**: beneficiary\_bank
      * **Next Steps**: Retry
    </Card>

    <Card title="beneficiary_bank_rejected" icon="ban">
      * **Description**: Payout rejected by the beneficiary bank. Please contact the beneficiary bank.
      * **Source**: beneficiary\_bank
      * **Next Steps**: NA
    </Card>

    <Card title="beneficiary_bank_technical_error" icon="building-columns">
      * **Description**: Payout failed due to a technical issue at the beneficiary bank. Please retry after 30 min.
      * **Source**: beneficiary\_bank
      * **Next Steps**: Retry
    </Card>

    <Card title="beneficiary_psp_offline" icon="circle-exclamation">
      * **Description**: Beneficiary PSP systems are offline. Please retry after 30 min.
      * **Source**: beneficiary\_bank
      * **Next Steps**: Retry
    </Card>

    <Card title="imps_not_allowed" icon="circle-exclamation">
      * **Description**: IMPS is not enabled on beneficiary account. Please retry with different mode.
      * **Source**: beneficiary\_bank
      * **Next Steps**: Retry with a different payment mode.
    </Card>

    <Card title="invalid_ifsc_code" icon="building-columns">
      * **Description**: Payout failed as the IFSC code is invalid. Please correct the IFSC code and retry.
      * **Source**: beneficiary\_bank
      * **Next Steps**: Retry with correct IFSC code.
    </Card>

    <Card title="npci_beneficiary_timeout" icon="clock">
      * **Description**: Temporary technical issue between NPCI and the beneficiary bank. Please retry after 30 min.
      * **Source**: beneficiary\_bank
      * **Next Steps**: Retry
    </Card>

    <Card title="transaction_limit_exceeded" icon="gauge-high">
      * **Description**: Payout amount greater than the limit supported by the beneficiary account.
      * **Source**: beneficiary\_bank
      * **Next Steps**: NA
    </Card>

    <Card title="amount_limit_exhausted_neft" icon="gauge-high">
      * **Description**: The NEFT 24\*7 limits for your account has been exhausted. Please retry after sometime.
      * **Source**: business
      * **Next Steps**: Retry
    </Card>

    <Card title="beneficiary_account_invalid" icon="circle-exclamation">
      * **Description**: Payout failed due to invalid beneficiary account number.
      * **Source**: business
      * **Next Steps**: NA
    </Card>

    <Card title="beneficiary_vpa_invalid" icon="at">
      * **Description**: UPI validation failed. If the UPI ID is valid, please retry after sometime.
      * **Source**: business
      * **Next Steps**: Ensure UPI ID is valid and retry.
    </Card>

    <Card title="insufficient_funds" icon="wallet">
      * **Description**: Payout failed due to insufficient funds in your account.
      * **Source**: business
      * **Next Steps**: Add funds to your account and retry.
    </Card>

    <Card title="invalid_beneficiary" icon="circle-exclamation">
      * **Description**: Customer account does not exist with the wallet provider for the given phone number.
      * **Source**: business
      * **Next Steps**: NA
    </Card>

    <Card title="gateway_down" icon="server">
      * **Description**: Payout failed as the partner bank is facing technical issues. Please retry.
      * **Source**: gateway
      * **Next Steps**: Retry
    </Card>

    <Card title="gateway_technical_error" icon="server">
      * **Description**: Payout failed due to a temporary technical issue at the partner bank. Please retry after 30 min.
      * **Source**: gateway
      * **Next Steps**: Retry
    </Card>

    <Card title="gateway_timeout" icon="clock">
      * **Description**: Payout timed out at the partner bank. Please retry after 30 min.
      * **Source**: gateway
      * **Next Steps**: Retry
    </Card>

    <Card title="server_error" icon="server">
      * **Description**: Payout failed. Contact support for help.
      * **Source**: internal
      * **Next Steps**: Contact support to find out the exact issue.
    </Card>

    <Card title="server_error_temporary" icon="server">
      * **Description**: Payout failed due to temporary technical issue. Please retry.
      * **Source**: internal
      * **Next Steps**: Retry
    </Card>
  </CardGroup>
</div>

### Status: processing

<div className="error-code-cards">
  <CardGroup cols={2}>
    <Card title="beneficiary_bank_confirmation_pending" icon="building-columns">
      * **Description**: Confirmation of credit to the beneficiary is pending from `beneficiary_bank`. Please check the status after (date,time).
      * **Source**: beneficiary\_bank
      * **Next Steps**: Inform the customer of the delay, reason for the same and by when it will be cleared.
    </Card>

    <Card title="bank_window_closed" icon="building-columns">
      * **Description**: The `mode` window for the day is closed. Please check the status after (date,time).
      * **Source**: gateway
      * **Next Steps**: Inform the customer of the delay, reason for the same and by when it will be cleared.
    </Card>

    <Card title="payout_bank_processing" icon="building-columns">
      * **Description**: Payout is being processed by the partner bank. Please check the final status after (date,time).
      * **Source**: gateway
      * **Next Steps**: Inform the customer of the delay, reason for the same and by when it will be cleared.
    </Card>

    <Card title="amount_limit_exhausted" icon="gauge-high">
      * **Description**: The (mode) 24\*7 limits for your account has been exhausted. Please check the status after (date,time).
      * **Source**: business
      * **Next Steps**: Inform the customer of the delay, reason for the same and by when it will be cleared.
    </Card>

    <Card title="partner_bank_pending" icon="building-columns">
      * **Description**: Payout is being processed by our partner bank. Please check the final status after (date,time).
      * **Source**: internal
      * **Next Steps**: Inform the customer of the delay, reason for the same and by when it will be cleared.
    </Card>
  </CardGroup>
</div>

### Status: processed

<div className="error-code-cards">
  <CardGroup cols={2}>
    <Card title="payout_processed" icon="circle-check">
      * **Description**: Payout is processed and the money has been credited into the beneficiary's account.
      * **Source**: beneficiary\_bank
      * **Next Steps**: NA
    </Card>
  </CardGroup>
</div>

### Status: pending

<div className="error-code-cards">
  <CardGroup cols={2}>
    <Card title="pending_approval" icon="hourglass-half">
      * **Description**: Workflow for the payout is pending approval from the approver(s).
      * **Source**: business
      * **Next Steps**: NA
    </Card>
  </CardGroup>
</div>

### Status: queued

<div className="error-code-cards">
  <CardGroup cols={2}>
    <Card title="gateway_degraded" icon="server">
      * **Description**: Payout is queued as Partner bank systems are down.
      * **Source**: gateway
      * **Next Steps**: NA
    </Card>

    <Card title="beneficiary_bank_down" icon="building-columns">
      * **Description**: Beneficiary bank's systems are not working. Payout will be processed after the system starts working else it will be failed after the pre-defined time limit.
      * **Source**: gateway
      * **Next Steps**: NA
    </Card>

    <Card title="low_balance" icon="wallet">
      * **Description**: Payout is queued as there is insufficient balance in your account to process the payout.
      * **Source**: business
      * **Next Steps**: NA
    </Card>

    <Card title="syncing_balance" icon="wallet">
      * **Description**: Payout is queued as your balance is being synced with the bank. Please check the status after some time.
      * **Source**: gateway
      * **Next Steps**: Check status after some time.
    </Card>

    <Card title="fee_recovery_pending" icon="hourglass-half">
      * **Description**: Payout is queued as you have a pending fee recovery payout. It will get processed after the fee recovery payout is cleared.
      * **Source**: business
      * **Next Steps**: NA
    </Card>
  </CardGroup>
</div>

### Related Information

* [About Payouts](/docs/x/payouts)
* [Payout Best Practices](/docs/x/payouts/best-practices)
* [Status Details via Dashboard](/docs/x/payouts/status-details)
