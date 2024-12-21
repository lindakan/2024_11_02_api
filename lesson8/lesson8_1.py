import streamlit as st

# 初始化計數器
if "visit_counter" not in st.session_state:
    st.session_state.visit_counter = 0

def update_counter(increment=1, decrement=0):
    """更新計數器的值"""
    st.session_state.visit_counter += increment
    st.session_state.visit_counter -= decrement

# 顯示頁面標題和計數器
st.header(f"計數器: {st.session_state.visit_counter}")

# 添加按鈕控制計數器
st.button(
    label="更新計數",
    key="counter_button",
    help="點擊後增加5並減少3",
    on_click=update_counter,
    kwargs={"increment": 5, "decrement": 3}
)

# 顯示所有session狀態（用於調試）
st.write("Session 狀態:", st.session_state)


