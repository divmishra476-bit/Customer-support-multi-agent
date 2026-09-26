> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Install Razorpay n8n Community Node

> Install and configure the Razorpay n8n Community Node. Follow this step-by-step guide to set up API keys and start automating payments.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Follow the steps given below to install the Razorpay n8n Community Node.

### Prerequisites

Before installing, ensure you have:

* **n8n Instance**: Running n8n v1.104.2 or higher
* **Node.js**: Version 14.x or higher (for self-hosted)
* **Razorpay Account**: Active account at [razorpay.com](https://razorpay.com)
* **Admin Access**: Permission to install community nodes

## Step 1: Generate Razorpay API Keys

You need to generate Razorpay API keys before using the node.

### Access API Keys

1. Log in to [Razorpay Dashboard](https://dashboard.razorpay.com/).
2. Navigate to **Account & Settings** → **API Keys** under **Website and app settings**.
3. Click **Generate Key**.
4. Copy both **Key ID** and **Key Secret**.

<Warning>
  **Watch out!**

  Save the Key id and Secret immediately - it will not be shown again.
</Warning>

#### Understand Key Types

<Tabs>
  <Tab title="Test Keys (Start Here)">
    **For Development & Testing**

    * Prefix: `rzp_test_`
    * No real money transactions
    * Free to use
    * Use [test cards](/docs/payments/payments/test-card-details)

    Always start with test keys for safe development.
  </Tab>

  <Tab title="Live Keys">
    **For Production**

    * Prefix: `rzp_live_`
    * Real money transactions
    * Requires completed KYC
    * Transaction fees apply

    Only use after thorough testing.
  </Tab>
</Tabs>

### Set Up API Keys in n8n

In n8n, create a new Razorpay API credential:

1. Enter your credentials:
   * Key id: Your Razorpay Key id (For example, `rzp_test_1234567890` or `rzp_live_1234567890`)
   * Key Secret: Your Razorpay Key Secret.
2. Test the connection to ensure your credentials are working correctly.

## Step 2: Install the Razorpay n8n Community Node

Choose your installation method based on your n8n deployment:

<AccordionGroup>
  <Accordion title="Method 1: Install via n8n Community Nodes (Recommended)">
    1. Log in to the **n8n Dashboard**.
    2. Click **Settings** in the left sidebar.
    3. Click **Community Nodes** in the settings menu.
    4. Install the Node.
       1. Click **Install a community node**.
       2. Enter the package name: `@razorpay/n8n-nodes-razorpay`.
       3. Click **Install**.
    5. Restart **n8n**. After restart, the Razorpay node will be available.
  </Accordion>

  <Accordion title="Method 2: Install via npm (Self-hosted)">
    For self-hosted n8n installations, run the following commands:

    ```bash theme={null}
    # Navigate to n8n directory
    cd ~/.n8n

    # Install the Razorpay community node
    npm install @razorpay/n8n-nodes-razorpay

    # Restart n8n service
    pm2 restart n8n
    # OR
    systemctl restart n8n
    ```
  </Accordion>

  <Accordion title="Method 3: Docker Installation">
    If you are using n8n with Docker, add the package to your Docker setup:

    ```yml Add Package theme={null}
     # In your Dockerfile or docker-compose.yml
     FROM n8nio/n8n:latest
     USER root
     RUN npm install -g @razorpay/n8n-nodes-razorpay
     USER node
    ```
  </Accordion>
</AccordionGroup>

You have successfully installed the Razorpay n8n Community Node.

## Next Steps

After installation, you can proceed with the following:

* Create a new workflow or open an existing one.
* Add the **Razorpay** node by searching and dragging it from the node panel.
* Set up your Razorpay API credentials.
* Choose the [operation](/docs/razorpay-n8n-node/operations-reference) you want to perform (Create Order, Fetch Payment and so on.)
* Configure the required parameters for your selected operation.
* Test your workflow to ensure everything works correctly.

<Info>
  **Handy Tips**

  * Start with Test Mode: Always use test credentials when setting up and testing your workflows.
  * Check API Documentation: Refer to [Razorpay API documentation](/docs/api) for detailed parameter information.
  * Use Webhooks: Consider setting up [Razorpay webhooks](/docs/webhooks) for real-time payment updates in your workflows.
</Info>

### Related Documentation

* [Explore Use Cases & Examples](/docs/razorpay-n8n-node/use-cases)
* [View Available Operations](/docs/razorpay-n8n-node/operations-reference)
* [Frequently Asked Questions](/docs/razorpay-n8n-node/troubleshooting-faqs)
* [Set up Webhooks](/docs/webhooks)
