import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":pisces:")
st.title("Pisces - Song Ngư")
st.subheader("Từ ngày 19/02 đến ngày 20/03")
st.write("Tương ứng với chòm sao Song Ngư , hai con cá bơi ngược chiều.")
st.write("Cuối cùng, thuộc top các cung hoàng đạo sinh tháng 3 sở hữu biểu tượng của biển cả – hai chú cá do thần tình yêu và nữ thần sắc đẹp hóa thân thành chính là cung hoàng đạo Song Ngư. Với hình ảnh bơi lượn tự do, đan xen ngược chiều nhau theo dòng nước chảy, hai chú cá này cho thấy đức hi sinh cũng như hành động cảm tính cao cả dành cho người khác."

" Song Ngư vốn là người sống rất tình cảm, ngây thơ, yếu đuối và chân thành. Họ thường không kiên định với những quyết định của mình mà dễ bị tác động bởi các yếu tố xung quanh. Chắc chắn rằng, Song Ngư sở hữu vẻ ngoài vô cùng đáng yêu lẫn ngọt ngào khiến mọi người luôn muốn được che chở.")
image = Image.open('pisces_astrology_sign.jpg')
st.image(image, caption='Song Ngư mang hình tượng hai con cá song sing đang bơi cùng với nhau')