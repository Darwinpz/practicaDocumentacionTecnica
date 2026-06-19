# AI_USAGE.md

## Uso de Inteligencia Artificial

### Herramienta utilizada

* **Herramienta:** ChatGPT (OpenAI GPT-5.5)
* **Propósito:** Mejorar la calidad, robustez y mantenibilidad de un programa Python para realizar la suma de dos números.

---

## Prompt utilizado

```text
Mejora el siguiente código, hazlo más robusto y completo:

# Programa básico para sumar dos números

# Pedir los números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar la suma
resultado = numero1 + numero2

# Mostrar el resultado
print("La suma es:", resultado)
```

---

## Código original

```python
# Programa básico para sumar dos números

# Pedir los números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar la suma
resultado = numero1 + numero2

# Mostrar el resultado
print("La suma es:", resultado)
```

---

## Código generado

```python
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
    print("      CALCULADORA DE SUMA")
    print("=" * 40)

    numero1 = obtener_numero("Ingresa el primer número: ")
    numero2 = obtener_numero("Ingresa el segundo número: ")

    resultado = numero1 + numero2

    print("\n📊 Resultado")
    print(f"{numero1} + {numero2} = {resultado}")

if __name__ == "__main__":
    main()
```

---

## Cambios realizados

### 1. Validación de entrada de datos

**Cambio:**
Se creó la función `obtener_numero()` utilizando un bloque `try-except`.

**Antes:**

```python
numero1 = float(input("Ingresa el primer número: "))
```

**Después:**

```python
def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
```

**Motivo:**
Evita que el programa termine abruptamente cuando el usuario introduce texto u otros valores no numéricos.

---

### 2. Reutilización de código

**Cambio:**
La lógica para solicitar números se encapsuló en una función.

**Motivo:**
Reduce duplicación de código y facilita futuras modificaciones o ampliaciones.

---

### 3. Uso de función principal (`main`)

**Cambio:**
Se creó una función principal para contener el flujo del programa.

**Antes:**
Todo el código se ejecutaba directamente.

**Después:**

```python
def main():
    ...
```

**Motivo:**
Mejora la organización del código y sigue buenas prácticas de desarrollo en Python.

---

### 4. Uso de la condición `if __name__ == "__main__"`

**Cambio:**
Se añadió:

```python
if __name__ == "__main__":
    main()
```

**Motivo:**
Permite reutilizar el archivo como módulo sin ejecutar automáticamente el programa.

---

### 5. Mejora de la experiencia de usuario

**Cambio:**
Se añadieron títulos, separadores visuales y mensajes más descriptivos.

**Ejemplo:**

```python
print("=" * 40)
print("      CALCULADORA DE SUMA")
print("=" * 40)
```

**Motivo:**
Hace que la interacción sea más clara y amigable para el usuario.

---

### 6. Salida formateada

**Cambio:**
Se reemplazó:

```python
print("La suma es:", resultado)
```

por

```python
print(f"{numero1} + {numero2} = {resultado}")
```

**Motivo:**
Muestra la operación completa realizada, facilitando la comprensión del resultado.

---

## Beneficios obtenidos

* Mayor robustez ante errores de entrada.
* Mejor organización y mantenibilidad del código.
* Cumplimiento de buenas prácticas de Python.
* Código más reutilizable y escalable.
* Mejor experiencia de usuario.
* Mayor claridad en la salida generada.

---

## Conclusión

La asistencia de IA permitió transformar un script básico en una versión más robusta, estructurada y mantenible, incorporando validación de errores, modularización y buenas prácticas de programación sin alterar la funcionalidad principal del programa.
