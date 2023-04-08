import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":cancer:")
st.title("Cancer - Cự Giải hay Bắc Giải")
st.subheader("Từ ngày 22/06 đến ngày 22/07")
st.write("Tương ứng với chòm sao Cự Giải , tức con cua.")
st.write("Cự giải là cung hoàng đạo thuộc nguyên tố Nước đầu tiên. Chính vì thế, biểu tượng của chúng là hình một con cua. Nhìn chung, cung hoàng đạo Cự Giải sở hữu tính cách thiện lương, dịu dàng, hay ngại thể hiện cảm xúc và mang một nội tâm khép kín."
         
" Điểm mạnh của Cự Giải là sự khéo léo, hài hước, giỏi thuyết phục người khác bằng các lập luận đanh thép, cứng rắn như lớp vỏ cua. Đặc biệt, họ có một tình yêu thương vô bờ bến đối với gia đình. Tuy nhiên, điểm yếu của họ cũng là quá yếu đuối, hay buồn bã, bi quan, luôn có cảm giác không an toàn nên sẽ thu mình lại trong những suy nghĩ tiêu cực.")
image = Image.open('cancer_astrology_sign.jpg')
st.image(image, caption='Cự Giải mang hình tượng một con cua')
