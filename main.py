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


with tab2:
    st.subheader("Arbitragem entre 3 resultados (1X2)")

    st.markdown("### Odds Bet365")
    odd1_a = st.number_input("Vitória Bet365", min_value=1.01, step=0.10, key="v1")
    oddx_a = st.number_input("Empate Bet365", min_value=1.01, step=0.10, key="x1")
    odd2_a = st.number_input("Derrota Bet365", min_value=1.01, step=0.10, key="d1")

    st.markdown("### Odds da Casa B")
    odd1_b = st.number_input("Vitória (Casa B)", min_value=1.01, step=0.10, key="v2")
    oddx_b = st.number_input("Empate (Casa B)", min_value=1.01, step=0.10, key="x2")
    odd2_b = st.number_input("Derrota (Casa B)", min_value=1.01, step=0.10, key="d2")

    if st.button("Verificar Arbitragem"):
        best_odd1 = max(odd1_a, odd1_b)
        best_oddx = max(oddx_a, oddx_b)
        best_odd2 = max(odd2_a, odd2_b)

        inv1 = 1 / best_odd1
        invx = 1 / best_oddx
        inv2 = 1 / best_odd2

        soma = inv1 + invx + inv2
        lucro_maximo_percentual = (1 - soma) * 100

        st.markdown(f"""
        **Melhores odds encontradas:**
        - Vitória: `{best_odd1}`
        - Empate: `{best_oddx}`
        - Derrota: `{best_odd2}`
        """)

        if soma < 1:
            st.success(f"✅ Arbitragem detectada! Lucro máximo possível: **{lucro_maximo_percentual:.2f}%**")

            investimento_total = 100 
            aposta1 = (inv1 / soma) * investimento_total
            apostax = (invx / soma) * investimento_total
            aposta2 = (inv2 / soma) * investimento_total

            retorno1 = aposta1 * best_odd1
            retornox = apostax * best_oddx
            retorno2 = aposta2 * best_odd2

            lucro_real = min(retorno1, retornox, retorno2) - investimento_total

            if lucro_real > 0:
                investimento_necessario = (100 * lucro_real) / lucro_real
                fator = 100 / lucro_real

                st.markdown(f"""
                💰 Para obter um lucro garantido de **R$ {lucro_real:.2f}**, você deve investir **R$ 100.00**

                📊 Divisão das apostas:
                - Aposte **R$ {aposta1:.2f}** na **Vitória ({best_odd1})**
                - Aposte **R$ {apostax:.2f}** no **Empate ({best_oddx})**
                - Aposte **R$ {aposta2:.2f}** na **Derrota ({best_odd2})**

                🔐 Lucro garantido: **R$ {lucro_real:.2f}** ({lucro_maximo_percentual:.2f}%)
                """)
        else:
            st.error("❌ Não há arbitragem com essas odds.")