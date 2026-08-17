from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Variable simple solicitada en la guía
    usuario = "Carlos"
    return render_template('index.html', usuario=usuario)

@app.route('/productos')
def productos():
    # Lista de diccionarios con datos de Dermopiel
    servicios = [
        {"id": 1, "nombre": "limpieza facial profunda", "precio": 35.00, "disponible": True, "categoria": "Faciales"},
        {"id": 2, "nombre": "peeling quimico", "precio": 60.00, "disponible": False, "categoria": "Tratamientos Avanzados"},
        {"id": 3, "nombre": "masaje descontracturante", "precio": 45.00, "disponible": True, "categoria": "Corporales"},
        {"id": 4, "nombre": "podologia clinica", "precio": 25.00, "disponible": True, "categoria": "Cuidado Especial"}
    ]
    return render_template('productos.html', servicios=servicios)

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html')

if __name__ == '__main__':
    app.run(debug=True)