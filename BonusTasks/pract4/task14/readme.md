
## **Язык HTML-тегов с помощью менеджера контекста**

Реализовать классы для выполнения следующего примера:

```python
html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
```
Результат:

```html
<body>
<div>
<div>
<p>Первая строка.</p>
<p>Вторая строка.</p>
</div>
<div>
<p>Третья строка.</p>
</div>
</div>
</body>
```
