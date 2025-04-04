from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Données modifiables
produits = [
    {"id": 1, "nom": "Ordinateur", "prix": 9999.99, "stock": False},
    {"id": 2, "nom": "Smartphone", "prix": 6999.99, "stock": False},
    {"id": 3, "nom": "Tablette", "prix": 3499.99, "stock": False}
]

@app.route('/')
def index():
    return render_template('produits.html', produits=produits)

@app.route('/modifier_stock/<int:id>')
def modifier_stock(id):
    for p in produits:
        if p['id'] == id:
            p['stock'] = not p['stock']
            break
    return redirect(url_for('index'))

@app.route('/supprimer/<int:id>')
def supprimer(id):
    global produits
    produits = [p for p in produits if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()