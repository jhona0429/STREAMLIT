# Ejercicio 1 — Conversor de moneda con comisión y redondeo bancario

## 🧩 Enfoque
Este ejercicio simula una pasarela de pagos que convierte montos aplicando tipo de cambio mayorista, comisión y redondeo bancario. Se rechazan pagos menores a 1.00 en moneda destino.

## ⚙️ Lógica
- Conversión con `Decimal` para precisión.
- Comisión: 1.4% + 0.30.
- Redondeo bancario `ROUND_HALF_EVEN`.
- Validaciones estrictas y errores claros.

## 🧪 Tests
- Casos normales, bordes y errores.
- Ejecutables desde la app con botón “Run tests”.

## 🚀 Cómo ejecutar
1. Instala dependencias: `streamlit`, `unittest`.
2. Ejecuta localmente: `streamlit run app.py`.
3. O publica en [Streamlit Community Cloud](https://streamlit.io/cloud).

## 📊 Ejemplos esperados
- `convert(100, 6.96)` → `685.96`
- `convert(10.5, 6.96)` → `71.76`
- `convert(250.75, 6.9)` → `1705.65`
- `convert(1.0, 1.05)` → ❌ Error: Below minimum payout
