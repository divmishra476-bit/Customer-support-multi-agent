> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Commission Reports and Auto-generated Invoices

> View the commission settlement reports and the various states of commission payouts.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
  <span>🇲🇾 Malaysia</span>
</div>

Under the **Earnings** tab, there are three sections under which you can view detailed commission reports and auto-generated invoices on the **3rd day of every month** on the Razorpay Partner Dashboard.

<Warning>
  **Watch Out!**

  RazorpayX referral bonus calculation and disbursal happens manually. For any queries, send an email to our [Partnerships team](mailto:partnerships@razorpay.com) or contact our [Support team](https://razorpay.com/support/#request).
</Warning>

## View Commission Reports

#### Requirements for Commission Data to be Displayed

The commission data under the **Earnings** tab is based on the Partner type and the following factors:

<Tabs>
  <Tab title="Service Partners">
    The commission data is displayed under the **Earnings** tab if at least 3 sub-merchants are added.
  </Tab>

  <Tab title="Technology Partners">
    The commission data is displayed if the third-party application with Razorpay is created (for client credentials) and [OAuth](/docs/partners/technology-partners/onboard-businesses/integrate-oauth) integration is necessary.
  </Tab>
</Tabs>

## Daily Earnings

This report displays the earnings generated from referred accounts by you on a day-to-day basis. There are two columns in this report:

* **Base Earnings**: This is the amount you earn from the platform fee.
* **Add-on Earnings**: This is the additional commission you charged your customers. For example, platform fees.

<img class="click-zoom" src="https://razorpay.com/docs/build/browser/assets/images/partner-daily-earnings.jpg" alt="partner daily earnings" width="800" />

## Transactional Details

You can view the earnings details from each transaction made by your affiliate accounts. This report is available only for the partner types `Aggregator` and `Technology Partner`.

<img class="click-zoom" src="https://razorpay.com/docs/build/browser/assets/images/partner-transactions.jpg" alt="partner transactions" width="800" />

## Check Auto-generated Invoices

The **Invoices** section is available for partners who have commissions processed using the [Commission Payout with Auto-generated Invoice](/docs/partners/commissions/settlement-process#automated-invoice-commission-payout-recommended) process. The following columns are displayed:

* **Invoice ID**: This is the unique identifier of the invoice. Click **Invoice Id** to view **Commission Period**, **Invoice Date**, **Status** and detailed commission **Amount Breakup** displayed in the side panel.
* **Amount**: This is the commission receivable balance (Base Commission + GST - TDS).
* **Created Date**: The date at which the invoice is created.
* **Status**: The status of the invoice. Possible states are **Issued**, **Under Review** and **Processed**.

You can download the commission invoice details in PDF format.

<img class="click-zoom" src="https://razorpay.com/docs/build/browser/assets/images/partners-download-invoice.jpg" alt="download invoice" width="800" />

### Related Information

* [Commission for Payment Products](/docs/partners/commissions)
* [Referral Bonus for RazorpayX powered Current Accounts](/docs/partners/commissions/referral-bonus)
* [Commission Settlement Process](/docs/partners/commissions/settlement-process)
