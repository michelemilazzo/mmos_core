from __future__ import unicode_literals

app_name = "mmos_core"
app_title = "MMOS"
app_publisher = "OneKey SRL"
app_description = "MMOS Business Management Platform - Powered by OneKeyco"
app_icon = "octicon octicon-file-directory"
app_color = "#0057B8"
app_email = "support@onekeyco.com"
app_license = "MIT"
app_version = "1.0.0"

# ── Branding ──────────────────────────────────────────────
brand_html = '<img src="/assets/mmos_core/img/mmos-logo.svg" alt="MMOS" class="brand-logo" style="height:26px;vertical-align:middle;"> <span style="font-weight:600;color:#0057B8;font-size:18px;">MMOS</span>'
favicon = "/assets/mmos_core/img/mmos-favicon.svg"

# ── Lifecycle hooks ───────────────────────────────────────
after_install = "mmos_core.install.after_install"
after_migrate = "mmos_core.install.after_migrate"

# ── Override Jinja context (support links) ────────────────
update_website_context = "mmos_core.overrides.update_website_context"

# ── Fixtures (system defaults) ────────────────────────────
fixtures = [
    {
        "doctype": "System Settings",
        "filters": [["name", "=", "System Settings"]]
    }
]
