# Ejercicio 3 — Validador de contraseñas con reglas de negocio e i18n

## 🧩 Enfoque
Este ejercicio valida contraseñas robustas para un portal corporativo, considerando reglas de seguridad y normalización internacional (acentos, mayúsculas, etc.).

## ⚙️ Reglas implementadas
- Longitud mínima de 10 caracteres.
- Al menos una mayúscula, una minúscula, un dígito y un símbolo.
- No debe contener el nombre de usuario (sin acentos y sin distinción de mayúsculas).
- No debe tener 3 o más caracteres consecutivos idénticos.
- No debe tener espacios al inicio o al final.

## 🧪 Tests
- Casos válidos, inválidos y bordes.
- Ejecutables desde la app con botón “Run tests”.

## 🚀 Cómo ejecutar
1. Instala dependencias: `streamlit`, `unittest`.
2. Ejecuta localmente: `streamlit run app.py`.
3. O publica en [Streamlit Community Cloud](https://streamlit.io/cloud).

## 📊 Ejemplos esperados
- `"Abcdef1!xy"` con usuario `"jose"` → ✅ Válido
- `"xxJOSEyy1!"` con usuario `"José"` → ❌ Inválido
- `"Ab111cdef!"` → ❌ Inválido por repeticiones
- `"A1!bcdefgh"` → ✅ Válido
