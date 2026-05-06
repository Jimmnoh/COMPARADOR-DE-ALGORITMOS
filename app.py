#!/usr/bin/env python3


import random
import time
import webbrowser
import threading
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder=".")

# ──────────────────────────────────────────────
#  ALGORITMOS
# ──────────────────────────────────────────────

def bubble_sort(arr):
    a = arr[:]
    steps = 0
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            steps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a, steps

def selection_sort(arr):
    a = arr[:]
    steps = 0
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            steps += 1
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a, steps

def insertion_sort(arr):
    a = arr[:]
    steps = 0
    for i in range(1, len(a)):
        key = a[i]; j = i - 1
        while j >= 0 and a[j] > key:
            steps += 1; a[j + 1] = a[j]; j -= 1
        steps += 1; a[j + 1] = key
    return a, steps

def merge_sort(arr):
    steps = [0]
    def merge(l, r):
        res = []; i = j = 0
        while i < len(l) and j < len(r):
            steps[0] += 1
            if l[i] <= r[j]: res.append(l[i]); i += 1
            else:             res.append(r[j]); j += 1
        res.extend(l[i:]); res.extend(r[j:])
        return res
    def ms(a):
        if len(a) <= 1: return a
        m = len(a) // 2
        return merge(ms(a[:m]), ms(a[m:]))
    return ms(arr[:]), steps[0]

def quick_sort(arr):
    steps = [0]
    def partition(a, lo, hi):
        pivot = a[hi]; i = lo - 1
        for j in range(lo, hi):
            steps[0] += 1
            if a[j] <= pivot: i += 1; a[i], a[j] = a[j], a[i]
        a[i+1], a[hi] = a[hi], a[i+1]
        return i + 1
    def qs(a, lo, hi):
        if lo < hi:
            p = partition(a, lo, hi)
            qs(a, lo, p - 1); qs(a, p + 1, hi)
    a = arr[:]
    if a: qs(a, 0, len(a) - 1)
    return a, steps[0]

def heap_sort(arr):
    a = arr[:]; steps = 0; n = len(a)
    def heapify(n, i):
        nonlocal steps
        lg = i; l = 2*i+1; r = 2*i+2
        steps += 1
        if l < n and a[l] > a[lg]: lg = l
        steps += 1
        if r < n and a[r] > a[lg]: lg = r
        if lg != i: a[i], a[lg] = a[lg], a[i]; heapify(n, lg)
    for i in range(n//2-1, -1, -1): heapify(n, i)
    for i in range(n-1, 0, -1): a[0], a[i] = a[i], a[0]; heapify(i, 0)
    return a, steps

def shell_sort(arr):
    a = arr[:]; steps = 0; n = len(a); gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            tmp = a[i]; j = i
            while j >= gap and a[j-gap] > tmp:
                steps += 1; a[j] = a[j-gap]; j -= gap
            steps += 1; a[j] = tmp
        gap //= 2
    return a, steps

def counting_sort(arr):
    if not arr: return arr[:], 0
    a = arr[:]; steps = 0
    mn, mx = min(a), max(a); rng = mx - mn + 1
    count = [0]*rng; out = [0]*len(a)
    for x in a: steps += 1; count[x-mn] += 1
    for i in range(1, rng): steps += 1; count[i] += count[i-1]
    for x in reversed(a): steps += 1; out[count[x-mn]-1] = x; count[x-mn] -= 1
    return out, steps

def radix_sort(arr):
    if not arr: return arr[:], 0
    steps = [0]
    off = -min(arr) if min(arr) < 0 else 0
    a = [x + off for x in arr]
    def cpass(a, exp):
        n = len(a); out = [0]*n; cnt = [0]*10
        for x in a: steps[0] += 1; cnt[(x//exp)%10] += 1
        for i in range(1,10): cnt[i] += cnt[i-1]
        for x in reversed(a): steps[0] += 1; idx=(x//exp)%10; cnt[idx]-=1; out[cnt[idx]]=x
        return out
    mx = max(a); exp = 1
    while mx // exp > 0: a = cpass(a, exp); exp *= 10
    return [x-off for x in a], steps[0]

def tim_sort(arr):
    a = arr[:]; steps = 0; RUN = 32
    def ins(a, l, r):
        nonlocal steps
        for i in range(l+1, r+1):
            k = a[i]; j = i-1
            while j >= l and a[j] > k: steps+=1; a[j+1]=a[j]; j-=1
            a[j+1] = k
    def mrg(a, l, m, r):
        nonlocal steps
        L = a[l:m+1]; R = a[m+1:r+1]; i=j=0; k=l
        while i<len(L) and j<len(R):
            steps+=1
            if L[i]<=R[j]: a[k]=L[i]; i+=1
            else:           a[k]=R[j]; j+=1
            k+=1
        while i<len(L): a[k]=L[i]; i+=1; k+=1
        while j<len(R): a[k]=R[j]; j+=1; k+=1
    n = len(a)
    for i in range(0, n, RUN): ins(a, i, min(i+RUN-1, n-1))
    sz = RUN
    while sz < n:
        for l in range(0, n, sz*2):
            m = min(l+sz-1, n-1); r = min(l+2*sz-1, n-1)
            if m < r: mrg(a, l, m, r)
        sz *= 2
    return a, steps

ALGORITHMS = [
    ("Bubble Sort",    bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Shell Sort",     shell_sort),
    ("Merge Sort",     merge_sort),
    ("Quick Sort",     quick_sort),
    ("Heap Sort",      heap_sort),
    ("Tim Sort",       tim_sort),
    ("Counting Sort",  counting_sort),
    ("Radix Sort",     radix_sort),
]

# ──────────────────────────────────────────────
#  RUTAS
# ──────────────────────────────────────────────

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/benchmark", methods=["POST"])
def benchmark():
    data = request.get_json()
    n    = int(data.get("n", 20))
    lo   = int(data.get("lo", 1))
    hi   = int(data.get("hi", 100))

    n  = max(1, min(n, 100_000))
    if lo > hi: lo, hi = hi, lo

    arr = [random.randint(lo, hi) for _ in range(n)]

    results = []
    for name, func in ALGORITHMS:
        t0 = time.perf_counter_ns()
        sorted_arr, steps = func(arr[:])
        elapsed = time.perf_counter_ns() - t0
        results.append({"name": name, "steps": steps, "time_ns": elapsed})

    results.sort(key=lambda x: x["time_ns"])
    for i, r in enumerate(results):
        r["position"] = i + 1

    return jsonify({"array": arr, "results": results})

# ──────────────────────────────────────────────
#  ARRANQUE
# ──────────────────────────────────────────────

def open_browser():
    import time as _t
    _t.sleep(0.8)
    webbrowser.open("http://localhost:5050")

if __name__ == "__main__":
    print("\n  ╔══════════════════════════════════════╗")
    print("  ║   SortBench — Iniciando servidor...  ║")
    print("  ║   http://localhost:5050              ║")
    print("  ╚══════════════════════════════════════╝\n")
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(port=5050, debug=False)
