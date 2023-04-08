import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":libra:")
st.title("Libra - Thiên Bình hoặc Thiên Xứng")
st.subheader("Từ ngày 23/09 đến ngày 23/10")
st.write("Tương ứng với chòm sao Thiên Xứng , tức cái cân.")
st.write("Thiên Bình – biểu tượng của cung hoàng đạo tháng 9 cũng như cung hoàng đạo tháng 10 là hình ảnh chiếc cân công lý. Khi xưa, nữ thần Hy lạp Astraea đã dùng cán cân đó để phán xét tội lỗi con người, dựa trên cái Thiện và cái Ác. Thiên Bình tức nghĩa sự công bằng, hài hòa trong mọi vấn đề cuộc sống."

" Chính vì thế, người cung Thiên Bình sở hữu tính cách thẳng thắn, thông minh. Họ rất giỏi nhìn nhận sự việc theo chiều hướng công bằng, khách quan. Hơn nữa, hợp tác với Thiên Bình sẽ giúp mang lại rất nhiều thành công bởi họ là những người thông minh, ngoại giao tốt. Tuy nhiên, đặt nặng mối tư thù, dễ tủi thân cũng là một điểm yếu mà Thiên Bình cần khắc phục.")
image = Image.open('libra_astrology_sign.jpg')
st.image(image, caption='Thiên Bình mang hình tượng cái cân tượng trưng cho công lý')
