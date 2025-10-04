import streamlit as st
from io import StringIO
import unittest
from domain import convert

st.title("💱 Conversor con comisión y redondeo bancario")

amount = st.number_input("Monto en moneda origen", min_value=0.0, value=100.0, step=1.0)
fx_rate = st.number_input("Tipo de cambio (destino/origen)", min_value=0.0001, value=6.96, step=0.01)

if st.button("Convertir"):
    try:
        result = convert(amount, fx_rate)
        st.success(f"💰 Total en moneda destino: {result}")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

st.subheader("🧪 Pruebas unitarias")

if st.button("Run tests"):
    stream = StringIO()
    suite = unittest.defaultTestLoader.discover(".", pattern="test_*.py")
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)
    st.text(stream.getvalue())
    st.write(f"✅ Passed: {result.wasSuccessful()} | "
             f"🔢 Ran: {result.testsRun} | "
             f"❌ Failures: {len(result.failures)} | Errors: {len(result.errors)}")
