Comparador de Algoritmos de Ordenamiento

Herramienta interactiva que genera un arreglo aleatorio y mide el rendimiento de **10 algoritmos de ordenamiento** en tiempo real, mostrando resultados ordenados por tiempo de ejecución en nanosegundos.

Tabla de Contenidos

- [Vista Previa]
- [Requisitos]
- [Instalación y Ejecución]
- [Estructura del Proyecto]
- [Algoritmos Implementados]
- [Cómo Funciona]


Vista Previa

La interfaz web permite configurar los parámetros, ejecutar el benchmark y visualizar los resultados con barras de rendimiento proporcionales, medallas para los 3 primeros lugares y un resumen comparativo.

---

Requisitos

| Requisito | Versión mínima |
|-----------|---------------|
| Python    | 3.8+          |
| Flask     | 2.0+          |

> No se requiere ninguna librería externa para los algoritmos. Flask es la única dependencia.

---

Instalación y Ejecución

1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sortbench.git
cd sortbench
```

2. Instalar dependencias

bash
pip install flask


3. Ejecutar

Windows:
```bash
Opción A — doble clic en:
run.bat

Opción B — desde terminal:
python app.py
```

Linux / macOS:
```bash
Opción A:
bash run.sh

Opción B — desde terminal:
python3 app.py

4. Abrir en el navegador

El programa abre el navegador automáticamente en:

http://localhost:5050

Si no abre automáticamente, pega esa URL en tu navegador.

Estructura del Proyecto

sortbench/
├── app.py       ← Servidor Flask + implementación de los 10 algoritmos
├── index.html   ← Interfaz web (frontend completo en un solo archivo)
├── run.bat      ← Lanzador para Windows
├── run.sh       ← Lanzador para Linux / macOS
└── README.md    ← Este archivo



 Algoritmos Implementados

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

Cómo Funciona

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
       │  Muestra resumen (1 2 3)    │


1. El usuario ingresa la **cantidad de números**, el **valor mínimo** y el **valor máximo** del rango.
2. El frontend envía una petición `POST /benchmark` al servidor Flask.
3. Python genera el arreglo aleatorio y ejecuta cada algoritmo sobre una **copia independiente** del mismo arreglo.
4. Se mide el tiempo con `time.perf_counter_ns()` (precisión de nanosegundos) y se cuentan los pasos (comparaciones/intercambios).
5. Los resultados se ordenan de menor a mayor tiempo y se devuelven como JSON.
6. El frontend renderiza la tabla con barras proporcionales y el resumen comparativo.

