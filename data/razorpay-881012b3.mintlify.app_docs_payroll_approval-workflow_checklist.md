> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Approval Checklist

> Refer to the workflow checklist before approving requests on RazorpayX Payroll.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Before you approve requests on the [Approvals Dashboard](/docs/payroll/approval-workflow/approvers), refer to the following checklist to understand what an approver must review in the request.

<br />

<AccordionGroup>
  <Accordion title="For Edit Payroll">
    Verify the following as an approver when you receive requests for [Edit Payroll](/docs/payroll/run-payroll#additions-and-deductions) actions:

    * Employee name and employee id
    * Payroll month
    * New Additions and the amount added
    * Previous Additions and the amount added
    * New Deductions amount calculated from [Loss of Pay](/docs/payroll/run-payroll#loss-of-pay)
    * Previous Deductions amount calculated from [Loss of Pay](/docs/payroll/run-payroll#loss-of-pay)
    * New Arrears amount
    * Previous Arrears amount <br />

    When you reject a request, the employee's salary remains unchanged. This is not applicable to <a href="/docs/payroll/run-payroll#skip-salary>" target="_blank">skipping</a> or [resuming](/docs/payroll/run-payroll#resume-skipped-salary) employees' salaries.
  </Accordion>

  <Accordion title="For Finalise Payroll">
    Verify the following as an approver when you receive requests for [Finalise Payroll](/docs/payroll/run-payroll#execute-payroll) actions:

    * Payroll month
    * Number of employees whose payroll is finalised
    * Number of employees whose payroll is skipped <br />

    You can check the details in the Salary Register linked on the Dashboard.
  </Accordion>

  <Accordion title="For Salary Revision">
    Verify the following as an approver when you receive requests for [Salary Revision](/docs/payroll/run-payroll#revise-salary):

    * Employee name and employee id
    * Effective date
    * Old CTC
    * New CTC
    * Arrears
    * Variable pay <br />

    If you use a [custom salary structure](/docs/payroll/run-payroll#custom-salary-structure), check the following:

    * Basic Salary
    * Dearness Allowance
    * HRA
    * LTA
    * Special Allowance
    * PF contribution
    * ESI contribution
    * Total Custom Allowances <br />

    After you approve any Salary Revision request, we email that employee's manager about the revision. You can also withdraw the request if the revision is no longer applicable.
  </Accordion>
</AccordionGroup>

### Related Information

* [Payroll Checklist](/docs/payroll/execute-payroll)
* [Approvals Dashboard](/docs/payroll/approval-workflow/approvers)
* [Salary Actions in Payroll](/docs/payroll/salary)
