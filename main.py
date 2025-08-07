# -*- coding: utf-8 -*-
import streamlit as st
from modules import detect_modules, generate_schema, generate_pseudocode

# Fancy header
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#00BFFF; margin-bottom:0;">✨ High-Level to Low-Level Architecture Tool ✨</h1>
        <p style="color:#fafafa; font-size:1.2em;">
            Transform your ideas into technical blueprints instantly!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown("### 📝 Enter a high-level business requirement:")
    requirement = st.text_area("", placeholder="e.g., Users can register, login, browse products, add to cart, and checkout.", height=90)

if requirement:
    modules = detect_modules(requirement)
    st.success("✅ **Identified Modules:**")
    st.write(", ".join(modules) if modules else "No modules identified.")

    st.markdown("#### 🗄️ Generated Database Schema (SQL)")
    st.code(generate_schema(modules), language="sql")

    st.markdown("#### 🤖 Generated Pseudocode")
    st.code(generate_pseudocode(modules), language="python")
else:
    st.info("⬆️ Please enter a business requirement above to get started.")