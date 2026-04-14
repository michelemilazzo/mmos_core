import frappe


def after_install():
    """Set MMOS/OneKey platform defaults after app install"""
    _set_system_defaults()


def after_migrate():
    """Ensure defaults are maintained after migrations"""
    _set_system_defaults()


def _set_system_defaults():
    settings = {
        "language": "it",
        "time_zone": "Europe/Rome",
        "country": "Italy",
        "app_name": "MMOS",
        "footer_powered_by_link": "https://onekeyco.com",
        "footer_powered_by_label": "MMOS by OneKey",
    }
    for key, value in settings.items():
        try:
            frappe.db.set_single_value("System Settings", key, value)
        except Exception:
            pass

    # Default language for new users
    frappe.db.set_default("lang", "it")
    frappe.db.commit()
