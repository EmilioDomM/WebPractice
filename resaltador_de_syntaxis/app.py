from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def lexerAritmetico(codigo):
    patrones = [
        (r'\b(print|input|import)\b', 'Palabra reservada', 'palabra-reservada'),  # Palabras reservadas
        (r'[a-zA-Z_]\w*', 'Variable', 'variable'),  # Variables
        (r'\d+\.\d*([eE][-+]?\d+)?', 'Real', 'real'),  # Numeros reales
        (r'\d+', 'Entero', 'entero'),  # Numeros enteros
        (r'#.*', 'Comentario', 'comentario'),  # Comentarios
        (r'=', 'Asignación', 'asignacion'),  # Asignacion
        (r'\+', 'Suma', 'suma'),  # Suma
        (r'-', 'Resta', 'resta'),  # Resta
        (r'\*', 'Multiplicación', 'multiplicacion'),  # Multiplicacion
        (r'/', 'División', 'division'),  # Division
        (r'\^', 'Potencia', 'potencia'),  # Potencia
        (r'\(', 'Parentesis que abre', 'parentesis'),  # Parentesis izquierdo
        (r'\)', 'Parentesis que cierra', 'parentesis'),  # Parentesis derecho
        (r'(["\'])(?:(?=(\\?))\2.)*?\1', 'String', 'string'),  # Strings
        (r'\[', 'Corchete que abre', 'corchete'),  # Corchete izquierdo
        (r'\]', 'Corchete que cierra', 'corchete'),  # Corchete derecho
        (r'\{', 'Llave que abre', 'llave'),  # Llave izquierda
        (r'\}', 'Llave que cierra', 'llave'),  # Llave derecha
        (r',', 'Coma', 'coma')  # Coma
    ]

    errores_sintacticos = [
        (r'(\d+\.\d*([eE][-+]?\d+)?|\d+)', 'Número mal formado', 10),  # Números mal formados
        (r'(int|float|str)', 'Palabra reservada mal utilizada', 10),  # Palabras reservadas mal utilizadas
        (r'([^"\\\n]*"([^"\\]|\\.)*)(?!"|\n)', 'String sin cerrar', 20),  # String sin cerrar
        (r'(?P<cita>["\'])(?:(?=(\\?))\2.)*?(?P=cita)', 'Uso incorrecto de comillas', 10),  # Comillas diferentes dentro de un string
        (r'(\([^()]*)(?!\))', 'Paréntesis sin cerrar', 10),  # Paréntesis sin cerrar
        (r'(\[[^\[\]]*)(?!\])', 'Corchete sin cerrar', 10),  # Corchete sin cerrar
        (r'(\{[^{}\n]*)(?!\})', 'Llave sin cerrar', 10)  # Llave sin cerrar
    ]

    lineas = codigo.split('\n')
    tokens = []
    errores = []

    for num_linea, linea in enumerate(lineas, start=1):
        try:
            compile(linea, '<string>', 'exec')

            while linea:
                token_encontrado = False
                for patron, tipo, clase_css in patrones:
                    match = re.match(patron, linea)
                    if match:
                        token = match.group(0)
                        tokens.append((token, tipo, clase_css))
                        linea = linea[len(token):].lstrip()
                        token_encontrado = True
                        break

                if not token_encontrado:
                    errores.append((f"Error léxico en línea {num_linea}: Token no reconocido", linea))
                    break
        except SyntaxError as e:
            errores.append((f"Error de sintaxis en línea {num_linea}: {e}", ""))
            while linea:
                error_encontrado = False
                for patron, mensaje, _ in errores_sintacticos:
                    match = re.match(patron, linea)
                    if match:
                        token = match.group(0)
                        errores.append((f"{token}\t{mensaje}", ""))
                        linea = linea[len(token):].lstrip()
                        error_encontrado = True
                        break

                if not error_encontrado:
                    errores.append((f"Error léxico en línea {num_linea}: Token no reconocido", linea))


    return tokens, errores

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.get_json()
    codigo = data['codigo']
    tokens, errores = lexerAritmetico(codigo)
    return jsonify({'tokens': tokens, 'errores': errores})

if __name__ == '__main__':
    app.run(debug=True)
