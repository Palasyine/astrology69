import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":capricorn:")
st.title("Capricornus - Ma Kết")
st.subheader("Từ ngày 22/12 đến ngày 19/01")
st.write("Tương ứng với chòm sao Ma Kết , tức con dê có đuôi cá.")
st.write("Trong tất cả các cung hoàng đạo của tháng 1 tượng trưng cho sự kiên nhẫn, cẩn trọng và có trách nhiệm nhất chính là cung hoàng đạo Ma Kết nữ lẫn nam. Được Thổ Tinh chiếu mệnh nên Ma Kết sở hữu một trí thông minh tuyệt vời, tư duy logic mọi tình huống. Tuy nhiên, họ cũng thường có xu hướng thu mình lại trong những nguyên tắc quá khuôn khổ."

" Chính vì thế, Ma Kết mang tâm thế phòng bị khá cao đối với những người mình không quen biết. Họ tin rằng, càng làm việc chăm chỉ, tiếp xúc nhiều mới có thể giúp mối quan hệ gắn chặt hơn.")
image = Image.open('capricorn_astrology_sign.jpg')
st.image(image, caption='Ma Kết mang hình tượng một con dê')