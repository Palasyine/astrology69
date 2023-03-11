import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":scorpio:")
st.title("Scorpio - Hổ Cáp hoặc Thần Nông, Thiên Yết, Thiên Hạt")
st.subheader("Từ ngày 24/10 đến ngày 22/11")
st.write("Tương ứng với chòm sao Thiên Hạt , mang hình dáng con bọ cạp.")
st.write("Cung hoàng đạo Bọ Cạp được xem là một trong những cung đa dạng tên gọi nhất trong các chòm sao. Thuộc cung hoàng đạo tháng 11 cuối năm, gắn liền với truyền thuyết nữ thần Hy Lạp Hera, nên chúng được xếp vào hàng nguyên tố Nước. Người sở hữu chòm sao này có một vẻ ngoài lạnh lùng, thu hút, tháo vát và đặc biệt vô cùng ngoan cố."

" Đôi khi, Bọ Cạp thể hiện ra mình là người mạnh mẽ, quyết liệt đạt được tham vọng trước mắt. Tuy nhiên, họ cũng mang nội tâm khá trầm lắng, rất khó để bạn có thể tạo được niềm tin với họ. Luôn luôn làm hết sức, hết mình, kiên trì đến cùng chính là lý tưởng sống của Bọ Cạp.")
image = Image.open('scorpio_astrology_sign.jpg')
st.image(image, caption='Hổ Cáp mang hình tượng một con bọ cạp')