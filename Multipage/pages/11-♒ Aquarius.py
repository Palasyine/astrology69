import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":aquarius:")
st.title("Aquarius - Bảo Bình , hay Thủy Bình")
st.subheader("Từ ngày 20/01 đến ngày 18/02")
st.write("Tương ứng với chòm sao Bảo Bình , tức người mang nước.")
st.write("Với hình ảnh tượng trương của một vị thần mang bình nước cao quý, cung hoàng đạo Bảo Bình thể hiện cho sự ham học hỏi, trí tuệ cao. Đặc biệt nhất là khả năng sáng suốt, thông minh, tách biệt tình cảm khỏi tư thù cá nhân. Về mặt tính cách, Bảo Bình thường hay rất tò mò, khiến họ dễ suy nghĩ khá nhiều."

" Tuy nhiên, không hẳn Bảo Bình khép mình lại mà họ có xu hướng sống hoạt bát, hướng ngoại, đem đến năng lượng tích cực cho mọi người xung quanh. Cung hoàng đạo Bảo Bình cũng có phần ương bướng, ưa chuộng tự do và không thích bị chi phối quá nhiều trong cuộc sống.")
image = Image.open('aquarius_astrology_sign.jpg')
st.image(image, caption='Bảo Bình')