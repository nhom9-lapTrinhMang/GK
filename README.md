# Nhóm 09 – Rock Paper Scissors (Mini Game Socket)

## Giới thiệu

**Rock–Paper–Scissors (Oẳn Tù Tì)** là mini game được xây dựng bằng **Python**, áp dụng **Socket Programming** theo mô hình **Multi Client – Server**.
Mỗi client gửi lựa chọn của mình (Rock, Paper hoặc Scissors) đến server.
Server xử lý kết quả và phản hồi thắng/thua/hòa cho từng người chơi.


## Công nghệ sử dụng

* Python 3.x
* Thư viện: `socket`, `select`, `queue`, `streamlit`
* Mô hình: Multi Client – Server
* Quản lý mã nguồn: Git & GitHub


## Cách chạy chương trình

### 1️⃣ Chạy **Server**

Mở terminal tại thư mục dự án và chạy:

```bash
python server.py "ip máy bạn"
```

Server phải chạy **trước** khi các client kết nối.


## 2️⃣ Chạy **Client**

### 🧍‍♂️ Người chơi thứ nhất (Player 1)

Player 1 là người **khởi chạy giao diện Streamlit** để mọi người truy cập.

Chạy lệnh:

```bash
streamlit run client.py
```

Sau khi chạy, Streamlit hiển thị:

```
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

### 🧍‍♂️ Người chơi thứ hai (Player 2)

Player 2 **không cần chạy lệnh**.

Chỉ cần mở Chrome và truy cập vào:

```
http://<IP-của-Player-1>:8501
```

Ví dụ:

```
http://192.168.1.20:8501
```

> 📌 **Yêu cầu:** Hai máy phải cùng mạng LAN / Wi-Fi.


## Lưu ý

* Server phải khởi động **trước** client.
* Nếu một client thoát, server sẽ chờ người chơi mới.
* Nếu Player 2 không truy cập được, hãy kiểm tra firewall và port 8501.


## Kết quả chạy chương trình

Hình dưới minh họa quá trình chạy **Server** và **2 Client**.
Server nhận và xử lý dữ liệu, đồng thời gửi kết quả thắng/thua cho từng người chơi trong game **Rock–Paper–Scissors**.

<img width="1920" height="1080" alt="Screenshot (1276)" src="https://github.com/user-attachments/assets/a1791ced-b368-4e44-a029-27b47a44001f" />


