> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Razorpay MCP Server to Windsurf

> Connect the Razorpay MCP Server to the Windsurf Cascade agent by adding the server entry to the raw mcp_config.json file.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

The Windsurf Cascade agent reads MCP servers from a single configuration file. Add the Razorpay Remote MCP Server using the raw configuration editor.

<Info>
  **Handy Tips**

  Windsurf requires Node.js and `npm` for the `mcp-remote` bridge. Refer to the [Remote MCP Server setup](/docs/mcp-server/remote#step-1-install-node-js) to install Node.js and generate your Base64-encoded merchant token.
</Info>

## Windsurf Configuration

1. Open **Windsurf** and navigate to **Windsurf Settings** → **Cascade** → **MCP Servers**. You can also click the MCP icon at the top-right of the Cascade panel.
2. Click **Manage MCPs**, then click **View raw config** to open the `mcp_config.json` file.
3. Add the following Razorpay server entry to the file and save it:

```json Windsurf Configuration theme={null}
{
  "mcpServers": {
    "rzp-mcp-server": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.razorpay.com/mcp",
        "--header",
        "Authorization: Basic <your-base64-encoded-key-secret>"
      ]
    }
  }
}
```

4. Return to the **Manage MCPs** page and click **Refresh** to connect to the server and fetch the Razorpay tools.

<Info>
  **Handy Tips**

  The configuration file is located at `~/.codeium/windsurf/mcp_config.json` on macOS and `%USERPROFILE%\.codeium\windsurf\mcp_config.json` on Windows. Windsurf supports global configuration only and does not interpolate environment variables, so enter the token value directly.
</Info>

<Info>
  **Need Help?**

  If you need any assistance with the integration, reach out to us at [agentic-payments@razorpay.com](mailto:agentic-payments@razorpay.com).
</Info>
