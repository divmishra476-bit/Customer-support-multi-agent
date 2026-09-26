> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Frequently Asked Questions (FAQs)

> Find answers to frequently asked questions about Refunds via Razorpay and IRCTC refunds.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

<AccordionGroup>
  <Accordion title="How do I initiate a refund?">
    You can issue partial or full refund using:

    * [The Dashboard](/docs/pos/refunds/issue#issue-refunds).
    * [APIs](/docs/api/refunds).

    By default, the entire amount is refunded. If you issue a partial refund, ensure the partial refund option is selected and enter the desired value in INR.

    <Warning>
      **Watch Out!**

      Razorpay issues immediate refunds. Once a refund is issued, it cannot be canceled or reversed.
    </Warning>
  </Accordion>

  <Accordion title="Do you charge for refunds?">
    No, we do not charge for the regular refunds. However, fees and taxes charged for a captured payment are not reversed.
  </Accordion>

  <Accordion title="I am unable to refund a payment. What do I do?">
    If your current balance is less than the amount you are trying to refund, you can either initiate the refund once you receive further payments or you can [add funds](/docs/payments/dashboard/account-settings#add-funds) to your account from the Dashboard.
  </Accordion>
</AccordionGroup>
