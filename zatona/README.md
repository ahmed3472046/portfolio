# Zatona Market

A simple product and order management system with two interfaces: Seller and Buyer.

## Project Structure

```
zatona/
├── app.py                 # Flask app entry point and routes only
├── models.py               # Database models (Product, Order)
├── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css       # All page styling
│   └── js/
│       └── script.js       # Delete confirmation + auto-hide flash messages
└── templates/
    ├── index.html          # Home page
    ├── seller.html         # Seller dashboard
    └── buyer.html          # Buyer page
```

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the server:
   ```
   python app.py
   ```
3. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

The SQLite database is created automatically at `instance/erp.db` the first time you run the server, seeded with two sample products (Laptop, Mouse).

## What Changed from the Original Single-File Version

- **`models.py`**: Contains the `db` instance and models (`Product`, `Order`) on their own, so they can be imported anywhere without redefining them.
- **`app.py`**: Now imports `db` and the models from `models.py`, and uses `render_template()` instead of `render_template_string()` — meaning it reads from real HTML files in the `templates/` folder.
- **`templates/*.html`**: The same three pages as before, but now they link to a shared CSS file and a shared script instead of having styles and scripts embedded inline.
- **`static/css/style.css`**: All the `<style>` blocks that were duplicated across the three pages have been merged into a single file.
- **`static/js/script.js`**: Added a delete confirmation (previously an inline `onclick="confirm(...)"`) and an auto-hide behavior for success/error flash messages after 4 seconds.

Everything works with the exact same logic as before — just organized into separate files, connected via `url_for()` and imports.