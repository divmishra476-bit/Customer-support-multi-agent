> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Resgination Setup

> Set up and handle resignations on the Payroll Dashboard.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

On the Payroll Dashboard, you can dismiss employees at the end of their tenure at your organisation, or allow them to resign. After receiving a resignation request, you can process the [Full and final settlement](#process-fnf) and successfully dismiss the employee.

<Info>
  **Handy Tips**

  Both the administrator and the employee's manager can approve resignations.
</Info>

## Enable Resignation

To allow employees to resign, you must enable it.

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Go to **Settings** → **Employee Resignation Setup** → **EDIT**.
   <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-enable-resignation.jpg" alt="Scroll to Enable Resignation set up. Click EDIT on RazorpayX Payroll" width="800" />
3. Select the **Enable resignations feature** check box.

This enables resignation submission for employees.

## Pending Requests

After an employee submits their resignation, you can view the request and take action on it.

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Click either of the following. The Resignation reports page opens.

<Tabs>
  <Tab title="Resignation Report">
    1) Navigate to ADMIN OPTIONS → Reports.
    2) Click **Resignations**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-resignation-report.jpg" alt="Resignation report in Settings on the Razorpay Payroll Dashboard" width="800" />
  </Tab>

  <Tab title="Dashboard Reminders">
    In the reminders tab, click **resignations**.

    <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-resignations-reminders.jpg" alt="Resignation reminders on the RazorpayX Payroll Dashboard" width="800" />
  </Tab>
</Tabs>

1. View the resignation requests pending your review. Select the employee and click **REVIEW RESIGNATION**. You can only review one request at a time.
2. In the Update Resignation Request pop-up modal, you can:
   * Change the employee's **Last Working Day**.
   * Provide **Remarks** on the resignation request.
3. Click **UPDATE** to make changes to the employee's resignation. Then, click **APPROVE**.
   <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-resignation-modal-approve-reject.jpg" alt="Approve or Reject resignations on Payroll Dashboard" width="800" />

This successfully approves the employee's resignation.

* To reject the request, click **REJECT**.
* Click View Resignation History on the right pane to view older requests.
  * You can filter the older requests using the **Resignation Status** and duration.
  * Click DOWNLOAD CSV to download the resignation data.

<Warning>
  **Watch Out!**

  You cannot undo an approved resignation request.
</Warning>

## Process Full & Final Settlement

Once you approve the resignation request, you can process the employee's full and final settlement.

1. On the Resignations report page, select the employee to process the FnF for. Click **PROCESS FNF SETTLEMENT**. This opens the **Full and final settlement** page.
2. On the Full and final settlement page:
   1. Provide the leave encashment details. You can either enter the number of leaves to encash or the total leave encashment amount.
   2. Enter any additions or deductions to the employee's salary. You can also enter the [Loss of Pay](/docs/payroll/run-payroll#loss-of-pay) days, or the [Jibble Integration](/docs/payroll/integrations/jibble)  to sync the LOP data automatically.

      <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-fnf-additions-deductions.jpg" alt="Payroll Dashboard make additions deductions FNF" width="800" />

<Warning>
  **Watch Out!**

  Ensure you do not include loan recovery, bonus clawback, gratuity payments and other salary components or deductions here.
</Warning>

1. Select whether the deductions happen from the employee's gross or net pay.

<AccordionGroup>
  <Accordion title="What is the difference between Gross Pay and Net Pay?">
    <Tabs>
      <Tab title="Gross Pay">
        Gross pay is the total amount an employee earns before any relevant deductions, including taxes, benefits, bonuses, reimbursements and more. This also includes the basic, ad hoc and the allowance components of an employee's salary.

        Examples of gross pay deductions include loss of pay, bonus recovery after clawback and more, depending on the employee's performance. Gross pay deductions are mandatory and affect compliance payments (TDS, PF).
      </Tab>

      <Tab title="Net Pay">
        Net pay is the employee's take-home salary after all applicable deductions such as benefits, taxes and compliances. Net pay = Gross pay - TDS - PF - PT - ad hoc deductions.

        Examples of net pay deductions include laptop repair recovery charges, penalties, insurance payments and more.
      </Tab>
    </Tabs>
  </Accordion>
</AccordionGroup>

1. Enter the employee's personal email address for further communication.

   If Payroll had been handling the employee's [Form 16s](/docs/payroll/salary#employee-s-form-16), the employee receives it on their personal email address at the end of the financial year.
2. Click **Add to Payment**.

You have successfully modified the full and final settlement for the employee. The employee receives the settlement payment after you [execute payroll](/docs/payroll/run-payroll#execute-payroll) for the month.

### Maintain Employee Directory

After dismissing employees, you can choose to:

* **DELETE EMPLOYEE** from the employee directory.
* **DISABLE LOGIN** for the employee during the notice period, if necessary.

The above options are available on the employee's **User Profile**.

## Reports

You can access the following reports:

| Report Name               | Description                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Resignation               | View the resignation requests initiated and approved so far.                                                                 |
| Full and final settlement | View the details of full and final settlements processed month-wise. You can refresh the data and download it in a CSV file. |

### Related Information

* [Dismiss Employees on the Payroll Dashboard](/docs/payroll/run-payroll#terminate-and-run-last-payroll)
* [About Full and Final Settlement](https://razorpay.com/payroll/learn/full-and-final-settlement-fnf/)
