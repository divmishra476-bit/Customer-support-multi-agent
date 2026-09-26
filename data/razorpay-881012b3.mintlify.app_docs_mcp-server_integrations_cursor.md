> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Razorpay MCP Server to Cursor

> Connect the Razorpay MCP Server to Cursor through the mcp-remote bridge by editing the mcp.json configuration file.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Cursor connects to the Razorpay Remote MCP Server through the `mcp-remote` bridge. You can add it from Cursor Settings, or by editing the MCP configuration file directly.

<Info>
  **Handy Tips**

  Cursor requires Node.js and `npm` for the `mcp-remote` bridge. Refer to the [Remote MCP Server setup](/docs/mcp-server/remote#step-1-install-node-js) to install Node.js and generate your Base64-encoded merchant token.
</Info>

## Cursor Configuration

1. Open **Cursor** and navigate to **Settings** → **Cursor Settings**.
2. Go to **MCP Tools** and click **Add Custom MCP**. This opens your `mcp.json` file.
3. Paste the following configuration and save the file:

```json Cursor Configuration theme={null}
{
  "mcpServers": {
    "rzp-mcp-server": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.razorpay.com/mcp",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Basic <Base64(key:secret)>"
      }
    }
  }
}
```

4. Replace `<Base64(key:secret)>` with your Base64-encoded token.
5. Cursor starts the server and lists the available Razorpay tools, which confirms a successful connection.

<Info>
  **Handy Tips**

  The `.cursor/mcp.json` file in a repository root applies to that project only, while `~/.cursor/mcp.json` applies globally. If both files define the server, the project configuration takes precedence.
</Info>

## Video Walkthrough

Watch this video to see how to set up the Razorpay MCP Server in the Cursor agent.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vpm94BATvUc" title="Set up Razorpay MCP Server in Cursor Agent" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Watch this video to see how to configure the Razorpay MCP Server in the Cursor CLI.

<iframe width="560" height="315" src="https://www.youtube.com/embed/priYWCinKpI" title="Configure Razorpay MCP Server in Cursor CLI" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<Info>
  **Need Help?**

  If you need any assistance with the integration, reach out to us at [agentic-payments@razorpay.com](mailto:agentic-payments@razorpay.com).
</Info>
