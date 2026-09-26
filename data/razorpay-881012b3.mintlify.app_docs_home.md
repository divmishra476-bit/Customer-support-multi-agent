> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Documentation

> Explore Razorpay's documentation for Payments, POS, Banking Plus, Partners and Developer Tools.

export const HomeFooter = ({cc = "IN"}) => {
  const ASSETS = "/static/docs-home/assets";
  const ACCEPT = {
    IN: [{
      href: "/docs/payments/payment-gateway",
      label: "Payment Gateway"
    }, {
      href: "/docs/payments/payment-pages",
      label: "Payment Pages"
    }, {
      href: "/docs/payments/payment-links",
      label: "Payment Links"
    }, {
      href: "/docs/payments/subscriptions",
      label: "Subscriptions"
    }, {
      href: "/docs/payments/smart-collect",
      label: "Smart Collect"
    }, {
      href: "/docs/payments/qr-codes",
      label: "QR Codes"
    }],
    SG: [{
      href: "/docs/sg/payments/payment-gateway",
      label: "Payment Solutions"
    }, {
      href: "/docs/sg/payments/payment-links",
      label: "Payment Links"
    }],
    US: [{
      href: "/docs/us/payments/payment-gateway",
      label: "Payment Solutions"
    }]
  };
  return <footer className="rzpn-footer" id="footer-rzpn">
      <div className="rzpn-foot-body">
        <div className="rzpn-foot-cols">
          <div className="rzpn-foot-about">
            <div className="rzpn-foot-lockup">
              <img className="rzpn-foot-logo" src={`${ASSETS}/logo.svg`} alt="Razorpay" />
              <img className="rzpn-foot-docs" src={`${ASSETS}/logo-docs.svg`} alt="Docs" />
            </div>
            <p className="rzpn-foot-blurb">Everything you need to accept payments, move money and reconcile it — with the API reference, SDKs and integration guides behind each one.</p>
          </div>
          <div className="rzpn-foot-col">
            <div className="rzpn-foot-links">
              <p className="rzpn-foot-col-title">Accept Payments</p>
              {ACCEPT[cc].map(l => <a href={l.href} key={l.href}>{l.label}</a>)}
            </div>
            {cc === "IN" && <div className="rzpn-foot-links">
                <p className="rzpn-foot-col-title">Banking Plus</p>
                <a href="/docs/x">RazorpayX</a>
                <a href="/docs/x/account-types">Current Accounts</a>
                <a href="/docs/x/payouts">Payouts</a>
                <a href="/docs/x/payout-links">Payout Links</a>
                <a href="https://razorpay.com/corporate-cards/" target="_blank" rel="noreferrer">Corporate Credit Card</a>
                <a href="https://razorpay.com/payroll/" target="_blank" rel="noreferrer">Payroll</a>
              </div>}
          </div>
          <div className="rzpn-foot-col">
            <div className="rzpn-foot-links">
              <p className="rzpn-foot-col-title">Developers</p>
              <a href="/docs">Docs</a>
              <a href="/docs/api">API Reference</a>
              <a href="https://razorpay.com/integrations/" target="_blank" rel="noreferrer">Integrations</a>
              <a href="/docs/payments/server-integration">SDKs</a>
              <a href="/docs/webhooks">Webhooks</a>
              <a href="https://razorpay.com/docs/api-postman-collections/" target="_blank" rel="noreferrer">Postman Collections</a>
            </div>
            <div className="rzpn-foot-links">
              <p className="rzpn-foot-col-title">Resources</p>
              <a href="https://razorpay.com/blog/" target="_blank" rel="noreferrer">Blog</a>
              <a href="https://razorpay.com/learn/" target="_blank" rel="noreferrer">Learn</a>
              <a href="/docs/payments/settlements">Settlement Guide</a>
            </div>
          </div>
          <div className="rzpn-foot-col">
            <div className="rzpn-foot-links">
              <p className="rzpn-foot-col-title">Company</p>
              <a href="https://razorpay.com/about/" target="_blank" rel="noreferrer">About Us</a>
              <a href="https://razorpay.com/jobs/" target="_blank" rel="noreferrer">Careers</a>
              <a href="/docs/partners">Partners</a>
              <a href="https://razorpay.com/corporate-information/" target="_blank" rel="noreferrer">Corporate Information</a>
              <a href="https://razorpay.com/responsible-disclosure/" target="_blank" rel="noreferrer">Responsible Disclosure</a>
            </div>
            <div className="rzpn-foot-links">
              <p className="rzpn-foot-col-title">Help & Support</p>
              <a href="https://razorpay.com/support/" target="_blank" rel="noreferrer">Support</a>
              <a href="https://status.razorpay.com/" target="_blank" rel="noreferrer">Status Page</a>
            </div>
          </div>
        </div>
        <div className="rzpn-foot-bottom">
          <div className="rzpn-foot-legalese">
            <p>© Razorpay 2026. All rights reserved.</p>
            <p className="rzpn-foot-rbi">Razorpay Payments Private Limited is an RBI Authorised Payment Aggregator.</p>
          </div>
          <div className="rzpn-foot-legal">
            <a href="https://razorpay.com/terms/" target="_blank" rel="noreferrer">Terms of Use</a>
            <a href="https://razorpay.com/privacy/" target="_blank" rel="noreferrer">Privacy Policy</a>
          </div>
        </div>
      </div>
    </footer>;
};

export const HomeAgents = ({onCopy}) => {
  const ASSETS = "/static/docs-home/assets";
  return <section className="rzpn-agents">
      <div className="rzpn-agents-stage">
        <h2 className="rzpn-agents-h">Build with Agents</h2>

        <div className="rzpn-agents-panel">
          <div className="rzpn-agents-term">
            <div className="rzpn-agents-term-head"><span>Ask your AI</span></div>
            <div className="rzpn-agents-term-body">
              <img className="rzpn-agents-glow" src={`${ASSETS}/agents-glow.svg`} alt="" aria-hidden="true" />
              <div className="rzpn-agents-row">
                <span className="rzpn-agents-cmdwrap">
                  <span className="rzpn-agents-key">CLI</span>
                  <code className="rzpn-agents-cmd">curl -fsSL https://razorpay.com/cli/latest/<wbr />install.sh | bash</code>
                </span>
                <button type="button" className="rzpn-agents-copy" onClick={onCopy("curl -fsSL https://razorpay.com/cli/latest/install.sh | bash")}>
                  <img src={`${ASSETS}/agents-copy.svg`} width="16" height="16" alt="" /><span data-rzpn-copy-label>Copy</span>
                </button>
              </div>
              <hr className="rzpn-agents-line" />
              <div className="rzpn-agents-row">
                <span className="rzpn-agents-cmdwrap">
                  <span className="rzpn-agents-key">MCP</span>
                  <code className="rzpn-agents-cmd">Install the Razorpay MCP server: https://mcp.razorpay.com/<wbr />mcp</code>
                </span>
                <button type="button" className="rzpn-agents-copy" onClick={onCopy("Install the Razorpay MCP server: https://mcp.razorpay.com/mcp")}>
                  <img src={`${ASSETS}/agents-copy.svg`} width="16" height="16" alt="" /><span data-rzpn-copy-label>Copy</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <div className="rzpn-agents-aside">
          <div className="rzpn-agents-aside-item">
            <p>Razorpay CLI</p>
            <a className="rzpn-agents-link" href="/docs/cli">View setup<span className="rzpn-agents-ico rzpn-agents-ico--arrow" aria-hidden="true" /></a>
          </div>
          <div className="rzpn-agents-aside-item">
            <p>Razorpay MCP</p>
            <a className="rzpn-agents-link" href="/docs/mcp-server">View setup<span className="rzpn-agents-ico rzpn-agents-ico--arrow" aria-hidden="true" /></a>
          </div>
          <div className="rzpn-agents-aside-item">
            <p>Are you an LLM agent?</p>
            <a className="rzpn-agents-link" href="/docs/llms.txt">Read llms.txt<span className="rzpn-agents-ico rzpn-agents-ico--doc" aria-hidden="true" /></a>
          </div>
        </div>
      </div>
    </section>;
};

export const HomePartners = () => {
  const ASSETS = "/static/docs-home/assets";
  return <section className="rzpn-section rzpn-section--partners">
      <div className="rzpn-wrap">
        <hr className="rzpn-rule" />
        <div className="rzpn-block">
          <h2 className="rzpn-h2">Partners</h2>
          <div className="rzpn-block-aside">
            <p>The Razorpay Partner Program is a referral program through which you can offer the Razorpay product suite to your customers and get monetary rewards.</p>
            <a className="rzpn-link" href="/docs/partners">Explore Partner Program<img src={`${ASSETS}/link-arrow.svg`} width="12" height="12" alt="" /></a>
          </div>
        </div>
        <div className="rzpn-grid rzpn-grid--peach">
          {[{
    icon: "rzpn-i-code",
    title: "Embedded payments",
    desc: "Offer payments inside your own product, as a native feature of your platform.",
    href: "/docs/partners/technology-partners/embedded-payments"
  }, {
    icon: "rzpn-i-useradd",
    title: "Sub-merchants",
    desc: "Bring merchants onto Razorpay and manage their onboarding.",
    href: "/docs/partners/aggregators"
  }, {
    icon: "rzpn-i-tag",
    title: "White-label",
    desc: "Resell the full payments stack under your own brand and your own pricing.",
    href: "/docs/partners"
  }, {
    icon: "rzpn-i-split",
    title: "Route splits",
    desc: "Onboard sellers and split payments across their accounts.",
    href: "/docs/payments/route"
  }].map(c => <a className="rzpn-card" href={c.href} key={c.title}>
              <span className="rzpn-dot"><svg className="rzpn-dot-ico" aria-hidden="true"><use href={`#${c.icon}`} /></svg></span>
              <h3><span className="rzpn-u">{c.title}</span></h3>
              <p>{c.desc}</p>
            </a>)}
        </div>
      </div>
    </section>;
};

export const HomeBanking = () => {
  const ASSETS = "/static/docs-home/assets";
  return <section className="rzpn-section rzpn-section--banking">
      <div className="rzpn-wrap">
        <div className="rzpn-block">
          <h2 className="rzpn-h2">Banking plus</h2>
          <div className="rzpn-block-aside">
            <p>Manage your company's finances with a Business Banking Hub. It helps business owners and finance teams automate financial task and provide insights into money flow.</p>
            <a className="rzpn-link" href="/docs/x">Explore Banking Plus<img src={`${ASSETS}/link-arrow.svg`} width="12" height="12" alt="" /></a>
          </div>
        </div>
        <div className="rzpn-grid rzpn-grid--green">
          {[{
    icon: "rzpn-i-send",
    title: "Send a payout",
    desc: "Transfer funds to any bank account or UPI ID.",
    href: "/docs/x/payouts"
  }, {
    icon: "rzpn-i-link",
    title: "Share a payout link",
    desc: "Let recipients claim a payout themselves.",
    href: "/docs/x/payout-links"
  }, {
    icon: "rzpn-i-store",
    title: "Pay a vendor",
    desc: "Automate recurring vendor payments.",
    href: "/docs/x/vendor-payments"
  }, {
    icon: "rzpn-i-users",
    title: "Run payroll",
    desc: "Pay salaries to your entire team in one batch.",
    href: "/docs/payroll"
  }, {
    icon: "rzpn-i-receipt",
    title: "Pay business taxes",
    desc: "Settle GST and other statutory dues on time.",
    href: "/docs/x/tax-payments"
  }, {
    icon: "rzpn-i-card",
    title: "Issue corporate cards",
    desc: "Give employees controlled spending cards.",
    href: "/docs/x/capital/corporate-cards"
  }, {
    icon: "rzpn-i-check",
    title: "Reconcile money out",
    desc: "Match every payout against your books.",
    href: "/docs/x/payouts"
  }].map(c => <a className="rzpn-card" href={c.href} key={c.title}>
              <span className="rzpn-dot"><svg className="rzpn-dot-ico" aria-hidden="true"><use href={`#${c.icon}`} /></svg></span>
              <h3><span className="rzpn-u">{c.title}</span></h3>
              <p>{c.desc}</p>
            </a>)}
        </div>
      </div>
    </section>;
};

export const HomePOS = () => {
  const ASSETS = "/static/docs-home/assets";
  return <section className="rzpn-section rzpn-section--pos">
      <div className="rzpn-wrap">
        <hr className="rzpn-rule" />
        <div className="rzpn-pos">
          <div className="rzpn-pos-copy">
            <h2 className="rzpn-h2">POS</h2>
            <p className="rzpn-pos-sub">Accept payments<br />in person</p>
          </div>
          <div className="rzpn-pos-art" aria-hidden="true">
            <div className="rzpn-pos-window rzpn-win rzpn-win--soft">
              <span className="rzpn-win-tint rzpn-pos-tint" />
            </div>
            <img className="rzpn-pos-device" src={`${ASSETS}/pos-device.png`} alt="" />
          </div>
          <div className="rzpn-pos-aside-anchor">
            <div className="rzpn-pos-aside">
              <p>Razorpay POS is a point-of-sale payment solution that enables businesses to accept payments using UPI, credit and debit cards, wallets, EMI and more.</p>
              <a className="rzpn-link" href="https://accounts.razorpay.com/auth/?redirecturl=https://easy.razorpay.com&amp;auth_intent=signup&amp;x-country-code=IN">Know how to sign up for POS<img src={`${ASSETS}/link-arrow.svg`} width="12" height="12" alt="" /></a>
              <a className="rzpn-link" href="/docs/pos">Explore more<img src={`${ASSETS}/link-arrow.svg`} width="12" height="12" alt="" /></a>
            </div>
          </div>
        </div>
        <hr className="rzpn-rule" />
      </div>
    </section>;
};

export const HomePayments = ({cc = "IN"}) => {
  const ASSETS = "/static/docs-home/assets";
  const STEPS = {
    IN: [{
      num: "01",
      name: "Build",
      cards: [{
        icon: "rzpn-i-card",
        title: "Payment products",
        desc: "Compare Payment Gateway, Links and Pages, then pick your fit.",
        href: "/docs/payments/payment-gateway"
      }, {
        icon: "rzpn-i-cart",
        title: "Ecommerce plugins",
        desc: "Add Razorpay to Shopify, WooCommerce or Magento — no code.",
        href: "/docs/payments/payment-gateway/ecommerce-plugins"
      }, {
        icon: "rzpn-i-zap",
        title: "Webhooks",
        desc: "Get notified on every event, and keep your handler idempotent.",
        href: "/docs/webhooks"
      }]
    }, {
      num: "02",
      name: "Go live",
      cards: [{
        icon: "rzpn-i-beaker",
        title: "Test mode",
        desc: "Run the full payment lifecycle on test keys and test cards.",
        href: "/docs/payments/dashboard/test-live-modes"
      }, {
        icon: "rzpn-i-alert",
        title: "Payment states",
        desc: "Follow an order from created to captured, and decode failures.",
        href: "/docs/payments/payments#payment-life-cycle"
      }, {
        icon: "rzpn-i-power",
        title: "Activation",
        desc: "Finish KYC, swap test keys for live keys, take real payments.",
        href: "/docs/payments/dashboard/account-settings/activation-details"
      }]
    }, {
      num: "03",
      name: "Grow",
      cards: [{
        icon: "rzpn-i-repeat",
        title: "Settlements",
        desc: "Match each payout to its transactions, or settle instantly.",
        href: "/docs/payments/settlements"
      }, {
        icon: "rzpn-i-undo",
        title: "Refunds & disputes",
        desc: "Issue instant refunds and answer chargebacks before the deadline.",
        href: "/docs/payments/refunds"
      }, {
        icon: "rzpn-i-trend",
        title: "Optimizer",
        desc: "Route across gateways and tune checkout to lift success rate.",
        href: "/docs/payments/optimizer"
      }]
    }],
    SG: [{
      num: "01",
      name: "Build",
      cards: [{
        icon: "rzpn-i-card",
        title: "Payment products",
        desc: "Compare Payment Gateway, Links and Pages, then pick your fit.",
        href: "/docs/sg/payments/payment-gateway"
      }, {
        icon: "rzpn-i-cart",
        title: "Ecommerce plugins",
        desc: "Add Razorpay to Shopify, WooCommerce or Magento — no code.",
        href: "/docs/sg/payments/payment-gateway/ecommerce-plugins"
      }, {
        icon: "rzpn-i-zap",
        title: "Webhooks",
        desc: "Get notified on every event, and keep your handler idempotent.",
        href: "/docs/sg/webhooks"
      }]
    }, {
      num: "02",
      name: "Go live",
      cards: [{
        icon: "rzpn-i-beaker",
        title: "Test mode",
        desc: "Run the full payment lifecycle on test keys and test cards.",
        href: "/docs/sg/payments/dashboard/test-live-modes"
      }, {
        icon: "rzpn-i-alert",
        title: "Payment states",
        desc: "Follow an order from created to captured, and decode failures.",
        href: "/docs/sg/payments/payments#payment-life-cycle"
      }]
    }, {
      num: "03",
      name: "Grow",
      cards: [{
        icon: "rzpn-i-repeat",
        title: "Settlements",
        desc: "Match each payout to its transactions and keep your books clean.",
        href: "/docs/sg/payments/settlements"
      }, {
        icon: "rzpn-i-undo",
        title: "Refunds & disputes",
        desc: "Issue instant refunds and answer chargebacks before the deadline.",
        href: "/docs/sg/payments/refunds"
      }, {
        icon: "rzpn-i-trend",
        title: "Subscriptions",
        desc: "Bill customers on a schedule with automatic retries.",
        href: "/docs/sg/payments/subscriptions"
      }]
    }],
    US: [{
      num: "01",
      name: "Build",
      cards: [{
        icon: "rzpn-i-card",
        title: "Payment products",
        desc: "Compare Payment Gateway, Links and Pages, then pick your fit.",
        href: "/docs/us/payments/payment-gateway"
      }, {
        icon: "rzpn-i-cart",
        title: "Ecommerce plugins",
        desc: "Add Razorpay to Shopify, WooCommerce or Magento — no code.",
        href: "/docs/us/payments/payment-gateway/ecommerce-plugins"
      }, {
        icon: "rzpn-i-zap",
        title: "Webhooks",
        desc: "Get notified on every event, and keep your handler idempotent.",
        href: "/docs/us/webhooks"
      }]
    }, {
      num: "02",
      name: "Go live",
      cards: [{
        icon: "rzpn-i-beaker",
        title: "Test mode",
        desc: "Run the full payment lifecycle on test keys and test cards.",
        href: "/docs/us/payments/dashboard/test-live-modes"
      }, {
        icon: "rzpn-i-alert",
        title: "Payment states",
        desc: "Follow an order from created to captured, and decode failures.",
        href: "/docs/us/payments/payments#payment-life-cycle"
      }]
    }, {
      num: "03",
      name: "Grow",
      cards: [{
        icon: "rzpn-i-repeat",
        title: "Settlements",
        desc: "Match each payout to its transactions and keep your books clean.",
        href: "/docs/us/payments/settlements"
      }, {
        icon: "rzpn-i-undo",
        title: "Refunds & disputes",
        desc: "Issue instant refunds and answer chargebacks before the deadline.",
        href: "/docs/us/payments/refunds"
      }, {
        icon: "rzpn-i-trend",
        title: "Subscriptions",
        desc: "Bill customers on a schedule with automatic retries.",
        href: "/docs/us/payments/subscriptions"
      }]
    }]
  };
  return <section className="rzpn-section rzpn-section--payments">
      <div className="rzpn-wrap">
        <hr className="rzpn-rule" />
        <div className="rzpn-block">
          <h2 className="rzpn-h2">Payments</h2>
          <div className="rzpn-block-aside">
            <p>Cards, UPI, netbanking, wallets, and EMI — a single Payments API that adapts to how your customers want</p>
            <a className="rzpn-link" href="/docs/payments">Know more <img src={`${ASSETS}/link-arrow.svg`} width="12" height="12" alt="" /></a>
          </div>
        </div>

        <p className="rzpn-steps-lead">Explore payments step by step</p>

        <div className="rzpn-steps">
          {STEPS[cc].map(step => <div className="rzpn-step rzpn-win rzpn-win--soft" key={step.num}>
              <span className="rzpn-win-tint rzpn-step-tint" aria-hidden="true" />
              <div className="rzpn-step-label"><span className="rzpn-step-num">{step.num}</span><span className="rzpn-step-name">{step.name}</span></div>
              <div className="rzpn-step-cards">
                {step.cards.map(c => <a className="rzpn-card" href={c.href} key={c.title}>
                    <span className="rzpn-dot"><svg className="rzpn-dot-ico" aria-hidden="true"><use href={`#${c.icon}`} /></svg></span>
                    <h3><span className="rzpn-u">{c.title}</span></h3>
                    <p>{c.desc}</p>
                  </a>)}
              </div>
            </div>)}
        </div>
      </div>
    </section>;
};

