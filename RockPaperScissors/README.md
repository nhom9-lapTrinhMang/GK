Nhóm 09 – Rock Paper Scissors (Mini Game Socket)

## Giới thiệu

**Rock–Paper–Scissors (Oẳn Tù Tì)** là mini game được xây dựng bằng **Python**, áp dụng **Socket Programming** theo mô hình **Multi Client – Server**.
Mỗi client gửi lựa chọn của mình (Rock, Paper hoặc Scissors) đến server.
Server xử lý kết quả và phản hồi thắng/thua/hòa cho từng người chơi.


## Công nghệ sử dụng

* Python 3.x
* Thư viện: `socket`, `select`, `queue`
* Mô hình: Multi Client–Server
* Quản lý mã nguồn: Git & GitHub


## Cách chạy chương trình

### 1️⃣ Chạy **Server**

Mở terminal tại thư mục dự án và chạy:

```bash
python Server.py 127.0.0.1 5000 2 1024
```

### 2️⃣ Chạy **2 Client** (ở 2 terminal khác nhau)

```bash
python Client.py 127.0.0.1 5000 1024
python Client.py 127.0.0.1 5000 1024
```

**Lưu ý:**

* Server phải khởi động **trước** các client.
* Khi đủ 2 client kết nối, trò chơi sẽ tự động bắt đầu.
* Nếu 1 client thoát, server sẽ chờ người chơi mới.
  
  ## Kết quả chạy chương trình

Hình dưới minh họa quá trình chạy **Server** và **2 Client** trên Visual Studio Code.  
Server nhận và xử lý dữ liệu, đồng thời gửi kết quả thắng/thua cho từng client trong trò chơi **Rock–Paper–Scissors**.

<img width="1920" height="1080" alt="Screenshot (1007)" src="https://github.com/user-attachments/assets/65ddf4fc-eca9-449d-8c89-61e938d4291e" />




