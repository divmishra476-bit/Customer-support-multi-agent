> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Frequently Asked Questions (FAQs)

> Find answers to frequently asked questions about Razorpay Payments.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

<AccordionGroup>
  <Accordion title="How much does Razorpay charge per transaction?">
    Razorpay offers an enterprise plan designed for large volumes, which gives you the best prices possible for your business. Know more about [pricing](https://razorpay.com/pricing/).
  </Accordion>

  <Accordion title="Is GST mandatory to accept payments?">
    No, GST is not mandatory if your business does not have an annual turnover of over ₹20 lakhs. However, if you do not provide your GST details, you would not be able to claim TDS at the time of filing your tax returns.
  </Accordion>

  <Accordion title="What is the applicable GST? How is it charged?">
    18% GST is charged on the fee deducted for all payment methods except domestic card transactions of amount \< = ₹ 2,000. You can check the [Monthly Invoice Report](/docs/payments/magic-checkout/analytics/reports#generate-reports) from the **Reports** section of your Dashboard to understand GST charged.
  </Accordion>

  <Accordion title="How are payments made by my customers settled to my account? Is any action required from my end?">
    No action is required from your end for the settlements. Razorpay automatically settles the captured payments to your account as per your settlement cycle. Know more about [Settlements](/docs/payments/settlements).
  </Accordion>

  <Accordion title="A payment is marked as 'failed' on my Dashboard but money is debited from the customer’s account. What do I do?">
    A payment is said to be in the 'failed' state when we do not receive a successful callback message on the transaction from the issuing bank. If the customer’s account is debited and we do not receive a successful callback, the amount will be auto-refunded by the customer’s issuing bank in 7-10 working days.<br />
    In case of a failed payment, we verify the status with the bank at regular intervals. If there is a change in status, the payment moves to the `authorized` state, and a notification is sent to you and the customer.<br />
    In such scenarios, you can choose to do any one of the following:

    * **Provide services**: Capture the payment and provide the service/good as was promised earlier to the customer.
    * **Refund the transaction**: If you are not able to provide service to the customer as per the agreed terms (such as, time of delivery, cost of purchase or inventory issues), refund the payment to the customer.
  </Accordion>

  <Accordion title="Is Razorpay PCI-DSS compliant?">
    Yes, Razorpay is PCI-DSS compliant.
  </Accordion>
</AccordionGroup>