export const HomeAICards = ({onCopyPrompt, onCopy, cc = "IN"}) => {
  const ASSETS = "/static/docs-home/assets";
  const intl = cc !== "IN";
  const DOCS = intl ? `/docs/${cc.toLowerCase()}` : "/docs";
  return <section className="rzpn-ai">
      <div className="rzpn-wrap">
        <div className="rzpn-ai-head">
          <h2 className="rzpn-eyebrow">Integrate Razorpay using AI</h2>
          <span className="rzpn-ai-agents">
            <span className="rzpn-ai-agent"><img src={`${ASSETS}/agent-1.png`} alt="Claude" /></span>
            <span className="rzpn-ai-agent"><img src={`${ASSETS}/agent-2.png`} alt="OpenAI" /></span>
            <span className="rzpn-ai-agent rzpn-ai-agent--3"><img src={`${ASSETS}/agent-3-mark.png`} alt="Cursor" /></span>
          </span>
        </div>

        <div className="rzpn-ai-cards">
          {[{
    img: intl ? "asset-6.png" : "asset-1.svg",
    title: "Accept payment online on website",
    promptFile: "website-checkout.txt",
    href: `${DOCS}/payments/payment-gateway/web-integration/standard`
  }, {
    img: "asset-2.svg",
    title: "Accept payment online on mobile",
    promptFile: "mobile-checkout.txt",
    href: `${DOCS}/payments/payment-gateway/android-integration/standard`
  }, {
    img: intl ? "asset-7.svg" : "asset-3.svg",
    title: "Setup recurring billing",
    promptFile: "subscriptions.txt",
    href: `${DOCS}/payments/subscriptions`
  }, {
    img: intl ? "asset-8.svg" : "asset-4.svg",
    title: "Issue invoices to your customers",
    promptFile: "invoice.txt",
    href: intl ? `${DOCS}/api/payments/invoices` : `${DOCS}/payments/invoices`
  }, {
    img: "asset-5.svg",
    title: "Generate payment link",
    promptFile: "payment-link.txt",
    href: `${DOCS}/payments/payment-links/create`
  }].map(c => <article className="rzpn-pcard" key={c.img}>
              <div className="rzpn-pcard-media rzpn-win rzpn-win--soft">
                <span className="rzpn-win-tint rzpn-pcard-tint" aria-hidden="true" />
                <div className="rzpn-pcard-shot">
                  <img src={`${ASSETS}/${c.img}`} alt="" />
                </div>
              </div>
              <div className="rzpn-pcard-body">
                <h3 className="rzpn-pcard-title"><a className="rzpn-pcard-link" href={c.href}><span className="rzpn-u">{c.title}</span></a></h3>
                <button type="button" className="rzpn-pcard-pill" onClick={c.promptFile ? onCopyPrompt(c.promptFile) : onCopy(c.prompt)}>
                  <span className="rzpn-copy-ico" aria-hidden="true" />
                  <span data-rzpn-copy-label>Copy prompt</span>
                </button>
              </div>
            </article>)}
        </div>

        <hr className="rzpn-rule rzpn-ai-rule" />

        <div className="rzpn-devrow">
          <div className="rzpn-devtools">
            <h2 className="rzpn-eyebrow">Developer tools</h2>
            <div className="rzpn-devcards">
              {[{
    icon: "rzpn-i-book",
    label: "API Reference",
    href: "/docs/api"
  }, {
    icon: "rzpn-i-zap",
    label: "Webhooks",
    href: "/docs/webhooks"
  }, {
    icon: "rzpn-i-package",
    label: "SDK",
    href: "/docs/payments/server-integration"
  }, {
    icon: "rzpn-i-terminal",
    label: "CLI",
    href: "/docs/cli"
  }, {
    icon: "rzpn-i-plug",
    label: "MCP",
    href: "/docs/mcp-server"
  }, {
    icon: "rzpn-i-alert",
    label: "Error codes",
    href: "/docs/errors"
  }].map(t => <a className="rzpn-devcard" href={t.href} key={t.label}>
                  <svg className="rzpn-devcard-ico" aria-hidden="true"><use href={`#${t.icon}`} /></svg>
                  <span className="rzpn-u">{t.label}</span>
                </a>)}
            </div>
          </div>
        </div>
      </div>
    </section>;
};

