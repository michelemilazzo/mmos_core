def update_website_context(context):
    """Override support and help links with MMOS/OneKey URLs"""
    context["help_url"] = "https://support.onekeyco.com"
    context["support_url"] = "https://support.onekeyco.com"
    context["docs_url"] = "https://docs.onekeyco.com"
    context["community_url"] = "https://community.onekeyco.com"
    context["company"] = "OneKey"
    context["brand"] = "MMOS"
    return context
