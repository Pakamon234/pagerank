
# Cài đặt Demo

## BƯỚC 1 – Cài đặt Python trên Window

1. Tải và cài đặt Python từ trang chủ chính thức.
2. Lưu ý: Chọn **Add Path** để thêm vào biến môi trường của Window.

## BƯỚC 2 – Cài đặt Hadoop trên Window

### 1. Cài Java JDK

Tải và cài đặt JDK từ trang web chính thức của Oracle.

Sau khi cài đặt JDK và cấu hình biến môi trường như sau:

```plaintext
JAVA_HOME = C:\Program Files\Java\jdk1.8.0_xx\bin
PATH += %JAVA_HOME%\bin
```

### 2. Cài Hadoop

Tải bản Hadoop 3.3.x từ trang chính thức.

Sau khi cài đặt Hadoop và cấu hình biến môi trường như sau:

```plaintext
HADOOP_HOME = D:\hadoop-3.3.x
PATH += %HADOOP_HOME%\bin
```

### 3. Cấu hình Hadoop

Vào đường dẫn: `D:\hadoop-3.3.x\etc\hadoop`

Chỉnh sửa file `hadoop-env` với nội dung sau:

```plaintext
set JAVA_HOME=C:\Progra~1\Java\jdk1.8.0_xx
```

Sau đó dung Cmd để kiểm tra version Hadoop:

```bash
hadoop version
```

## BƯỚC 3 – Git clone mã nguồn

Chọn thư mục lưu trữ và thực hiện clone mã nguồn:

```bash
git clone https://github.com/Pakamon234/pagerank.git
```

Di chuyển đến thư mục pagerank:

```bash
cd pagerank
```

## BƯỚC 4 – Điều chỉnh input

Điều chỉnh file `graph.txt` theo ý muốn sau đó copy nó vào trong thư mục `input`.

![Điều chỉnh input](image/image5.png)

## BƯỚC 5 – Cấu hình `run_pagerank.bat`

![Cấu hình run_pagerank.bat](image/image6.png)

Thay đổi số lần lặp để có được giá trị hội tụ:

```plaintext
set iterations = [Số lần lặp]
```

Thay đổi đường dẫn đảm bảo rằng đường dẫn đến thư viện Hadoop streaming là đúng:

```plaintext
hadoop jar D:\hadoop-3.3.6\share\hadoop\tools\lib\hadoop-streaming-3.3.x.jar
```

## BƯỚC 6 – Chạy Demo

Để chạy chương trình, chạy `run_pagerank.bat`.

![Chạy run_pagerank.bat](image/image7.png)

Sau khi chạy hoàn tất, xuất hiện thư mục `output`.

![Thư mục Output](image/image10.png)

Mở file `part-00000` (bằng Notepad) để xem kết quả.

![Dùng Cmd để xem kết quả](image/image11.png)

Hoặc sử dụng Cmd: 

```bash
type output\part-00000
```

## Kết quả Demo: (Dữ liệu mẫu)

Với file input `graph.txt` chứa dữ liệu về đồ thị:

![Input Demo](image/image1.png)

Ta sẽ có được kết quả sau khi chạy chương trình như sau:

![Kết quả Demo](image/image12.png)
