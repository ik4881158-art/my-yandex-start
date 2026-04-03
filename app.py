from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

def search(query):
    results = []
    # Ищем файлы в текущей папке
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read()
                count = text.lower().count(query.lower())
                if count > 0:
                    results.append({'name': filename, 'count': count, 'text': text[:100] + "..."})
    
    results.sort(key=lambda x: x['count'], reverse=True)
    return results

# HTML-код страницы (дизайн нашего Яндекса)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Мой Поисковик</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; text-align: center; }
        input { padding: 10px; width: 300px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px 20px; background: #ffcc00; border: none; border-radius: 5px; cursor: pointer; }
        .result { text-align: left; margin: 20px auto; width: 500px; border-bottom: 1px solid #eee; padding-bottom: 10px; }
        h2 { color: #d00; }
    </style>
</head>
<body>
    <h1>Наш Яндекс</h1>
    <form method="GET">
        <input type="text" name="q" placeholder="Что ищем?" value="{{ query }}">
        <button type="submit">Найти</button>
    </form>

    {% if results %}
        <p>Найдено результатов: {{ results|length }}</p>
        {% for res in results %}
            <div class="result">
                <h3>{{ res.name }}</h3>
                <p>Упоминаний: <b>{{ res.count }}</b></p>
                <p>{{ res.text }}</p>
            </div>
        {% endfor %}
    {% elif query %}
        <p>Ничего не найдено :(</p>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def index():
    query = request.args.get('q', '')
    results = []
    if query:
        results = search(query)
    return render_template_string(HTML_TEMPLATE, results=results, query=query)

if __name__ == '__main__':
    # Render передает порт в переменной окружения PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
