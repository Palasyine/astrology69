import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":leo:")
st.title("Leo - Sư Tử")
st.subheader("Từ ngày 23/07 đến ngày 22/08")
st.write("Tương ứng với chòm sao Hải Sư.")
st.write("Cung hoàng đạo Sư Tử nam và cung hoàng đạo Sư Tử nữ đều thuộc nguyên tố Lửa mạnh mẽ. Thế nên tính cách đặc trưng của họ chính là can đảm, thông minh, ấm áp và táo bạo. Sinh ra với vận mệnh trở thành một nhà lãnh đạo tài ba, từ nhỏ Sư Tử đã cho thấy tài năng thiên phú của mình thông qua các cuộc thi, điểm số học tập… luôn đứng top đầu."

" Tuy nhiên, cung hoàng đạo tháng 8 này cũng sở hữu những tính cách khá kiêu ngạo, bướng bỉnh, lười biếng hay tự cho mình là trung tâm của vũ trụ. Nhược điểm đó khiến nhiều người cảm thấy khó chịu mặc dù họ cho rằng tài năng của Sư Tử là điều không thể phủ nhận.")
image = Image.open('leo_astrology_sign.jpg')
st.image(image, caption='Sư Tử mang hình tượng là một con sư tử')
