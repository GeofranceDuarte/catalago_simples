from flash import Flash, render_template


app= Flash(__name__)

@app.router('/')
def index ():
    #lista de produtos fictícios
    produtos=[
        {"nome": "camiseta", "preco": 29.29, "imagem": "camiseta.jpg"},
        {"nome": "calça Jeans", "preco": 59.99, "imagem": "calca_jeans.jpg"},
        {"nome": "Tênis", "preco": 85.99, "imagem": "tenis.jpg"},
    ]
    return render_template('index.html', produtos=produtos)
if __name__ == '__main__':
    app.run(debug=True)