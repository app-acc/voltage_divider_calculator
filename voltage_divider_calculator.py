import streamlit as st
import schemdraw
import schemdraw.elements as elm

# d = schemdraw.Drawing()
# d.add(elm.Dot(label="V1", width=10, heig=10))
# d.add(elm.Resistor(label="R1"))
# d.add(elm.Dot(label="V"))
# d.add(elm.Resistor(label="R2"))
# d.add(elm.Dot(label="V2"))
# d.draw()
# d.save("r.png", dpi=200)

st.image("circuit.png")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    v1 = st.number_input("V1", value=1000)
with col2:
    r1 = st.number_input("R1", value=50)
with col3:
    v = st.number_input("V", value=500)
with col4:
    r2 = st.number_input("R2", value=50)
with col5:
    v2 = st.number_input("V2", value=0)

v1_ans = ((r1 + r2) * v) / r2 - r1 * v2 / r2
v_ans = (r2 * v1 + r1 * v2) / (r1 + r2)
r1_ans = ((v1 - v) * r2) / (v - v2)
r2_ans = ((v - v2) * r1) / (v1 - v)
v2_ans = (r1 * v - r2 * v1 + r2 * v) / r1

with col1:
    st.write(v1_ans)
with col2:
    st.write(r1_ans)
with col3:
    st.write(v_ans)
with col4:
    st.write(r2_ans)
with col5:
    st.write(v2_ans)
