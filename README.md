# ⬡ SortBench — Comparador de Algoritmos de Ordenamiento

> Herramienta interactiva que genera un arreglo aleatorio y mide el rendimiento de **10 algoritmos de ordenamiento** en tiempo real, mostrando resultados ordenados por tiempo de ejecución en nanosegundos.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-CSS3-E34F26?style=flat-square&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=flat-square)

---

## 📋 Tabla de Contenidos

- [Vista Previa](#-vista-previa)
- [Requisitos](#-requisitos)
- [Instalación y Ejecución](#-instalación-y-ejecución)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Algoritmos Implementados](#-algoritmos-implementados)
- [Cómo Funciona](#-cómo-funciona)
- [Modificar el Proyecto](#-modificar-el-proyecto)

---

## 🖥 Vista Previa

La interfaz web permite configurar los parámetros, ejecutar el benchmark y visualizar los resultados con barras de rendimiento proporcionales, medallas para los 3 primeros lugares y un resumen comparativo.

---

## ✅ Requisitos

| Requisito | Versión mínima |
|-----------|---------------|
| Python    | 3.8+          |
| Flask     | 2.0+          |

> No se requiere ninguna librería externa para los algoritmos. Flask es la única dependencia.

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sortbench.git
cd sortbench
```

### 2. Instalar dependencias

```bash
pip install flask
```

### 3. Ejecutar

**Windows:**
```bash
# Opción A — doble clic en:
run.bat

# Opción B — desde terminal:
python app.py
```

**Linux / macOS:**
```bash
# Opción A:
bash run.sh

# Opción B — desde terminal:
python3 app.py
```

### 4. Abrir en el navegador

El programa abre el navegador automáticamente en:

```
http://localhost:5050
```

Si no abre automáticamente, pega esa URL en tu navegador.

---

## 📁 Estructura del Proyecto

```
sortbench/
├── app.py       ← Servidor Flask + implementación de los 10 algoritmos
├── index.html   ← Interfaz web (frontend completo en un solo archivo)
├── run.bat      ← Lanzador para Windows
├── run.sh       ← Lanzador para Linux / macOS
└── README.md    ← Este archivo
```

---

## 🔢 Algoritmos Implementados

| # | Algoritmo | Complejidad Promedio | Complejidad Peor Caso |
|---|-----------|---------------------|-----------------------|
| 1 | Bubble Sort    | O(n²)        | O(n²)         |
| 2 | Selection Sort | O(n²)        | O(n²)         |
| 3 | Insertion Sort | O(n²)        | O(n²)         |
| 4 | Shell Sort     | O(n log n)   | O(n²)         |
| 5 | Merge Sort     | O(n log n)   | O(n log n)    |
| 6 | Quick Sort     | O(n log n)   | O(n²)         |
| 7 | Heap Sort      | O(n log n)   | O(n log n)    |
| 8 | Tim Sort       | O(n log n)   | O(n log n)    |
| 9 | Counting Sort  | O(n + k)     | O(n + k)      |
| 10| Radix Sort     | O(nk)        | O(nk)         |

Todos los algoritmos están implementados **desde cero** en Python, sin usar `sorted()` ni `.sort()`.

---

## ⚙ Cómo Funciona

```
Usuario (navegador)          Backend (Python/Flask)
       │                              │
       │  Ingresa: n, mín, máx        │
       │ ──── POST /benchmark ──────► │
       │                              │  Genera array aleatorio
       │                              │  Ejecuta los 10 algoritmos
       │                              │  Mide tiempo (nanosegundos)
       │                              │  Cuenta pasos por algoritmo
       │                              │  Ordena por tiempo ↑
       │ ◄──── JSON con resultados ── │
       │                              │
       │  Renderiza tabla + barras    │
       │  Muestra resumen (🥇🥈🥉)    │
```

1. El usuario ingresa la **cantidad de números**, el **valor mínimo** y el **valor máximo** del rango.
2. El frontend envía una petición `POST /benchmark` al servidor Flask.
3. Python genera el arreglo aleatorio y ejecuta cada algoritmo sobre una **copia independiente** del mismo arreglo.
4. Se mide el tiempo con `time.perf_counter_ns()` (precisión de nanosegundos) y se cuentan los pasos (comparaciones/intercambios).
5. Los resultados se ordenan de menor a mayor tiempo y se devuelven como JSON.
6. El frontend renderiza la tabla con barras proporcionales y el resumen comparativo.

---

## 🔧 Modificar el Proyecto

### Agregar un nuevo algoritmo

En `app.py`:

```python
# 1. Define la función — debe retornar (lista_ordenada, pasos)
def mi_algoritmo(arr):
    a = arr[:]
    steps = 0
    # ... tu lógica aquí ...
    return a, steps

# 2. Regístralo en la lista ALGORITHMS
ALGORITHMS = [
    ...
    ("Mi Algoritmo", mi_algoritmo),  # ← agrega esta línea
]
```

### Cambiar el límite máximo de elementos

En `app.py`, línea:
```python
n = max(1, min(n, 100_000))   # cambia 100_000 por el límite que quieras
```

### Cambiar el puerto del servidor

En `app.py`, última línea:
```python
app.run(port=5050)   # cambia 5050 por el puerto deseado
```
Recuerda actualizar también la URL en `index.html` si cambias el puerto.

### Personalizar la interfaz

Todos los colores y fuentes están definidos como variables CSS al inicio de `index.html`:

```css
:root {
  --green:  #00ff9d;   /* color principal / acento */
  --bg:     #080c10;   /* fondo general */
  --panel:  #161b22;   /* fondo de paneles */
  /* ... */
}
```

---

## 📄 Licencia

MIT — libre para usar, modificar y distribuir.
