import streamlit as st
import random

st.title("✊✋✌️ 가위바위보 게임")

choices = ["가위", "바위", "보"]
user_choice = st.selectbox("당신의 선택을 고르세요:", choices)

if st.button("대결 시작!"):
    computer_choice = random.choice(choices)

    st.write(f"👤 당신의 선택: {user_choice}")
    st.write(f"💻 컴퓨터의 선택: {computer_choice}")

    # 승패 결정 로직
    if user_choice == computer_choice:
        st.success("🤝 비겼습니다!")
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        st.success("🎉 당신이 이겼습니다!")
    else:
        st.error("😢 당신이 졌습니다.")
