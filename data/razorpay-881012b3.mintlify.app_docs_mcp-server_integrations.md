> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Razorpay MCP Server Integrations

> Connect the Razorpay MCP Server to AI platforms such as Claude, ChatGPT, Cursor, VS Code, Windsurf, Replit, and Gemini CLI.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

The Razorpay MCP Server connects to a wide range of AI platforms, letting your AI tool create and track payments, Payment Links, orders, refunds, settlements, payouts, and QR codes using natural language commands.

Each platform has its own configuration method, so follow the guide that matches the tool you use. Where Razorpay is already available as a built-in connector or app, no manual configuration is required. All guides use the recommended [Remote MCP Server](/docs/mcp-server/remote) endpoint `https://mcp.razorpay.com/mcp`.

<Info>
  **Handy Tips**

  Before you begin, generate your [Razorpay API keys](/docs/payments/dashboard/account-settings/api-keys#generate-api-keys) and, for platforms that connect through the `mcp-remote` bridge (Cursor, Visual Studio Code, and Windsurf), install Node.js. Refer to the [Remote MCP Server setup](/docs/mcp-server/remote) for prerequisites and to encode your merchant token.
</Info>

## Choose Your Platform

<CardGroup cols={2}>
  <Card title="Claude" href="/docs/mcp-server/integrations/claude">
    Connect using the official Razorpay connector or Claude Code (CLI).
  </Card>

  <Card title="ChatGPT" href="/docs/mcp-server/integrations/chatgpt">
    Install the official Razorpay app and authorise it using OAuth.
  </Card>

  <Card title="Cursor" href="/docs/mcp-server/integrations/cursor">
    Add the server through the mcp-remote bridge in mcp.json.
  </Card>

  <Card title="Visual Studio Code" href="/docs/mcp-server/integrations/vs-code">
    Configure agent mode with a secure merchant token prompt.
  </Card>

  <Card title="Windsurf" href="/docs/mcp-server/integrations/windsurf">
    Add the server to the Cascade agent via mcp\_config.json.
  </Card>

  <Card title="Replit" href="/docs/mcp-server/integrations/replit">
    Add the server from Integrations settings and authorise via OAuth.
  </Card>

  <Card title="Gemini CLI" href="/docs/mcp-server/integrations/gemini-cli">
    Add the server to the mcpServers block in settings.json.
  </Card>
</CardGroup>
