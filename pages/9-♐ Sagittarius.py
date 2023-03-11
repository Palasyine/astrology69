import streamlit as st
from PIL import Image
st.set_page_config(page_icon=":sagittarius:")
st.title("Sagittarius - Nhân Mã hoặc Xạ Thủ, Cung Thủ")
st.subheader("Từ ngày 23/11 đến ngày 21/12")
st.write("Tương ứng với chòm sao Nhân Mã.")
st.write("Nhân Mã – cung hoàng đạo sinh tháng 12 cuối năm có biểu tượng đặc biệt nhất trong số tất cả các chòm sao chính là hình ảnh chàng trai nửa người nửa ngựa đang giương cung tên đầy mạnh mẽ."

" Cụ thể hơn, Nhân Mã có xu hướng sống tự do, tình cảm, tràn đầy khát vọng nhiệt huyết và vô cùng hài hước. Theo một số chuyên gia văn học cho rằng, những người thuộc cung Nhân Mã được đánh giá là trung thực và thẳng thắn nhất."

" Họ yêu thích việc đem đến tiếng cười lạc quan cho mọi người xung quanh. Chính vì mang hình ảnh tự do nên họ thường không thích bị quản chặt hoặc kiểm soát khi đang trong một mối quan hệ nào đó")
image = Image.open('sagittarius_astrology_sign.jpg')
st.image(image, caption='Nhân Mã mang hình tượng một chiến binh nhân mã hoặc cây cung')