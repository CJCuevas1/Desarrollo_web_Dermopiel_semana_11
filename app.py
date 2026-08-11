from flask import Flask, render_template

app = Flask(__name__)

# Ruta Principal (Carga la página informativa)
@app.route('/')
def index():
    return render_template('index.html')

# Módulo de Productos
@app.route('/productos')
def productos():
    lista_productos = [
        {"id": 1, "nombre": "Crema Hidratante Facial", "precio": 25.00, "stock": 15},
        {"id": 2, "nombre": "Sérum Vitamina C", "precio": 38.50, "stock": 10},
        {"id": 3, "nombre": "Mascarilla Purificante", "precio": 18.00, "stock": 20}
    ]
    return render_template('productos.html', productos=lista_productos)

# Módulo de Clientes
@app.route('/clientes')
def clientes():
    lista_clientes = [
        {"id": 1, "nombre": "María García", "telefono": "0991234567", "email": "maria@gmail.com"},
        {"id": 2, "nombre": "Juan Pérez", "telefono": "0987654321", "email": "juan@gmail.com"}
    ]
    return render_template('clientes.html', clientes=lista_clientes)

# Módulo de Proveedores
@app.route('/proveedores')
def proveedores():
    lista_proveedores = [
        {"id": 1, "empresa": "DermoLab S.A.", "contacto": "Dra. Ana López", "telefono": "022555123"},
        {"id": 2, "empresa": "Cosmética Natural Co.", "contacto": "Carlos Ruiz", "telefono": "022888456"}
    ]
    return render_template('proveedores.html', proveedores=lista_proveedores)

# Módulo de Facturación
@app.route('/facturacion')
def facturacion():
    lista_facturas = [
        {"num": "001-001-0001", "cliente": "María García", "fecha": "2026-08-11", "total": 63.50},
        {"num": "001-001-0002", "cliente": "Juan Pérez", "fecha": "2026-08-11", "total": 25.00}
    ]
    return render_template('facturacion.html', facturas=lista_facturas)

if __name__ == '__main__':
    app.run(debug=True)