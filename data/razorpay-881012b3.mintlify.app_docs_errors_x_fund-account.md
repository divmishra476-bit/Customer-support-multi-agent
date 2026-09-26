> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Fund Account Error Codes

> RazorpayX Fund Account Error Codes. Understand why they occur and the steps to resolve them.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Fund Account error codes are returned when a fund account creation fails for some reason. You can identify when a Fund Account API has failed with the response or webhooks.

## Errors Sample Code and Description

Here is an example of how an error code appears when a fund account creation fails.

### Sample Code

```json Sample Error Response theme={null}
{
  "error": 
  {
      "code": "BAD_REQUEST_ERROR",
      "description": "The id provided does not exist",
      "source": "business",
      "step": null,
      "reason": "input_validation_failed",
      "metadata": {}
  }
}
```

`code`
: `string` Not applicable for Error Codes, value displayed to maintain consistency of error object.

`description`
: `string` A description for the error. For example, `IMPS is not enabled on beneficiary account, Retry with different mode`.

`source`
: `string` Possible values:

* `business`: The error can be fixed from your end.

`step`
: `string` Not applicable for API Error Codes, value displayed to maintain consistency of error object.

`reason`
: `string` The error reason. For example, `input_validation_failed`.

`metadata`
: `Null Value` Not applicable for API Error Codes, value displayed to maintain consistency of error object.

### Related Information

* [Fund Account APIs](/docs/api/x/fund-accounts)
* [Payout Status Details](/docs/errors/x/payout-status-details)
