> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Razorpay MCP Server to Gemini CLI

> Connect the Razorpay MCP Server to Gemini CLI by adding the server to the mcpServers block in settings.json using HTTP transport.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Gemini CLI discovers MCP servers from the `mcpServers` block in its `settings.json` file. Add the Razorpay Remote MCP Server using HTTP transport.

## Gemini CLI Configuration

1. Open your Gemini CLI settings file. Use `~/.gemini/settings.json` for global configuration, or `.gemini/settings.json` within a project.
2. Add the following Razorpay server entry and save the file:

```json Gemini CLI Configuration theme={null}
{
  "mcpServers": {
    "razorpay": {
      "httpUrl": "https://mcp.razorpay.com/mcp",
      "headers": {
        "Authorization": "Basic <your-base64-encoded-key-secret>"
      }
    }
  }
}
```

3. Replace `<your-base64-encoded-key-secret>` with your Base64 token. You can also reference an environment variable, such as `$RAZORPAY_TOKEN`, as Gemini CLI expands variables in the configuration. Refer to the [Remote MCP Server setup](/docs/mcp-server/remote#step-3-authenticate-razorpay-account) to generate the token.
4. Restart Gemini CLI and run `/mcp` to check the server status. If required, run `/mcp reload` to fetch the tools again.

<Info>
  **Need Help?**

  If you need any assistance with the integration, reach out to us at [agentic-payments@razorpay.com](mailto:agentic-payments@razorpay.com).
</Info>
