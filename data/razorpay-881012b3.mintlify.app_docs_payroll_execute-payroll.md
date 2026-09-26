> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute Payroll Checklist

> Use the RazorpayX Payroll execution checklist before executing your next payroll.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Once you complete [Payroll account setup](/docs/payroll/quickstart), you can execute payroll for your organisation. Payroll automates transactions and manages payroll as per settings enabled. Use the following checklist to execute payroll without any misses.

<Warning>
  **Watch Out!**

  Your employees and company depend on this one-click payroll processing mechanism. Use this checklist to ensure all prerequisite steps are completed before processing payroll.
</Warning>

## 1. Update Employee List

Before disbursing salaries, ensure that your employee list is up-to-date. Add, modify or dismiss employees according to their employment status and compensation changes. To do so:

1. Log in to your [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. In the left menu, navigate to **Admin Options** → **People**.
3. Select the relevant employee as per from **ALL** or other tabs.
4. Click **EDIT** against the applicable sections, as shown.
   <img src="https://razorpay.com/docs/build/browser/assets/images/xpayroll-modify-employee.gif" alt="Editing employee information in Payroll." width="800" />

Edit their personal and payment information, their leaves and their attendance before the payroll execution date.

## 2. Check Missing Information

Check if any employee's critical information, like their bank account number, UAN, PAN or so on is missing. To do so:

1. Log in to your [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Go to **Admin Options** → **Reports**
3. Click **Missing Information**. It provides a list of employees in the left column the information missing about them against their name.

<img src="https://razorpay.com/docs/build/browser/assets/images/xpayroll-reports-missing-info.jpg" alt="Employee missing info highlighted in employee's missing info modal in RazorpayX Payroll." width="800" />

## 3. Adjust Variables

Variables can either be an addition to the salary, a deduction based on a loss of pay, a recovery or a reimbursement.

<img src="https://razorpay.com/docs/build/browser/assets/images/xpayroll-edit-salary-additions-deductions.jpg" alt="Edit Salary window to enter amount and labels on Payroll." width="500" />

### Additions

To update your employees' **Additions**:

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Navigate to the payroll month, and click **EDIT** against the employee's name.
3. Add any bonus or incentives under **Additions**.
4. Click **Done** once updated.

### Deductions

To update your employees' **Deductions**:

* If your organisation uses the Payroll attendance module to track leaves, navigate to **Reports** → **Attendance** → **Payroll Adjustments** and approve any loss of pay recommendations that Payroll suggests.
  <img src="https://razorpay.com/docs/build/browser/assets/images/xpayroll-leave-suggestions.jpg" alt="Leave reccomendations tab on Payroll on the right hand side menu." width="600" />

* If you are tracking the loss of pay (LOP) days outside of Payroll or using the [Jibble integration](/docs/payroll/integrations/jibble), follow the given steps:

<Tabs>
  <Tab title="Using Jibble Integration">
    Know how to [sync loss of pay data from Jibble](/docs/payroll/integrations/jibble#verify-lop-in-payroll).
  </Tab>

  <Tab title="Manual Deductions">
    1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Navigate to **Pay Employees** → **Run Payroll**. Select the employee here.
    3. Click **EDIT** and update this data under **Deductions**.
    4. Click **Done**.
  </Tab>
</Tabs>

Check how you can modify other salary components as part of [Run Payroll](/docs/payroll/run-payroll).

## 4. Verify Salaries

Before processing payroll, check under **Reports** → **Salary Register** on your [Payroll Dashboard](https://payroll.razorpay.com/dashboard) whether your employees are paid as per the applicable cost-to-company (CTC). Cross-verify their salaries and update the information accurately.

<Warning>
  **Watch Out!**

  You **cannot** modify payroll after it is executed.
</Warning>

## 5. Check Due Dates

For Payroll to make timely compliance payments, you must execute Payroll on or before 5th or 10th of the month, depending on the compliances applicable to your organisation.

| Compliance                     | Payroll Due Date  | Government Due Date |
| ------------------------------ | ----------------- | ------------------- |
| TDS (Salaried/Employees)       | 5th of the month  | 7th of the month    |
| TDS (Non-salaried/Contractors) | 5th of the month  | 7th of the month    |
| PF                             | 10th of the month | 15th of the month   |
| ESIC                           | 10th of the month | 15th of the month   |

## 6. Finalise and Execute

Finalise the payroll for the month. [Transfer the funds](/docs/payroll/payroll-payouts) required to process payroll and then **Request Execution** with ease. You **cannot** [make changes](/docs/payroll/exceptional-cases) to payroll after you have executed it.

Authorise the payroll execution using the OTP received at your registered email address/authenticator app.

### Related Information

* [Run Payroll](/docs/payroll/run-payroll)
* [Salary](/docs/payroll/salary)
* [Statutory Compliance](/docs/payroll/statutory-compliance)
