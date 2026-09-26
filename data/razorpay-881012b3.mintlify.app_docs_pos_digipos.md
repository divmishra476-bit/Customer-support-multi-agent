> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# DigiPOS

> Razorpay DigiPOS for iOS enables Apple Premium Resellers to securely accept in-store payments on iPhones and iPads, streamlining the purchase process for Apple products.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Razorpay DigiPOS is a comprehensive payment solution designed for Apple Premium Resellers (APRs). It allows them to seamlessly accept in-store payments through iPhones and iPads.

With DigiPOS, businesses can offer a secure, efficient, and fully digital checkout experience, enhancing customer satisfaction while simplifying payment management. Ideal for resellers, DigiPOS integrates seamlessly with Apple devices, providing a modern and reliable way to process transactions. This will eliminate the dependency on Android POS devices and payment apps. Using DigiPOS one can complete the purchase on apple devices.

## Frequently Asked Questions (FAQs)

Here are some frequently asked questions for DigiPOS.

### DigiPOS App

<AccordionGroup>
  <Accordion title="How do I download Razorpay DigiPOS?">
    Razorpay DigiPOS is available for download on the [Apple App Store](https://apps.apple.com/in/app/razorpay-digipos/id6520383285?platform=iphone).
  </Accordion>

  <Accordion title="Is there a fee for using the app?">
    No. The app is free to use.
  </Accordion>

  <Accordion title="Do I need user credentials to access DigiPOS?">
    Yes, to access DigiPOS on each device, users must log in with their authorised usernames and passwords.
  </Accordion>

  <Accordion title="Where can I find my user credentials?">
    Your login credentials will be sent to you through email. You can also reach out to your dedicated Razorpay POC who can help you.
  </Accordion>

  <Accordion title="Who should have the username and password credentials?">
    Your login credentials should only be shared with trusted in-store employees who conduct transactions. APR stores are responsible for sharing login credentials.
  </Accordion>

  <Accordion title="How do I change my store's user credentials?">
    Contact your dedicated Razorpay POC to have your new credentials configured in the backend and ready for use. Alternatively, you can email us at `digipos-support@razorpay.com` for assistance.
  </Accordion>

  <Accordion title="Can I install DigiPOS on all Apple devices?">
    DigiPOS v1 supports iPadOS and iOS, allowing installation on iPhones and iPads. As it is not compatible with MacOS, it cannot be installed on MacBooks.
  </Accordion>

  <Accordion title="What payment modes are supported on DigiPOS v1?">
    DigiPOS v1 supports full-swipe card payments, UPI, Bank EMI, Apple brand EMI, and SMS Payment Links.
  </Accordion>

  <Accordion title="Is Exchange flow supported on DigiPOS?">
    Yes, exchange flow is supported on DigiPOS.
  </Accordion>

  <Accordion title="What are the steps to do an Exchange transaction on DigiPOS?">
    1. Follow the standard steps for Brand EMI or Full Swipe Offers flows using cards or payment links.
    2. Select the Exchange Device checkbox on the Device Selection and IMEI Input screen if it is an exchange transaction.
    3. Enter the old device's IMEI or Serial Number.
    4. Proceed to complete the transaction.
  </Accordion>

  <Accordion title="What transaction amount should I enter for an exchange transaction?">
    Enter the original amount minus the value of the old device being exchanged.
  </Accordion>

  <Accordion title="I cannot find the Exchange flow on the DigiPOS app.">
    Please ensure you have updated the app to the latest version. Please visit Razorpay DigiPOS on the App Store to [update the app](https://apps.apple.com/in/app/razorpay-digipos/id6520383285).
  </Accordion>
</AccordionGroup>

### DigiPOS Device

<AccordionGroup>
  <Accordion title="Do I need another device apart from iPhone or iPad to accept payments?">
    Yes, for card payments, a PAX DigiPOS device must be connected via Bluetooth to your iPhone or iPad. UPI and other non-card transactions can be processed directly on your device using DigiPOS without the DigiPOS device.
  </Accordion>

  <Accordion title="What is the DigiPOS device used for?">
    DigiPOS is a light, compact device used for card reading and PIN input. It securely processes card transactions.
  </Accordion>

  <Accordion title="Can I connect multiple iPhones or iPads to a single DigiPOS device?">
    No. Currently, you can connect only one iPhone or iPad to a single DigiPOS device at a time. To connect a different device, you should first disconnect from the existing device.
  </Accordion>

  <Accordion title="I am facing issues with the DigiPOS device. How do I fix them?">
    We apologise for the inconvenience. Contact your Razorpay Key Account Manager for a DigiPOS device replacement within 2 days, or email  [digipos-support@razorpay.com](mailto:digipos-support@razorpay.com)  with your concerns and our team will respond within a business day. Meanwhile, please ensure you fully charge the DigiPOS device.
  </Accordion>

  <Accordion title="Can I void a transaction from my iPad?">
    Yes, void capability is available for card transactions in full-swipe, EMI, and payment link modes. Only authorised users with void access can perform void transactions to ensure security.
  </Accordion>

  <Accordion title="How can I share the charge slip of the payment with customers?">
    With DigiPOS, digital charge slips can be easily shared with customers by:

    * Scanning the QR code on the payment success screen.
    * Sending an SMS with the charge slip link by entering the customer’s phone number.
    * Sending an email containing the charge slip by entering the customer’s email address.
  </Accordion>

  <Accordion title="Can I print a charge slip?">
    As the DigiPOS device is a compact, printerless device, DigiPOS v1 does not offer direct print capability. However, businesses can retrieve the digital chargeslip from the transaction success screen, transaction history, or Dashboard, and print it by connecting a printer to the Dashboard.
  </Accordion>

  <Accordion title="How will I know whether my DigiPOS device is connected to my iPad?">
    A device icon on the amount entry screen indicates whether the DigiPOS device is connected to the iPad. A green dot shows an active connection, while a red dot indicates no connection. Users can also check the device connection status on the accounts page.
  </Accordion>

  <Accordion title="Can I initiate a card transaction without being connected to a DigiPOS device?">
    On the amount entry page, users can select card payments after entering the amount. If no DigiPOS device connection is detected, they will be redirected to establish one. Card transactions cannot proceed without a connection. For card-not-present scenarios, an SMS payment link can be sent without needing a DigiPOS device connection.
  </Accordion>

  <Accordion title="How can I get Apple Brand EMI enabled on DigiPOS device?">
    Apple assigns a Dealer Code to verified businesses, including Apple Premium Resellers. Share your Apple-issued Dealer Code with your Razorpay Key Account Manager for backend activation. If you are an existing POS business, Razorpay will match your GST with Apple's business database to enable Apple Brand EMI.
  </Accordion>
</AccordionGroup>

### Account and Business Queries for APR HQ

<AccordionGroup>
  <Accordion title="How will I receive Settlements?">
    As you are onboarded on the Direct model, all settlements will be handled by your acquiring bank. However, Razorpay POS will process Offer and Debit Card EMI settlements on a T+1 basis.
  </Accordion>

  <Accordion title="What transaction details are included in the Offer Settlement Report?">
    A single comprehensive report will be provided for both Card and Payment Link transactions, including details on:

    * Instant Cashback for Offers
    * Instant EMI Subvention for Brand EMI
    * Debit Card EMI transactions
  </Accordion>

  <Accordion title="When will I receive the funds and the report?">
    Funds will be transferred on T+1 (T being the transaction day) at 6 pm, and the report will be sent to the APR HQ’s registered email address by 8 pm.
  </Accordion>

  <Accordion title="Will UTR be shared in the Offer Settlement Report?">
    Yes, the UTR will be included in the Offer Settlement Report as proof of settlement for easy reconciliation.
  </Accordion>

  <Accordion title="How can I view the transaction details for all my stores in one place?">
    As a Razorpay POS business, you can access the Razorpay POS Dashboard to view the transaction history of all your stores in one place.
  </Accordion>

  <Accordion title="How can I create a username and password for the Dashboard?">
    To create your username and password, provide the details to your dedicated Razorpay Key Account Manager, who will configure them for you in the backend.
  </Accordion>

  <Accordion title="I have forgotten my username and password for the Dashboard. How can I recover them?">
    You can contact your dedicated Razorpay Key Account Manager, and they will configure a new set of credentials for you in the backend.
  </Accordion>

  <Accordion title="Is it possible to integrate DigiPOS with my billing software?">
    DigiPOS v1 does not support billing integrations. Sales representatives should use DigiPOS as a standalone POS system, manually entering the payment amount on the iPad/iPhone screen.
  </Accordion>
</AccordionGroup>
