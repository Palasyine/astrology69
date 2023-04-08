import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":virgo:")
st.title("Virgo - Xử Nữ (Trinh Nữ, Thất Nữ)")
st.subheader("Từ ngày 23/08 đến ngày 22/09")
st.write("Tương ứng với chòm sao Thất Nữ.")
st.write("Để giải đáp câu hỏi tháng 9, tháng 8 cung hoàng đạo gì, ta có thể xét theo ngày sinh từng của mỗi người. Trong đó, có thể kể đến như cung hoàng đạo Xử Nữ – đứng vị trí hoàng đạo số 6 trong nguyên tố Đất. Điểm nổi bật của cung này chính là sự tinh tế, tốt bụng, luôn sẵn sàng đưa ra nhiều lời khuyên bổ ích cũng như giúp đỡ người khác lúc họ gặp khó khăn."

" Chính vì thế, Xử Nữ được đại đa số mọi người yêu mến nhờ tính cách tốt bụng lẫn xinh đẹp. Những cô gái cung Xử Nữ thường sở hữu vẻ đẹp sắc sảo, thông minh nhưng ngược lại đối với các chàng trai Xử Nữ, ta cảm nhận được ở họ là người khá trầm tính và ít nói.")
image = Image.open('virgo_astrology_sign.jpg')
st.image(image, caption='Xử Nữ tượng trưng cho những cô gái trẻ đẹp và tốt bụng')
