import streamlit as st
st.set_page_config(page_title="Dukan Hisab - Chai Wala", layout="centered")
st.title("Dukan Hisab - Chai Wala Version")
st.caption("Online Demo - Customer ke liye")

if "products" not in st.session_state:
    st.session_state.products = [{"name": "chai", "price": 200, "stock": 48}]
if "earning" not in st.session_state:
    st.session_state.earning = 0

tab1, tab2, tab3 = st.tabs(["Bechna", "Stock Dekhna", "Add Karna"])

with tab1:
    st.subheader("Product Bechna")
    prod_names = [p["name"] for p in st.session_state.products]
    selected = st.selectbox("Product Select Karo", prod_names)
    qty = st.number_input("Kitna bechna hai?", min_value=1, value=1)
    if st.button("Bech Do"):
        for p in st.session_state.products:
            if p["name"] == selected:
                if p["stock"] >= qty:
                    p["stock"] -= qty
                    st.session_state.earning += p["price"] * qty
                    st.success(f"{qty} {selected} bech diya!")

with tab2:
    st.subheader("Stock")
    st.write(f"Total Earning: Rs. {st.session_state.earning}")
    st.dataframe(st.session_state.products)

with tab3:
    st.subheader("Naya Product Add Karo")
    name = st.text_input("Product ka naam")
    price = st.number_input("Price", min_value=1)
    stock = st.number_input("Stock", min_value=1)
    if st.button("Add Karo"):
        if name:
            st.session_state.products.append({"name": name, "price": price, "stock": stock})
            st.success(f"{name} add ho gaya!")
