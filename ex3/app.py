import streamlit as st
from io import StringIO
import unittest
from domain import is_strong_password

st.title("🔐 Validador de contraseñas (i18n rules)")

username = st.text_input("Username", value="José")
pwd = st.text_input("Password", type="password", value="Abcdef1!xy")

if st.button("Validar"):
    ok = is_strong_password(pwd, username)
    if ok:
        st.success("✅ Contraseña fuerte")
    else:
        st.error("❌ Contraseña inválida (revisa reglas)")

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
