import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":gemini:")
st.title("Gemini - Song Tử (Song Nam)")
st.subheader("Từ ngày 21/05 đến ngày 21/06")
st.write("Tương ứng với chòm sao Song Tử , tức hai cậu bé song sinh.")
st.write("Một trong những cung được cho là dễ dàng thích nghi và hòa nhập với môi trường mới chính là cung hoàng đạo Song Tử. Nằm ở vị trí thứ ba theo thứ tự hoàng đạo, Song Tử có bản tính thông minh lanh lợi, ham học hỏi, đặc biệt vô cùng tình cảm."

" Sở hữu hình ảnh song sinh của cặp anh em Pollux và Castor trong thần thoại Hy Lạp nên những người mang cung mệnh này, thường tồn tại hai bản tính trái ngược nhau như hai tâm hồn trong một cơ thể. Chính vì thế, đối với người khác, họ cảm nhận Song Tử là người hay thay đổi suy nghĩ, thiếu sự kiên định trong tất cả mọi việc.")
image = Image.open('gemini_astrology_sign.jpg')
st.image(image, caption='Song Tử thường mang hình ảnh một cặp song sinh')