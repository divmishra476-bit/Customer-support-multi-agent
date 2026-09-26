> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Payment Method Error Parameters

> List of values for Source and Step parameters for each payment method supported by Razorpay.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
  <span>🇲🇾 Malaysia</span>
  <span>🇸🇬 Singapore</span>
  <span>🇺🇸 United States</span>
</div>

There are certain error codes specific for each payment method supported by Razorpay. To understand the errors and their `reasons`, it is recommended to know the `source` (stakeholders) and the `steps` involved in the payment flows:

* [Cards](#cards)
* [UPI](#upi)
* [Netbanking](#netbanking)
* [Wallet](#wallet)
* [Cardless EMI](#cardless-emi)
* [Emandate](#emandate)

## Cards

The payment flow for **Card** payments is illustrated below.

<img src="https://razorpay.com/docs/build/browser/assets/images/payment-flow-card.jpg" class="click-zoom" alt="Errors Payment Methods Cards" width="800" />

<Tabs>
  <Tab title="Source Parameter">
    The possible values for the `source` parameter for cards are listed below:

    * `customer`
    * `business`
    * `internal`
    * `gateway`
    * `issuer_bank`
  </Tab>

  <Tab title="Step Parameter">
    The possible values for the `step` parameter, along with the description, are listed below:

    1. `payment_initiation`<br />
       Your system initiates and sends the payment request to our server. Our server validates your request, creates the payment flow and forwards the request to the Gateway.

    2. `card_enrollment_check`<br />
       Upon receiving a request from Razorpay, Gateway sends the enrollment check request to the bank for the enrollment of the card check.

    3. `payment_authentication`<br />
       The bank verifies the enrollment of the card, and then requests the authentication of the customer by sending 3DS URL and OTP to the customer.

       * 3DS URL<br />
         Bank sends the Authentication (3DS URL), which is routed through Gateway > Razorpay > Customer.

       * OTP<br />
         The bank sends the OTP to the customer’s mobile directly. The customer enters the valid OTP within the time on the bank's OTP page.

    4. `payment_authorization`<br />
       Once the customer has completed the authentication, the bank authorises the release of the funds. The authorisation status is communicated to the Gateway which in turn communicates the same to Razorpay.

    5. `payment_capture`<br />
       Once the payment is successfully authorised, Razorpay sends the capture request to the Gateway which in turn sends the same to the bank to capture the authorised payment.
  </Tab>
</Tabs>

## UPI

**UPI** payments can be made using the following:

<CardGroup cols={2}>
  <Card title="Intent Flow">
    The payment flow for UPI Intent payments is illustrated below.

    <img src="https://razorpay.com/docs/build/browser/assets/images/payment-flow-upi_intent.jpg" />

    <Tabs>
      <Tab title="Source Parameter">
        The possible values for the `source` parameter for both collect and intent flows in UPI are as follows:

        * `customer`
        * `business`
        * `internal`
        * `customer_psp`
        * `gateway`
        * `network`
        * `issuer_bank`
        * `beneficiary_bank`
      </Tab>

      <Tab title="Step Parameter">
        The possible values for the `step` parameter for UPI Intent flow, along with the description, are listed below:

        1. `mandate_creation`<br />
           Request to create a new UPI mandate.

        2. `payment_initiation`<br />
           Your system initiates and sends the payment request to our server.

        3. `payment_creation`<br />
           Razorpay creates an intent URL and passes it back to you.

        4. `payment_authentication`<br />
           Payer clicks on the pay button (pointing to the intent url), which prompts the payer to open the PSP App. After the App opens, the payer enters the M-PIN on the PSP App, and then authenticates the transaction.

        5. `payment_request`<br />
           Payer PSP sends the payment request to the UPI network.

        6. `payment_request_beneficiary_details`<br />
           The UPI network requests the beneficiary details from the Payee PSP.

        7. `payment_response_beneficiary_details`<br />
           Payee PSP  sends the beneficiary details to the UPI network.

        8. `payment_debit_request`<br />
           The UPI network requests a debit of the given payment amount from the customer's bank.

        9. `payment_debit_response`<br />
           Customer’s bank sends the debit response to the NPCI.

        10. `payment_credit_request`<br />
            The UPI network sends the payment credit request to your account maintained with Razorpay.

        11. `payment_credit_response`<br />
            The beneficiary bank sends the credit response to the UPI network.

        12. `payment_status_request`<br />
            UPI network requests the transaction confirmation status from Payee PSP which acts as the gateway in UPI transactions.

        13. `payment_status_response`<br />
            Payee PSP sends the transaction confirmation response to the UPI Network.

        14. `payment_response`<br />
            Payee PSP sends the callback to our server. This will contain the final transaction status.

        15. `refund_request`<br />
            Request to initiate a refund.
      </Tab>
    </Tabs>
  </Card>

  <Card title="Collect Flow">
    The payment flow for UPI Collect payments is illustrated below.

    <img src="https://razorpay.com/docs/build/browser/assets/images/payment-flow-upi_collect.jpg" />

    <Tabs>
      <Tab title="Source Parameter">
        The possible values for the `source` parameter for both collect and intent flows in UPI are as follows:

        * `customer`
        * `business`
        * `internal`
        * `customer_psp`
        * `gateway`
        * `network`
        * `issuer_bank`
        * `beneficiary_bank`
      </Tab>

      <Tab title="Step Parameter">
        The possible values for the `step` parameter for the UPI Collect flow, along with the description, are listed below:

        1. `mandate_creation`<br />
           Request to create a new UPI mandate.

        2. `payment_initiation`<br />
           Your system initiates and sends the payment request to our server.

        3. `payment_creation`<br />
           Razorpay creates the payment and sends the collect request via Payee PSP (Gateway).

        4. `payment_request`<br />
           Payee PSP sends the payment request to the UPI network.

        5. `payment_authentication_request`<br />
           The UPI network sends an authentication request for the given payment amount to the Payer PSP.

        6. `payment_authentication`<br />
           Customer clicks on the payment notification received on mobile which opens the PSP App. After the App opens, the customer enters the M-PIN on the PSP App, and then authenticates the transaction.

        7. `payment_authentication_response`<br />
           Payer PSP  sends the authentication details to the UPI network.

        8. `payment_debit_request`<br />
           Upon successful authentication, the UPI network requests a debit of the given payment amount from the customer's bank.

        9. `payment_debit_response`<br />
           Customer’s bank sends the debit response to the UPI Network.

        10. `payment_credit_request`<br />
            The UPI network sends the payment credit request to your account maintained with Razorpay.

        11. `payment_credit_response`<br />
            The beneficiary bank sends the credit response to the UPI network.

        12. `payment_status_request`<br />
            UPI network sends the transaction confirmation request to payer PSP (Google Pay).

        13. `payment_status_response`<br />
            Payer PSP (Google Pay) sends acknowledge, informs the customer and sends the response to NPCI.

        14. `payment_response`<br />
            Payee PSP sends the callback to our server. This will contain the final transaction status.

        15. `refund_request`<br />
            Request to initiate a refund.
      </Tab>
    </Tabs>
  </Card>
</CardGroup>

<Warning>
  **UPI Collect Flow Deprecated**

  According to NPCI guidelines, the UPI Collect flow is being deprecated effective 28 February 2026. Customers can no longer make payments or register UPI mandates by manually entering VPA/UPI id/mobile numbers.

  **Exemptions:** UPI Collect will continue to be supported for:

  * MCC 6012 & 6211 (IPO and secondary market transactions).
  * iOS mobile app and mobile web transactions.
  * UPI Mandates (execute/modify/revoke operations only)
  * eRupi vouchers.
  * PACB businesses (cross-border/international payments).

  **Action Required:**

  * If you are a new Razorpay user, use [UPI Intent](/docs/payments/payment-methods/upi/upi-intent).
  * If you are an existing Razorpay user not covered by exemptions, you must migrate to UPI Intent or UPI QR code to continue accepting UPI payments. For detailed migration steps, refer to the [migration documentation](/docs/announcements/upi-collect-migration/standard-integration).
</Warning>

## Netbanking

The payment flow for **Netbanking** payments is illustrated below:

<img src="https://razorpay.com/docs/build/browser/assets/images/payment-flow-netbanking.jpg" class="click-zoom" alt="Errors Payment Methods Netbanking" width="800" />

<Tabs>
  <Tab title="Source Parameter">
    The possible values for the `source` parameter for netbanking are listed below:

    * `customer`
    * `business`
    * `internal`
    * `issuer_bank`
  </Tab>

  <Tab title="Step Parameter">
    The possible values for the `step` parameter, along with the description, are listed below:

    1. `payment_initiation`<br />
       Your system initiates and sends the payment request to our server. Razorpay sends the bank URL back to you.

    2. `payment_authentication`<br />
       The customer logs into his netbanking account and completes the transaction.

    3. `payment_authorization`<br />
       Upon successful authentication, bank authorises the release of funds and notifies Razorpay. Razorpay in turn, notifies the business.
  </Tab>
</Tabs>

## Wallet

The payment flow for **Wallet** payments is illustrated below:

<img src="https://razorpay.com/docs/build/browser/assets/images/payment-flow-wallet.jpg" class="click-zoom" alt="Errors Payment Methods Wallets" width="800" />

The payment flow for **Wallet** payments is illustrated below:

<img src="https://razorpay.com/docs/build/browser/assets/images/payment-flow-wallet.jpg" class="click-zoom" alt="Errors Payment Methods Wallets" width="800" />

<Tabs>
  <Tab title="Source Parameter">
    The possible values for the `source` parameter for wallet are listed below:

    * `customer`
    * `business`
    * `internal`
    * `issuer`
  </Tab>

  <Tab title="Step Parameter">
    The possible values for the `step` parameter, along with the description, are listed below:

    1. `payment_initiation`<br />
       Your system initiates and sends the payment request to our server. Our server sends the same request to the Bank/Gateway.

    2. `payment_eligibility_check`<br />
       Razorpay sends the eligibility check request to the issuer to determine if the entered customer information is correct.

    3. `payment_authentication`<br />
       Customer authenticates the payment using OTP provided by the issuer.

    4. `payment_authorization`<br />
       Issuer authorises the release of funds and sends confirmation to Razorpay.
  </Tab>
</Tabs>

## Cardless EMI

The payment flow for **Cardless EMI** payments is illustrated below:

<img src="https://razorpay.com/docs/build/browser/assets/images/payment-flow-cardless_emi.jpg" class="click-zoom" alt="Errors Payment Methods Cardless EMI" width="800" />

<Tabs>
  <Tab title="Source Parameter">
    The possible values for the `source` parameter for Cardless EMI flow are:

    * `customer`
    * `business`
    * `internal`
    * `network`
    * `issuer`
  </Tab>

  <Tab title="Step Parameter">
    The possible values for the `step` parameter, along with the description, are listed below:

    1. `payment_initiation`<br />
       Your system initiates and sends the payment request to our server. Our server sends the same request to the Bank/Gateway.

    2. `payment_eligibility_check`<br />
       Razorpay sends the eligibility check request to the issuer to determine if the entered customer information is correct and to determine the credit eligibility of the customer.

    3. `payment_authentication`<br />
       Customer authenticates the payment using OTP provided by the issuer.

    4. `payment_authorization`<br />
       Issuer authorizes the release of funds and sends confirmation to Razorpay.
  </Tab>
</Tabs>

## Emandate

<Tabs>
  <Tab title="Source Parameter">
    The possible values for the `source` parameter for Emandate are listed below:

    * `customer`
    * `bank`
    * `business`
    * `internal`
    * `gateway`
    * `issuer_bank`
  </Tab>

  <Tab title="Step Parameter">
    The possible values for the `step` parameter, along with the description, are listed below:

    1. `payment_initiation`<br />
       Your system initiates and sends the payment request to our server. Our server validates your request, creates the payment flow and forwards the request to the Gateway.

    2. `payment_authentication`<br />
       The bank verifies the enrollment of the Emandate by asking customers to authenticate themselves.

    3. `payment_authorization`<br />
       Once the customer has completed the authentication, the bank authorizes the release of the funds. The authorization status is communicated to the Gateway which in turn communicates the same to Razorpay.
  </Tab>
</Tabs>
