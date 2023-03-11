import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":taurus:")
st.title("Taurus - Kim Ngưu")
st.subheader("Từ ngày 21/04 đến ngày 20/05")
st.write("Tương ứng với chòm sao Kim Ngưu , tức con bò đực.")
st.write("Tiếp theo, tham vọng, thông minh lẫn đáng tin cậy là những đặc điểm của cung hoàng đạo Kim Ngưu. Trong văn hóa phương Tây, ai sở hữu cung mệnh Kim Ngưu đều sẽ trở thành người bạn trung thực, đồng nghiệp tuyệt vời trong công việc lẫn cuộc sống."

" Hơn thế nữa, họ cũng là người hiền lành, chu đáo và khá cứng đầu, chẳng hạn như việc kiên trì theo đuổi một ai đó. Ngoài ra, Kim Ngưu đa phần có một sức hút đặc biệt, mang bản tính trách nhiệm cao. Luôn âm thầm hăng say làm việc để trở thành biểu tượng của sự giàu có, thành công trong sự nghiệp.")
image = Image.open('taurus-astrology-sign.jpg')
st.image(image, caption='Kim Ngưu mang hình tượng một con trâu')