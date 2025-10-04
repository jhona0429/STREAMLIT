# Ejercicio 2 — Punto de reorden (ROP) con stock de seguridad

## 🧩 Enfoque
Este ejercicio calcula el punto de reorden en inventarios considerando demanda media, variabilidad y nivel de servicio. Ideal para farmacias y retail.

## ⚙️ Lógica
- Redondeo de lead time hacia arriba.
- Cálculo de base y stock de seguridad.
- Validación de parámetros ≥ 0.
- Resultado entero y no negativo.

## 🧪 Tests
- Casos típicos, bordes y errores.
- Ejecutables desde la app con botón “Run tests”.

## 🚀 Cómo ejecutar
1. Instala dependencias: `streamlit`, `unittest`.
2. Ejecuta localmente: `streamlit run app.py`.
3. O publica en [Streamlit Community Cloud](https://streamlit.io/cloud).

## 📊 Ejemplos esperados
- `reorder_point(50, 2, 10, 1.65)` → `124`
- `reorder_point(40, 2.2, 8, 1.65)` → `143`
- `reorder_point(0, 3.5, 12, 1.96)` → `48`
- `reorder_point(30, 1.2, 0, 1.65)` → `60`
