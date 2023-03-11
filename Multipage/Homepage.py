import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="The Zodiac", page_icon=":star:", layout="wide")
st.sidebar.success("Hãy chọn cung hoàng đạo của bạn nào ヾ(•ω•`)o")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with st.container():
    st.subheader("Trang này là để bạn biết được cung hoàng đạo của mình :wave:")
    st.title("Cung hoàng đạo là gì?")

lottie_homepage = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_dewchafy.json")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Cung Hoàng Đạo được tạo ra bởi các nhà chiêm tinh học Babylon cổ đại từ những năm 1645 trước Công nguyên . Vòng tròn 12 Cung Hoàng Đạo hoàn hảo với 12 cung tương xứng với bốn Mùa và 12 tháng."

"Theo các nhà thiên văn học thời cổ đại, trong khoảng thời gian chừng 30 - 31 ngày , Mặt Trời sẽ điqua một trong mười hai chòm sao đặc biệt. Ai sinh ra trong thời gian Mặt Trời đi qua chòm sao nào thì họ sẽ được chòm sao đó chiếu mệnh và tính cách của họ cũng bị chòm sao ảnh hưởng nhiều. 12 chòm sao tạo thành 12 cung trong vòng tròn Hoàng đạo , có nghĩa ""Đường đi của mặt trời"". Theo phương Tây, vòng tròn này tên là Zodiac , tiếng Hy Lạp nghĩa là ""Vòng tròn của các linh vật.""")
        st.write("Tuy nhiên, để biết bản thân thuộc vị trí cung hoàng đạo gì, bạn cần phải xem xét dựa trên rất nhiều yếu tố cung hoàng đạo của 12 tháng sinh. Bài viết sau đây của bọn mình sẽ giúp bạn giải đáp những điều ấy.")

    with right_column:
        st_lottie(lottie_homepage, height=300, key="zodiac")