# Programa mejorado para sumar dos números

def obtener_numero(mensaje):
    """Solicita un número al usuario y valida la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")

def main():
    print("=" * 40)
    print("      CALCULADORA DE SUMA    ")
    print("=" * 40)

    numero1 = obtener_numero("Ingresa el primer número: ")
    numero2 = obtener_numero("Ingresa el segundo número: ")

    resultado = numero1 + numero2

    print("\n📊 Resultado")
    print(f"{numero1} + {numero2} = {resultado}")

if __name__ == "__main__":
    main()