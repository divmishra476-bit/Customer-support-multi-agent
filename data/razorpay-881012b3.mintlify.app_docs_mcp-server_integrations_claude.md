> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Razorpay MCP Server to Claude

> Connect the Razorpay MCP Server to Claude Desktop, the web app, and Claude Code (CLI) using the official connector or HTTP transport.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Razorpay is available as an official connector in Claude. As it is already listed in the Claude connector directory, you do not need to add a custom connector or edit any configuration file. Connect the listed connector and authorise it to get started.

## Claude Desktop and Web App

1. Open Claude and go to **Settings** → **Connectors**, or visit the connector directory at [claude.com/connectors](https://claude.com/connectors).
2. Locate the **Razorpay** connector in the directory. You can also open it directly at [claude.com/connectors/razorpay](https://claude.com/connectors/razorpay).
3. Click **Connect**. You are redirected to the Razorpay sign-in and consent screen.
4. Sign in with your Razorpay merchant credentials and approve the requested permissions.
5. Return to Claude. The Razorpay connector is now active. To use it within a chat, click the **+** icon (or type **/**) and enable Razorpay as a tool source.

<Info>
  **Handy Tips**

  Directory connectors that access private data use OAuth, so access is scoped to your own Razorpay permissions. Access to the connector directory requires a paid Claude plan.
</Info>

Watch this video to see how to install the Razorpay MCP Server in Claude Desktop.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4nK81peG4oM" title="Install Razorpay MCP Server in Claude Desktop" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Claude Code (CLI)

Claude Code connects to the Razorpay Remote MCP Server over HTTP transport. Run the following command in your terminal:

```bash Add Razorpay MCP Server theme={null}
claude mcp add --transport http razorpay https://mcp.razorpay.com/mcp \
  --header "Authorization: Basic <your-base64-encoded-key-secret>"
```

1. Replace `<your-base64-encoded-key-secret>` with the Base64 token you generated. Refer to the [Remote MCP Server setup](/docs/mcp-server/remote#step-3-authenticate-razorpay-account) to generate it.
2. Run `claude mcp list` to confirm the server is registered. To authenticate using OAuth, run `/mcp` within a Claude Code session.
3. Test the connection by asking: **Show me available Razorpay tools**.

Watch this video to see how to connect the Razorpay MCP Server to Claude Code (CLI).

<iframe width="560" height="315" src="https://www.youtube.com/embed/5pOub7uSo_s" title="Connect Razorpay MCP Server to Claude Code (CLI)" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<Info>
  **Need Help?**

  If you need any assistance with the integration, reach out to us at [agentic-payments@razorpay.com](mailto:agentic-payments@razorpay.com).
</Info>
