> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About BBPS Integration

> Integrate Bharat Bill Payment System (BBPS) with Razorpay to enable customers to pay utility bills, recharges, insurance, and more on your platform.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Razorpay is a licensed Customer Operating Unit (COU) on the [Bharat Bill Payment System (BBPS)](https://www.npci.org.in/what-we-do/bharat-billpay/about), India's centralised, interoperable bill payment platform managed by NPCI. Using Razorpay's BBPS integration, your platform can let customers discover billers, fetch bill amounts, and make payments across hundreds of utility categories.

## How It Works

BBPS bill payments follow an asynchronous, multi-step flow:

1. **Fetch Biller Categories** - retrieve all available bill categories (electricity, water, gas, broadband, insurance, etc.).
2. **Fetch Billers** - list billers within a chosen category.
3. **Fetch Biller Plans**(optional) - retrieve plans offered by a biller where applicable (e.g. prepaid recharges).
4. **Create a Bill Request** - submit the customer's biller-specific identifiers (account number, consumer ID, etc.) to fetch the outstanding bill amount from the biller.
5. **Poll Bill Request** - poll the Fetch Bill Request API until the status becomes `success` or `failed`.
6. **Create a Bill Payment** - initiate payment for the fetched bill amount.
7. **Poll Bill Payment** - poll the Fetch Bill Payment API until the status becomes `success` or `failed`.

<Warning>
  **Watch Out!**

  Bill Request and Bill Payment APIs are asynchronous. After creating a resource, always poll the corresponding Fetch API at regular intervals until the status reaches a terminal state (`success` or `failed`). Do not assume success based on the creation response alone.
</Warning>

## Prerequisites

Before you begin:

* Complete [API key generation](/docs/payments/dashboard/account-settings/api-keys) on the Razorpay Dashboard.
* Ensure your account has BBPS access enabled. Contact [Razorpay Support](https://razorpay.com/support/) if you need it activated.
* Use your **Test API Keys** during development. Payments made with test keys are not processed on the live BBPS network.

## Integration Steps

<AccordionGroup>
  <Accordion title="Step 1: Fetch Biller Categories">
    Use the [Fetch Biller Categories](/docs/api/bills/bill-payments/fetch-biller-categories) API to retrieve all supported bill categories. Present these to your customer so they can choose the type of bill they want to pay. Use the returned `id` in Step 2.
  </Accordion>

  <Accordion title="Step 2: Fetch Billers">
    Use the [Fetch Billers](/docs/api/bills/bill-payments/fetch-billers) API with the selected `category` to retrieve all billers within that category. Each biller includes a `gateway_data.account_holder_config.params` list describing the customer inputs (for example, consumer number, account number) needed to identify the customer's account on the biller. Use `gateway_data.bill_request_config.bill_request_required` to decide whether bill fetch is mandatory, optional, or unsupported.
  </Accordion>

  <Accordion title="Step 3: Fetch Biller Plans (optional)">
    For billers that offer plans (such as prepaid recharges), use the [Fetch Biller Plans](/docs/api/bills/bill-payments/fetch-biller-plans) API to retrieve available plans. Skip this step if the biller does not offer plans.
  </Accordion>

  <Accordion title="Step 4: Create a Bill Request">
    Use the [Create a Bill Request](/docs/api/bills/bill-payments/create-bill-request) API to fetch the outstanding bill amount for your customer from the biller's system. This API returns immediately with a `processing` status - move to Step 5 to poll for the result.
  </Accordion>

  <Accordion title="Step 5: Poll the Bill Request">
    Use the [Fetch Bill Request](/docs/api/bills/bill-payments/fetch-bill-request) API with the `id` returned in Step 4. Poll at regular intervals until `status` is `success` or `failed`. On success, use the returned `bills[].amount` and `bills[].bill_number` in Step 6.

    <Warning>
      **Watch Out!**

      Always wait for the Bill Request status to reach `success` before creating a Bill Payment. A `failed` status means the biller could not retrieve the bill - surface an appropriate error to the customer.
    </Warning>
  </Accordion>

  <Accordion title="Step 6: Create a Bill Payment">
    Use the [Create a Bill Payment](/docs/api/bills/bill-payments/create-bill-payment) API with the `bill_request_id` from the successful bill request and the `bills[].amount` returned. Pass a unique `X-Bill-Payments-Idempotency` header (4-36 characters, alphanumeric with hyphens, underscores, or spaces; UUID v4 recommended) on every request to safely retry without creating duplicate payments. This API is asynchronous - move to Step 7 to poll for the result.
  </Accordion>

  <Accordion title="Step 7: Poll the Bill Payment">
    Use the [Fetch Bill Payment](/docs/api/bills/bill-payments/fetch-bill-payment) API with the `id` returned in Step 6. Poll until `status` is `success` or `failed`, then display the result to your customer.
  </Accordion>
</AccordionGroup>

## Supported Bill Categories

BBPS supports a wide range of bill categories, including but not limited to:

| Category           | Examples                                            |
| ------------------ | --------------------------------------------------- |
| Utilities          | Electricity, Water, Gas (piped)                     |
| Telecom            | Mobile Postpaid, Broadband Postpaid, Landline       |
| Financial Services | Loan Repayment, Insurance Premium, Credit Card Bill |
| Government         | Municipal Tax, Housing Society Charges              |
| Education          | School Fees, University Fees                        |
| Transportation     | FASTag Recharge, Metro Card Recharge                |

## API Reference

<CardGroup cols={2}>
  <Card title="Bill Payments API Home" href="/docs/api/bills/bill-payments">
    Overview of all BBPS API endpoints.
  </Card>
</CardGroup>
