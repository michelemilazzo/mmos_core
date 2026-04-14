from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [r for r in f.read().strip().split("\n") if r]

setup(
    name="mmos_core",
    version="1.0.0",
    description="MMOS Core - Branding and EU localization for Frappe/ERPNext",
    author="OneKey",
    author_email="support@onekeyco.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
