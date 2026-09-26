> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Frequently Asked Questions (FAQs)

> Common issues, debugging techniques, and solutions for the Razorpay MCP Server.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

<AccordionGroup>
  <Accordion title="What is MCP (Model Context Protocol)?">
    The Model Context Protocol (MCP) is an open standard that allows AI models to interact with external tools and services. It enables AI assistants like Claude to execute operations on platforms like Razorpay through a standardised interface, allowing for seamless integration and natural language interactions with payment systems.
  </Accordion>

  <Accordion title="Can I use the Razorpay MCP Server in production?">
    Yes, the Razorpay MCP Server is an official integration designed for production use. Make sure to use appropriate API keys based on your environment (test keys for development, live keys for production) and follow security best practices for API key management.
  </Accordion>

  <Accordion title="How do I switch between test and live modes?">
    Use the corresponding [Razorpay API keys](/docs/payments/dashboard/account-settings/api-keys#generate-api-keys) for your desired environment. For test mode, use test environment API keys (starting with rzp\_test\_). For live mode, use production API keys (starting with rzp\_live\_). The MCP Server automatically detects the environment based on your API keys.
  </Accordion>

  <Accordion title="What is the difference between Remote and Local MCP Server?">
    Remote MCP Server is hosted by Razorpay with zero infrastructure management, automatic updates, and quick setup using npx. Local MCP Server is self-hosted using Docker, providing complete control over infrastructure and access to all tools without restrictions. We recommend Remote MCP Server for most use cases.
  </Accordion>

  <Accordion title="Which AI-assisted applications are supported?">
    The Razorpay MCP Server works with Claude Desktop, Cursor, Visual Studio Code (with MCP extension), and other MCP-compatible tools. Each application has slightly different configuration requirements, but all follow the same MCP standard.
  </Accordion>
</AccordionGroup>
