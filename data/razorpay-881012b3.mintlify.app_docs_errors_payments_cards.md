> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Cards Error Codes

> Explore errors related to card payments, discover reasons, merchant descriptions, and actionable next steps.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
  <span>🇲🇾 Malaysia</span>
  <span>🇸🇬 Singapore</span>
  <span>🇺🇸 United States</span>
</div>

Below are the top error codes associated with card payments, along with their reasons, descriptions and subsequent steps for resolution.

<div className="error-code-cards">
  <CardGroup cols={2}>
    <Card title="payment_timed_out" icon="clock">
      * **Description**: The payment could not be completed as the customer exceeded the time limit for payment processing. This time limit is typically 10 minutes unless otherwise specified.
      * **Next Steps**: Please request your customer to pay within the specified time limits for the payment.
    </Card>

    <Card title="gateway_technical_error" icon="server">
      * **Description**: There was a downtime on our partner bank due to which the payment has failed.
      * **Next Steps**: Payment Aggregators depend on partner banks for payment processing, and instances of failure like these are beyond our control. <br />
        Nevertheless, there is a proactive solution to address these issues. Inquire with your Customer Support Executive/ Sales Executive about implementing multi-terminal routing.
    </Card>

    <Card title="payment_cancelled" icon="circle-xmark">
      **Customer Cancelled Transaction**

      * **Description**: The payment could not be completed because the customer cancelled the transaction or pressed the back button during the payment processing period.
      * **Next Steps**: Please suggest to your customers to make another attempt or complete the payment at a later time.

      **Bank Downtime**

      * **Description**: There was a downtime on the customer's bank due to which the payment has failed.
      * **Next Steps**: In the case of Standard Checkout, please guide your customers on interpreting downtime information during the checkout process. Encourage them to consider using a different bank to complete the transaction successfully.<br />
        In the case of Custom/S2S checkout, if you have not done so already, integrate the <a href="/docs/api/payments/downtime" target="_blank">Downtime API</a> into your checkout system. This will allow you to showcase downtime information directly on your checkout interface.
    </Card>

    <Card title="card_declined" icon="ban">
      * **Description**: The payment was declined by the customer's bank, resulting in the transaction being unsuccessful.
      * **Next Steps**: Razorpay may not have access to specific details regarding the failure reason, as customer banks typically do not provide such information. To understand the cause and address the issue, we recommend customers reach out directly to their banks. <br />
        Please advise your customer to attempt the payment again using another card.
    </Card>

    <Card title="insufficient_funds" icon="wallet">
      * **Description**: The payment did not go through because the customer's bank account did not have enough funds to complete the transaction.
      * **Next Steps**: We recommend informing your customers to ensure they have an adequate balance before initiating a transaction. Additionally, customers can verify their account balance through the Banking Partner app prior to proceeding with any transactions.
    </Card>

    <Card title="card_not_enrolled" icon="credit-card">
      * **Description**: The payment was unsuccessful as the card was not activated or enabled by the customer for online transactions.
      * **Next Steps**:  We recommend guiding your customers to enable online transaction functionality for their card through their Card Control page. This can be easily accomplished either through their Banking App or by logging in via their net banking portal.
    </Card>

    <Card title="bank_technical_error" icon="building-columns">
      * **Description**: There was a downtime on the customer's bank due to which the payment has failed.
      * **Next Steps**: In the case of Standard Checkout, please guide your customers on interpreting downtime information during the checkout process. Encourage them to consider using a different bank to complete the transaction successfully.<br />
        In the case of Custom/S2S checkout, if you have not done so already, integrate the <a href="/docs/api/payments/downtime" target="_blank">Downtime API</a> into your checkout system. This will allow you to showcase downtime information directly on your checkout interface.
    </Card>

    <Card title="card_disabled_for_online_payments" icon="lock">
      * **Description**: The payment was unsuccessful as the card was not activated or enabled by the customer for online transactions.
      * **Next Steps**: We recommend guiding your customers to enable online transaction functionality for their card through their Card Control page. This can be easily accomplished either through their Banking App or by logging in via their net banking portal.
    </Card>

    <Card title="authentication_failed" icon="shield-halved">
      * **Description**: The payment did not go through as the customer entered incorrect OTP/verification details or accidentally closed the browser/pressed the back button during the authentication stage of the transaction.
      * **Next Steps**: Please ensure customers correctly enter the OTP during transactions and avoid closing the browser during authentication. If the card supports <a href="/docs/payments/optimizer/native-otp" target="_blank">Native OTP</a>, encourage its use to prevent errors.
    </Card>

    <Card title="payment_risk_check_failed" icon="triangle-exclamation">
      * **Description**: The transaction was unsuccessful as the customer's bank declined the payment, citing it as fraudulent.
      * **Next Steps**: Razorpay may not have access to specific details regarding the failure reason, as customer banks typically do not provide such information. To understand the cause and address the issue, we recommend customers reach out directly to their bank.<br />
        Please advise your customer to attempt the payment again using another card.
    </Card>

    <Card title="payment_failed" icon="circle-exclamation">
      * **Description**: The payment was declined by the customer's bank, resulting in the transaction being unsuccessful.
      * **Next Steps**: Razorpay may not have access to specific details regarding the failure reason, as customer banks typically do not provide such information. To understand the cause and address the issue, we recommend customers reach out directly to their bank.<br />
        Please advise your customer to attempt the payment again using another card.
    </Card>

    <Card title="incorrect_cvv" icon="hashtag">
      * **Description**: The payment was unsuccessful as the customer entered an incorrect CVV during the payment process.
      * **Next Steps**: Additionally, you can promote the convenience of saving their card details at checkout, which can enable a <a href="/docs/payments/payment-methods/cards/features/cvv-less-flow" target="_blank">CVV-less flow</a> and simplify the payment process for future transactions.
    </Card>

    <Card title="debit_instrument_inactive" icon="credit-card">
      * **Description**: The payment was unsuccessful as the card was not activated or enabled by the customer for online transactions.
      * **Next Steps**: We recommend guiding your customers to enable online transaction functionality for their card through their card control page. This can be easily accomplished either through their banking app or by logging in via their net banking portal.
    </Card>

    <Card title="debit_instrument_blocked" icon="lock">
      * **Description**: The payment could not be processed due to the card being blocked, either by the customer or their bank.
      * **Next Steps**: We suggest informing customers to reach out to their bank to resolve the issues and unblock their cards. However, they can attempt the transaction again using an active card.
    </Card>

    <Card title="card_expired" icon="calendar-xmark">
      * **Description**: The payment could not be completed because the customer's card is expired.
      * **Next Steps**: We suggest urging customers to reach out to their bank to resolve the issues and unblock their cards. Alternatively, they can attempt the transaction again using an active card.
    </Card>

    <Card title="transaction_limit_exceeded" icon="gauge-high">
      * **Description**: The payment did not go through because the customer has already reached the maximum transaction limit on their card for the day.
      * **Next Steps**: We recommend suggesting to your customer to retry the payment using a different card or alternative payment methods to complete the payment.
    </Card>
  </CardGroup>
</div>
