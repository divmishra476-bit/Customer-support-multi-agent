> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Contact Error Codes

> RazorpayX Contacts Error Codes. Understand why they occur and the steps to resolve them.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

When firing [Contact APIs](/docs/api/x/contacts), you might run into errors for various reasons. These error codes are returned in an error body, which you can use to understand the reason for the error and the steps to resolve it.

## Error Sample Code and Description

Here is an example of how an error code appears when any Contact API fails.

<CodeGroup>
  ```json Sample Error Response theme={null}
  {
    "error": {
        "code": "BAD_REQUEST_ERROR",
        "description": "The name field is required.",
        "source": "business",
        "step": null,
        "reason": "input_validation_failed",
        "metadata": {},
        "field": "name"
    }
  }
  ```
</CodeGroup>

`code`
: `string` Not applicable for Error Codes. The value is displayed to maintain consistency of the error object.

`description`
: `string` A description for the error. For example, `The name field is required.`.

`source`
: `string` Possible value is `business`. The error can be fixed from your end.

`step`
: `string` Not applicable for API Error Codes. The value is displayed to maintain consistency of the error object.

`reason`
: `string` The error reason. For example, `input_validation_failed`.

`metadata`
: `Null Value` Not applicable for API Error Codes. The value displayed to maintain consistency of the error object.

`field`
: The Contact details in the [Contact entity](/docs/api/x/contacts#contact-entity) such as `name`, `email`, `type` and so on.

### Related Information

* [Contact APIs](/docs/api/x/contacts)
* [Payout Status Details](/docs/errors/x/payout-status-details)
