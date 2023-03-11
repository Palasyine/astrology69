import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":aries:")
st.title("Aries - Dương Cưu hay Bạch Dương")
st.subheader("Từ 21/3 đến 20/4")
st.write("Tương ứng với chòm sao Bạch Dương , tức con cừu đực.")
st.write("Cung hoàng đạo Bạch Dương nữ lẫn nam bao gồm những người sinh vào cuối tháng ba tới đầu tháng tư. Có biểu tượng là chú cừu đực sở hữu bộ lông vàng truyền thuyết, dựa trên một câu chuyện thần thoại Hy Lạp cổ đại."
         
" Là cung hoàng đạo đi trước, tiên phong đầu tiên trong 12 cung nên Bạch Dương sở hữu tính cách dẫn đầu, dũng cảm, luôn sẵn sàng chiến đấu với mọi thử thách. Họ có xu hướng thiếu kiên nhẫn, ngay thẳng, mạnh mẽ và hay lãnh đạo người khác. Chính vì thế, Bạch Dương thường sẽ không nghe theo bất kỳ lời khuyên của ai làm cản trở mục đích ban đầu.")
image = Image.open('aries_astrology_sign.jpg')
st.image(image, caption='Bạch Dương mang hình tượng một con cừu với cặp sừng dài')