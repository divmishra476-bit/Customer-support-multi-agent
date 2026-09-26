> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate with Current Account

> Integrate RazorpayX Payroll with RazorpayX powered Current Account for easier transactions.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

You can integrate your RazorpayX powered Current Account  with Payroll integration to make transactions and reconciliation easier.

Here's a rewritten version that removes the invite-basis requirement:

RazorpayX powered Current Account integration is available for all eligible customers. To enable the integration, [contact support](mailto:Payroll@razorpay.com) and our Payroll team will assist with setting up the integration from our end.

## Prerequisites

* You must have a [RazorpayX - Current Account](/docs/x/account-types/current-account).

* Share your Razorpay MID when you request for the integration. You can find this on the [RazorpayX Dashboard](https://x.razorpay.com/auth) on the top-right corner under **Profile**.
  <img src="https://razorpay.com/docs/build/browser/assets/images/x-payroll-ca-int-profile-dashboard.jpg" alt="RazorpayX Dashboard- Profile" width="300" />

* There should not be any `Pending` transactions in the ledger for your organisation (**Reports** → **Ledger**). You cannot integrate if there are pending transactions.

* There should be no balance in your Payroll account before integration.
  * If there is any balance, add the Current Account as a [Contractor](/docs/payroll/administrator#differences-between-employee-and-contractor) and [transfer funds](/docs/payroll/payroll-payouts#transfer-funds) to this account.
  * Select **Reimbursement** / **No TDS** for the transfer.

## Points To Remember

The integration process is easy and does not require much effort. However, there are a few things to keep in mind before you request for the integration. They are listed as follows:

### Approval Workflows

Approval Workflows or maker-checkers in RazorpayX provide different permissions to the team members. As such, you might have **Transactions Pending for Approval** on the Payroll Dashboard.

* If you have [approval workflows (maker-checker)](/docs/x/manage-teams/approval-workflow) enabled on your RazorpayX account, the same is applicable to all transactions originating from Payroll by default.
* The transactions made in Payroll (salary, contractor payments, reimbursements, advance salaries and compliance payments) follow the Approval Workflow (in terms of both amount and approvers) that you have set up on RazorpayX.
* These transactions are not executed until they are approved from the [RazorpayX Dashboard](https://x.razorpay.com/auth).

Watch this video to know more about the approval process on RazorpayX.

<img src="https://razorpay.com/docs/build/browser/assets/images/x-payroll-approval-workflow.gif" alt="X Approval Workflow" width="800" />

[Contact support](mailto:Payroll@razorpay.com) if you wish to remove the approval workflow functionality for payouts happening via Payroll.

### Visibility Of Transactions On RazorpayX Dashboard

With the integration, all your transactions will happen via your RazorpayX account. These are visible on the RazorpayX Dashboard under **Payouts** and **Account Statements**.

* Every user who has access to your RazorpayX account can view the transactions that originate from Payroll on the RazorpayX Dashboard.
* All transactions, like salary transfers, contractor payments, reimbursements, salary advances and compliance payments, among others, are visible on the RazorpayX Dashboard.

## Post Integration

Once your RazorpayX powered Current Account is integrated with Payroll:

* Your RBL Current Account balance replaces the Payroll Account on the Payroll Dashboard, as shown.

  <img src="https://razorpay.com/docs/build/browser/assets/images/x-payroll-ca-int-acc-balance.jpg" alt="Payroll Account Balance" width="300" />

  You will see the balance of the current account.

* Your Payroll Account becomes non-functional.

<Warning>
  **Watch Out!**

  Do not transfer any funds to your Payroll account after the integration since you cannot access this account.
</Warning>

* All your transactions and payments from Payroll will now happen from your Current Account.
* For your employees, your company name reflects on the bank transfer narrations.
* You do not have to transfer funds between multiple accounts.

## Remove Integration

You can choose to remove the integration between Payroll and RazorpayX powered Current Account.

<Warning>
  **Watch Out!**

  The integration can be disconnected only when there are no `Pending` transactions in your Payroll account. If there are `Pending` transactions, then wait to clear them before disconnecting the accounts.
</Warning>

[Contact support](mailto:Payroll@razorpay.com) to disconnect the integration.

### Related Information

* [RazorpayX - Current Account](/docs/x/account-types/current-account)
* [Approval Workflow](/docs/x/manage-teams/approval-workflow)
* [Integrations](/docs/payroll/integrations)
