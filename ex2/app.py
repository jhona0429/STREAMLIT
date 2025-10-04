import streamlit as st
from io import StringIO
import unittest
from domain import reorder_point

st.title("📦 Punto de reorden con stock de seguridad")

dd = st.number_input("Demanda diaria", min_value=0.0, value=50.0, step=1.0)
lt = st.number_input("Lead time (días)", min_value=0.0, value=2.0, step=0.1)
sd = st.number_input("Sigma demanda", min_value=0.0, value=10.0, step=0.5)
z = st.number_input("Z (nivel de servicio)", min_value=0.0, value=1.65, step=0.01)

if st.button("Calcular ROP"):
    try:
        rop = reorder_point(dd, lt, sd, z)
        st.success(f"✅ ROP recomendado: {rop} unidades")
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