export const HomeHero = ({children}) => {
  const ART = "/static/docs-home/assets";
  const IconAskSpark = () => <svg className="rzpn-ask-spark" preserveAspectRatio="none" overflow="visible" style={{
    display: "block"
  }} width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">

      <g opacity="0.6">
        <path d="M6 5.5C6 5.22386 5.77614 5 5.5 5C5.22386 5 5 5.22386 5 5.5C5 6.48063 4.78279 7.0726 4.4277 7.4277C4.0726 7.78279 3.48063 8 2.5 8C2.22386 8 2 8.22386 2 8.5C2 8.77614 2.22386 9 2.5 9C3.48063 9 4.0726 9.21721 4.4277 9.5723C4.78279 9.9274 5 10.5194 5 11.5C5 11.7761 5.22386 12 5.5 12C5.77614 12 6 11.7761 6 11.5C6 10.5194 6.21721 9.9274 6.5723 9.5723C6.9274 9.21721 7.51937 9 8.5 9C8.77614 9 9 8.77614 9 8.5C9 8.22386 8.77614 8 8.5 8C7.51937 8 6.9274 7.78279 6.5723 7.4277C6.21721 7.0726 6 6.48063 6 5.5Z" fill="#2F404C" />
        <path d="M11 1.5C11 1.22386 10.7761 1 10.5 1C10.2239 1 10 1.22386 10 1.5C10 2.13341 9.85918 2.47538 9.66728 2.66728C9.47538 2.85918 9.13341 3 8.5 3C8.22386 3 8 3.22386 8 3.5C8 3.77614 8.22386 4 8.5 4C9.13341 4 9.47538 4.14082 9.66728 4.33272C9.85918 4.52462 10 4.86659 10 5.5C10 5.77614 10.2239 6 10.5 6C10.7761 6 11 5.77614 11 5.5C11 4.86659 11.1408 4.52462 11.3327 4.33272C11.5246 4.14082 11.8666 4 12.5 4C12.7761 4 13 3.77614 13 3.5C13 3.22386 12.7761 3 12.5 3C11.8666 3 11.5246 2.85918 11.3327 2.66728C11.1408 2.47538 11 2.13341 11 1.5Z" fill="#2F404C" />
        <path fillRule="evenodd" clipRule="evenodd" d="M21 15C15.4444 15 13 17.4444 13 23C13 17.4444 10.5556 15 5 15C10.5556 15 13 12.5556 13 7C13 12.5556 15.4444 15 21 15Z" stroke="#2F404C" strokeWidth="1.5" strokeLinejoin="round" />
      </g>
    </svg>;
  const IconAskArrow = () => <svg preserveAspectRatio="none" overflow="visible" style={{
    display: "block"
  }} width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g>
        <path d="M18.6641 7.66699L26.9972 16.0002L18.6641 24.3333" stroke="#626368" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
        <path d="M26 16.0005H5" stroke="#626368" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
      </g>
    </svg>;
  const openSearch = () => {
    const el = document.getElementById("search-bar-entry") || document.querySelector('[data-testid="search-bar-entry"], [id*="search-bar"], button[aria-label*="earch"]');
    if (el) el.click();
  };
  return <section className="rzpn-hero rzpn-win">
      {children}

      <div className="rzpn-art" aria-hidden="true">
        <div className="rzpn-art-strip">
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    height: "330.5px",
    left: "882.452px",
    top: "119px",
    width: "488px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/7a7e9fe79b4cb82d0d357e287634a441fa93b6cc.svg`} />
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    display: "flex",
    height: "179px",
    alignItems: "center",
    justifyContent: "center",
    left: "1272.548px",
    top: "89px",
    width: "173.441px"
  }}>
            <div style={{
    flex: "none",
    transform: "rotate(-17.27deg)"
  }}>
              <div style={{
    position: "relative",
    height: "145px",
    width: "136.553px"
  }}>
                <div style={{
    position: "absolute",
    inset: "-22.07% -23.43% -22.07% -23.43%"
  }}>
                  <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/1e897b9e57be77f917c1393358fd6380cffb2636.svg`} />
                </div>
              </div>
            </div>
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    height: "293.283px",
    left: "862.742px",
    top: "139px",
    width: "191.794px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/1092d80c2c3f78c095b88d79bca0e14ed73a9a7d.svg`} />
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    height: "132px",
    left: "855.952px",
    top: "235px",
    width: "128.5px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/f52c9a7b162659065297c358828193ea6e56155e.svg`} />
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    height: "206.478px",
    left: "663.958px",
    top: "137.51px",
    width: "391.619px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/e9111091b8a1304bd80140f2efea28e2f661e9ca.svg`} />
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    display: "flex",
    height: "128.569px",
    alignItems: "center",
    justifyContent: "center",
    left: "700.61px",
    top: "174.716px",
    width: "113.228px"
  }}>
            <div style={{
    flex: "none",
    transform: "rotate(40.51deg)"
  }}>
              <div style={{
    position: "relative",
    height: "155.01px",
    width: "16.492px"
  }}>
                <div style={{
    position: "absolute",
    inset: "-28.39% -266.79%"
  }}>
                  <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/v42-highlight-new2.svg`} />
                </div>
              </div>
            </div>
          </div>

          <div className="rzpn-doc-6-badge" style={{
    position: "absolute",
    height: "73.938px",
    left: "689.141px",
    top: "76.679px",
    width: "75.636px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/doc6-a11d8814.svg`} />
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    height: "333.162px",
    left: "662.548px",
    top: "-13.66px",
    width: "889px"
  }}>
            <div style={{
    position: "absolute",
    inset: "0 0 0 0.14%"
  }}>
              <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/e417b2a6-8998-4490-8d68-5027e9a3fe84.svg`} />
            </div>
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    height: "726.691px",
    left: "-21px",
    top: "233.788px",
    width: "1537.928px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/v42-strip-longest-v1.svg`} />
          </div>
          <div className="rzpn-strip-piece" style={{
    position: "absolute",
    height: "139.5px",
    left: "983.548px",
    top: "245.5px",
    width: "131.5px"
  }}>
            <div style={{
    position: "absolute",
    inset: "-7.17% -7.6% -7.17% -7.6%"
  }}>
              <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/da7cac6a82b28c195f90f3108713c17478a6721f.svg`} />
            </div>
          </div>
        </div>
        <div className="rzpn-art-ascii"><canvas className="rzpn-flow"></canvas></div>
        <div className="rzpn-doc rzpn-doc-3">
          <div style={{
    position: "absolute",
    height: "116.283px",
    left: "1239.99px",
    top: "17px",
    width: "117.989px",
    transform: "translateX(-50%)"
  }}>
            <div style={{
    position: "absolute",
    inset: "0 -9.6% 0 -8.09%"
  }}>
              <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/9903a8fc1b507184da7b9e26f77459d0f4946469.svg`} />
            </div>
          </div>
        </div>
        <div className="rzpn-doc rzpn-doc-4">
          <div style={{
    position: "absolute",
    display: "flex",
    height: "51.984px",
    alignItems: "center",
    justifyContent: "center",
    left: "1085.698px",
    top: "60.39px",
    width: "52.733px",
    transform: "translateX(-50%)"
  }}>
            <div style={{
    flex: "none",
    transform: "rotate(-0.45deg)"
  }}>
              <div style={{
    position: "relative",
    height: "51.572px",
    width: "52.327px"
  }}>
                <div style={{
    position: "absolute",
    inset: "0 -9.6% 0 -8.09%"
  }}>
                  <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/0aa2b4deece40c040f843d1ccdf8857b5f6233d1.svg`} />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="rzpn-doc rzpn-doc-5">
          <div style={{
    position: "absolute",
    height: "99.862px",
    left: "1005px",
    top: "158.994px",
    width: "83px"
  }}>
            <div style={{
    position: "absolute",
    inset: "-0.07% -13.86%"
  }}>
              <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/v42-doc5-ref-flat.svg`} />
            </div>
          </div>
        </div>
        <div className="rzpn-doc rzpn-doc-1">
          <div style={{
    position: "absolute",
    height: "149.675px",
    left: "1146.898px",
    top: "167.98px",
    width: "137.102px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/v42-doc1-code-flat.svg`} />
          </div>
        </div>
        <div className="rzpn-doc rzpn-doc-2">
          <div style={{
    position: "absolute",
    height: "165.271px",
    left: "782.07px",
    top: "94.68px",
    width: "157.466px"
  }}>
            <img alt="" style={{
    position: "absolute",
    display: "block",
    inset: 0,
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/doc2-5227a479.svg`} />
          </div>
        </div>
        <div className="rzpn-doc rzpn-doc-7">
          <div style={{
    position: "absolute",
    display: "flex",
    height: "179px",
    alignItems: "center",
    justifyContent: "center",
    left: "576.522px",
    top: "87.16px",
    width: "173.441px"
  }}>
            <div style={{
    flex: "none",
    transform: "rotate(-17.27deg)"
  }}>
              <div style={{
    position: "relative",
    height: "145px",
    width: "136.553px"
  }}>
                <div style={{
    position: "absolute",
    inset: "-87.52% -92.93% -87.52% -92.93%"
  }}>
                  <img alt="" style={{
    display: "block",
    maxWidth: "none",
    width: "100%",
    height: "100%"
  }} src={`${ART}/0df27521db41988910812de3b884b6ed892400a6.svg`} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="rzpn-hero-inner">
        <h1 className="rzpn-hero-h1">Just ask the docs</h1>
        <form className="rzpn-ask" onSubmit={e => {
    e.preventDefault();
    openSearch();
  }} onMouseDown={e => {
    e.preventDefault();
    e.stopPropagation();
  }} onMouseUp={e => {
    e.preventDefault();
    e.stopPropagation();
    openSearch();
  }} onClick={e => {
    e.preventDefault();
    e.stopPropagation();
  }}>
          <IconAskSpark />
          <span className="rzpn-ask-field">
            <input className="rzpn-ask-input" type="text" placeholder="Ask AI anything about docs, APIs…" aria-label="Ask AI anything about docs, APIs" readOnly tabIndex={-1} />
            <span className="rzpn-ask-ph" aria-hidden="true">Ask AI anything about docs, APIs…</span>
          </span>
          <button type="button" className="rzpn-ask-go" aria-label="Ask">
            <IconAskArrow />
          </button>
        </form>
      </div>
    </section>;
};

export const HomeNav = ({cc = "IN"}) => {
  const ASSETS = "/static/docs-home/assets";
  const prefix = ({
    IN: "",
    SG: "sg",
    US: "us"
  })[cc] || "";
  const L = h => prefix ? `/docs/${prefix}${h.slice(5)}` : h;
  const NAV_LINKS = [{
    href: "/docs/payments",
    label: "Payments"
  }, {
    href: "/docs/x",
    label: "Banking+",
    only: ["IN"]
  }, {
    href: "/docs/payroll",
    label: "Payroll",
    overflow: true,
    only: ["IN"]
  }, {
    href: "/docs/engage",
    label: "Engage",
    overflow: true,
    only: ["IN"]
  }, {
    href: "/docs/pos",
    label: "POS",
    overflow: true,
    only: ["IN"]
  }, {
    href: "/docs/partners",
    label: "Partners",
    overflow: true,
    only: ["IN"]
  }, {
    href: "/docs/api",
    label: "API Reference",
    overflow: true
  }, {
    href: "/docs/developer-tools",
    label: "Developer Tools",
    dd: true
  }];
  const shown = NAV_LINKS.filter(l => !l.only || l.only.includes(cc));
  const DEV_TOOLS = [{
    icon: "rzpn-i-book",
    label: "API Reference",
    href: "/docs/api"
  }, {
    icon: "rzpn-i-zap",
    label: "Webhooks",
    href: "/docs/webhooks"
  }, {
    icon: "rzpn-i-package",
    label: "SDK",
    href: "/docs/payments/server-integration"
  }, {
    icon: "rzpn-i-terminal",
    label: "CLI",
    href: "/docs/cli"
  }, {
    icon: "rzpn-i-plug",
    label: "MCP",
    href: "/docs/mcp-server"
  }, {
    icon: "rzpn-i-alert",
    label: "Error codes",
    href: "/docs/errors"
  }];
  const IN_HOME = {
    cc: "IN",
    flag: "in",
    label: "India",
    href: "/docs/home"
  };
  const OTHER_HOMES = [{
    cc: "MY",
    flag: "my",
    label: "Malaysia",
    href: "https://curlec.com/docs/home"
  }, {
    cc: "SG",
    flag: "sg",
    label: "Singapore",
    href: "/docs/sg/home"
  }, {
    cc: "US",
    flag: "us",
    label: "United States",
    href: "/docs/us/home"
  }];
  const currentHome = cc === "IN" ? IN_HOME : OTHER_HOMES.find(c => c.cc === cc) || IN_HOME;
  const menuHomes = OTHER_HOMES.map(c => c.cc === cc ? IN_HOME : c);
  const openSearch = () => {
    const el = document.getElementById("search-bar-entry") || document.querySelector('[data-testid="search-bar-entry"], [id*="search-bar"], button[aria-label*="earch"]');
    if (el) el.click();
  };
  const setBurgerOpen = open => {
    const menu = document.getElementById("rzpn-nav-menu");
    const btn = document.querySelector("#page-rzpn .rzpn-nav-burger");
    if (!menu || !btn) return;
    if (open) menu.removeAttribute("hidden"); else menu.setAttribute("hidden", "");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.classList.toggle("is-open", open);
  };
  const onBurgerClick = e => {
    e.stopPropagation();
    const menu = document.getElementById("rzpn-nav-menu");
    if (!menu) return;
    setBurgerOpen(menu.hasAttribute("hidden"));
  };
  const setMoreOpen = open => {
    const menu = document.getElementById("rzpn-nav-more-menu");
    const btn = document.querySelector("#page-rzpn .rzpn-nav-more-btn");
    if (!menu || !btn) return;
    if (open) menu.removeAttribute("hidden"); else menu.setAttribute("hidden", "");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.classList.toggle("is-open", open);
  };
  const onMoreClick = e => {
    e.stopPropagation();
    const menu = document.getElementById("rzpn-nav-more-menu");
    if (!menu) return;
    setMoreOpen(menu.hasAttribute("hidden"));
  };
  const setDevOpen = open => {
    const menu = document.getElementById("rzpn-nav-dev-menu");
    const btn = document.querySelector("#page-rzpn .rzpn-nav-dd-btn");
    if (!menu || !btn) return;
    if (open) menu.removeAttribute("hidden"); else menu.setAttribute("hidden", "");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.classList.toggle("is-open", open);
  };
  const onDevClick = e => {
    e.stopPropagation();
    const menu = document.getElementById("rzpn-nav-dev-menu");
    if (!menu) return;
    setDevOpen(menu.hasAttribute("hidden"));
  };
  const setPrefsOpen = open => {
    const menu = document.getElementById("rzpn-nav-prefs-menu");
    const btn = document.querySelector("#page-rzpn .rzpn-nav-prefs-btn");
    if (!menu || !btn) return;
    if (open) menu.removeAttribute("hidden"); else menu.setAttribute("hidden", "");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.classList.toggle("is-open", open);
  };
  const onPrefsClick = e => {
    e.stopPropagation();
    const menu = document.getElementById("rzpn-nav-prefs-menu");
    if (!menu) return;
    setPrefsOpen(menu.hasAttribute("hidden"));
  };
  const onCountryClick = c => e => {
    e.preventDefault();
    window.location.href = `${c.href}?preferred_country=${c.cc}`;
  };
  if (typeof window !== "undefined" && !window.__rzpnBurgerBound) {
    window.__rzpnBurgerBound = true;
    queueMicrotask(() => {
      document.addEventListener("click", e => {
        const menu = document.getElementById("rzpn-nav-menu");
        if (!menu || menu.hasAttribute("hidden")) return;
        if (menu.contains(e.target)) {
          if (e.target.closest("a")) setBurgerOpen(false);
          return;
        }
        if (e.target.closest(".rzpn-nav-burger")) return;
        setBurgerOpen(false);
      });
      document.addEventListener("keydown", e => {
        if (e.key === "Escape") setBurgerOpen(false);
      });
    });
  }
  if (typeof window !== "undefined" && !window.__rzpnMoreBound) {
    window.__rzpnMoreBound = true;
    queueMicrotask(() => {
      document.addEventListener("click", e => {
        const menu = document.getElementById("rzpn-nav-more-menu");
        if (!menu || menu.hasAttribute("hidden")) return;
        if (menu.contains(e.target)) {
          if (e.target.closest("a")) setMoreOpen(false);
          return;
        }
        if (e.target.closest(".rzpn-nav-more-btn")) return;
        setMoreOpen(false);
      });
      document.addEventListener("keydown", e => {
        if (e.key === "Escape") setMoreOpen(false);
      });
    });
  }
  if (typeof window !== "undefined" && !window.__rzpnDevBound) {
    window.__rzpnDevBound = true;
    queueMicrotask(() => {
      document.addEventListener("click", e => {
        const menu = document.getElementById("rzpn-nav-dev-menu");
        if (!menu || menu.hasAttribute("hidden")) return;
        if (menu.contains(e.target)) {
          if (e.target.closest("a")) setDevOpen(false);
          return;
        }
        if (e.target.closest(".rzpn-nav-dd-btn")) return;
        setDevOpen(false);
      });
      document.addEventListener("keydown", e => {
        if (e.key === "Escape") setDevOpen(false);
      });
    });
  }
  if (typeof window !== "undefined" && !window.__rzpnPrefsBound) {
    window.__rzpnPrefsBound = true;
    queueMicrotask(() => {
      document.addEventListener("click", e => {
        const menu = document.getElementById("rzpn-nav-prefs-menu");
        if (!menu || menu.hasAttribute("hidden")) return;
        if (menu.contains(e.target)) {
          if (e.target.closest("a")) setPrefsOpen(false);
          return;
        }
        if (e.target.closest(".rzpn-nav-prefs-btn")) return;
        setPrefsOpen(false);
      });
      document.addEventListener("keydown", e => {
        if (e.key === "Escape") setPrefsOpen(false);
      });
    });
  }
  const IconSearch = () => <svg preserveAspectRatio="none" overflow="visible" style={{
    display: "block"
  }} width="16" height="16" viewBox="0 0 13.3333 13.3334" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fillRule="evenodd" clipRule="evenodd" d="M9.74511 10.6879C8.71867 11.509 7.41667 12 6 12C2.68629 12 0 9.31371 0 6C0 2.68629 2.68629 0 6 0C9.31371 0 12 2.68629 12 6C12 7.41668 11.509 8.71869 10.6879 9.74514L13.1381 12.1953C13.3984 12.4556 13.3984 12.8777 13.1381 13.1381C12.8777 13.3984 12.4556 13.3984 12.1953 13.1381L9.74511 10.6879ZM1.33333 6C1.33333 3.42267 3.42267 1.33333 6 1.33333C8.57733 1.33333 10.6667 3.42267 10.6667 6C10.6667 7.25732 10.1694 8.39851 9.36087 9.23765C9.33807 9.25518 9.31614 9.27439 9.29526 9.29528C9.27437 9.31616 9.25516 9.33809 9.23763 9.36089C8.39849 10.1694 7.25731 10.6667 6 10.6667C3.42267 10.6667 1.33333 8.57733 1.33333 6Z" fill="#616D75" />
    </svg>;
  const IconSpark = () => <svg preserveAspectRatio="none" overflow="visible" style={{
    display: "block"
  }} width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g clipPath="url(#rzpn-spark-clip)">
        <path d="M4.0026 3.66683C4.0026 3.48274 3.85336 3.3335 3.66927 3.3335C3.48518 3.3335 3.33594 3.48274 3.33594 3.66683C3.33594 4.32058 3.19113 4.71523 2.9544 4.95196C2.71767 5.18869 2.32302 5.3335 1.66927 5.3335C1.48518 5.3335 1.33594 5.48274 1.33594 5.66683C1.33594 5.85092 1.48518 6.00016 1.66927 6.00016C2.32302 6.00016 2.71767 6.14497 2.9544 6.3817C3.19113 6.61843 3.33594 7.0131 3.33594 7.66683C3.33594 7.8509 3.48518 8.00016 3.66927 8.00016C3.85336 8.00016 4.0026 7.8509 4.0026 7.66683C4.0026 7.0131 4.14741 6.61843 4.38414 6.3817C4.62087 6.14497 5.01552 6.00016 5.66927 6.00016C5.85336 6.00016 6.0026 5.85092 6.0026 5.66683C6.0026 5.48274 5.85336 5.3335 5.66927 5.3335C5.01552 5.3335 4.62087 5.18869 4.38414 4.95196C4.14741 4.71523 4.0026 4.32058 4.0026 3.66683Z" fill="black" />
        <path d="M7.33594 0.999837C7.33594 0.815744 7.18667 0.666504 7.0026 0.666504C6.81854 0.666504 6.66927 0.815744 6.66927 0.999837C6.66927 1.42211 6.57539 1.65009 6.44746 1.77802C6.31952 1.90596 6.09154 1.99984 5.66927 1.99984C5.48518 1.99984 5.33594 2.14908 5.33594 2.33317C5.33594 2.51726 5.48518 2.6665 5.66927 2.6665C6.09154 2.6665 6.31952 2.76038 6.44746 2.88832C6.57539 3.01625 6.66927 3.24423 6.66927 3.6665C6.66927 3.8506 6.81854 3.99984 7.0026 3.99984C7.18667 3.99984 7.33594 3.8506 7.33594 3.6665C7.33594 3.24423 7.4298 3.01625 7.55774 2.88832C7.68567 2.76038 7.91367 2.6665 8.33594 2.6665C8.52 2.6665 8.66927 2.51726 8.66927 2.33317C8.66927 2.14908 8.52 1.99984 8.33594 1.99984C7.91367 1.99984 7.68567 1.90596 7.55774 1.77802C7.4298 1.65009 7.33594 1.42211 7.33594 0.999837Z" fill="black" />
        <path fillRule="evenodd" clipRule="evenodd" d="M14.0026 9.99984C10.2989 9.99984 8.66927 11.6294 8.66927 15.3332C8.66927 11.6294 7.03967 9.99984 3.33594 9.99984C7.03967 9.99984 8.66927 8.37024 8.66927 4.6665C8.66927 8.37024 10.2989 9.99984 14.0026 9.99984Z" stroke="black" strokeWidth="1.5" strokeLinejoin="round" />
      </g>
      <defs>
        <clipPath id="rzpn-spark-clip">
          <rect width="16" height="16" fill="white" />
        </clipPath>
      </defs>
    </svg>;
  const openAssistant = () => {
    const candidates = Array.from(document.querySelectorAll('button, a, [role="button"]')).filter(n => {
      const label = (n.getAttribute("aria-label") || "") + " " + (n.textContent || "") + " " + (n.id || "");
      return (/assistant|ask ai|ask-ai/i).test(label) && !n.closest("#page-rzpn");
    });
    if (candidates.length) {
      candidates[0].click();
      return true;
    }
    return false;
  };
  return <div className="rzpn-nav-wrap">
      <nav className="rzpn-nav" aria-label="Docs">
        <a className="rzpn-nav-logo" href={L("/docs/home")} aria-label="Razorpay Docs">
          <img src={`${ASSETS}/logo.svg`} alt="" />
          <span className="rzpn-nav-rule" />
          <img src={`${ASSETS}/logo-docs.svg`} alt="" className="rzpn-nav-logo-docs" />
        </a>
        <div className="rzpn-nav-links">
          {shown.map(l => l.dd ? <div className="rzpn-nav-dd" key={l.href}>
                <button type="button" className="rzpn-nav-dd-btn" aria-haspopup="true" aria-expanded="false" aria-controls="rzpn-nav-dev-menu" onClick={onDevClick}>
                  {l.label}
                  <svg className="rzpn-nav-dd-chev" width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                    <path d="M4 6l4 4 4-4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                </button>
                <div className="rzpn-nav-dd-menu" id="rzpn-nav-dev-menu" hidden>
                  {DEV_TOOLS.map(t => <a href={L(t.href)} key={t.label}>
                      <svg className="rzpn-nav-dd-ico" aria-hidden="true"><use href={`#${t.icon}`} /></svg>
                      {t.label}
                    </a>)}
                </div>
              </div> : <a href={L(l.href)} className={l.overflow ? "rzpn-nav-overflow" : undefined} key={l.href}>{l.label}</a>)}
          <div className="rzpn-nav-more">
            <button type="button" className="rzpn-nav-more-btn" aria-haspopup="true" aria-expanded="false" aria-controls="rzpn-nav-more-menu" onClick={onMoreClick}>
              More
              <svg className="rzpn-nav-more-chev" width="8" height="8" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                <path d="M4 6l4 4 4-4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </button>
            <div className="rzpn-nav-more-menu" id="rzpn-nav-more-menu" hidden>
              {shown.filter(l => l.overflow).map(l => <a href={L(l.href)} key={l.href}>{l.label}</a>)}
            </div>
          </div>
        </div>
        <div className="rzpn-nav-right">
          <button type="button" className="rzpn-nav-icobtn" aria-label="Search" onClick={openSearch}>
            <IconSearch />
          </button>
          <button type="button" className="rzpn-nav-assistant" onClick={openAssistant}>
            <IconSpark />
            <span>Ask Assistant</span>
          </button>
          <div className="rzpn-nav-prefs">
            <button type="button" className="rzpn-nav-prefs-btn" aria-label="Change country" aria-haspopup="true" aria-expanded="false" aria-controls="rzpn-nav-prefs-menu" onClick={onPrefsClick}>
              <img src={`https://flagcdn.com/${currentHome.flag}.svg`} width="25" height="15" alt={currentHome.label} className="rzpn-nav-flag" />
              <svg className="rzpn-nav-prefs-chev" width="8" height="8" viewBox="0 0 16 16" fill="none" aria-hidden="true">
                <path d="M4 6l4 4 4-4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </button>
            <div className="rzpn-nav-prefs-menu" id="rzpn-nav-prefs-menu" hidden>
              {menuHomes.map(c => <a href={c.href} data-country={c.cc} onClick={c.cc == 'MY' ? undefined : onCountryClick(c)} key={c.cc}>
                  <img src={`https://flagcdn.com/${c.flag}.svg`} width="25" height="15" alt="" className="rzpn-nav-flag" />
                  <span>{c.cc}</span>
                </a>)}
            </div>
          </div>
          <div className="rzpn-nav-meta">
            <a href="https://razorpay.com/support/" target="_blank" rel="noreferrer">Support</a>
            <a href="https://dashboard.razorpay.com/signin" target="_blank" rel="noreferrer">Login</a>
          </div>
          <button type="button" className="rzpn-nav-burger" aria-label="Menu" aria-expanded="false" aria-controls="rzpn-nav-menu" onClick={onBurgerClick}>
            <span className="rzpn-nav-burger-ico" aria-hidden="true" />
          </button>
        </div>
      </nav>
      <div className="rzpn-nav-menu" id="rzpn-nav-menu" hidden>
        {shown.map(l => <a href={L(l.href)} key={l.href}>{l.label}</a>)}

        {DEV_TOOLS.map(t => <a href={L(t.href)} className="rzpn-nav-menu-sub" key={t.label}>
            <svg className="rzpn-nav-dd-ico" aria-hidden="true"><use href={`#${t.icon}`} /></svg>
            {t.label}
          </a>)}
        <hr className="rzpn-nav-menu-rule" />
        <a href="https://razorpay.com/support/" target="_blank" rel="noreferrer">Support</a>
        <a href="https://dashboard.razorpay.com/signin" target="_blank" rel="noreferrer">Login</a>
      </div>
    </div>;
};

export const HomeMain = ({children}) => <main id="page-rzpn" data-theme="light">
    <svg className="rzpn-icon-sprite" aria-hidden="true" width="0" height="0">
      <symbol id="rzpn-i-card" viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="2" /><path d="M2 10h20" /></symbol>
      <symbol id="rzpn-i-cart" viewBox="0 0 24 24"><circle cx="9" cy="20" r="1" /><circle cx="18" cy="20" r="1" /><path d="M2 3h3l2.4 12.2a2 2 0 0 0 2 1.6h8.7a2 2 0 0 0 2-1.6L22 7H6" /></symbol>
      <symbol id="rzpn-i-zap" viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z" /></symbol>
      <symbol id="rzpn-i-beaker" viewBox="0 0 24 24"><path d="M9 3h6M10 3v6.5L5 19a2 2 0 0 0 1.8 3h10.4A2 2 0 0 0 19 19l-5-9.5V3" /></symbol>
      <symbol id="rzpn-i-alert" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" /><path d="M12 8v5M12 16h.01" /></symbol>
      <symbol id="rzpn-i-power" viewBox="0 0 24 24"><path d="M12 3v9" /><path d="M6.3 6.3a8 8 0 1 0 11.4 0" /></symbol>
      <symbol id="rzpn-i-repeat" viewBox="0 0 24 24"><path d="M17 2l4 4-4 4" /><path d="M3 11V9a4 4 0 0 1 4-4h14" /><path d="M7 22l-4-4 4-4" /><path d="M21 13v2a4 4 0 0 1-4 4H3" /></symbol>
      <symbol id="rzpn-i-undo" viewBox="0 0 24 24"><path d="M3 2v6h6" /><path d="M3.5 14a9 9 0 1 0 2.1-9.4L3 8" /></symbol>
      <symbol id="rzpn-i-trend" viewBox="0 0 24 24"><path d="M22 7l-8.5 8.5-5-5L2 17" /><path d="M16 7h6v6" /></symbol>
      <symbol id="rzpn-i-send" viewBox="0 0 24 24"><path d="M22 2 11 13" /><path d="M22 2l-7 20-4-9-9-4 20-7Z" /></symbol>
      <symbol id="rzpn-i-link" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7" /><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7" /></symbol>
      <symbol id="rzpn-i-store" viewBox="0 0 24 24"><path d="M3 9l1.5-5h15L21 9" /><path d="M4 9v11h16V9" /><path d="M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0" /></symbol>
      <symbol id="rzpn-i-users" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M22 21v-2a4 4 0 0 0-3-3.9" /><path d="M16 3.1a4 4 0 0 1 0 7.8" /></symbol>
      <symbol id="rzpn-i-receipt" viewBox="0 0 24 24"><path d="M5 2v20l3-2 2 2 2-2 2 2 2-2 3 2V2l-3 2-2-2-2 2-2-2-2 2-3-2Z" /><path d="M9 8h6M9 12h6" /></symbol>
      <symbol id="rzpn-i-check" viewBox="0 0 24 24"><path d="M9 11l3 3 6-6" /><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11" /></symbol>
      <symbol id="rzpn-i-code" viewBox="0 0 24 24"><path d="M16 18l6-6-6-6" /><path d="M8 6l-6 6 6 6" /></symbol>
      <symbol id="rzpn-i-useradd" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M19 8v6M22 11h-6" /></symbol>
      <symbol id="rzpn-i-tag" viewBox="0 0 24 24"><path d="M20.6 13.4 12 22l-9-9V3h10l7.6 7.6a2 2 0 0 1 0 2.8Z" /><path d="M7.5 7.5h.01" /></symbol>
      <symbol id="rzpn-i-split" viewBox="0 0 24 24"><path d="M6 3v12" /><circle cx="18" cy="6" r="3" /><circle cx="6" cy="18" r="3" /><path d="M18 9a9 9 0 0 1-9 9" /></symbol>
      <symbol id="rzpn-i-book" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" /><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z" /></symbol>
      <symbol id="rzpn-i-package" viewBox="0 0 24 24"><path d="M21 8v8a2 2 0 0 1-1 1.73l-7 4a2 2 0 0 1-2 0l-7-4A2 2 0 0 1 3 16V8a2 2 0 0 1 1-1.73l7-4a2 2 0 0 1 2 0l7 4A2 2 0 0 1 21 8Z" /><path d="m3.3 7 8.7 5 8.7-5" /><path d="M12 22V12" /></symbol>
      <symbol id="rzpn-i-terminal" viewBox="0 0 24 24"><path d="m4 17 6-6-6-6" /><path d="M12 19h8" /></symbol>
      <symbol id="rzpn-i-plug" viewBox="0 0 24 24"><path d="M12 22v-5" /><path d="M9 8V2" /><path d="M15 8V2" /><path d="M18 8v3a6 6 0 0 1-12 0V8Z" /></symbol>
    </svg>

    {children}
  </main>;

