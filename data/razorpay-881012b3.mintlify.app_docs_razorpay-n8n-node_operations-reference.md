> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Operations Reference

> Complete reference for all available operations in the Razorpay n8n Community Node with detailed configuration and examples.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

The Razorpay n8n Community Node provides comprehensive access to Razorpay APIs through multiple operations. Each operation corresponds to specific Razorpay API endpoints and enables you to automate payment workflows.

## Operations Overview

The n8n node provides **12 core operations** organised across the following categories:

<Info>
  **Extended Operations via MCP Server**

  The node can access an additional **28 operations** through the [Razorpay MCP Server](/docs/mcp-server) integration, bringing the total to 40 operations.
</Info>

## Complete Operations List

### Orders

| Operation        | Description                                           | Required Parameters | Optional Parameters                        | API Documentation                      |
| ---------------- | ----------------------------------------------------- | ------------------- | ------------------------------------------ | -------------------------------------- |
| Fetch All Orders | Retrieve a list of all orders with optional filtering | -                   | from, to, count, skip, authorized, receipt | [API Docs](/docs/api/orders/fetch-all) |

### Payment Links

| Operation           | Description                                 | Required Parameters      | Optional Parameters                                                    | API Documentation                                              |
| ------------------- | ------------------------------------------- | ------------------------ | ---------------------------------------------------------------------- | -------------------------------------------------------------- |
| Create Payment Link | Generate a Payment Link for customers       | amount (paise), currency | description, customer details, notify, callback\_url, callback\_method | [API Docs](/docs/api/payments/payment-links/create-standard)   |
| Fetch Payment Link  | Retrieve details of a specific Payment Link | payment\_link\_id        | -                                                                      | [API Docs](/docs/api/payments/payment-links/fetch-id-standard) |

### Payments

| Operation           | Description                                       | Required Parameters | Optional Parameters              | API Documentation                                 |
| ------------------- | ------------------------------------------------- | ------------------- | -------------------------------- | ------------------------------------------------- |
| Fetch Payment by id | Get detailed information about a specific payment | payment\_id         | expand\[]                        | [API Docs](/docs/api/payments/fetch-with-id)      |
| Fetch All Payments  | Retrieve all payments with filtering options      | -                   | from, to, count, skip, expand\[] | [API Docs](/docs/api/payments/fetch-all-payments) |

### Refunds

| Operation         | Description                         | Required Parameters | Optional Parameters                | API Documentation                       |
| ----------------- | ----------------------------------- | ------------------- | ---------------------------------- | --------------------------------------- |
| Fetch All Refunds | Retrieve all refunds with filtering | -                   | from, to, count, skip, payment\_id | [API Docs](/docs/api/refunds/fetch-all) |

### Settlements

| Operation              | Description                             | Required Parameters | Optional Parameters   | API Documentation                               |
| ---------------------- | --------------------------------------- | ------------------- | --------------------- | ----------------------------------------------- |
| Fetch Settlement by id | Get details of a specific settlement    | settlement\_id      | expand\[]             | [API Docs](/docs/api/settlements/fetch-with-id) |
| Fetch All Settlements  | Retrieve all settlements with filtering | -                   | from, to, count, skip | [API Docs](/docs/api/settlements/fetch-all)     |

### Invoices

| Operation                       | Description                                  | Required Parameters | Optional Parameters | API Documentation                                           |
| ------------------------------- | -------------------------------------------- | ------------------- | ------------------- | ----------------------------------------------------------- |
| Fetch Invoices for Subscription | Get all invoices for a specific subscription | subscription\_id    | -                   | [API Docs](/docs/api/payments/subscriptions/fetch-invoices) |

### Disputes

| Operation          | Description                    | Required Parameters | Optional Parameters                | API Documentation                        |
| ------------------ | ------------------------------ | ------------------- | ---------------------------------- | ---------------------------------------- |
| Fetch All Disputes | Retrieve all customer disputes | -                   | from, to, count, skip, payment\_id | [API Docs](/docs/api/disputes/fetch-all) |

## Best Practices

1. Use Pagination for Large Datasets: Always paginate when fetching large numbers of records to prevent timeout errors and reduce API load.

2. Filter by Date Range: Limit results using `from` and `to` parameters to improve response time and reduce data transfer.

3. Expand Selectively: Only expand necessary nested objects to reduce response size and improve performance.

4. Handle Errors Gracefully: Implement proper error handling to ensure workflow reliability and easier debugging.

5. Test Mode First: Always test workflows with test credentials to prevent accidental real transactions and charges.

6. Use Expressions for Dynamic Values: Reference data from previous nodes using expressions to create flexible, reusable workflows.

7. Implement Rate Limit Handling: Add delays between batch operations to prevent rate limit errors (429 responses).

8. Log Important Data: Use **Set** or **Function** nodes to log key information.

## Next Steps

* [View Use Cases & Examples](/docs/razorpay-n8n-node/use-cases)
* [Troubleshooting & FAQs](/docs/razorpay-n8n-node/troubleshooting-faqs)
