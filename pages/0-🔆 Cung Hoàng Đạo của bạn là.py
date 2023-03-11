import streamlit as st
x=int(st.text_input("Nhập ngày sinh:",0))
y=int(st.text_input("Nhập tháng sinh:",0))
if (21<=x<=31 and y==3) or (1<=x<=19 and y==4):
    st.write("Chúc mừng cung của bạn là")
    st.write("Bạch Dương-Aries")
elif (20<=x<=30 and y==4) or (1<=x<=20 and y==5):
    st.write("Chúc mừng cung của bạn là")
    st.write("Kim Ngưu-Taurus")
elif (21<=x<=31 and y==5) or (1<=x<=21 and y==6):
    st.write("Chúc mừng cung của bạn là")
    st.write("Song Tử-Gemini")
elif (22<=x<=30 and y==6) or (1<=x<=22 and y==7):
    st.write("Chúc mừng cung của bạn là")
    st.write("Cự Giải-Cancer")
elif (23<=x<=31 and y==7) or (1<=x<=22 and y==8):
    st.write("Chúc mừng cung của bạn là")
    st.write("Sư Tử-Leo")
elif (23<=x<=31 and y==8) or (1<=x<=22 and y==9):
    st.write("Chúc mừng cung của bạn là")
    st.write("Xử Nữ-Virgo")
elif (23<=x<=30 and y==9) or (1<=x<=23 and y==10):
    st.write("Chúc mừng cung của bạn là")
    st.write("Thiên Bình-Libra")
elif (24<=x<=31 and y==10) or (1<=x<=22 and y==11):
    st.write("Chúc mừng cung của bạn là")
    st.write("Thiên Yết-Scorpio")
elif (23<=x<=30 and y==11) or (1<=x<=21 and y==12):
    st.write("Chúc mừng cung của bạn là")
    st.write("Nhân Mã-Sagittarius")
elif (22<=x<=31 and y==12) or (1<=x<=19 and y==1):
    st.write("Chúc mừng cung của bạn là")
    st.write("Ma Kết-Capricornus")
elif (20<=x<=31 and y==1) or (1<=x<=18 and y==2):
    st.write("Chúc mừng cung của bạn là")
    st.write("Bảo Bình-Aquarius")
elif (19<=x<=29 and y==2) or (1<=x<=20 and y==3):
    st.write("Chúc mừng cung của bạn là")
    st.write("Song Ngư-Pisces")
else:
    st.write("Sai rồi nhập lại đi")
