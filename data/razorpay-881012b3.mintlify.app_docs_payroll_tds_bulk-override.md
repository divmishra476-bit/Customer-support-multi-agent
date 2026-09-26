> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# RazorpayX Payroll Bulk TDS Override

> Learn how to override the TDS amount for unfinalised payroll for multiple employees for a specific payroll month using RazorpayX Payroll's bulk TDS override feature.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

The Bulk TDS Override feature in RazorpayX Payroll enables you to override the TDS (Tax Deducted at Source) amount for multiple employees for a specific payroll month at once. Instead of overriding the TDS for each employee individually, you upload a single template and apply the overrides for your entire workforce in one operation, saving time and ensuring consistency. Bulk TDS Override is allowed only for unfinalised payroll. It is not allowed for finalised or executed payroll.

<Info>
  **Handy Tips**

  Bulk TDS Override is available for organisations on Payroll Engine 2.0 and needs to be enabled for your organisation. [Contact Payroll Support](mailto:xpayroll@razorpay.com) for assistance.
</Info>

## Use Cases

Bulk TDS override is beneficial when you want to set a specific TDS amount for a group of employees for a payroll month, such as:

* Adjusting the TDS to account for tax computed outside the system or for prior employment income.
* Correcting the TDS for a group of employees for a particular payroll month.

<Warning>
  **Watch Out!**

  * The override applies only to the payroll month you select and only one override per employee per payroll month is allowed.
  * Enter the TDS amount in rupees using whole numbers only.
</Warning>

## Step-by-Step Bulk TDS Override Process

<AccordionGroup>
  <Accordion title="Step 1: Access the Bulk TDS Override Feature">
    1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Navigate to the **Bulk Actions** section from the left navigation menu.
    3. Under **Select bulk action**, select **TDS Override** from the drop-down menu.
    4. Click **Next**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/bulk-tds-override-action.jpg" alt="Select TDS Override from the bulk action drop-down" width="800" />
  </Accordion>

  <Accordion title="Step 2: Download the Template">
    In the **Bulk TDS Override** modal, on the **Upload Template** step:

    1. Under **Select payroll month**, choose the payroll month for which you want to override the TDS.
    2. Click the **Download Template** button to download the template.
    3. Save the template to your local system.

           <img src="https://razorpay.com/docs/build/browser/assets/images/bulk-tds-override-template.jpg" alt="Download the bulk TDS override template for the selected payroll month" width="800" />

           <Info>
             **Handy Tips**

             The TDS override applies to the payroll month you select here.
           </Info>
  </Accordion>

  <Accordion title="Step 3: Fill the Template">
    Open the downloaded template in Microsoft Excel or a compatible spreadsheet application and fill in the employee email and TDS amount in rupees as per the instructions:

    1. Enter the TDS amount in rupees using whole numbers only.
    2. Only one override per employee per payroll month is allowed.
    3. Do not add or remove any columns.
    4. You can upload a maximum of 500 employees per upload.
    5. Mandatory fields are marked with a \* sign.
    6. Save the file in .xlsx format.
  </Accordion>

  <Accordion title="Step 4: Upload the Template">
    1. Return to the **Bulk TDS Override** modal.
    2. Under **Upload the updated sheet below**, click **Browse files to upload** and select your updated file.
    3. Only the .xlsx file format is allowed, with a maximum size of 5MB.
    4. Click **Upload & Preview** to proceed to the preview step.
  </Accordion>

  <Accordion title="Step 5: Preview and Confirm">
    1. On the **Preview Details** step, the system displays a preview of all the TDS overrides to be applied.
    2. Review the employee emails and TDS amounts for any errors or discrepancies.
    3. After carefully reviewing all entries, confirm to apply the overrides.
    4. Upon successful processing, a confirmation message appears.

           <Info>
             **Handy Tips**

             The preview stage is crucial for catching potential errors. Review all records carefully, especially when overriding TDS for a large number of employees.
           </Info>
  </Accordion>
</AccordionGroup>

After completing the bulk TDS override, you can finalise the payroll.

1. The overridden TDS amounts are applied to the payroll month you selected.
2. The overrides reflect in the selected month's payroll for each employee.

### Related Information

* [Tax Deducted at Source (TDS)](/docs/payroll/tds)
* [Bulk One-Time Payment](/docs/payroll/bulk-one-time-payment)
* [Run Payroll](/docs/payroll/run-payroll)
* [Statutory Compliance](/docs/payroll/statutory-compliance)
