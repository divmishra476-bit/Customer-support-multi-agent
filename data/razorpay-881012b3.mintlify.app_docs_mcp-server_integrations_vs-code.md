> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Razorpay MCP Server to VS Code

> Connect the Razorpay MCP Server to Visual Studio Code in agent mode using user settings that prompt securely for your merchant token.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Visual Studio Code supports MCP servers in agent mode through user settings. The following configuration prompts you securely for your merchant token instead of storing it in plain text.

<Info>
  **Handy Tips**

  Visual Studio Code requires Node.js and `npm` for the `mcp-remote` bridge. Refer to the [Remote MCP Server setup](/docs/mcp-server/remote#step-1-install-node-js) to install Node.js and generate your Base64-encoded merchant token.
</Info>

## Visual Studio Code Configuration

1. Open **Visual Studio Code**.
2. Open the Command Palette and select **Preferences: Open User Settings (JSON)**.
3. Paste the following configuration into the settings file and save it:

```json Visual Studio Code Configuration theme={null}
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "merchant_token",
        "description": "Razorpay Merchant Token",
        "password": true
      }
    ],
    "servers": {
      "razorpay-remote": {
        "command": "npx",
        "args": [
          "mcp-remote",
          "https://mcp.razorpay.com/mcp",
          "--header",
          "Authorization: Basic ${input:merchant_token}"
        ]
      }
    }
  }
}
```

4. When you start the server, Visual Studio Code prompts you to enter your Base64-encoded merchant token. Paste the token to complete the connection.

<Info>
  **Handy Tips**

  To learn more about running MCP servers in Visual Studio Code, refer to the [agent mode documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).
</Info>

## Video Walkthrough

Watch this video to see how to connect the Razorpay MCP Server to Visual Studio Code.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rVJvaLu_1UA" title="Connect Razorpay MCP Server to Visual Studio Code" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<Info>
  **Need Help?**

  If you need any assistance with the integration, reach out to us at [agentic-payments@razorpay.com](mailto:agentic-payments@razorpay.com).
</Info>
