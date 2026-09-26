> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate with Zaggle

> Integrate RazorpayX Payroll with Zaggle to simplify flexible benefits management for employees.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Integrate with Zaggle to simplify the flexible benefits declaration and reimbursement process for your employees.

With the Zaggle integration, employees can declare flexible benefits on their Zaggle card. You can then approve the declared amounts and transfer funds to their card, that employees can then use the card to make purchases.

<AccordionGroup>
  <Accordion title="Advantages">
    * **Central Data Tracking**: <br />
      Your Payroll account maintains all employees' flexible benefits data. On the Payroll Dashboard, you can configure flexible benefits at an organisational level and allocate funds accordingly.

    * **Smooth Declaration and Reimbursement Process**: <br />
      Employees can use their Zaggle cards to declare flexible benefits. After declaring, you can transfer the approved amount and funds to their Zaggle card. This streamlines the flexible benefits process.

    * **Simplified Reconcilaition**: <br />
      Since employees use their Zaggle card to make payments from their declared benefits, collecting proofs for the declarations becomes easy.

    * **Automatic Data Sync**: <br />
      Your organisation's employee data is automatically transferred to Zaggle during setup. This eliminates the manual effort and errors in exporting data to Zaggle.
  </Accordion>
</AccordionGroup>

## How it Works

1. [Integrate Zaggle with Payroll](#integration-steps).
2. Set up flexible benefits plan (FBP) and allocate monthly amounts on the Payroll Dashboard.
3. Complete the KYC and arrange card delivery for employees.

## Integration Steps

To integrate with Zaggle:

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Navigate to **Integrations** in the left menu under **ADMIN OPTIONS**.
3. Look for **Zaggle** and click **Explore**.
4. On the Zaggle integration page, click **CONTINUE SETUP** at the bottom. This opens the setup page.
5. On the setup page:
   1. In the **WALLETS** tab, select the check boxes to make flexible benefits available to your employees. Click **SAVE AND NEXT**.
      <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-integrations-zaggle-setup.jpg" alt="Set up Zaggle FBP plan on Payroll Dashboard" width="800" />
   2. In the **COMPONENT** tab, enter the maximum monthly amount allowed for flexible benefits at an employee level in the **Monthly amount** text box.

      If you enter 5000 in the text box, ₹5000 is the total flexible benefits amount allocated for every employee in your organisation.

<AccordionGroup>
  <Accordion title="What does this mean?">
    * When you add a specific amount in the text box, Payroll creates flexible benefits component in your employees' salary structure.
    * The amount added here is the sum total of all the flexible benefits and allocation.
  </Accordion>
</AccordionGroup>

Click **SAVE AND NEXT**.

<img src="https://razorpay.com/docs/build/browser/assets/images/payroll-integrations-zaggle-component.jpg" alt="Add monthly amount on Payroll Dashboard" width="800" />

1. In the **ADDRESS** tab, select whether Zaggle should deliver the cards to your organisation's address or individually to your employees' addresses.

<Warning>
  **Watch Out!**

  You cannot change the delivery address details after integrating.
</Warning>

1. On the **CONFIRM** tab, review the integration details and click **CONFIRM**.

This successfully completes the integration.

## Manage Integration

To manage your integration with Zaggle on the Payroll Dashboard:

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Navigate to **Integrations** in the left menu under **ADMIN OPTIONS**.
3. Click **Manage** in the Zaggle card.

   <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-integrations-zaggle-manage.jpg" alt="Click Manage in Payroll Integrations Dashboard Zaggle" width="800" />

The following actions are available:

<AccordionGroup>
  <Accordion title="Update KYC">
    You must complete the Zaggle KYC process to deliver your employees' cards.

    1. Navigate to the [Zaggle integration page](#manage-integration) and click **START VERIFICATION**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-integrations-zaggle-manage1.jpg" alt="Zaggle Payroll Integration KYC and modify FBP" width="800" />
    2. On the KYC Verification page, provide your **GSTIN Number**, **GSTIN Certificate** and a **Cancelled Cheque**.
    3. Click **Request Verification**.

    This successfully initiates the verification process.
  </Accordion>

  <Accordion title="Modify Flexible Benefit Plan">
    To modify the flexible benefits plan:

    1. Navigate to the [Zaggle integration page](#manage-integration).
    2. **Click here** opens the FBP modification page.
    3. On the **WALLETS** page, you can re-configure the flexible benefits plan and the monthly amount in the **COMPONENT** tab.
    4. Click **SAVE AND NEXT**.
  </Accordion>
</AccordionGroup>

### Related Information

* [About Payroll Integrations](/docs/payroll/integrations)
* [Integrate with Jibble for Attendance](/docs/payroll/integrations/jibble)
