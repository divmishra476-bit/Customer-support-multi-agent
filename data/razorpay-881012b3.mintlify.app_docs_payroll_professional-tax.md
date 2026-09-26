> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Professional Tax (PT)

> Set up, pay and check Professional Tax (PT) payments on RazorpayX Payroll.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Professional Tax (PT) is a state-level, mandatory tax levied u/s 16 of the Income Tax Act, 1961. It varies between states and applies to all earning individuals regardless of their profession, trade or employment in India.

Payroll seamlessly handles professional tax deductions for your employees based on the state in which you are registered. Know how you can set up and check payment records in Payroll.

<Warning>
  **Watch Out!**

  Automated Professional Tax (PT) payments for employees in Karnataka are temporarily unavailable on Payroll. Know more about the [PT rule change](/docs/payroll/faqs#professional-tax).

  You must make Professional Tax payments [via the e-Prerana portal](#pt-payments-via-pt-portal) for Karnataka employees after processing the monthly payroll.
</Warning>

## Set Up PT

Payroll only handles Professional Tax (PT) payments and filings, not the initial registration. Know more about the people and resources available for [initial registration](/docs/payroll/statutory-compliance#initial-registration).

<AccordionGroup>
  <Accordion title="Set up Professional Tax (PT) Payments and Filings">
    To set up PT payments for your organisation:

    1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Navigate to **ADMIN OPTIONS** → **Company Details**. Here:
       1. Go to **Provident Fund / ESIC / Professional Tax / LWF** → **Edit**.
       2. Select **Enabled** from the **PT Status** drop-down menu and click **Continue**.
              <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-setup.jpg" alt="PT Setup on Payroll Dashboard" width="800" />
       3. On the **Company Details** page, go to **External Credentials** → **Edit**.
       4. Go to the **PT** section and update the credentials to the PT portal of your registered state.
    3. Go to **Settings** → **Payments & Compliance Setup** and enable PT Payments and Filings.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-setup-filings.jpg" alt="Payroll professional tax filings setup" width="800" />
  </Accordion>
</AccordionGroup>

You have successfully set up PT for your organisation.

* Know more about [enabling compliances](/docs/payroll/quickstart#enable-compliances).
* If PT is disabled under **Company Details** → **Provident Fund** / **ESIC** / **Professional Tax**, it is not deducted for any employee.

## Manage PT

On the Payroll Dashboard, you can check and modify the PT settings for your organisation and review PT payments.

<AccordionGroup>
  <Accordion title="Home State PT Deduction">
    By default, when you add a new employee, they get added to the same state as your organisation. If PT applies to your state, it is also automatically enabled for the employee.

    PT is not deducted automatically for employees who are not in the home state.

    * If you are registered for PT in that employee's state, enable PT for that employee.
      1. Log in to your [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
      2. Go to the particular employee's profile.
      3. Edit the **Provident Fund, Professional Tax & ESI** section and enable PT.
    * If you are not registered for PT in that employee's state, you can:
      * Change the employee's location to your home state in Payroll. In this case, PT is deducted as per your state's policy.
      * Keep the employee's current location/state as is. PT will not be deducted for them.
  </Accordion>

  <Accordion title="PT Deduction">
    To check whether PT is being deducted for your employees:

    1. Log in to your [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Go to **Reports** → **Salary Register**.
    3. Look for PT as a **column** and ensure deductions are showing up for all employees.

    When you finalise the payroll for that employee, click on the Payroll Amount and ensure PT is visible as a **row**.
  </Accordion>

  <Accordion title="PT Payment">
    Professional Tax payment and filing is done between the 15th and 31st of the following month, depending on the state. Until then, it remains in the `pending` state. To check the PT payment status:

    1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Navigate to **Admin Options**.
    3. Go to **Reports** → **Ledger**. A filter view screen appears.
    4. Select filter **Type** and choose **Professional Tax**.

    After payment, you can find the challans under **Reports** → **Provident Fund, Professional Tax & ESI**.
  </Accordion>
</AccordionGroup>

## PT Payment for Karnataka Employees

The Karnataka government has introduced 2-Factor Authentication (2FA) when logging into the PT portal, effective September 2024. Due to this, Payroll is unable to automate PT payments.

You must manually make PT payments for your employees. Ensure you make the PT payments before October 20, 2024.

#### PT Payments via PT Portal

Watch the video below or read along.

<iframe width="950" height="534" src="https://www.youtube.com/embed/BfQYOC3kxS4" title="Make Professional Tax (PT) Payments for Karnataka Employees | RazorpayX Payroll" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />

There are three steps to make PT payments:

<AccordionGroup>
  <Accordion title="List Employees with Pending PT Payments">
    Your organisation may have employees from multiple locations. Use the filter option to list the employees located in Karnataka. This is a prerequisite step.

    To check the list of employees as well as the amount payable:

    1. Log in [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Navigate to **ADMIN OPTIONS** → **Reports** in the left menu.
    3. Click **Salary Register**.
    4. Use the **PT Location** filter to list the employees whose PT payments you must make.
    5. Scroll horizontally against the employees' names to view the PT amounts.

           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-professional-tax-update.jpg" alt="Payroll Dashboard PT payments" width="800" />

       The amount mentioned in the **PT** column is the PT amount payable to the government.
    6. Click **Download CSV**.

    This downloads the salary report for the month. Filter the **PT Location** as Karnataka in the file and calculate the total amount payable for the number of employees whose PT payments are pending.
  </Accordion>

  <Accordion title="File e-Return">
    To file the e-Return:

    1. Log in to the Karnataka PT e-Prerana portal.
    2. Enter the OTP and authenticate your access to the portal.
    3. Click **File Return**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-update-prerana-portal.jpg" alt="e-Prerana portal RazorpayX Payroll File Return" width="800" />
    4. Select the **Return Entry** details from the respective drop-down menus. This includes:
       * **Return Period Type:** Annual/Monthly.
       * **Month:**
       * **Year:**
       * **Return Type:** Original/Revised

             <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-update-file-return-details.jpg" alt="Payroll PT Return details enter" width="800" />
    5. Click **NEXT**.
    6. In the new table displayed on-screen, enter the number of employees with pending PT payments in the **No. of Employees** column. For example, `10`.

       The portal automatically calculates the total tax payable.
    7. Click **Save Return**.

    You have successfully filed the e-return, after which you receive the confirmation message on the same page.

    Click **Home** at the top-left corner to return to PT home page.
  </Accordion>

  <Accordion title="Make E-Payment">
    After filing the PT e-Return, you must make the E-Payment.

    1. On the PT e-Prerana home page, click **Make E-Payment**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-update-prerana-portal.jpg" alt="e-Prerana portal RazorpayX Payroll File Return" width="800" />
    2. On the **Make E-Payment** page, you can view the returns filed in step 2. Click **Pay**.
    3. Review the **PT-Demand Details** as populated from the returns you filed. Click **Make e-Payment**.
    4. This redirects you to the Khajane II portal. Here:
       * Select the **Mode of Payment** from the drop-down menu. We recommend you select netbanking as the payment mode.
       * Select the **Type of E-Payment** as **SBI Aggregator**.
    5. Enter the captcha and click **Submit**.

    This successfully makes the PT payment for the month. You are automatically redirected to the PT portal.

    Click **Home** at the top-left corner to return to PT home page.
  </Accordion>

  <Accordion title="Submit Returns">
    After successfully making the E-Payments, you must submit the returns for which you made the PT payment. This is a mandatory reconciliation practice.

    1. Click **Home** to go to the e-Prerana portal home page. Here, click **Submit Return**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-update-prerana-portal.jpg" alt="e-Prerana portal RazorpayX Payroll File Return" width="800" />
    2. Review the return details and click **Submit**. This opens the **Verify and Submit Return** page.
    3. Click **Add CTD reference number** to link the auto-generated CTD number with your submit return request.

       You can now view the tax payable details and the CTD reference number.
    4. Click **Verify & Submit**.

    You have successfully submitted the returns. Click **Home** at the top-left corner to return to PT home page.
  </Accordion>
</AccordionGroup>

You have successfully made the PT payments. You can view the details on the home page directly for the current FY.

Click **Verify/Print** on the e-Prerana portal home page to download the Returns receipt.

<img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-update-verify-print.jpg" alt="e-Prerana portal RazorpayX Payroll download Return" width="800" />

### Troubleshooting Steps

When you submit Returns in step 4, you may not find the necessary details on the page. There are two ways to resolve this:

<AccordionGroup>
  <Accordion title="Re-verify Payments">
    1. Navigate to e-Prerana portal home page and click **Verify failed payments**.
    2. Copy the CTD Reference number.
    3. Click **Verify** against the respective payments.

    <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-upadte-verify-failed-payments.jpg" alt="Click verify against respective payments PT portal" width="800" />

    This can verify your payments post which, you can submit the returns.
  </Accordion>

  <Accordion title="Verify Challan Payment Status">
    If the above process fails, follow the below steps to verify failed payments.

    1. Go to the [E-Khajane II Portal](https://k2.karnataka.gov.in/K2/index_en.html).
    2. Click **Verify Challan Payment Status**.

           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-pt-update-khajane-.jpg" alt="Click Verify Challan Payment Status on Khajane portal Payroll Dashboard" width="800" />
    3. Enter the CTD number you previously copied and the captcha on-screen.
    4. Ensure the transaction status is successful.

    This successfully verifies the failed payments. You can now [Submit Returns](#4-submit-returns).
  </Accordion>
</AccordionGroup>

### Related Information

* [TDS](/docs/payroll/tds)
* [Statutory Compliance](/docs/payroll/statutory-compliance)
* [Provident Fund](/docs/payroll/provident-fund)
* [Enable Compliance during Account Setup](/docs/payroll/administrator#welcome-mail-from-xpayroll)
