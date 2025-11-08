Custom Packaging module (ready for Odoo.sh)
-----------------------------------------
Install steps:
1. Upload this folder to your custom_addons on GitHub (or extract in Odoo.sh repo).
2. Commit & push. Wait for Odoo.sh build to finish (green).
3. In Odoo, activate developer mode -> Apps -> Update Apps List.
4. Install 'Custom Packaging'.
Notes:
- Ensure models/__init__.py imports product_packaging_line before product_packaging.
- If any old conflicting views exist, delete them from Settings > Technical > User Interface > Views.