export const HomeShell = ({children}) => {
  const setBurgerOpen = open => {
    const menu = document.getElementById("rzpn-nav-menu");
    const btn = document.querySelector("#page-rzpn .rzpn-nav-burger");
    if (!menu || !btn) return;
    if (open) menu.removeAttribute("hidden"); else menu.setAttribute("hidden", "");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.classList.toggle("is-open", open);
  };
  const setMoreOpen = open => {
    const menu = document.getElementById("rzpn-nav-more-menu");
    const btn = document.querySelector("#page-rzpn .rzpn-nav-more-btn");
    if (!menu || !btn) return;
    if (open) menu.removeAttribute("hidden"); else menu.setAttribute("hidden", "");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.classList.toggle("is-open", open);
  };
  const setDevOpen = open => {
    const menu = document.getElementById("rzpn-nav-dev-menu");
    const btn = document.querySelector("#page-rzpn .rzpn-nav-dd-btn");
    if (!menu || !btn) return;
    if (open) menu.removeAttribute("hidden"); else menu.setAttribute("hidden", "");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.classList.toggle("is-open", open);
  };
  if (typeof window !== "undefined") {
    const killTopPad = () => {
      const page = document.getElementById("page-rzpn");
      if (!page) return;
      let node = page.parentElement;
      while (node && node !== document.body) {
        const cls = typeof node.className === "string" ? node.className : "";
        if (cls.indexOf("pt-[120px]") !== -1) {
          node.style.setProperty("padding-top", "0px", "important");
        }
        node = node.parentElement;
      }
    };
    queueMicrotask(killTopPad);
    setTimeout(killTopPad, 100);
    setTimeout(killTopPad, 500);
    window.addEventListener("resize", killTopPad);
  }
  if (typeof window !== "undefined") {
    const loadHomeScript = () => {
      const existing = document.getElementById("rzpn-home-script");
      if (existing) existing.remove();
      const s = document.createElement("script");
      s.id = "rzpn-home-script";
      s.src = "/static/docs-home/script.js?t=" + Date.now();
      document.body.appendChild(s);
    };
    const waitForPageAndLoad = (attempts = 0) => {
      if (document.getElementById("page-rzpn")) {
        loadHomeScript();
      } else if (attempts < 100) {
        setTimeout(() => waitForPageAndLoad(attempts + 1), 50);
      }
    };
    queueMicrotask(() => {
      waitForPageAndLoad();
      if (!window.__rzpnAssistantWatch) {
        window.__rzpnAssistantWatch = true;
        const RZPN_W_BPS = [1280, 1180, 1129, 900, 620, 600, 420];
        const wState = {
          el: null,
          ro: null
        };
        const applyWidth = () => {
          const home = document.getElementById("rzpn-home");
          if (!home) return;
          if (wState.el !== home) {
            if (!wState.ro) wState.ro = new ResizeObserver(() => applyWidth());
            if (wState.el) wState.ro.unobserve(wState.el);
            wState.ro.observe(home);
            wState.el = home;
          }
          const w = home.clientWidth;
          if (!w) return;
          RZPN_W_BPS.forEach(bp => home.classList.toggle("rzpn-lte-" + bp, w <= bp));
          if (w > 900) {
            const menu = document.getElementById("rzpn-nav-menu");
            if (menu && !menu.hasAttribute("hidden")) setBurgerOpen(false);
          }
          if (w > 1129) {
            const more = document.getElementById("rzpn-nav-more-menu");
            if (more && !more.hasAttribute("hidden")) setMoreOpen(false);
          }
          if (w <= 900) {
            const dev = document.getElementById("rzpn-nav-dev-menu");
            if (dev && !dev.hasAttribute("hidden")) setDevOpen(false);
          }
        };
        const findPanel = () => {
          const candidates = document.querySelectorAll('#chat-assistant-sheet, [data-assistant-sheet-container], [aria-label="Assistant"]');
          for (const n of candidates) {
            if (n.closest("#page-rzpn")) continue;
            if (n.hasAttribute("hidden")) continue;
            if (n.getAttribute("data-closed") !== null && n.getAttribute("data-closed") !== "false") continue;
            const r = n.getBoundingClientRect();
            const s = getComputedStyle(n);
            if (r.width > 100 && r.height > 100 && s.display !== "none" && s.visibility !== "hidden" && parseFloat(s.opacity) > 0.1) {
              return n;
            }
          }
          return null;
        };
        let raf = 0;
        const apply = () => {
          if (raf) return;
          raf = requestAnimationFrame(() => {
            raf = 0;
            applyWidth();
            const page = document.getElementById("page-rzpn");
            if (!page) return;
            const panel = findPanel();
            let sideDocked = false;
            let r = null;
            if (panel) {
              r = panel.getBoundingClientRect();
              sideDocked = r.top < 80 && r.left > 40 && window.innerWidth - r.right < 40;
            }
            if (panel && sideDocked) {
              const rightInset = Math.max(0, Math.round(window.innerWidth - r.left));
              page.style.setProperty("--rzpn-assistant-w", rightInset + "px");
              page.classList.add("is-assistant-open");
            } else {
              page.style.removeProperty("--rzpn-assistant-w");
              page.classList.remove("is-assistant-open");
            }
          });
        };
        const mo = new MutationObserver(apply);
        mo.observe(document.body, {
          childList: true,
          subtree: true,
          attributes: true,
          attributeFilter: ["class", "style", "hidden", "aria-hidden", "open", "data-state", "data-closed"]
        });
        window.addEventListener("resize", apply);
        apply();
      }
    });
  }
  const RZPN_BPS = [1280, 1180, 1129, 900, 620, 600, 420];
  const rzpnW0 = typeof window === "undefined" ? 1440 : window.innerWidth;
  const rzpnHomeCls = RZPN_BPS.filter(bp => rzpnW0 <= bp).map(bp => "rzpn-lte-" + bp).join(" ");
  return <>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=TASA+Orbiter:wght@400;500;600;700&family=Instrument+Serif&family=Inter+Tight:wght@200;400;500&family=JetBrains+Mono:wght@400;700&display=swap');
        @import url('/static/docs-home/styles.css');

        header#navbar { display: none !important; }

        .pt-\[120px\] { padding-top: 0 !important; }

        #page-rzpn .rzpn-nav-wrap { z-index: 30 !important; }

        #page-rzpn.is-assistant-open .rzpn-nav-wrap {
          right: var(--rzpn-assistant-w, 0) !important;
          transition: right .18s ease;
        }
      `}</style>

      <div id="rzpn-home" className={rzpnHomeCls}>
        {children}
      </div>
    </>;
};

export const makeCopyPrompt = promptTexts => file => e => {
  e.preventDefault();
  e.stopPropagation();
  const text = promptTexts[file];
  if (text) copyText(text, e.currentTarget);
};

export const onCopyClick = text => e => {
  e.preventDefault();
  e.stopPropagation();
  copyText(text, e.currentTarget);
};

export const copyText = async (text, btn) => {
  let ok = false;
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      ok = true;
    }
  } catch (_) {}
  if (!ok) {
    try {
      const ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.top = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      ok = document.execCommand("copy");
      document.body.removeChild(ta);
    } catch (_) {}
  }
  if (!btn) return ok;
  const label = btn.querySelector("[data-rzpn-copy-label]");
  const resting = label ? label.textContent : null;
  btn.classList.add("is-copied");
  if (label) label.textContent = "Copied";
  setTimeout(() => {
    btn.classList.remove("is-copied");
    if (label && resting !== null) label.textContent = resting;
  }, 1700);
  return ok;
};

export const PROMPT_TEXTS = {
  "invoice.txt": "Integrate Razorpay Invoices into this codebase.\n\n=== CREDENTIALS ===\n\nRAZORPAY_KEY_ID: {{keyId}}\nRAZORPAY_KEY_SECRET: {{keySecret}}\n\nThese values are for the USER to place into their own environment. Never write them into any file (including .env), source code, or output \u2014 refer to them only by environment-variable name.\n\nIf either value above is empty or still looks like an unfilled template placeholder (e.g. a token wrapped in {{ }} double curly braces), STOP and ask the user to provide their Razorpay Key ID and Key Secret before proceeding (they can generate them in Razorpay Dashboard \u2192 Account & Settings \u2192 API Keys). Never copy placeholder text into any file, code, or output.\n\n=== TASK ===\n\nDetect the project stack and implement Razorpay Invoices with:\n1. Backend endpoint to create an Invoice via the Razorpay API\n2. Delivery of the invoice to the customer (Razorpay-side SMS/email or return the short_url)\n3. Backend webhook endpoint to receive and verify invoice payment events, reconciling paid / partially paid / expired states against the local order\n\n=== GUARDRAILS (STRICT \u2014 DO NOT VIOLATE) ===\n\nEnvironment & secrets:\n- Do NOT read, open, print, or otherwise access any .env file (or .env.*, .envrc) at any point \u2014 not to inspect existing values and not to write new ones.\n- Never hardcode, log, echo, or write KEY_SECRET / WEBHOOK_SECRET into any file, source code, comment, README, or output. Refer to secrets only by environment-variable name.\n- The code you WRITE may load environment variables at runtime (process.env / os.environ / getenv); the no-.env-access rule applies to you performing this task, not to the generated code.\n\nVersion control:\n- Do NOT commit any changes (no git add / git commit).\n- Do NOT push to any remote (no git push).\n- Do NOT create branches or tags, amend history, or modify git config/hooks.\n- Do NOT run destructive git commands (git reset, git checkout/restore to discard changes, git clean, git stash drop) \u2014 never discard or revert existing changes; assume uncommitted changes belong to the user.\n- Leave all changes uncommitted in the working tree for the user to review.\n\nExecution:\n- Do NOT run the application or any dev server.\n- Do NOT run tests, builds, linters, formatters, migrations, or package scripts.\n- Do NOT execute package-manager install commands (npm/yarn/pnpm/pip/composer/bundle/go get). Declare dependencies by editing the manifest only, and give the user the exact install command to run themselves.\n- Do NOT call the Razorpay API (or any external API) yourself during this task \u2014 only write code that calls it.\n\nScope:\n- Create or modify only the files strictly required for this integration. Do not refactor, reformat, rename, or delete unrelated code.\n- Do NOT perform destructive actions: never delete files, data, databases, or configurations, and never overwrite existing functionality.\n- If an existing Razorpay integration is present, extend only the missing pieces \u2014 do not duplicate or rewrite it.\n\nStack & monorepo detection (do this FIRST):\n- Determine the stack from manifests and workspace configs: package.json (workspaces), pnpm-workspace.yaml, lerna.json, turbo.json, nx.json, requirements.txt / pyproject.toml, composer.json, Gemfile, go.mod / go.work, settings.gradle, etc.\n- If the repository is a monorepo, identify the specific project/package that will own these routes, determine THAT package's language/framework, and use the Razorpay SDK for that language in that package only. Do NOT assume a single SDK for the entire repository.\n- If the target package, language, or framework is ambiguous, STOP and ask the user which package to integrate into. Do not guess.\n\n=== IMPLEMENTATION DETAILS ===\n\nSTEP 1: BACKEND - Create Invoice\n- Merchant backend route (create this): POST /api/create-invoice\n- Call Razorpay API from that route: POST https://api.razorpay.com/v1/invoices\n- Auth: HTTP Basic Auth with KEY_ID:KEY_SECRET\n- Request body (JSON) \u2014 note the root-level siblings of customer:\n{\n  \"type\": \"invoice\",\n  \"description\": \"Invoice for order #<id>\",\n  \"customer\": {\n    \"name\": \"<customer name>\",\n    \"email\": \"<customer email>\",\n    \"contact\": \"<customer-phone-with-country-code>\",\n    \"billing_address\": { \"line1\": \"...\", \"line2\": \"...\", \"zipcode\": \"...\", \"city\": \"...\", \"state\": \"...\", \"country\": \"<country-code>\" },\n    \"shipping_address\": { \"line1\": \"...\", \"line2\": \"...\", \"zipcode\": \"...\", \"city\": \"...\", \"state\": \"...\", \"country\": \"<country-code>\" }\n  },\n  \"line_items\": [\n    { \"name\": \"Item name\", \"description\": \"Item description\", \"amount\": 50000, \"currency\": \"<currency>\", \"quantity\": 1 }\n  ],\n  \"sms_notify\": 1,\n  \"email_notify\": 1,\n  \"partial_payment\": false,\n  \"currency\": \"<currency>\",\n  \"expire_by\": <unix-epoch-seconds-in-future>,\n  \"notes\": { \"order_id\": \"<internal id>\" }\n}\n- Root-level fields (siblings of customer): type, description, line_items, sms_notify, email_notify, partial_payment, currency, expire_by, notes, draft, customer_id. Nested inside customer: name, email, contact, billing_address, shipping_address.\n- Field rules:\n  - type must be \"invoice\" (values \"link\" / \"ecod\" also exist; use \"invoice\" here).\n  - amount on each line_items[] entry is in the smallest currency subunit (e.g., paise for INR, cents for USD). Minimum invoice amount 100 subunits.\n  - customer.name is the only mandatory customer field (3\u201350 chars). email/contact are optional but strongly recommended if you want Razorpay to deliver the invoice.\n  - customer.contact: 8\u201314 chars including country code; E.164 format with country code recommended.\n  - line_items[]: name and amount required per line; quantity defaults to 1; currency optional (defaults to invoice currency).\n  - sms_notify / email_notify: integer 1 or 0 \u2014 set to 1 to let Razorpay dispatch the invoice.\n  - partial_payment defaults to false.\n  - expire_by is optional (Unix epoch seconds); if set, must be a future time. Once past expire_by the invoice status flips to expired.\n  - notes is a free-form object (max 15 keys, 256 chars each) \u2014 pin your internal order id here.\n  - Alternative: pass root-level customer_id (of a previously created Customer) instead of an inline customer object.\n  - Use root-level \"draft\": 1 to create the invoice in draft state instead of issued; issue later with POST /v1/invoices/{id}/issue.\n- Response \u2014 persist these fields:\n  - id (inv_XXXX), short_url, status (see state machine below), order_id (auto-created Razorpay order), invoice_number, amount, amount_paid, amount_due, currency, receipt, customer_id, customer_details, line_items, issued_at, expire_by, paid_at\n- Return to caller: { id, short_url, status, order_id, amount, amount_due }\n\nState machine: draft \u2192 issued \u2192 (partially_paid) \u2192 paid, plus terminal cancelled / expired / deleted.\n\nSTEP 2: DELIVERY - Send Invoice to Customer\n- Preferred: sms_notify: 1 and email_notify: 1 at creation time \u2192 Razorpay dispatches SMS + email.\n- If sending yourself: use the short_url from the response over your own transactional channel. Never expose KEY_SECRET.\n- Resend: POST /v1/invoices/{id}/notify_by/{medium} where {medium} is sms or email.\n- Cancel an issued invoice with POST /v1/invoices/{id}/cancel (allowed only in draft or issued state; not on paid).\n\nSTEP 3: BACKEND - Reconcile via Webhook\n- Merchant backend route (create this): POST /api/razorpay-webhook\n- Webhook configuration in Razorpay Dashboard \u2192 Settings \u2192 Webhooks (MANUAL USER STEP \u2014 document it in your output; never attempt it yourself):\n  - URL: your public endpoint pointing to the route above\n  - Active events: invoice.paid, invoice.partially_paid, invoice.expired\n  - Set a webhook secret; the user stores it as RAZORPAY_WEBHOOK_SECRET in their environment\n  - Regional note: invoice.partially_paid does not fire for razorpay-MY / razorpay-SG; only invoice.paid and invoice.expired do.\n- Signature verification:\n  - Read the raw request body (bytes). Do NOT parse before verifying.\n  - Read header X-Razorpay-Signature.\n  - Compute HMAC-SHA256(raw_body, RAZORPAY_WEBHOOK_SECRET) \u2192 hex digest.\n  - Compare using constant-time compare (hmac.compare_digest / crypto.timingSafeEqual).\n- Reconciliation logic:\n  - On invoice.paid \u2192 mark the internal order as fully paid using payload.invoice.entity.id (and/or notes.order_id). Also available: payload.order.entity.id, payload.payment.entity.id.\n  - On invoice.partially_paid \u2192 update amount_paid / amount_due; keep order open.\n  - On invoice.expired \u2192 mark the order as expired; trigger any retry flow.\n  - Handler must be idempotent (retries send the same event again).\n- Respond 200 OK quickly; defer heavy work.\n- Note: there is no invoice.cancelled webhook. If you cancel via API, update local state at cancel time \u2014 do not wait for a webhook.\n\nSTEP 4: (Optional) Status Check API\n- Merchant backend route (create this): GET /api/invoice/:id\n- Calls Razorpay API from that route: GET https://api.razorpay.com/v1/invoices/{id} and returns status, amount_paid, amount_due, paid_at, payments[] (once populated).\n- Useful as a fallback if webhook delivery is delayed.\n\n=== ENVIRONMENT SETUP ===\n\nDo not read, create, or modify any .env file (see GUARDRAILS). Instead:\n\n1. Create or update .env.example with variable NAMES only (no real values):\nRAZORPAY_KEY_ID=\nRAZORPAY_KEY_SECRET=\nRAZORPAY_WEBHOOK_SECRET=\n\n2. Ensure .env is listed in .gitignore (edit .gitignore only; never touch .env itself).\n3. Wire the backend to read these variables from the environment via the project's existing config mechanism. At startup or first use, fail fast with a clear error naming any missing variable (never its value).\n4. In your final output, instruct the user to set the real values themselves: RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET from the CREDENTIALS section; RAZORPAY_WEBHOOK_SECRET after creating the webhook in the Razorpay Dashboard.\n5. KEY_SECRET and WEBHOOK_SECRET are backend-only \u2014 never prefix with NEXT_PUBLIC_, VITE_, or REACT_APP_, and never reference them in client-side code.\n\n=== SDK DEPENDENCY (DECLARE ONLY \u2014 DO NOT INSTALL) ===\n\nSelect ONE SDK: the one matching the language of the target package identified during stack/monorepo detection (not the repository as a whole). Declare it by editing that package's manifest; do not run any install command. Tell the user the exact install command to run.\n\n- Node.js: add \"razorpay\" to dependencies in the target package's package.json \u2192 user runs npm install (or yarn/pnpm install)\n- Python: add razorpay to requirements.txt or [project] dependencies in pyproject.toml \u2192 user runs pip install -r requirements.txt\n- PHP: add \"razorpay/razorpay\" to require in composer.json \u2192 user runs composer install\n- Ruby: add gem \"razorpay\" to the Gemfile \u2192 user runs bundle install\n- Go: import github.com/razorpay/razorpay-go in code \u2192 user runs go mod tidy\n- Java: add com.razorpay:razorpay-java to the dependencies in pom.xml (or build.gradle) \u2192 user runs mvn compile (or the Gradle sync/build) to resolve it\n- .NET: add a PackageReference to the Razorpay package in the .csproj \u2192 user runs dotnet restore\n- No SDK for the stack? This fallback applies ONLY when the target language is not listed above \u2014 if an official SDK exists for the language, use it; never choose raw HTTP just to avoid adding a dependency. In that no-SDK case, use the project's EXISTING HTTP client with HTTP Basic Auth against https://api.razorpay.com/v1/invoices \u2014 do not add a new HTTP client dependency if one already exists.\n\n=== OPERATION ORDER ===\n\n1. Detect the stack / target package (per GUARDRAILS); stop and ask if ambiguous\n2. Declare the SDK dependency in the target package's manifest (do not install)\n3. Create/update .env.example and .gitignore; wire environment loading with fail-fast validation\n4. Create the merchant route POST /api/create-invoice\n5. Create the merchant route POST /api/razorpay-webhook with signature verification + reconciliation\n6. Write the OUTPUT summary, listing every manual step left to the user (install command, env values, Dashboard webhook registration)\n\n=== ERROR HANDLING ===\n\nImplement BOTH classes below. They are distinct problems \u2014 do not conflate them.\n\nA) Integration-time errors (SDK/API wiring, configuration, request/response contract) \u2014 detect at startup or first use, fail fast with actionable messages:\n- Missing or empty RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET / RAZORPAY_WEBHOOK_SECRET \u2192 refuse to serve the route; return 500 \"payment provider misconfigured\" and log the missing variable NAME (never its value).\n- SDK initialization/import failure (wrong SDK for the package's language, incompatible version) \u2192 surface the error clearly; do not silently fall back.\n- 401 Unauthorized from Razorpay \u2192 invalid key id/secret; log as a configuration error, return 500 to the caller. Never retry.\n- Response contract mismatch (create response missing id/short_url/order_id) \u2192 treat as integration failure; log and return 502.\n\nB) Runtime errors (per-request exceptions, failed API calls, invalid inputs):\n- Validate inputs BEFORE calling Razorpay, each with a field-specific 400:\n  - customer.name present (3\u201350 chars)\n  - line_items[] non-empty, each row with name + integer amount\n  - invoice total (sum of line_items[].amount * quantity) >= 100 (smallest currency subunit)\n  - expire_by, if set, is a future Unix epoch (seconds)\n- Razorpay 400 BAD_REQUEST_ERROR \u2192 return 400 with the returned error.description.\n- Network timeout / 5xx from Razorpay \u2192 retry with bounded exponential backoff (max 2 retries), then return 503. Never retry a 4xx blindly.\n- Concrete example \u2014 Create Invoice failure: wrap the create call in try/catch and map the outcome:\n  - HTTP 400 \u2192 respond 400 { \"error\": error.description }\n  - HTTP 401 \u2192 respond 500 \"payment provider misconfigured\" (configuration issue \u2014 alert ops, do not retry)\n  - timeout / 5xx \u2192 retry up to 2 times with backoff, then respond 503\n  - Log Razorpay's error code/description for debugging; never log credentials or the raw Authorization header.\n\nBackend - Webhook (runtime):\n- Missing / invalid signature \u2192 400, do not process.\n- Unknown event type \u2192 200 (ignore), do not error.\n- Duplicate delivery \u2192 detect via payload.invoice.entity.id + event type; treat as no-op.\n\nDelivery (runtime):\n- If self-delivery fails, still return the created short_url so ops can resend.\n- Use the resend API rather than re-creating the invoice.\n\n=== EDGE CASES ===\n\n- No backend (pure static site): use a serverless function; never call the Invoices API from the browser.\n- GST invoices (India accounts): only non-GST invoices can be created via API. GST invoices must be created from the Dashboard.\n- International currencies: non-GST invoices support international currencies, but tax rates cannot be attached.\n- Partial payments: set partial_payment: true; the invoice stays in partially_paid until fully paid or expired. Ensure your reconciliation handles both invoice.partially_paid and invoice.paid.\n- Draft workflow: create with \"draft\": 1, review, then POST /v1/invoices/{id}/issue to send.\n- Cancellation: cancel only works in draft / issued state, and no webhook fires \u2014 update local state at cancel time.\n- Line item catalog: if SKUs are reused, write code that creates Items via POST /v1/items and references them by item_id inside line_items[] instead of inlining name/amount (the user runs that code; never call the API yourself).\n- Local development (document for the user; never start it yourself): the user must expose the webhook via a tunnel (ngrok, cloudflared) so the Dashboard can reach it.\n- Already integrated: don't duplicate. If a create route exists, add only the missing webhook reconciliation, or vice versa.\n\n=== REQUIREMENTS ===\n\n- Never hardcode credentials; load from environment\n- KEY_SECRET and WEBHOOK_SECRET must never reach the frontend\n- Use constant-time comparison for signature verification\n- Webhook handler must be idempotent\n- Match the project's existing router, error-response shape, and code style\n- Don't create DB tables unless the project already has one; otherwise store invoice.id + order_id on the existing order record\n\n=== REFERENCE ===\n\n- Invoices API index: https://razorpay.com/docs/api/payments/invoices/\n- Create with details: https://razorpay.com/docs/api/payments/invoices/create-with-details/\n- Cancel: https://razorpay.com/docs/api/payments/invoices/cancel/\n- Resend / notify_by: https://razorpay.com/docs/api/payments/invoices/resend/\n- Fetch: https://razorpay.com/docs/api/payments/invoices/fetch-with-id/\n- Invoices product docs: https://razorpay.com/docs/payments/invoices/\n- Webhook setup: https://razorpay.com/docs/webhooks/\n- Invoice webhook events: https://razorpay.com/docs/webhooks/invoices/\n- Test cards: https://razorpay.com/docs/payments/payments/test-card-details/\n\n=== OUTPUT ===\n\n1. List files created or modified\n2. Show a sample curl to hit POST /api/create-invoice (the merchant route) and the expected response \u2014 documentation only; do not execute it\n3. List the manual steps the user must perform (you must NOT perform any of these):\n   - Run the dependency install command (state it exactly)\n   - Set RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET / RAZORPAY_WEBHOOK_SECRET in their environment\n   - Register the webhook URL + secret in the Razorpay Dashboard \u2192 Settings \u2192 Webhooks\n   - For local development: start a tunnel (ngrok, cloudflared) so the Dashboard can reach the webhook\n4. Explain how the user can verify manually: open the returned short_url, pay with a Razorpay test card (see reference URL) \u2014 any future expiry, any CVV, then complete the test OTP or simulated bank page step \u2014 and confirm the webhook fires and the internal order transitions to paid / partially paid\n5. Confirm compliance with the GUARDRAILS: nothing committed, nothing pushed, nothing executed, no .env file read or written\n\nBegin integration now.\n",
  "mobile-checkout.txt": "Integrate Razorpay mobile payments into this codebase.\n\n=== CREDENTIALS ===\n\nRAZORPAY_KEY_ID: {{keyId}}\nRAZORPAY_KEY_SECRET: {{keySecret}}\n\nThese values are for the USER to place into their own environment. Never write them into any file (including .env), source code, or output \u2014 refer to them only by environment-variable name.\n\nIf either value above is empty or still looks like an unfilled template placeholder (e.g. a token wrapped in {{ }} double curly braces), STOP and ask the user to provide their Razorpay Key ID and Key Secret before proceeding (they can generate them in Razorpay Dashboard \u2192 Account & Settings \u2192 API Keys). Never copy placeholder text into any file, code, or output.\n\n=== TASK ===\n\nDetect the mobile stack (Android native / iOS native / both) and implement Razorpay Standard Checkout with:\n1. Backend endpoint to create orders (shared across platforms)\n2. Android SDK integration with checkout invocation and callback handling\n3. iOS SDK integration with checkout invocation and delegate handling\n4. Backend endpoint to verify the payment signature returned by the SDK\n\n=== GUARDRAILS (STRICT \u2014 DO NOT VIOLATE) ===\n\nEnvironment & secrets:\n- Do NOT read, open, print, or otherwise access any .env file (or .env.*, .envrc) at any point \u2014 not to inspect existing values and not to write new ones.\n- Never hardcode, log, echo, or write KEY_SECRET into any file, source code, comment, README, or output. Refer to secrets only by environment-variable name.\n- The backend code you WRITE may load environment variables at runtime (process.env / os.environ / getenv); the no-.env-access rule applies to you performing this task, not to the generated code.\n\nVersion control:\n- Do NOT commit any changes (no git add / git commit).\n- Do NOT push to any remote (no git push).\n- Do NOT create branches or tags, amend history, or modify git config/hooks.\n- Do NOT run destructive git commands (git reset, git checkout/restore to discard changes, git clean, git stash drop) \u2014 never discard or revert existing changes; assume uncommitted changes belong to the user.\n- Leave all changes uncommitted in the working tree for the user to review.\n\nExecution:\n- Do NOT run the application, backend server, or any dev server.\n- Do NOT run tests, builds, linters, formatters, or package scripts.\n- Do NOT run Gradle/gradlew tasks, xcodebuild, pod install, or launch emulators/simulators/devices.\n- Do NOT execute package-manager install commands (npm/yarn/pnpm/pip/composer/bundle/go get/pod). Declare dependencies by editing the manifests only, and give the user the exact install commands to run themselves.\n- Do NOT call the Razorpay API (or any external API) yourself during this task \u2014 only write code that calls it.\n\nScope:\n- Create or modify only the files strictly required for this integration. Do not refactor, reformat, rename, or delete unrelated code.\n- Do NOT perform destructive actions: never delete files, data, databases, or configurations, and never overwrite existing functionality.\n- If an existing Razorpay integration is present, extend only the missing pieces \u2014 do not duplicate or rewrite it.\n\nStack & monorepo detection (do this FIRST):\n- Identify each target separately: the backend package, the Android app module, and the iOS target. In a monorepo, locate each via its own manifest (package.json / requirements.txt / pyproject.toml / composer.json / Gemfile / go.mod for the backend; settings.gradle + app build.gradle for Android; .xcodeproj/.xcworkspace + Podfile for iOS).\n- Each target gets its own dependency in its own manifest: the backend SDK must match the BACKEND package's language (not the repository as a whole); Android uses Gradle; iOS uses CocoaPods. Do NOT assume a single SDK for the entire repository.\n- If any target (backend package, Android module, or iOS target) is missing or ambiguous, STOP and ask the user which one to integrate into. Do not guess.\n\n=== IMPLEMENTATION DETAILS ===\n\nSTEP 1: BACKEND - Create Order (shared)\n- Merchant backend route (create this): POST /api/create-order\n- Call Razorpay API from that route: POST https://api.razorpay.com/v1/orders\n- Auth: HTTP Basic Auth using KEY_ID:KEY_SECRET\n- Request: { \"amount\": 50000, \"currency\": \"<currency>\", \"receipt\": \"<internal-receipt>\" }\n- Response \u2014 return to the mobile app: { order_id, amount, currency, key_id, receipt }\n- Include key_id so the mobile client never hardcodes KEY_ID (Razorpay recommends fetching it as app metadata).\n- Minimum amount: 100 (smallest currency subunit).\n\nSTEP 2: ANDROID - SDK Integration\n\n2a. Dependency (app-level build.gradle) \u2014 pin to 1.6.40; the SDK auto-updates internally so a floating 1.6.+ isn't needed:\nrepositories { mavenCentral() }\ndependencies { implementation 'com.razorpay:checkout:1.6.40' }\n\n2b. AndroidManifest.xml \u2014 required internet permission; add the SDK override only if your minSdkVersion is lower than the SDK's:\n<uses-permission android:name=\"android.permission.INTERNET\" />\n<uses-sdk tools:overrideLibrary=\"com.razorpay\" />\nDo NOT put KEY_ID in the manifest.\n\n2c. ProGuard (proguard-rules.pro) for release builds:\n-keepclassmembers class * { @android.webkit.JavascriptInterface <methods>; }\n-keepattributes JavascriptInterface\n-keepattributes *Annotation*\n-dontwarn com.razorpay.**\n-keep class com.razorpay.** {*;}\n-optimizations !method/inlining/*\n-keepclasseswithmembers class * { public void onPayment*(...); }\n\n2d. Preload in Application.onCreate() (optional, faster first open):\nCheckout.preload(applicationContext)\n\n2e. Open checkout (Kotlin; Java is fully supported with identical names):\nimport com.razorpay.Checkout\nimport com.razorpay.PaymentResultWithDataListener\nimport org.json.JSONObject\n\nclass CheckoutActivity : AppCompatActivity(), PaymentResultWithDataListener {\n  fun startPayment(o: OrderResponse) {\n    val checkout = Checkout().apply { setKeyID(o.keyId) }\n    val options = JSONObject().apply {\n      put(\"name\", \"<Business name>\")\n      put(\"description\", \"Order #${o.receipt}\")\n      put(\"image\", \"https://<your-logo>.png\")\n      put(\"order_id\", o.orderId)\n      put(\"currency\", o.currency)\n      put(\"amount\", o.amount) // smallest currency subunit\n      put(\"prefill\", JSONObject()\n        .put(\"email\", \"<user email>\")\n        .put(\"contact\", \"<user phone>\"))\n      put(\"notes\", JSONObject().put(\"order_id\", \"<internal-id>\"))\n      put(\"theme\", JSONObject().put(\"color\", \"#3399cc\"))\n    }\n    try { checkout.open(this, options) } catch (e: Exception) { Log.e(\"RZP\", \"open failed\", e) }\n  }\n  override fun onPaymentSuccess(paymentId: String?, data: PaymentData?) {\n    // POST to /api/verify-payment as { \"razorpay_payment_id\": data.paymentId, \"razorpay_order_id\": data.orderId, \"razorpay_signature\": data.signature }\n  }\n  override fun onPaymentError(code: Int, response: String?) {\n    // code: Checkout.NETWORK_ERROR | INVALID_OPTIONS | PAYMENT_CANCELED | TLS_ERROR\n  }\n}\n\nUse PaymentResultWithDataListener (recommended) \u2014 success gives you paymentId, orderId, and signature. The error callback signature is onPaymentError(code, response) \u2014 no PaymentData on the error path. Legacy PaymentResultListener gives only the payment id on success.\n\nSTEP 3: iOS - SDK Integration\n\n3a. Dependency \u2014 CocoaPods only; SPM is not supported. Use the manual xcframework as fallback.\npod 'razorpay-pod'\n\n3b. Xcode 11+ \u2014 Target \u2192 General \u2192 Frameworks, Libraries, and Embedded Content \u2192 set the Razorpay framework to \"Embed & Sign\" (else the app crashes on launch).\n\n3c. Info.plist \u2014 add LSApplicationQueriesSchemes entries only if you enable UPI Intent (India accounts; see reference URL). Do NOT put KEY_ID in Info.plist.\n\n3d. Open checkout (Swift 5.1+; older Swift declares var razorpay: Razorpay! instead):\nimport Razorpay\n\nfinal class CheckoutViewController: UIViewController, RazorpayPaymentCompletionProtocolWithData {\n  var razorpay: RazorpayCheckout!\n  func startPayment(_ o: OrderResponse) {\n    // Initialize with the key_id from the /api/create-order response \u2014 it is not available before this point\n    razorpay = RazorpayCheckout.initWithKey(o.keyId, andDelegate: self)\n    let options: [String: Any] = [\n      \"amount\": \"\\(o.amount)\", // smallest currency subunit, string\n      \"currency\": o.currency,\n      \"name\": \"<Business name>\",\n      \"description\": \"Order #\\(o.receipt)\",\n      \"order_id\": o.orderId,\n      \"image\": \"https://<your-logo>.png\",\n      \"prefill\": [\"contact\": \"<user phone>\", \"email\": \"<user email>\"],\n      \"theme\": [\"color\": \"#3399cc\"],\n      \"notes\": [\"order_id\": \"<internal-id>\"]\n    ]\n    razorpay.open(options, displayController: self)\n  }\n  func onPaymentSuccess(_ payment_id: String, andData response: [AnyHashable: Any]?) {\n    // POST { razorpay_payment_id, razorpay_order_id, razorpay_signature } from `response` to /api/verify-payment\n  }\n  func onPaymentError(_ code: Int32, description str: String, andData response: [AnyHashable: Any]?) {\n    // code: 0 = Network, 1 = Init/unexpected, 2 = User cancelled\n  }\n}\n\nUse RazorpayPaymentCompletionProtocolWithData (recommended) \u2014 the success callback carries razorpay_payment_id, razorpay_order_id, and razorpay_signature. Legacy RazorpayPaymentCompletionProtocol returns only the payment id. Full Objective-C bindings ship with the pod.\n\nSTEP 4: BACKEND - Verify Signature (shared)\n- Merchant backend route (create this): POST /api/verify-payment\n- Body from the mobile app: { razorpay_payment_id, razorpay_order_id, razorpay_signature }\n- Algorithm: HMAC-SHA256(razorpay_order_id + \"|\" + razorpay_payment_id, RAZORPAY_KEY_SECRET) \u2192 hex digest\n- Constant-time compare (hmac.compare_digest / crypto.timingSafeEqual)\n- Match \u2192 mark order paid. Mismatch or missing fields \u2192 400.\n\n=== ENVIRONMENT SETUP ===\n\nDo not read, create, or modify any .env file (see GUARDRAILS). Instead:\n\n1. Create or update the backend package's .env.example with variable NAMES only (no real values):\nRAZORPAY_KEY_ID=\nRAZORPAY_KEY_SECRET=\n\n2. Ensure .env is listed in .gitignore (edit .gitignore only; never touch .env itself).\n3. Wire the backend to read these variables from the environment via the project's existing config mechanism. At startup or first use, fail fast with a clear error naming any missing variable (never its value).\n4. In your final output, instruct the user to set the real values themselves from the CREDENTIALS section.\n5. KEY_SECRET must never leave the backend. KEY_ID reaches the mobile app only via the /api/create-order response \u2014 never hardcode it in the APK/IPA, AndroidManifest.xml, or Info.plist.\n\n=== SDK DEPENDENCIES (DECLARE ONLY \u2014 DO NOT INSTALL OR BUILD) ===\n\nEach target gets its own dependency declared in its own manifest. Do not run Gradle, pod install, or any package manager \u2014 edit the files and tell the user the exact commands to run.\n\n- Android: add implementation 'com.razorpay:checkout:1.6.40' to the app module's build.gradle (mavenCentral repository) \u2192 user runs the Gradle sync/build\n- iOS: add pod 'razorpay-pod' to the Podfile (CocoaPods; manual xcframework as fallback; no SPM) \u2192 user runs pod install\n- Backend (match the BACKEND package's language, not the repo): Node \u2192 \"razorpay\" in package.json dependencies; Python \u2192 razorpay in requirements.txt/pyproject.toml; PHP \u2192 \"razorpay/razorpay\" in composer.json require; Ruby \u2192 gem \"razorpay\" in Gemfile; Go \u2192 import github.com/razorpay/razorpay-go; Java \u2192 com.razorpay:razorpay-java in pom.xml/build.gradle; .NET \u2192 Razorpay PackageReference in the .csproj \u2192 user runs the matching install command (npm install / pip install -r requirements.txt / composer install / bundle install / go mod tidy / mvn compile / dotnet restore)\n\n=== OPERATION ORDER ===\n\n1. Detect the targets (backend package, Android module, iOS target) per GUARDRAILS; stop and ask if ambiguous\n2. Backend: declare the SDK dependency in the manifest (do not install), create/update .env.example + .gitignore, wire env loading with fail-fast validation, implement /api/create-order and /api/verify-payment\n3. Android: declare the Gradle dependency + ProGuard rules + INTERNET permission (file edits only \u2014 do not run Gradle), wire the Checkout activity to call /api/create-order, open checkout, and post results to /api/verify-payment\n4. iOS: declare pod 'razorpay-pod' in the Podfile (do not run pod install), wire the CheckoutViewController with the same flow; note the \"Embed & Sign\" step as a manual user step\n5. Write the OUTPUT summary, listing every manual step left to the user (installs, env values, pod install, Embed & Sign)\n\n=== ERROR HANDLING ===\n\nImplement BOTH classes below. They are distinct problems \u2014 do not conflate them.\n\nA) Integration-time errors (SDK/API wiring, configuration, request/response contract):\n- Backend: missing or empty RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET \u2192 refuse to serve the routes; return 500 \"payment provider misconfigured\" and log the missing variable NAME (never its value). 401 Unauthorized from Razorpay \u2192 invalid credentials; log as a configuration error, return 500, never retry. Create-order response missing order id \u2192 integration failure; log and return 502.\n- Android: missing Gradle dependency, missing INTERNET permission, or missing ProGuard rules in release builds cause checkout.open() to fail or callbacks to be stripped \u2014 these are integration defects; verify the declarations in code review, not by building. Checkout.INVALID_OPTIONS in onPaymentError indicates a malformed options JSONObject (bad order_id, amount type, key) \u2014 fix the integration, do not retry.\n- iOS: framework not set to \"Embed & Sign\" crashes at launch; pod not declared fails the build. Document both as manual user steps; do not attempt builds yourself. Error code 1 (init/unexpected) usually indicates malformed options \u2014 fix the integration.\n\nB) Runtime errors (per-request exceptions, failed API calls, invalid inputs):\n- Backend /api/create-order: validate amount is an integer >= 100 (smallest currency subunit) \u2192 else 400. Razorpay 400 BAD_REQUEST_ERROR \u2192 400 with error.description. Timeout / 5xx \u2192 bounded retry (max 2, exponential backoff) then 503. Never retry a 4xx.\n  - Concrete example \u2014 Create Order failure: wrap the call in try/catch; map HTTP 400 \u2192 400 { \"error\": error.description }, HTTP 401 \u2192 500 \"payment provider misconfigured\" (alert ops), timeout/5xx \u2192 retry then 503. Log Razorpay's error code/description; never log credentials.\n- Backend /api/verify-payment: any of the three fields missing \u2192 400. Signature mismatch \u2192 400 using constant-time compare; never mark the order paid on failure.\n- Android: catch Exception from checkout.open(); in onPaymentError(code, response): NETWORK_ERROR \u2192 offer retry; PAYMENT_CANCELED \u2192 dismiss silently (not an error); TLS_ERROR \u2192 inform the user their device/OS is unsupported; log code + response. Do NOT call /api/verify-payment on any failure path.\n- iOS: code 2 (user cancelled) is not an error \u2014 dismiss silently. code 0 (network) \u2014 offer retry. code 1 \u2014 log as unexpected. Do NOT call /api/verify-payment on any failure path.\n\n=== EDGE CASES ===\n\n- KEY_ID delivery: return it in /api/create-order so it can be rotated on the server; don't ship it in the APK/IPA.\n- Version pin (Android): 1.6.40 (auto-updates internally); avoid floating ranges.\n- Xcode Embed pitfall: iOS crashes on launch if the framework isn't \"Embed & Sign\" on Xcode 11+.\n- Swift class rename: Swift 5.1+ \u2192 RazorpayCheckout; older \u2192 Razorpay.\n- No SPM on iOS: use CocoaPods for this dep or the manual xcframework path.\n- UI thread: checkout.open() must be called from the UI thread.\n- UPI Intent (iOS, India accounts): needs LSApplicationQueriesSchemes entries (reference URL).\n- Cross-platform: this prompt covers native Android + iOS. For RN use react-native-razorpay; for Flutter use razorpay_flutter. Same backend contract.\n- Already integrated: don't duplicate \u2014 add only what's missing.\n- No backend: mobile Standard Checkout requires a server; use a serverless function or switch to Payment Links.\n\n=== REQUIREMENTS ===\n\n- Never hardcode credentials in the mobile app\n- KEY_SECRET must never reach the mobile client\n- Fetch KEY_ID from the backend as part of the order response\n- Verify signature server-side before marking any order paid\n- Use constant-time comparison for signature verification\n- Match the project's existing code style (Kotlin/Java on Android, Swift/Obj-C on iOS)\n\n=== REFERENCE ===\n\n- Android integration: https://razorpay.com/docs/payments/payment-gateway/android-integration/standard/integration-steps/\n- iOS integration: https://razorpay.com/docs/payments/payment-gateway/ios-integration/standard/integration-steps/\n- Android sample: https://github.com/razorpay/razorpay-android-sample-app\n- iOS sample: https://github.com/razorpay/razorpay-ios-sample-app\n- Orders API: https://razorpay.com/docs/api/orders/\n- Signature verification: https://razorpay.com/docs/payments/server-integration/nodejs/payment-gateway/verify-signature/\n- Test cards: https://razorpay.com/docs/payments/payments/test-card-details/\n\n=== OUTPUT ===\n\n1. List files created or modified (backend + Android + iOS)\n2. Show sample curls for POST /api/create-order and POST /api/verify-payment with expected responses \u2014 documentation only; do not execute them\n3. List the manual steps the user must perform (you must NOT perform any of these):\n   - Run the dependency installs: backend package install, Gradle sync/build, pod install (state the exact commands)\n   - Set RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET in the backend environment\n   - Xcode: set the Razorpay framework to \"Embed & Sign\" (Target \u2192 General \u2192 Frameworks, Libraries, and Embedded Content)\n   - Confirm ProGuard rules are included in the Android release build configuration\n4. Explain how the user can verify manually: launch the app on a device / emulator / simulator, tap the pay button, complete payment with a Razorpay test card (see reference URL) \u2014 any future expiry, any CVV, then complete the test OTP or simulated bank page step \u2014 and confirm the WithData callback fires and /api/verify-payment returns success\n5. Confirm compliance with the GUARDRAILS: nothing committed, nothing pushed, nothing built or run, no .env file read or written\n\nBegin integration now.\n",
  "payment-link.txt": "Integrate Razorpay Payment Links into this codebase.\n\n=== CREDENTIALS ===\n\nRAZORPAY_KEY_ID: {{keyId}}\nRAZORPAY_KEY_SECRET: {{keySecret}}\n\nThese values are for the USER to place into their own environment. Never write them into any file (including .env), source code, or output \u2014 refer to them only by environment-variable name.\n\nIf either value above is empty or still looks like an unfilled template placeholder (e.g. a token wrapped in {{ }} double curly braces), STOP and ask the user to provide their Razorpay Key ID and Key Secret before proceeding (they can generate them in Razorpay Dashboard \u2192 Account & Settings \u2192 API Keys). Never copy placeholder text into any file, code, or output.\n\n=== TASK ===\n\nDetect the project stack and implement Razorpay Payment Links with:\n1. Backend endpoint to create a Payment Link via the Razorpay API\n2. Delivery of the Payment Link short URL to the customer (SMS/email/return-in-response)\n3. Backend webhook endpoint to receive and verify payment_link.paid events\n\n=== GUARDRAILS (STRICT \u2014 DO NOT VIOLATE) ===\n\nEnvironment & secrets:\n- Do NOT read, open, print, or otherwise access any .env file (or .env.*, .envrc) at any point \u2014 not to inspect existing values and not to write new ones.\n- Never hardcode, log, echo, or write KEY_SECRET / WEBHOOK_SECRET into any file, source code, comment, README, or output. Refer to secrets only by environment-variable name.\n- The code you WRITE may load environment variables at runtime (process.env / os.environ / getenv); the no-.env-access rule applies to you performing this task, not to the generated code.\n\nVersion control:\n- Do NOT commit any changes (no git add / git commit).\n- Do NOT push to any remote (no git push).\n- Do NOT create branches or tags, amend history, or modify git config/hooks.\n- Do NOT run destructive git commands (git reset, git checkout/restore to discard changes, git clean, git stash drop) \u2014 never discard or revert existing changes; assume uncommitted changes belong to the user.\n- Leave all changes uncommitted in the working tree for the user to review.\n\nExecution:\n- Do NOT run the application or any dev server.\n- Do NOT run tests, builds, linters, formatters, migrations, or package scripts.\n- Do NOT execute package-manager install commands (npm/yarn/pnpm/pip/composer/bundle/go get). Declare dependencies by editing the manifest only, and give the user the exact install command to run themselves.\n- Do NOT call the Razorpay API (or any external API) yourself during this task \u2014 only write code that calls it.\n\nScope:\n- Create or modify only the files strictly required for this integration. Do not refactor, reformat, rename, or delete unrelated code.\n- Do NOT perform destructive actions: never delete files, data, databases, or configurations, and never overwrite existing functionality.\n- If an existing Razorpay integration is present, extend only the missing pieces \u2014 do not duplicate or rewrite it.\n\nStack & monorepo detection (do this FIRST):\n- Determine the stack from manifests and workspace configs: package.json (workspaces), pnpm-workspace.yaml, lerna.json, turbo.json, nx.json, requirements.txt / pyproject.toml, composer.json, Gemfile, go.mod / go.work, settings.gradle, etc.\n- If the repository is a monorepo, identify the specific project/package that will own these routes, determine THAT package's language/framework, and use the Razorpay SDK for that language in that package only. Do NOT assume a single SDK for the entire repository.\n- If the target package, language, or framework is ambiguous, STOP and ask the user which package to integrate into. Do not guess.\n\n=== IMPLEMENTATION DETAILS ===\n\nSTEP 1: BACKEND - Create Payment Link\n- Merchant backend route (create this): POST /api/create-payment-link\n- Call Razorpay API from that route: POST https://api.razorpay.com/v1/payment_links\n- Auth: HTTP Basic Auth using KEY_ID:KEY_SECRET\n- Request body (JSON): { \"amount\": 50000, \"currency\": \"<currency>\", \"accept_partial\": false, \"expire_by\": <unix-epoch-seconds-at-least-15-min-in-future>, \"description\": \"Payment for order #<id>\", \"customer\": { \"name\": \"<customer name>\", \"email\": \"<customer email>\", \"contact\": \"<customer-phone-with-country-code>\" }, \"notify\": { \"sms\": true, \"email\": true }, \"reminder_enable\": true, \"notes\": { \"order_id\": \"<internal id>\" }, \"callback_url\": \"https://<your-domain>/payment-success\", \"callback_method\": \"get\" }\n- Field rules:\n  - amount in the smallest currency unit (e.g., paise for INR, cents for USD). Minimum 100 subunits.\n  - currency: ISO 4217 code for your account (e.g., INR, SGD, USD).\n  - expire_by is a Unix epoch (seconds) and must be at least 15 minutes in the future.\n  - customer.contact: 8\u201314 chars including country code; E.164 format with country code recommended.\n  - notify.sms/notify.email = true makes Razorpay dispatch the link on your behalf.\n  - callback_url + callback_method=\"get\" returns the customer to your site after payment.\n- Response - persist these fields:\n  - id (plink_XXXX), short_url, status, reference_id, amount, currency\n- Return to caller: { id, short_url, status }\n\nSTEP 2: DELIVERY - Send Link to Customer\n- Preferred: rely on Razorpay's built-in notification (notify.sms/notify.email = true).\n- If sending yourself: use short_url from the response over your own channel (transactional SMS provider, SES/SendGrid, WhatsApp Business API, etc.).\n- Do NOT expose KEY_SECRET in the message or in any client-side code.\n- Resend: POST /v1/payment_links/{id}/notify_by/{medium} where medium is sms or email.\n\nSTEP 3: BACKEND - Verify Payment via Webhook\n- Merchant backend route (create this): POST /api/razorpay-webhook\n- Webhook configuration in Razorpay Dashboard \u2192 Settings \u2192 Webhooks (MANUAL USER STEP \u2014 document it in your output; never attempt it yourself):\n  - URL: your public endpoint pointing to the route above\n  - Active events: payment_link.paid, payment_link.partially_paid, payment_link.expired, payment_link.cancelled\n  - Set a webhook secret; the user stores it as RAZORPAY_WEBHOOK_SECRET in their environment\n- Signature verification:\n  - Read raw request body (bytes) - do NOT parse before verifying\n  - Read header X-Razorpay-Signature\n  - Compute: HMAC-SHA256(raw_body, RAZORPAY_WEBHOOK_SECRET) \u2192 hex digest\n  - Compare using constant-time compare (hmac.compare_digest / crypto.timingSafeEqual)\n- On valid payment_link.paid: mark the internal order as paid using payload.payment_link.entity.id and/or notes.order_id. Make handling idempotent (same event may retry).\n- Respond 200 OK fast; do heavy work async if needed.\n\nSTEP 4: (Optional) Status Check API\n- Merchant backend route (create this): GET /api/payment-link/:id\n- Calls Razorpay API from that route: GET https://api.razorpay.com/v1/payment_links/{id} and returns status, amount_paid, payments[].\n- Useful as a fallback when webhooks are delayed.\n\n=== ENVIRONMENT SETUP ===\n\nDo not read, create, or modify any .env file (see GUARDRAILS). Instead:\n\n1. Create or update .env.example with variable NAMES only (no real values):\nRAZORPAY_KEY_ID=\nRAZORPAY_KEY_SECRET=\nRAZORPAY_WEBHOOK_SECRET=\n\n2. Ensure .env is listed in .gitignore (edit .gitignore only; never touch .env itself).\n3. Wire the backend to read these variables from the environment via the project's existing config mechanism (dotenv, config module, framework config). At startup or first use, fail fast with a clear error naming any missing variable (never its value).\n4. In your final output, instruct the user to set the real values themselves: RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET from the CREDENTIALS section; RAZORPAY_WEBHOOK_SECRET after creating the webhook in the Razorpay Dashboard.\n5. KEY_SECRET and WEBHOOK_SECRET are backend-only - never prefix with NEXT_PUBLIC_, VITE_, or REACT_APP_, and never reference them in client-side code.\n\n=== SDK DEPENDENCY (DECLARE ONLY \u2014 DO NOT INSTALL) ===\n\nSelect ONE SDK: the one matching the language of the target package identified during stack/monorepo detection (not the repository as a whole). Declare it by editing that package's manifest; do not run any install command. Tell the user the exact install command to run.\n\n- Node.js: add \"razorpay\" to dependencies in the target package's package.json \u2192 user runs npm install (or yarn/pnpm install)\n- Python: add razorpay to requirements.txt or [project] dependencies in pyproject.toml \u2192 user runs pip install -r requirements.txt\n- PHP: add \"razorpay/razorpay\" to require in composer.json \u2192 user runs composer install\n- Ruby: add gem \"razorpay\" to the Gemfile \u2192 user runs bundle install\n- Go: import github.com/razorpay/razorpay-go in code \u2192 user runs go mod tidy\n- Java: add com.razorpay:razorpay-java to the dependencies in pom.xml (or build.gradle) \u2192 user runs mvn compile (or the Gradle sync/build) to resolve it\n- .NET: add a PackageReference to the Razorpay package in the .csproj \u2192 user runs dotnet restore\n- No SDK for the stack? This fallback applies ONLY when the target language is not listed above \u2014 if an official SDK exists for the language, use it; never choose raw HTTP just to avoid adding a dependency. In that no-SDK case, use the project's EXISTING HTTP client with HTTP Basic Auth (KEY_ID:KEY_SECRET) against https://api.razorpay.com/v1/payment_links \u2014 do not add a new HTTP client dependency if one already exists.\n\n=== OPERATION ORDER ===\n\n1. Detect the stack / target package (per GUARDRAILS); stop and ask if ambiguous\n2. Declare the SDK dependency in the target package's manifest (do not install)\n3. Create/update .env.example and .gitignore; wire environment loading with fail-fast validation\n4. Create the merchant route POST /api/create-payment-link\n5. Create the merchant route POST /api/razorpay-webhook with signature verification\n6. Write the OUTPUT summary, listing every manual step left to the user (install command, env values, Dashboard webhook registration)\n\n=== ERROR HANDLING ===\n\nImplement BOTH classes below. They are distinct problems \u2014 do not conflate them.\n\nA) Integration-time errors (SDK/API wiring, configuration, request/response contract) \u2014 detect at startup or first use, fail fast with actionable messages:\n- Missing or empty RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET / RAZORPAY_WEBHOOK_SECRET \u2192 refuse to serve the route; return 500 \"payment provider misconfigured\" and log the missing variable NAME (never its value).\n- SDK initialization/import failure (wrong SDK for the package's language, incompatible version) \u2192 surface the error clearly; do not silently fall back.\n- 401 Unauthorized from Razorpay \u2192 invalid key id/secret; log as a configuration error, return 500 to the caller. Never retry.\n- Response contract mismatch (create response missing id/short_url) \u2192 treat as integration failure; log and return 502.\n\nB) Runtime errors (per-request exceptions, failed API calls, invalid inputs):\n- Validate inputs BEFORE calling Razorpay, each with a field-specific 400:\n  - amount is an integer and >= 100 (smallest currency subunit)\n  - expire_by is at least 15 minutes in the future\n  - customer.contact is valid E.164 when notify.sms is true\n- Razorpay 400 BAD_REQUEST_ERROR (e.g., invalid contact, amount below minimum) \u2192 return 400 with the returned error.description.\n- Network timeout / 5xx from Razorpay \u2192 retry with bounded exponential backoff (max 2 retries), then return 503. Never retry a 4xx blindly.\n- Concrete example \u2014 Payment Link creation failure: wrap the create call in try/catch and map the outcome:\n  - HTTP 400 \u2192 respond 400 { \"error\": error.description }\n  - HTTP 401 \u2192 respond 500 \"payment provider misconfigured\" (configuration issue \u2014 alert ops, do not retry)\n  - timeout / 5xx \u2192 retry up to 2 times with backoff, then respond 503\n  - Log Razorpay's error code/description for debugging; never log credentials or the raw Authorization header.\n\nBackend - Webhook (runtime):\n- Missing/invalid signature \u2192 400, do not process\n- Unknown event type \u2192 200 (ignore), do not error\n- Duplicate delivery \u2192 detect via payment_link.entity.id + event type; treat as no-op\n\nDelivery (runtime):\n- If self-sending SMS/email fails, still return the created short_url so ops can resend\n\n=== EDGE CASES ===\n\n- No backend (pure static site): use a serverless function (Vercel/Netlify/Cloud Functions) for both routes; never call the Payment Links API from the browser.\n- Partial payments: only enable accept_partial: true if the flow supports it; also configure first_min_partial_amount.\n- Multi-currency: instruct the user to verify the currency is enabled on their merchant account before sending; do not attempt to verify it yourself.\n- Already integrated: don't duplicate. If a create route exists, add only the missing webhook verification, or vice versa.\n- Local development (document for the user; never start it yourself): the user must expose the webhook via a tunnel (ngrok, cloudflared) so the Dashboard can reach it.\n\n=== REQUIREMENTS ===\n\n- Never hardcode credentials; load from environment\n- KEY_SECRET and WEBHOOK_SECRET must never reach the frontend\n- Use constant-time comparison for signature verification\n- Webhook handler must be idempotent\n- Match the project's existing code style, router, and error-response shape\n- Don't create DB tables unless the project already has a DB; otherwise store payment_link.id on the existing order record\n\n=== REFERENCE ===\n\n- Create Payment Link API: https://razorpay.com/docs/api/payments/payment-links/\n- Payment Links product docs: https://razorpay.com/docs/payments/payment-links/\n- Webhook setup: https://razorpay.com/docs/webhooks/\n- Payment Link webhook events: https://razorpay.com/docs/webhooks/payment-links/\n- Test cards: https://razorpay.com/docs/payments/payments/test-card-details/\n\n=== OUTPUT ===\n\n1. List files created or modified\n2. Show a sample curl to hit POST /api/create-payment-link (the merchant route) and the expected response \u2014 documentation only; do not execute it\n3. List the manual steps the user must perform (you must NOT perform any of these):\n   - Run the dependency install command (state it exactly)\n   - Set RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET / RAZORPAY_WEBHOOK_SECRET in their environment\n   - Register the webhook URL + secret in the Razorpay Dashboard \u2192 Settings \u2192 Webhooks\n   - For local development: start a tunnel (ngrok, cloudflared) so the Dashboard can reach the webhook\n4. Explain how the user can verify manually: open the returned short_url, pay with a Razorpay test card (see reference URL) \u2014 any future expiry, any CVV, then complete the test OTP or simulated bank page step \u2014 and confirm the webhook fires and the internal order flips to paid\n5. Confirm compliance with the GUARDRAILS: nothing committed, nothing pushed, nothing executed, no .env file read or written\n\nBegin integration now.\n",
  "subscriptions.txt": "Integrate Razorpay Subscriptions into this codebase.\n\n=== CREDENTIALS ===\n\nRAZORPAY_KEY_ID: {{keyId}}\nRAZORPAY_KEY_SECRET: {{keySecret}}\n\nThese values are for the USER to place into their own environment. Never write them into any file (including .env), source code, or output \u2014 refer to them only by environment-variable name.\n\nIf either value above is empty or still looks like an unfilled template placeholder (e.g. a token wrapped in {{ }} double curly braces), STOP and ask the user to provide their Razorpay Key ID and Key Secret before proceeding (they can generate them in Razorpay Dashboard \u2192 Account & Settings \u2192 API Keys). Never copy placeholder text into any file, code, or output.\n\n=== TASK ===\n\nDetect the project stack and implement Razorpay Subscriptions with:\n1. Backend endpoint to create a Plan (monthly schedule) \u2014 one-time setup, can be reused\n2. Backend endpoint to create a Subscription against that Plan\n3. Delivery of the Subscription authentication link to the customer\n4. Backend callback + webhook endpoints to authenticate the mandate and reconcile every recurring charge\n\n=== GUARDRAILS (STRICT \u2014 DO NOT VIOLATE) ===\n\nEnvironment & secrets:\n- Do NOT read, open, print, or otherwise access any .env file (or .env.*, .envrc) at any point \u2014 not to inspect existing values and not to write new ones.\n- Never hardcode, log, echo, or write KEY_SECRET / WEBHOOK_SECRET into any file, source code, comment, README, or output. Refer to secrets only by environment-variable name.\n- The code you WRITE may load environment variables at runtime (process.env / os.environ / getenv); the no-.env-access rule applies to you performing this task, not to the generated code.\n\nVersion control:\n- Do NOT commit any changes (no git add / git commit).\n- Do NOT push to any remote (no git push).\n- Do NOT create branches or tags, amend history, or modify git config/hooks.\n- Do NOT run destructive git commands (git reset, git checkout/restore to discard changes, git clean, git stash drop) \u2014 never discard or revert existing changes; assume uncommitted changes belong to the user.\n- Leave all changes uncommitted in the working tree for the user to review.\n\nExecution:\n- Do NOT run the application or any dev server.\n- Do NOT run tests, builds, linters, formatters, migrations, seed scripts, or package scripts.\n- Do NOT execute package-manager install commands (npm/yarn/pnpm/pip/composer/bundle/go get). Declare dependencies by editing the manifest only, and give the user the exact install command to run themselves.\n- Do NOT call the Razorpay API (or any external API) yourself during this task \u2014 only write code that calls it. This includes Plan creation: write the seed script/endpoint, but the USER runs it.\n\nScope:\n- Create or modify only the files strictly required for this integration. Do not refactor, reformat, rename, or delete unrelated code.\n- Do NOT perform destructive actions: never delete files, data, databases, or configurations, and never overwrite existing functionality.\n- If an existing Razorpay integration is present, extend only the missing pieces \u2014 do not duplicate or rewrite it.\n\nStack & monorepo detection (do this FIRST):\n- Determine the stack from manifests and workspace configs: package.json (workspaces), pnpm-workspace.yaml, lerna.json, turbo.json, nx.json, requirements.txt / pyproject.toml, composer.json, Gemfile, go.mod / go.work, settings.gradle, etc.\n- If the repository is a monorepo, identify the specific project/package that will own these routes, determine THAT package's language/framework, and use the Razorpay SDK for that language in that package only. Do NOT assume a single SDK for the entire repository.\n- If the target package, language, or framework is ambiguous, STOP and ask the user which package to integrate into. Do not guess.\n\n=== IMPLEMENTATION DETAILS ===\n\nSTEP 1: BACKEND - Create Plan (one-time, or on-demand)\n- Endpoint: POST /api/create-plan (or a one-time seed script that the USER runs \u2014 never execute it yourself)\n- Call Razorpay API: POST https://api.razorpay.com/v1/plans\n- Auth: HTTP Basic Auth (KEY_ID:KEY_SECRET)\n- Request body (monthly plan example):\n{\n  \"period\": \"monthly\",\n  \"interval\": 1,\n  \"item\": {\n    \"name\": \"Pro Plan\",\n    \"description\": \"Monthly pro subscription\",\n    \"amount\": 49900,\n    \"currency\": \"<currency>\"\n  },\n  \"notes\": { \"internal_plan_key\": \"pro-monthly-v1\" }\n}\n- Field rules:\n  - period \u2208 daily | weekly | monthly | quarterly | yearly. For a monthly schedule use \"monthly\".\n  - interval is the multiplier \u2014 period: \"monthly\", interval: 1 = every month; interval: 3 = every 3 months (a quarterly cadence via a monthly period).\n  - item.amount is in the smallest currency subunit (e.g., paise for INR, cents for USD). This is the recurring charge amount.\n  - item.currency: ISO 4217 code for your account (e.g., INR, SGD, USD); non-default currencies are subject to merchant enablement.\n- Response \u2014 persist:\n  - id (plan_XXXX), entity, period, interval, item{}, notes, created_at\n  - A Plan is reusable across many Subscriptions. Create once per pricing tier and store the plan_id.\n\nSTEP 2: BACKEND - Create Subscription\n- Merchant backend route (create this): POST /api/create-subscription\n- Call Razorpay API from that route: POST https://api.razorpay.com/v1/subscriptions\n- Request body:\n{\n  \"plan_id\": \"plan_XXXXXXXXXXXXXX\",\n  \"total_count\": 12,\n  \"quantity\": 1,\n  \"customer_notify\": true,\n  \"start_at\": <unix-epoch-seconds-in-future>,\n  \"expire_by\": <unix-epoch-seconds-in-future-after-start_at>,\n  \"addons\": [\n    { \"item\": { \"name\": \"Setup fee\", \"amount\": 30000, \"currency\": \"<currency>\" } }\n  ],\n  \"notes\": { \"user_id\": \"<internal id>\" }\n}\n- Field rules:\n  - plan_id (required): the Plan created in Step 1.\n  - total_count (required): number of billing cycles. Alternatively, end_at (Unix epoch) can substitute \u2014 Razorpay computes the count.\n  - quantity (optional, default 1): multiplies the per-cycle amount.\n  - customer_notify (optional, default true): if true, Razorpay sends the authentication link to the customer over SMS + email. NOTE: some SDKs form-encode request bodies (e.g. the Ruby SDK); with those, send customer_notify as 1 or 0 \u2014 a boolean true/false is rejected by the API when form-encoded.\n  - start_at (optional Unix epoch): when the first billing cycle begins.\n  - Immediate (start_at omitted or past): the first plan amount is charged during authentication.\n  - Future (start_at in future): only an authentication transaction runs now (a small auto-refunded verification charge for card mandates; zero-amount for eMandate/UPI AutoPay on India accounts); the first plan amount is charged on start_at.\n  - expire_by (optional Unix epoch): hard expiry \u2014 if not authenticated by this time, the subscription moves to expired.\n  - addons (optional): one-time charges taken alongside the first authentication. Use this for setup fees or an upfront amount.\n  - offer_id (optional): apply a promotional offer.\n  - notes (optional): free-form metadata (max 15 keys, 256 chars each) \u2014 pin your internal user id here.\n- Response \u2014 persist:\n  - id (sub_XXXX), plan_id, status, short_url, total_count, paid_count, remaining_count, current_start, current_end, start_at, end_at, charge_at, quantity, customer_notify, notes, has_scheduled_changes, created_at\n- Return to caller: { id, short_url, status }\n\nSubscription state machine (persist and act on):\ncreated \u2192 authenticated \u2192 active \u2192 (pending on retry) \u2192 (halted on final failure) or (paused \u2192 back to active) \u2192 completed (all cycles done) / cancelled (manual) / expired (not authenticated in time).\n\nSTEP 3: DELIVERY - Send Authentication Link\n- Preferred: customer_notify: true on creation \u2192 Razorpay sends the short_url over SMS + email.\n- Self-delivery: send the returned short_url from your own channel. Never expose KEY_SECRET.\n\nSTEP 4: BACKEND - Authenticate the Subscription (callback)\n- After the customer completes authentication at short_url (or via Checkout), Razorpay returns three fields via the configured redirect / handler:\n  - razorpay_payment_id\n  - razorpay_subscription_id\n  - razorpay_signature\n- Endpoint: POST /api/verify-subscription\n- Signature verification:\n  - Algorithm: HMAC-SHA256(razorpay_payment_id + \"|\" + razorpay_subscription_id, KEY_SECRET) \u2192 hex digest.\n  - Order matters: payment_id first, then subscription_id, joined by |.\n  - Compare to razorpay_signature using constant-time compare.\n  - On match: mark the local subscription record as authenticated. Do not mark it as active yet \u2014 wait for the subscription.activated webhook.\n  - On mismatch: 400, do not activate.\n\nSTEP 5: BACKEND - Reconcile Recurring Charges via Webhook\n- Endpoint: POST /api/razorpay-webhook (or reuse the project's existing webhook route)\n- Webhook configuration in Razorpay Dashboard \u2192 Settings \u2192 Webhooks (MANUAL USER STEP \u2014 document it in your output; never attempt it yourself):\n  - URL: your public endpoint\n  - Active events (subscription lifecycle):\n    - subscription.authenticated \u2014 mandate created, first auth successful\n    - subscription.activated \u2014 billing cycle started\n    - subscription.charged \u2014 a recurring payment succeeded (fires every cycle; payload includes payment entity)\n    - subscription.pending \u2014 a charge failed, Razorpay is retrying\n    - subscription.halted \u2014 retries exhausted, subscription frozen\n    - subscription.completed \u2014 all total_count cycles finished\n    - subscription.updated \u2014 plan/quantity/schedule changed\n    - subscription.paused \u2014 subscription paused\n    - subscription.resumed \u2014 subscription resumed (state returns to active)\n    - subscription.cancelled \u2014 cancelled by API or merchant\n  - Set a webhook secret; the user stores it as RAZORPAY_WEBHOOK_SECRET in their environment\n- Signature verification (same as any Razorpay webhook):\n  - Read raw request body (bytes). Do NOT parse before verifying.\n  - Read header X-Razorpay-Signature.\n  - Compute HMAC-SHA256(raw_body, RAZORPAY_WEBHOOK_SECRET) \u2192 hex digest.\n  - Compare using constant-time compare.\n- Reconciliation logic:\n  - subscription.charged \u2192 record a successful cycle payment (payload.payment.entity.id, amount), increment local paid_count, extend billing window.\n  - subscription.pending \u2192 surface a dunning UI / email to the customer; do not revoke access yet.\n  - subscription.halted \u2192 revoke access, alert the customer.\n  - subscription.completed / subscription.cancelled / subscription.paused \u2192 update local status; deprovision when appropriate.\n  - Handler must be idempotent \u2014 use payload.payment.entity.id (for charges) and payload.subscription.entity.id + event name as the dedupe key.\n  - Respond 200 OK quickly; defer heavy work.\n\nSTEP 6: (Optional) Lifecycle APIs\n- Fetch: GET /v1/subscriptions/{id} \u2192 current status, paid_count, remaining_count, charge_at.\n- Cancel: POST /v1/subscriptions/{id}/cancel with body { \"cancel_at_cycle_end\": false } (immediate) or true (at end of current billing cycle).\n- Pause: POST /v1/subscriptions/{id}/pause with body { \"pause_at\": \"now\" }.\n- Resume: POST /v1/subscriptions/{id}/resume with body { \"resume_at\": \"now\" }.\n- Update: PATCH /v1/subscriptions/{id} \u2014 change plan_id, quantity, remaining_count, or schedule_change_at.\n\n=== ENVIRONMENT SETUP ===\n\nDo not read, create, or modify any .env file (see GUARDRAILS). Instead:\n\n1. Create or update .env.example with variable NAMES only (no real values):\nRAZORPAY_KEY_ID=\nRAZORPAY_KEY_SECRET=\nRAZORPAY_WEBHOOK_SECRET=\n\n2. Ensure .env is listed in .gitignore (edit .gitignore only; never touch .env itself).\n3. Wire the backend to read these variables from the environment via the project's existing config mechanism. At startup or first use, fail fast with a clear error naming any missing variable (never its value).\n4. In your final output, instruct the user to set the real values themselves: RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET from the CREDENTIALS section; RAZORPAY_WEBHOOK_SECRET after creating the webhook in the Razorpay Dashboard.\n5. KEY_SECRET and WEBHOOK_SECRET are backend-only \u2014 never prefix with NEXT_PUBLIC_, VITE_, or REACT_APP_, and never reference them in client-side code.\n\n=== SDK DEPENDENCY (DECLARE ONLY \u2014 DO NOT INSTALL) ===\n\nSelect ONE SDK: the one matching the language of the target package identified during stack/monorepo detection (not the repository as a whole). Declare it by editing that package's manifest; do not run any install command. Tell the user the exact install command to run.\n\n- Node.js: add \"razorpay\" to dependencies in the target package's package.json \u2192 user runs npm install (or yarn/pnpm install)\n- Python: add razorpay to requirements.txt or [project] dependencies in pyproject.toml \u2192 user runs pip install -r requirements.txt\n- PHP: add \"razorpay/razorpay\" to require in composer.json \u2192 user runs composer install\n- Ruby: add gem \"razorpay\" to the Gemfile \u2192 user runs bundle install\n- Go: import github.com/razorpay/razorpay-go in code \u2192 user runs go mod tidy\n- Java: add com.razorpay:razorpay-java to the dependencies in pom.xml (or build.gradle) \u2192 user runs mvn compile (or the Gradle sync/build) to resolve it\n- .NET: add a PackageReference to the Razorpay package in the .csproj \u2192 user runs dotnet restore\n- No SDK for the stack? This fallback applies ONLY when the target language is not listed above \u2014 if an official SDK exists for the language, use it; never choose raw HTTP just to avoid adding a dependency. In that no-SDK case, use the project's EXISTING HTTP client with HTTP Basic Auth (KEY_ID:KEY_SECRET) against https://api.razorpay.com/v1 \u2014 do not add a new HTTP client dependency if one already exists.\n\n=== OPERATION ORDER ===\n\n1. Detect the stack / target package (per GUARDRAILS); stop and ask if ambiguous\n2. Declare the SDK dependency in the target package's manifest (do not install)\n3. Create/update .env.example and .gitignore; wire environment loading with fail-fast validation\n4. Write the Plan seed script or admin endpoint that stores plan_id in config/DB \u2014 do NOT execute it; the user runs it\n5. Implement POST /api/create-subscription\n6. Implement POST /api/verify-subscription (callback signature verification)\n7. Implement POST /api/razorpay-webhook (recurring reconciliation)\n8. Write the OUTPUT summary, listing every manual step left to the user (install command, env values, running the Plan seed, Dashboard webhook registration + event subscription)\n\n=== ERROR HANDLING ===\n\nImplement BOTH classes below. They are distinct problems \u2014 do not conflate them.\n\nA) Integration-time errors (SDK/API wiring, configuration, request/response contract) \u2014 detect at startup or first use, fail fast with actionable messages:\n- Missing or empty RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET / RAZORPAY_WEBHOOK_SECRET \u2192 refuse to serve the route; return 500 \"payment provider misconfigured\" and log the missing variable NAME (never its value).\n- SDK initialization/import failure (wrong SDK for the package's language, incompatible version) \u2192 surface the error clearly; do not silently fall back.\n- 401 Unauthorized from Razorpay \u2192 invalid key id/secret; log as a configuration error, return 500 to the caller. Never retry.\n- Invalid or missing stored plan_id (Razorpay rejects create-subscription with \"not a valid id\") \u2192 configuration error: log, alert, return 500. Do not auto-create a new Plan to work around it.\n- Response contract mismatch (create response missing id/short_url/status) \u2192 treat as integration failure; log and return 502.\n\nB) Runtime errors (per-request exceptions, failed API calls, invalid inputs):\n- Validate inputs BEFORE calling Razorpay, each with a field-specific 400:\n  - Plan creation: item.amount is an integer and >= 100 (smallest currency subunit); period is one of the allowed values; interval >= 1\n  - Subscription creation: total_count >= 1 (or end_at provided); start_at and expire_by, if set, are in the future\n- Razorpay 400 BAD_REQUEST_ERROR \u2192 return 400 with the returned error.description.\n- Network timeout / 5xx from Razorpay \u2192 retry with bounded exponential backoff (max 2 retries), then return 503. Never retry a 4xx blindly.\n- Concrete example \u2014 Create Subscription failure: wrap the create call in try/catch and map the outcome:\n  - HTTP 400 \u2192 respond 400 { \"error\": error.description }\n  - HTTP 401 \u2192 respond 500 \"payment provider misconfigured\" (configuration issue \u2014 alert ops, do not retry)\n  - timeout / 5xx \u2192 retry up to 2 times with backoff, then respond 503\n  - Log Razorpay's error code/description for debugging; never log credentials or the raw Authorization header.\n\nBackend - Callback Verification (runtime):\n- Missing any of the three fields \u2192 400\n- Signature mismatch \u2192 400, do not activate\n- Use constant-time compare\n\nBackend - Webhook (runtime):\n- Missing / invalid signature \u2192 400, do not process\n- Unknown event \u2192 200 (ignore)\n- Duplicate delivery \u2192 dedupe on payment_id (for charge events) or subscription.id + event for others\n\n=== EDGE CASES ===\n\n- Static site: use a serverless function; never call these APIs from the browser.\n- Payment method mix: authentication works with cards and, on India accounts, eMandate/UPI AutoPay; international cards where enabled. The customer picks the method at short_url.\n- Upfront / setup fees: use the addons[] array on Create Subscription \u2014 added to the first charge, not to every cycle.\n- Cancellation semantics: cancel_at_cycle_end: true lets the customer use what they've paid for; false cancels immediately (no proration refund).\n- Plan changes mid-cycle: use PATCH to change plan_id; schedule the change with schedule_change_at (now or cycle_end).\n- Halted subscriptions: cannot be resumed via API \u2014 customer must re-authenticate a new subscription.\n- Regional coverage: Subscriptions are primarily an India product. Ask the user to confirm availability before wiring for MY/SG/US.\n- Local dev (document for the user; never start it yourself): the user must expose the webhook via a tunnel (ngrok, cloudflared).\n- Already integrated: don't duplicate. Add only the missing pieces.\n\n=== REQUIREMENTS ===\n\n- Never hardcode credentials; load from environment\n- KEY_SECRET and WEBHOOK_SECRET must never reach the frontend\n- Use constant-time comparison for both callback signature and webhook signature\n- Webhook handler must be idempotent\n- Match the project's existing router, error-response shape, and code style\n- Don't create DB tables unless the project already has one; otherwise store subscription.id + plan_id + current status on the user record\n\n=== REFERENCE ===\n\n- Subscriptions API index: https://razorpay.com/docs/api/payments/subscriptions/\n- Create Plan: https://razorpay.com/docs/api/payments/subscriptions/create-plan/\n- Create Subscription: https://razorpay.com/docs/api/payments/subscriptions/create-subscription/\n- Cancel / Pause / Resume / Update: https://razorpay.com/docs/api/payments/subscriptions/\n- Subscription states: https://razorpay.com/docs/payments/subscriptions/states/\n- Integration guide (callback signature format): https://razorpay.com/docs/payments/subscriptions/integration-guide/\n- Webhook events + payloads: https://razorpay.com/docs/webhooks/subscriptions/\n- Webhook signature validation: https://razorpay.com/docs/webhooks/validate-test/\n- Test cards / mandates: https://razorpay.com/docs/payments/subscriptions/test/\n\n=== OUTPUT ===\n\n1. List files created or modified\n2. Show sample curls for /api/create-subscription and for /api/create-plan (or the seed-script invocation, whichever was implemented), with expected responses \u2014 documentation only; do not execute them\n3. List the manual steps the user must perform (you must NOT perform any of these):\n   - Run the dependency install command (state it exactly)\n   - Set RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET / RAZORPAY_WEBHOOK_SECRET in their environment\n   - Run the Plan seed (script or admin endpoint) and store the resulting plan_id\n   - Register the webhook URL + secret in the Razorpay Dashboard \u2192 Settings \u2192 Webhooks and subscribe to the subscription events listed above\n   - For local development: start a tunnel (ngrok, cloudflared) so the Dashboard can reach the webhook\n4. Explain how the user can verify manually: create a subscription with start_at a few minutes in the future, open the returned short_url, authenticate with a Razorpay test card (see reference URL), confirm callback signature verification passes and subscription.authenticated fires, then wait for subscription.activated and the first subscription.charged to confirm the recurring loop\n5. Confirm compliance with the GUARDRAILS: nothing committed, nothing pushed, nothing executed, no .env file read or written\n\nBegin integration now.\n",
  "website-checkout.txt": "Integrate Razorpay Standard Web Checkout into this codebase.\n\n=== CREDENTIALS ===\n\nRAZORPAY_KEY_ID: {{keyId}}\nRAZORPAY_KEY_SECRET: {{keySecret}}\n\nThese values are for the USER to place into their own environment. Never write them into any file (including .env), source code, or output \u2014 refer to them only by environment-variable name.\n\nIf either value above is empty or still looks like an unfilled template placeholder (e.g. a token wrapped in {{ }} double curly braces), STOP and ask the user to provide their Razorpay Key ID and Key Secret before proceeding (they can generate them in Razorpay Dashboard \u2192 Account & Settings \u2192 API Keys). Never copy placeholder text into any file, code, or output.\n\n=== TASK ===\n\nDetect the project stack and implement Razorpay Standard Web Checkout with:\n1. Backend endpoint to create a Razorpay Order via the Orders API\n2. Frontend integration that loads checkout.js and opens the Razorpay Checkout modal for that order\n3. Backend endpoint that verifies the payment signature server-side before marking the order paid\n\n=== GUARDRAILS (STRICT \u2014 DO NOT VIOLATE) ===\n\nEnvironment & secrets:\n- Do NOT read, open, print, or otherwise access any .env file (or .env.*, .envrc) at any point \u2014 not to inspect existing values and not to write new ones.\n- Never hardcode, log, echo, or write KEY_SECRET / WEBHOOK_SECRET into any file, source code, comment, README, or output. Refer to secrets only by environment-variable name.\n- The code you WRITE may load environment variables at runtime (process.env / os.environ / getenv); the no-.env-access rule applies to you performing this task, not to the generated code.\n\nVersion control:\n- Do NOT commit any changes (no git add / git commit).\n- Do NOT push to any remote (no git push).\n- Do NOT create branches or tags, amend history, or modify git config/hooks.\n- Do NOT run destructive git commands (git reset, git checkout/restore to discard changes, git clean, git stash drop) \u2014 never discard or revert existing changes; assume uncommitted changes belong to the user.\n- Leave all changes uncommitted in the working tree for the user to review.\n\nExecution:\n- Do NOT run the application or any dev server.\n- Do NOT run tests, builds, linters, formatters, migrations, or package scripts.\n- Do NOT execute package-manager install commands (npm/yarn/pnpm/pip/composer/bundle/go get). Declare dependencies by editing the manifest only, and give the user the exact install command to run themselves.\n- Do NOT call the Razorpay API (or any external API) yourself during this task \u2014 only write code that calls it.\n\nScope:\n- Create or modify only the files strictly required for this integration. Do not refactor, reformat, rename, or delete unrelated code.\n- Do NOT perform destructive actions: never delete files, data, databases, or configurations, and never overwrite existing functionality.\n- If an existing Razorpay integration is present, extend only the missing pieces \u2014 do not duplicate or rewrite it.\n\nStack & monorepo detection (do this FIRST):\n- Determine the stack from manifests and workspace configs: package.json (workspaces), pnpm-workspace.yaml, lerna.json, turbo.json, nx.json, requirements.txt / pyproject.toml, composer.json, Gemfile, go.mod / go.work, settings.gradle, etc.\n- If the repository is a monorepo, identify the specific project/package that will own these routes, determine THAT package's language/framework, and use the Razorpay SDK for that language in that package only. Do NOT assume a single SDK for the entire repository.\n- Identify the frontend separately (server-rendered templates, static pages, or a JS framework such as React/Vue/Next); the checkout.js integration goes there, the two routes go in the backend package.\n- If the target package, language, or framework is ambiguous, STOP and ask the user which package to integrate into. Do not guess.\n\n=== IMPLEMENTATION DETAILS ===\n\nSTEP 1: BACKEND - Create Order\n- Merchant backend route (create this): POST /api/create-order\n- Call Razorpay API from that route: POST https://api.razorpay.com/v1/orders\n- Auth: HTTP Basic Auth using KEY_ID:KEY_SECRET\n- Request body (JSON): { \"amount\": 50000, \"currency\": \"<currency>\", \"receipt\": \"<internal-receipt-id>\", \"notes\": { \"order_id\": \"<internal id>\" } }\n- Field rules:\n  - amount in the smallest currency unit (e.g., paise for INR, cents for USD). Minimum 100 subunits.\n  - Compute amount SERVER-SIDE from the cart/order record \u2014 never trust an amount sent by the browser. The Razorpay Order fixes the charge amount; the modal cannot change it.\n  - currency: ISO 4217 code for your account (e.g., INR, SGD, USD).\n  - receipt: your internal reference, max 40 characters.\n- Response \u2014 persist id (order_XXXX) against the internal order; return to the browser: { order_id, amount, currency, key_id }\n- Include key_id so the frontend never hardcodes KEY_ID (it stays rotatable on the server).\n\nSTEP 2: FRONTEND - Open Razorpay Checkout\n- Load the script from exactly https://checkout.razorpay.com/v1/checkout.js via a script tag (or dynamic script injection in SPA frameworks \u2014 open the modal only after the script has loaded). Do NOT bundle or self-host checkout.js.\n- On the pay action: call POST /api/create-order, then open the modal with these options:\n  - key: the key_id returned by /api/create-order\n  - order_id, amount, currency: from the /api/create-order response\n  - name / description: business and order display text\n  - prefill: { \"name\": \"<customer name>\", \"email\": \"<customer email>\", \"contact\": \"<customer phone>\" }\n  - notes: { \"order_id\": \"<internal id>\" }\n  - theme: { \"color\": \"<brand color hex>\" }\n  - handler: function receiving { razorpay_payment_id, razorpay_order_id, razorpay_signature } on success \u2192 POST all three to /api/verify-payment; show success to the user ONLY after the backend confirms.\n  - modal.ondismiss: the customer closed the modal \u2014 treat as cancelled, not an error.\n- Also register rzp.on('payment.failed', ...) \u2192 show the returned error.description and allow retry; do NOT call /api/verify-payment on any failure path.\n- Never reference KEY_SECRET in any frontend file, template, or bundle.\n\nSTEP 3: BACKEND - Verify Payment Signature\n- Merchant backend route (create this): POST /api/verify-payment\n- Body from the browser: { razorpay_payment_id, razorpay_order_id, razorpay_signature }\n- Algorithm: HMAC-SHA256(razorpay_order_id + \"|\" + razorpay_payment_id, RAZORPAY_KEY_SECRET) \u2192 hex digest\n- Compare using constant-time compare (hmac.compare_digest / crypto.timingSafeEqual)\n- Match \u2192 mark the internal order paid using the persisted razorpay order id. Make handling idempotent (the browser may retry the request), but validate the signature BEFORE any already-paid short-circuit \u2014 never return success for an unverified request.\n- Mismatch or missing fields \u2192 400; never mark the order paid on failure.\n- Signature verification happens ONLY on the backend \u2014 never in the browser.\n\nSTEP 4: (Optional) Payment Status Fallback\n- Merchant backend route (create this): GET /api/order-status/:order_id\n- Calls Razorpay API from that route: GET https://api.razorpay.com/v1/orders/{id}/payments and returns the payment status list.\n- Useful when the browser closed before the handler ran; for full reliability recommend the user also register webhooks (payment.captured) \u2014 a separate concern, out of scope here.\n\n=== ENVIRONMENT SETUP ===\n\nDo not read, create, or modify any .env file (see GUARDRAILS). Instead:\n\n1. Create or update .env.example with variable NAMES only (no real values):\nRAZORPAY_KEY_ID=\nRAZORPAY_KEY_SECRET=\n\n2. Ensure .env is listed in .gitignore (edit .gitignore only; never touch .env itself).\n3. Wire the backend to read these variables from the environment via the project's existing config mechanism (dotenv, config module, framework config). At startup or first use, fail fast with a clear error naming any missing variable (never its value).\n4. In your final output, instruct the user to set the real values themselves from the CREDENTIALS section.\n5. KEY_SECRET is backend-only \u2014 never prefix it with NEXT_PUBLIC_, VITE_, or REACT_APP_, and never reference it in client-side code. KEY_ID reaches the browser only via the /api/create-order response (preferred); if the project already exposes public config through a public-prefixed variable, that variable may hold KEY_ID ONLY, never KEY_SECRET.\n\n=== SDK DEPENDENCY (DECLARE ONLY \u2014 DO NOT INSTALL) ===\n\nSelect ONE SDK: the one matching the language of the target package identified during stack/monorepo detection (not the repository as a whole). Declare it by editing that package's manifest; do not run any install command. Tell the user the exact install command to run. The frontend needs NO package \u2014 checkout.js is loaded from Razorpay's CDN via script tag.\n\n- Node.js: add \"razorpay\" to dependencies in the target package's package.json \u2192 user runs npm install (or yarn/pnpm install)\n- Python: add razorpay to requirements.txt or [project] dependencies in pyproject.toml \u2192 user runs pip install -r requirements.txt\n- PHP: add \"razorpay/razorpay\" to require in composer.json \u2192 user runs composer install\n- Ruby: add gem \"razorpay\" to the Gemfile \u2192 user runs bundle install\n- Go: import github.com/razorpay/razorpay-go in code \u2192 user runs go mod tidy\n- Java: add com.razorpay:razorpay-java to the dependencies in pom.xml (or build.gradle) \u2192 user runs mvn compile (or the Gradle sync/build) to resolve it\n- .NET: add a PackageReference to the Razorpay package in the .csproj \u2192 user runs dotnet restore\n- No SDK for the stack? This fallback applies ONLY when the target language is not listed above \u2014 if an official SDK exists for the language, use it; never choose raw HTTP just to avoid adding a dependency. In that no-SDK case, use the project's EXISTING HTTP client with HTTP Basic Auth (KEY_ID:KEY_SECRET) against https://api.razorpay.com/v1/orders \u2014 do not add a new HTTP client dependency if one already exists.\n\n=== OPERATION ORDER ===\n\n1. Detect the stack / target package and the frontend (per GUARDRAILS); stop and ask if ambiguous\n2. Declare the SDK dependency in the target package's manifest (do not install)\n3. Create/update .env.example and .gitignore; wire environment loading with fail-fast validation\n4. Create the merchant route POST /api/create-order\n5. Add the frontend checkout.js integration (script load, pay action, modal options, handler, failure/dismiss handling)\n6. Create the merchant route POST /api/verify-payment with constant-time signature verification\n7. (Optional) Create the status fallback route GET /api/order-status/:order_id\n8. Write the OUTPUT summary, listing every manual step left to the user (install command, env values)\n\n=== ERROR HANDLING ===\n\nImplement BOTH classes below. They are distinct problems \u2014 do not conflate them.\n\nA) Integration-time errors (SDK/API wiring, configuration, request/response contract) \u2014 detect at startup or first use, fail fast with actionable messages:\n- Missing or empty RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET \u2192 refuse to serve the routes; return 500 \"payment provider misconfigured\" and log the missing variable NAME (never its value).\n- SDK initialization/import failure (wrong SDK for the package's language, incompatible version) \u2192 surface the error clearly; do not silently fall back.\n- 401 Unauthorized from Razorpay \u2192 invalid key id/secret; log as a configuration error, return 500 to the caller. Never retry.\n- Response contract mismatch (create-order response missing id) \u2192 treat as integration failure; log and return 502.\n\nB) Runtime errors (per-request exceptions, failed API calls, invalid inputs):\n- Validate inputs BEFORE calling Razorpay, each with a field-specific 400:\n  - amount resolves to an integer >= 100 (smallest currency subunit) \u2014 computed server-side, never taken from the browser\n  - currency, when configurable, is a valid ISO 4217 code\n- Razorpay 400 BAD_REQUEST_ERROR \u2192 return 400 with the returned error.description.\n- Network timeout / 5xx from Razorpay \u2192 retry with bounded exponential backoff (max 2 retries), then return 503. Never retry a 4xx blindly.\n- Concrete example \u2014 Order creation failure: wrap the create call in try/catch and map the outcome:\n  - HTTP 400 \u2192 respond 400 { \"error\": error.description }\n  - HTTP 401 \u2192 respond 500 \"payment provider misconfigured\" (configuration issue \u2014 alert ops, do not retry)\n  - timeout / 5xx \u2192 retry up to 2 times with backoff, then respond 503\n  - Log Razorpay's error code/description for debugging; never log credentials or the raw Authorization header.\n\nBackend - Verify (runtime):\n- Any of the three fields missing \u2192 400, do not verify\n- Signature mismatch \u2192 400 (constant-time compare); never mark the order paid on failure\n- Repeat verification of an already-paid order \u2192 validate the signature first, then return success without re-processing (idempotent); a tampered signature gets 400 even when the order is already paid\n\nFrontend (runtime):\n- payment.failed \u2192 show error.description; the customer may retry payment on the same order while it is unpaid\n- modal.ondismiss \u2192 cancelled by the customer; not an error, no verify call\n- /api/create-order failed \u2192 show a friendly error; do not open the modal\n\n=== EDGE CASES ===\n\n- No backend (pure static site): use a serverless function (Vercel/Netlify/Cloud Functions) for both routes; never create orders or verify signatures in the browser. If no server-side option is possible at all, recommend Razorpay Payment Links instead.\n- Amount tampering: because the Razorpay Order fixes the amount at creation, a tampered amount in the modal options cannot change the charge \u2014 but still compute the order amount server-side from the cart.\n- Already integrated: don't duplicate. If a create-order route exists, add only the missing signature verification, or vice versa.\n- SPA frameworks (React/Vue/Next.js): inject the checkout.js script dynamically and open the modal only after it loads; keep the verify route strictly server-side (API route / route handler), never in client components.\n- Content-Security-Policy: if the site sets CSP headers, checkout.razorpay.com (script-src, frame-src) and api.razorpay.com (connect-src) must be allowed. If headers live outside the repo, list this as a manual step for the user (MANUAL USER STEP \u2014 document it in your output; never attempt it yourself).\n- Multi-currency: instruct the user to verify the currency is enabled on their merchant account before sending; do not attempt to verify it yourself.\n\n=== REQUIREMENTS ===\n\n- Never hardcode credentials; load from environment\n- KEY_SECRET must never reach the frontend\n- Verify the signature server-side before marking any order paid\n- Use constant-time comparison for signature verification\n- Payment verification must be idempotent\n- Match the project's existing code style, router, and error-response shape\n- Don't create DB tables unless the project already has a DB; otherwise store the Razorpay order id on the existing order record\n\n=== REFERENCE ===\n\n- Web Standard Checkout integration: https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/integration-steps/\n- Orders API: https://razorpay.com/docs/api/orders/\n- Signature verification: https://razorpay.com/docs/payments/server-integration/nodejs/payment-gateway/verify-signature/\n- Test cards: https://razorpay.com/docs/payments/payments/test-card-details/\n\n=== OUTPUT ===\n\n1. List files created or modified\n2. Show sample curls for POST /api/create-order and POST /api/verify-payment with expected responses \u2014 documentation only; do not execute them\n3. List the manual steps the user must perform (you must NOT perform any of these):\n   - Run the dependency install command (state it exactly)\n   - Set RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET in their environment\n   - If CSP headers are managed outside the repo: allow checkout.razorpay.com and api.razorpay.com\n4. Explain how the user can verify manually: start their app, click the pay button, pay with a Razorpay test card (see reference URL) \u2014 any future expiry, any CVV, then complete the test OTP or simulated bank page step \u2014 and confirm the handler fires, /api/verify-payment returns success, and the internal order flips to paid\n5. Confirm compliance with the GUARDRAILS: nothing committed, nothing pushed, nothing executed, no .env file read or written\n\nBegin integration now.\n"
};

<HomeShell>
  <HomeMain>
    <HomeHero>
      <HomeNav cc="IN" />
    </HomeHero>

    <HomeAICards cc="IN" onCopyPrompt={makeCopyPrompt(PROMPT_TEXTS)} onCopy={onCopyClick} />

    <HomePayments cc="IN" />

    <HomePOS />

    <HomeBanking />

    <HomePartners />

    <HomeAgents onCopy={onCopyClick} />
  </HomeMain>

  <HomeFooter cc="IN" />
</HomeShell>
