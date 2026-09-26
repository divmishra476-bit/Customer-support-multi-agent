> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Tax Deductions Setup

> Check how to set up and operate declaration and proof upload windows for RazorpayX Payroll.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

[Income tax declarations and proof submission](https://razorpay.com/payroll/investment-proof-submission/) is a critical payroll activity. Employees declare the investments they have planned for the year and towards the end of the financial year, organisations collect proofs of the declarations and adjust the amounts on which the tax is calculated and deducted.

With Tax Deductions Setup on the Payroll Dashboard, you can set up:

<CardGroup cols={2}>
  <Card title="General Settings" href="/docs/payroll/tax-deductions-setup#general-settings">
    Setup verification settings for your organisation. Explore the [tax verification process](/docs/payroll/tax-verifications).
  </Card>

  <Card title="Declaration Window" href="/docs/payroll/tax-deductions-setup/windows">
    Set up declaration windows for your organisation.
  </Card>

  <Card title="Proof Upload Window" href="/docs/payroll/tax-deductions-setup/windows#set-up-proof-upload-window">
    Set up a proof upload window for employees in your organisation.
  </Card>

  <Card title="Custom Window" href="/docs/payroll/tax-deductions-setup/windows#advance-custom-settings">
    Set up a custom window for specific employees in your organisation.
  </Card>
</CardGroup>

<AccordionGroup>
  <Accordion title="Meaning of Windows">
    Declaration and Proof Upload windows refer to a duration where employees can perform declaration or proof upload activites on the Dashboard.

    It also creates a buffer period for your payroll team to finalise the monthly payroll and tax deductions.
  </Accordion>
</AccordionGroup>

## How it Works

To set up tax deductions for your organisation:

1. Enable tax deductions.
2. Define the tax verifications settings under General Settings.
3. Set up Declaration and Proof Upload windows.
4. Create custom windows as necessary.

## Enable & Set Up

To set up the IT Declaration windows:

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Navigate to **ADMIN OPTIONS** → **Settings**.
3. Go to the **Tax Deductions Setup** section. Click **Edit**. This opens the **General** settings page of **Tax Declaration & Proof Upload Settings**.
4. Toggle the setting against **Allow employees to update their tax deductions**. We usually enable this by default.
   <img src="https://razorpay.com/docs/build/browser/assets/images/x-xpayroll-tax-declaration-general.jpg" alt="RazorpayX Payroll enable Tax Declaration for employees" width="800" />

You have now enabled your employees to declare investment proofs. If you turn this setting off, you cannot modify the declaration and window settings.

## General Settings

After you [enable the declaration settings](#enable-set-up), you can further modify the following:

#### Verification Settings

You can modify the following verification settings on the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).

<AccordionGroup>
  <Accordion title="Opt for Verification">
    You can verify the investment proofs your employees submit in two ways. From the drop-down menu, you can select either:

    * **Let XPayroll Verify** to allow Payroll to verify your proofs.
    * **Let Organisation Verify** to carry out the [verification by yourself](/docs/payroll/tax-verifications).
  </Accordion>

  <Accordion title="Select Financial Year">
    You can select the financial year for which employees can declare and upload their investment proofs. This is useful to update employees' past/mid-year payroll information. You can select between:

    * **Let XPayroll choose**. By default, we recommend you allow Payroll to select the year (usually the current financial year) to calculate taxes.
    * The relevant financial years available in the drop-down menu.
  </Accordion>

  <Accordion title="Calculate Tax on Basis Of">
    Choose on which basis your organisation calculates employees' taxes. Select either:

    * **Declaration and verified proofs** to calculate tax based on the proofs employees submit.
    * **Amount declared by employee** to calculate as per their investment declarations only.

    <Warning>
      **Watch Out!**

      For dimissed employees, tax is calculated on the approved amount, not the declared amount.
    </Warning>
  </Accordion>
</AccordionGroup>

<img src="https://razorpay.com/docs/build/browser/assets/images/x-xpayroll-tax-declaration-verification-settings.jpg" alt="RazorpayX Payroll Tax Verification Settings" width="800" />

<Warning>
  **Watch Out!**

  * You cannot choose the [Calculate Tax On Basis Of](#calculate-tax-on-basis-of) if you chose **Let XPayroll Verify** when you [**Opt for Verification**](#opt-for-verification).
    * Payroll updates the Calculate Tax on Basis Of setting to **Amount declared by employee** after completing the verification process.
  * You can choose your organisation's [Proof Upload Window](/docs/payroll/tax-deductions-setup/windows#proof-upload-window) only if you choose **Let Organisation Verify** when you [**Opt for Verification**](#opt-for-verification).
</Warning>

#### Auto-Open Window & 80G Settings

You can choose to automatically enable the proof upload window for new joiners or dismissed employees on the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).

<AccordionGroup>
  <Accordion title="Auto-Open Window for New and Dismissed Employees">
    You can automatically open the investment declaration window for new joiners and auto-enable the proof upload window for dismissed employees awaiting their Last Working Day (LWD). To enable this:

    1. Select the toggle against **Auto open declaration window for new employees**.
    2. Enter the **Number of days** in the text box until the declaration window remains open.

    For dismissed employees, the investment proof upload window automatically opens when you dismiss the employee. It remains open until the employee's LWD.

    <Warning>
      **Watch Out!**

      Payroll does not verify the proofs for employees dismissed between April and December as it falls outside Payroll's proof verification period.

      This applies to both the options in the [**Opt for Verification**](#opt-for-verification) settings.
    </Warning>
  </Accordion>

  <Accordion title="Disable 80G">
    You can enable the setting to disable employees' 80G contributions. Select the toggle against **Disable 80G**.

    In such cases, the employee must individually declare their 80G contributions when they file their taxes in July.
  </Accordion>
</AccordionGroup>

<img src="https://razorpay.com/docs/build/browser/assets/images/x-xpayroll-tax-declaration-auto-open-settings.jpg" alt="RazorpayX Payroll Auto-open Windows Settings" width="800" />

## For Employees

Employees can declare their provisional investments and upload investment proofs via the [IT Declarations](/docs/payroll/employees/declarations) page. We communicate the window availability to your employees via email.

### Related Information

* [About Statutory Compliance](/docs/payroll/statutory-compliance)
