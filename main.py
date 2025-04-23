import streamlit as st

st.title("Cálculo de Arbitragem")

tab1, tab2 = st.tabs(["Arbitragem 2 Odds", "Arbitragem 6 Odds"])

with tab1:
    def calcular_arbitragem_por_investimento(odd1, odd2, investimento_total):
        inv1 = 1 / odd1
        inv2 = 1 / odd2
        soma = inv1 + inv2

        if soma >= 1:
            st.error("❌ Não há arbitragem com essas odds.")
            return

        lucro_maximo_percentual = (1 - soma) * 100

        aposta1 = (inv1 / soma) * investimento_total
        aposta2 = investimento_total - aposta1

        retorno1 = aposta1 * odd1
        retorno2 = aposta2 * odd2
        retorno_garantido = min(retorno1, retorno2)
        lucro = retorno_garantido - investimento_total

        st.markdown(f"""
        ✅ **Arbitragem possível!**

        - Odd 1: **{odd1:.2f}**
        - Odd 2: **{odd2:.2f}**

        💰 Investimento total: **R$ {investimento_total:.2f}**

        📊 Distribuição:
        - Aposte **R$ {aposta1:.2f}** na odd {odd1}
        - Aposte **R$ {aposta2:.2f}** na odd {odd2}

        🔐 Lucro garantido: **R$ {lucro:.2f}** ({lucro_maximo_percentual:.2f}%)
        """)

    odd1 = round(st.number_input("Odd da primeira casa", min_value=1.01, step=0.10), 2)
    odd2 = round(st.number_input("Odd da segunda casa", min_value=1.01, step=0.10), 2)
    investimento_total = st.number_input("Quanto deseja investir no total?", min_value=1.00, step=1.00)

    if st.button("Calcular Arbitragem"):
        calcular_arbitragem_por_investimento(odd1, odd2, investimento_total)
