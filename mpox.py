import streamlit as st

st.set_page_config(
    page_title="Monkey Pox",
    page_icon="🐒",
    layout="wide",
)

st.write("# Monkey Pox Simulation! 🐒")

col1, col2 = st.columns(2)
with col1:
    st.image(r"./images/mpox_image.jpeg", caption="Fig 1: The picture of a child with mpox", width=300)
with col2:  
    st.markdown(
        """
     #### Monkeypox is a viral zoonotic disease caused by the monkeypox virus, which belongs to the same family as the variola virus (the virus responsible for smallpox). While monkeypox is generally less severe than smallpox, it can cause significant illness in humans. The disease primarily occurs in Central and West Africa, but outbreaks have been reported in other parts of the world.
    """
    )

col3, col4 = st.columns([2,1])
with col3:
    st.markdown(
        """
        - **Transmission**: Monkeypox spreads through close contact with infected animals, humans, or contaminated materials. It can be transmitted via respiratory droplets, direct contact with skin lesions, or contact with bodily fluids.
        - **Symptoms**: Symptoms typically include fever, headache, muscle aches, swollen lymph nodes, and a distinctive rash that progresses from macules to pustules. The rash often spreads across the face and body.
        - **Incubation Period**: The incubation period for monkeypox is usually 6 to 13 days, but it can range from 5 to 21 days.
        - **Prevention**: Preventive measures include avoiding contact with infected individuals or animals, practicing good hygiene, and using personal protective equipment (PPE) in healthcare settings. Smallpox vaccines provide cross-protection against monkeypox.
        """
    )
with col4:
    st.image(r"./images/mpox_virus.jpeg", caption="Fig 2: The mpox virus ", width=300, use_column_width=True)