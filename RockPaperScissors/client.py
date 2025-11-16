import streamlit as st
import socket
import sys
import time

st.set_page_config(page_title="GROUP 9", layout="centered")
st.title("GROUP 9")

if 'status_message' not in st.session_state:
    st.session_state.status_message = "Chưa kết nối. Vui lòng nhập thông tin máy chủ."
if 'result_message' not in st.session_state:
    st.session_state.result_message = ""
if 'player_id' not in st.session_state:
    st.session_state.player_id = None


def connect_and_play(move: str, address: str, port: int, buffer_size: int = 1024):
    """Xử lý toàn bộ logic kết nối socket, gửi move và nhận kết quả."""
    st.session_state.status_message = f"Đang gửi nước đi: {move}..."
    st.session_state.result_message = ""
    st.session_state.player_id = None 

    try:
        
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((address, port))


        status = clientSocket.recv(buffer_size).decode()


        if 'queue' in status:
            st.session_state.status_message = "Phòng đã đầy, bạn đã được thêm vào hàng đợi. Vui lòng thử lại sau."
            clientSocket.close()
            return
        
        if '0' in status:
            st.session_state.player_id = '1'
        elif '1' in status:
            st.session_state.player_id = '2'
        else:
             
            st.session_state.status_message = f"Kết nối thành công. Bạn là Người chơi {st.session_state.player_id if st.session_state.player_id else 'không xác định'}. Đang gửi nước đi."
        
        player = st.session_state.player_id
        if not player:
            st.session_state.status_message = f"Lỗi: Không thể xác định ID người chơi từ máy chủ ({status})."
            clientSocket.close()
            return

        clientSocket.send((move + str(player)).encode())
        
        result = clientSocket.recv(buffer_size).decode()

        if 'wait' in result:
            st.session_state.status_message = "Đang chờ đối thủ. Vui lòng nhấp lại nút move của bạn một lần nữa sau khi đối thủ chơi (hoặc sau vài giây)."
            try:
                clientSocket.settimeout(2.0)
                final_result = clientSocket.recv(buffer_size).decode()
                try:
                    final_result_2 = clientSocket.recv(buffer_size).decode()
                    if final_result_2 and final_result_2.isdigit():
                        final_result = final_result_2
                except socket.timeout:
                    pass

                result = final_result
                st.session_state.status_message = "Đã nhận kết quả cuối cùng."

            except socket.timeout:
                st.session_state.result_message = "Đã gửi nước đi, nhưng đối thủ chưa chơi. Vui lòng thử lại sau."
                clientSocket.close()
                return
            except Exception as e:
                st.session_state.status_message = f"Lỗi khi chờ kết quả: {e}"
                clientSocket.close()
                return

        result_int = int(result)

        if result_int == 0:
            st.session_state.result_message = "Kết quả: 🤝 HÒA!"
        elif (result_int == 1 and player == '1') or (result_int == 2 and player == '2'):
            st.session_state.result_message = "Kết quả: 🎉 BẠN THẮNG!"
        else:
            st.session_state.result_message = "Kết quả: 😢 BẠN THUA!"
        
        st.session_state.status_message = "Đã ngắt kết nối. Sẵn sàng cho ván mới!"

    except ConnectionRefusedError:
        st.session_state.status_message = "Kết nối thất bại. Vui lòng kiểm tra địa chỉ và cổng máy chủ."
        st.session_state.result_message = ""
    except Exception as e:
        st.session_state.status_message = f"Lỗi không xác định: {e}"
        st.session_state.result_message = ""
    finally:
        try:
            clientSocket.close()
        except NameError:
            pass 

st.sidebar.header("Cấu hình Máy chủ")
server_address = st.sidebar.text_input("Địa chỉ Máy chủ (Server Address)", value="127.0.0.1")
server_port = st.sidebar.number_input("Cổng (Port)", value=8888, min_value=1000, max_value=65535, step=1)
buffer_size = 1024


st.header("Chọn nước đi của bạn")
st.write("Nhấp vào một nút để kết nối, chơi một ván, và nhận kết quả.")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✊ Búa (R)", use_container_width=True, help="Rock"):
        connect_and_play('R', server_address, server_port, buffer_size)
with col2:
    if st.button("✋ Bao (P)", use_container_width=True, help="Paper"):
        connect_and_play('P', server_address, server_port, buffer_size)
with col3:
    if st.button("✌️ Kéo (S)", use_container_width=True, help="Scissors"):
        connect_and_play('S', server_address, server_port, buffer_size)

st.divider()

st.info(f"**Trạng thái Kết nối:** {st.session_state.status_message}")

if st.session_state.result_message:
    st.markdown(f"## {st.session_state.result_message}")
