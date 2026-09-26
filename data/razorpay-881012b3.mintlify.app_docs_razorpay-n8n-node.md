> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Razorpay n8n Community Node

> Set up and use the Razorpay n8n Community Node to integrate Razorpay payment APIs with your n8n workflows for automated payment processing.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

<CardGroup cols={2}>
  <Card title="Razorpay n8n Node Repository" href="https://github.com/razorpay/n8n-nodes-razorpay">
    View source code, report issues, and contribute to the Razorpay n8n Community Node.
  </Card>

  <Card title="Razorpay n8n Node NPM Package" href="https://www.npmjs.com/package/@razorpay/n8n-nodes-razorpay">
    Official npm package for the Razorpay n8n Community Node.
  </Card>
</CardGroup>

The [Razorpay n8n Community Node](https://www.npmjs.com/package/@razorpay/n8n-nodes-razorpay) provides seamless integration between Razorpay payment APIs and [n8n workflow automation platform](https://n8n.io/). This node enables developers, operations teams, and business owners to automate payment operations, process transactions, manage refunds, and build sophisticated payment workflows without writing code.

## Features

1. **No-Code Automation** <br />
   Build complex payment workflows visually with drag-and-drop interface.

2. **400+ App Integrations** <br />
   Connect Razorpay with Google Sheets, Slack, WhatsApp, Gmail, Shopify and 400+ other services instantly.

3. **Test & Live Modes** <br />
   Develop and test workflows safely with test mode API keys before deploying to production.

4. **Real-Time Processing** <br />
   Process payments, refunds and settlements with minimal latency using efficient API operations.

5. **Flexible Data Handling** <br />
   Transform, filter and enrich payment data using built-in n8n nodes and custom functions.

6. **Secure & Compliant** <br />
   Enterprise-grade security with encrypted credential storage and PCI DSS-compliant operations.

## Available Operations

The Razorpay n8n Node provides comprehensive access to Razorpay APIs through **10 core operations**:

| Category          | Operations                          | Key Use Cases                                   |
| ----------------- | ----------------------------------- | ----------------------------------------------- |
| **Orders**        | Fetch All                           | Order management, payment tracking              |
| **Payment Links** | Create, Fetch                       | Instant payment collection, WhatsApp automation |
| **Payments**      | Fetch, Fetch All                    | Payment verification, reconciliation            |
| **Refunds**       | Fetch All                           | Fetch refund information                        |
| **Settlements**   | Fetch, Fetch All                    | Daily settlement sync, accounting               |
| **Invoices**      | Fetch Invoices for for Subscription | Subscription billing automation                 |
| **Disputes**      | Fetch All                           | Dispute monitoring and alerts                   |

View [Complete Operations Reference](/docs/razorpay-n8n-node/operations-reference).

<Info>
  **Extended Operations Available**

  Access **28 additional operations** via [Razorpay MCP Server](/docs/mcp-server) integration.
</Info>

## Use Cases

Explore real-world automation scenarios:

* **WhatsApp Booking Automation**: Chat-to-order-to-payment workflow.
* **Daily Settlement Reconciliation**: Automated sync to Google Sheets.
* **High-Value Payment Alerts**: Real-time Slack notifications.
* **Refund Processing**: Automated refund creation based on rules.
* **Customer Payment Lookup**: Internal tool for support teams.

View [Use Cases](/docs/razorpay-n8n-node/use-cases).

## Prerequisites

Ensure you have the following before starting:

<AccordionGroup>
  <Accordion title="n8n Platform">
    * **n8n Version**: v1.104.2 or higher (minimum required).
    * **Deployment**: n8n Cloud or self-hosted instance.
    * **Admin Access**: Permission to install community nodes.
  </Accordion>

  <Accordion title="For Self-Hosted n8n">
    * **Node.js**: Version 14.x or higher.
    * **npm**: Version 6.x or higher.
    * **Network Access**: HTTPS access to `api.razorpay.com`.
  </Accordion>

  <Accordion title="Razorpay Account">
    * **Active Account**: Sign up at [razorpay.com](https://razorpay.com).
    * **KYC Completed**: Required for live mode (not needed for test mode).
    * **API Keys**: Generate [API keys](/docs/payments/dashboard/account-settings/api-keys) from the Razorpay Dashboard.

    <Info>
      **Start with Test Mode**

      Use test mode API keys (`rzp_test_*`) for development and testing. No real money transactions, no KYC required. Switch to live mode (`rzp_live_*`) after thorough testing.
    </Info>
  </Accordion>
</AccordionGroup>

## Next Steps

1. **[Install the Node](/docs/razorpay-n8n-node/installation)**: Add Razorpay node to your n8n instance.
2. **Configure Credentials**: Generate and add your API keys.
3. **[Explore Use Cases](/docs/razorpay-n8n-node/use-cases)**: Learn from real-world examples.
4. **Build Your Workflow**: Start with a simple automation.
5. **[Troubleshoot Issues](/docs/razorpay-n8n-node/troubleshooting-faqs)**: Resolve common problems.

### Related Documentation

* [Razorpay API Reference](/docs/api)
* [Webhook Integration Guide](/docs/webhooks)
* [Test Card Details](/docs/payments/payments/test-card-details)
* [MCP Server Documentation](/docs/mcp-server)
* [n8n Documentation](https://docs.n8n.io/)
