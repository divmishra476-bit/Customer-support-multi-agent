> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Razorpay MCP Server Configuration

> Detailed configuration options and advanced setup for the Razorpay MCP Server.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

The Razorpay MCP Server requires the following environment variables for configuration:

| Variable              | Type    | Required | Description                                                 |
| --------------------- | ------- | -------- | ----------------------------------------------------------- |
| `RAZORPAY_KEY_ID`     | string  | Yes      | Your Razorpay API key ID                                    |
| `RAZORPAY_KEY_SECRET` | string  | Yes      | Your Razorpay API key secret                                |
| `LOG_FILE`            | string  | No       | Path to log file for server logs                            |
| `TOOLSETS`            | string  | No       | Comma-separated list of toolsets to enable (default: `all`) |
| `READ_ONLY`           | boolean | No       | Run server in read-only mode (default: `false`)             |

## Command Line Flags

When running the Local MCP Server binary directly, you can use the following command line flags:

| Flag (Short)        | Description                                |
| ------------------- | ------------------------------------------ |
| `--key` (`-k`)      | Your Razorpay API key ID                   |
| `--secret` (`-s`)   | Your Razorpay API key secret               |
| `--log-file` (`-l`) | Path to log file                           |
| `--toolsets` (`-t`) | Comma-separated list of toolsets to enable |
| `--read-only`       | Enable read-only mode                      |

## Related Information

* [Use Cases](/docs/mcp-server/use-cases)
* [Tools Reference](/docs/mcp-server/tools-reference)
* [FAQs](/docs/mcp-server/faqs)
