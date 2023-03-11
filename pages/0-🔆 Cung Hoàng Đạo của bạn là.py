import streamlit as st
x=int(st.text_input("Nhập ngày sinh:",0))
y=int(st.text_input("Nhập tháng sinh:",0))
if (21<=x<=31 and y==3) or (1<=x<=19 and y==4):
    st.write("Chúc mừng cung của bạn là")
    st.write("Bạch Dương-Aries-Dám nghĩ-Dám làm và sở hữu tham vọng mạnh mẽ-Ích kỷ và nóng nảy")
elif (20<=x<=30 and y==4) or (1<=x<=20 and y==5):
    st.write("Chúc mừng cung của bạn là")
    st.write("Kim Ngưu-Taurus-Sự kiên nhẫn tuyệt vời cùng khả năng cảm thụ-Bướng bỉnh và tham lam")
elif (21<=x<=31 and y==5) or (1<=x<=21 and y==6):
    st.write("Chúc mừng cung của bạn là")
    st.write("Song Tử-Gemini-Khôn ngoan và khó nắm bắt-Sự thất thường và hay nói dối")
elif (22<=x<=30 and y==6) or (1<=x<=22 and y==7):
    st.write("Chúc mừng cung của bạn là")
    st.write("Cự Giải-Cancer-Khả năng thấu cảm và trí nhớ đặc biệt-Quá nhạy cảm và bảo thủ")
elif (23<=x<=31 and y==7) or (1<=x<=22 and y==8):
    st.write("Chúc mừng cung của bạn là")
    st.write("Sư Tử-Leo-Sự tự tin và lãnh đạo-Luôn mong muốn trở thành tâm điểm và kiêu ngạo")
elif (23<=x<=31 and y==8) or (1<=x<=22 and y==9):
    st.write("Chúc mừng cung của bạn là")
    st.write("Xử Nữ-Virgo-Sự chăm chỉ và tỉ mỉ-Hay bắt bẻ và lo lắng")
elif (23<=x<=30 and y==9) or (1<=x<=23 and y==10):
    st.write("Chúc mừng cung của bạn là")
    st.write("Thiên Bình-Libra-Sự hòa nhã và công bằng-Để các mối quan hệ nắm giữ hạnh phúc và thiếu quyết đoán")
elif (24<=x<=31 and y==10) or (1<=x<=22 and y==11):
    st.write("Chúc mừng cung của bạn là")
    st.write("Thiên Yết-Scorpio-Sự sâu sắc và quyết liệt-Đố kỵ và báo thù")
elif (23<=x<=30 and y==11) or (1<=x<=21 and y==12):
    st.write("Chúc mừng cung của bạn là")
    st.write("Nhân Mã-Sagittarius-Sự lạc quan và phiêu lưu-Vô trách nhiệm và thiếu kiên nhẫn")
elif (22<=x<=31 and y==12) or (1<=x<=19 and y==1):
    st.write("Chúc mừng cung của bạn là")
    st.write("Ma Kết-Capricornus-Sự kiên trì và trách nhiệm-Cứng nhắc và ít biểu lộ cảm xúc")
elif (20<=x<=31 and y==1) or (1<=x<=18 and y==2):
    st.write("Chúc mừng cung của bạn là")
    st.write("Bảo Bình-Aquarius-Sự sáng tạo và tự do-Không chịu nghe lời và thiếu ổn định")
elif (19<=x<=29 and y==2) or (1<=x<=20 and y==3):
    st.write("Chúc mừng cung của bạn là")
    st.write("Song Ngư-Pisces-Sự nhân hậu và linh hoạt-Mơ mộng và dễ bị lợi dụng")
else:
    st.write("Sai rồi nhập lại đi")
