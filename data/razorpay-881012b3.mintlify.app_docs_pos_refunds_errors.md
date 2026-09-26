> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Handle Refund Errors

> Check the errors that may occur while processing Refunds and how to handle these errors.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Sometimes when you try to process a refund request, it fails to get processed and you may encounter `BAD_REQUEST_ERROR` messages stating refunds are not supported. This happens because most of the banks do not support refunds for payments that are more than 6 months old.

## List of Possible Refund Errors

```json Error Response theme={null}
{
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "description": "Refund is not supported by the bank because the payment is more than 6 months old",
    "source": null,
    "step": null,
    "reason": null,
    "metadata": {}
  }
}
```

```json Error Response theme={null}
{
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "description": "Payment is more than 6 months old, only instant refund is supported",
    "source": null,
    "step": null,
    "reason": null,
    "metadata": {}
  }
}
```

To check the refund status, navigate to the **Refund Details** pop-up by clicking on the specific **Refund Id** under the **Transactions** → **Refunds** tab.

You can get the ARN/RRN for successfully processed refunds under the [Dashboard Refunds tab](/docs/payments/refunds/view) or using the [Fetch Refund API](/docs/api/refunds#fetch-refund-by-id). This is a unique reference number that can be used by customers to track refunds.

### Related Information

* [About Refunds](/docs/pos/refunds)
* [Normal Refunds](/docs/pos/refunds/normal)
* [Refunds FAQs](/docs/pos/refunds/faqs)
