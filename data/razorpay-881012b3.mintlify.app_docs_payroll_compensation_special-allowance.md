> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Special Allowance

> Understand why Special Allowance shows a negative value in RazorpayX Payroll, why it skips finalisation and how to fix the salary structure.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

In Payroll, **Special Allowance is a balancing component**, not a value you set directly. It is the amount left in the CTC after every other component and employer contribution is allocated:

<Info>
  **How Special Allowance is calculated**

  Special Allowance = Annual CTC - (Basic + HRA + other fixed allowances + Employer PF + Employer ESI)
</Info>

When the other components use up the entire CTC, nothing is left and Special Allowance turns negative. This makes the salary structure invalid. Payroll skips the affected employees during finalisation. You usually see this as: *"All employees are showing as skipped and I cannot finalise payroll."*

## Why is Special Allowance showing negative?

This usually happens in one of two situations:

| Cause                                                                  | What happens                                                                                                                       |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Fixed components total 100% of CTC (for example, Basic 50% + HRA 50%). | No room is left for Special Allowance, so employer contributions push it negative.                                                 |
| Employer PF/ESI is high.                                               | Employer PF and ESI are carved out of the CTC before Special Allowance is calculated, so a larger contribution leaves less for it. |

<Info>
  **Employer PF/ESI and the CTC**

  Employer PF and ESI are met from within the CTC in both Payroll's older system and Payroll 2.0. They are employer contributions, not employee earnings, so they do not appear in the Earnings section of the payslip and you do not need to add them as earning components.
</Info>

## Payroll's older system vs Payroll 2.0

If a structure worked earlier and now shows an error, it is because of how each system handles a CTC overflow:

| When components exceed the CTC | Payroll's older system                                                                  | Payroll 2.0                                                                |
| ------------------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| What the system does           | Silently lowers Basic or HRA to keep Special Allowance positive.                        | Flags a negative Special Allowance and skips the employee at finalisation. |
| Effect on statutory components | Basic/HRA could be reduced without your knowledge, risking minimum-wage non-compliance. | Basic/HRA are never changed automatically, keeping you compliant.          |
| What you need to do            | Nothing, the adjustment was hidden.                                                     | Rebalance the components once, as shown below.                             |

## How to fix it

Reduce how much of the CTC is locked into Basic, HRA and other fixed components so there is room for a positive Special Allowance. **The CTC stays the same.**

<Tabs>
  <Tab title="For a specific employee">
    1. Go to **People → employee's profile → Compensation**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/compensation-pie-chart.jpg" alt="Employee Compensation tab showing the Annual CTC breakdown with CTC component, Perquisites and Flexi components." width="800" />
    2. Assign a different salary structure for the same CTC, with a lower Basic/HRA allocation.
    3. Save, then confirm Special Allowance is zero or positive.
    4. Re-attempt finalisation.
  </Tab>

  <Tab title="For everyone on a shared structure">
    1. Go to **Settings → Component Library → Salary Structures → Manage**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/salary-structure-manage.jpg" alt="Salary Structures Manage option highlighted under Component Library in Settings." width="800" />
    2. Edit the structure and lower the percentage allocated to Basic/HRA/other allowances. This corrects every employee on that structure at once.
           <img src="https://razorpay.com/docs/build/browser/assets/images/existing-structure-add-components.jpg" alt="Build your structure page showing Basic and HRA as a percentage of CTC, with the residual allowance and a sample CTC preview." width="800" />
    3. Save, then confirm Special Allowance is zero or positive.
    4. Re-attempt finalisation.

    Know more about [salary structures](/docs/payroll/multiple-salary-structure).
  </Tab>
</Tabs>

## Worked examples

<AccordionGroup>
  <Accordion title="Example 1: Employer PF makes Special Allowance negative">
    Annual CTC ₹6,00,000. The only change in the fix is dropping HRA from 30% to 25%; the CTC stays the same.

    | Component (₹/yr)                   | Before (negative) | After (fixed)   |
    | ---------------------------------- | ----------------- | --------------- |
    | Annual CTC                         | ₹6,00,000         | ₹6,00,000       |
    | Basic (60%)                        | ₹3,60,000         | ₹3,60,000       |
    | HRA                                | ₹1,80,000 (30%)   | ₹1,50,000 (25%) |
    | Conveyance (fixed)                 | ₹50,000           | ₹50,000         |
    | Employer PF (12% of Basic, capped) | ₹21,600           | ₹21,600         |
    | **Special Allowance (residual)**   | **-₹11,600 ✗**    | **+₹18,400 ✓**  |
  </Accordion>

  <Accordion title="Example 2: 100% allocated, no room for Special Allowance">
    Annual CTC ₹4,80,000. The only change in the fix is dropping HRA from 50% to 40%; the CTC stays the same.

    | Component (₹/yr)                 | Before (negative) | After (fixed)   |
    | -------------------------------- | ----------------- | --------------- |
    | Annual CTC                       | ₹4,80,000         | ₹4,80,000       |
    | Basic (50%)                      | ₹2,40,000         | ₹2,40,000       |
    | HRA                              | ₹2,40,000 (50%)   | ₹1,92,000 (40%) |
    | Employer PF                      | ₹21,600           | ₹21,600         |
    | **Special Allowance (residual)** | **-₹21,600 ✗**    | **+₹26,400 ✓**  |
  </Accordion>
</AccordionGroup>

## Related information

* [CTC Components](/docs/payroll/compensation/ctc-components)
* [Salary Structures](/docs/payroll/multiple-salary-structure)
* [Special Allowance FAQs](/docs/payroll/faqs#special-allowance)
