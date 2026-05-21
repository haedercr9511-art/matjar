from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "سماعات لاسلكية", "price": 149, "category": "إلكترونيات", "emoji": "🎧", "description": "صوت نقي وبطارية 30 ساعة"},
    {"id": 2, "name": "حقيبة جلد", "price": 89, "category": "أزياء", "emoji": "👜", "description": "جلد طبيعي فاخر"},
    {"id": 3, "name": "ساعة ذكية", "price": 299, "category": "إلكترونيات", "emoji": "⌚", "description": "تتبع الصحة والإشعارات"},
    {"id": 4, "name": "كتاب البرمجة", "price": 45, "category": "كتب", "emoji": "📚", "description": "تعلم Python من الصفر"},
    {"id": 5, "name": "نظارات شمسية", "price": 120, "category": "أزياء", "emoji": "🕶️", "description": "حماية UV400 بأسلوب"},
    {"id": 6, "name": "لوحة مفاتيح", "price": 199, "category": "إلكترونيات", "emoji": "⌨️", "description": "ميكانيكية مضيئة RGB"},
]

@app.route("/")
def home():
    category = request.args.get("category", "الكل")
    if category == "الكل":
        filtered = products
    else:
        filtered = [p for p in products if p["category"] == category]
    categories = ["الكل"] + list(set(p["category"] for p in products))
    return render_template("index.html", products=filtered, categories=categories, active=category)

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
