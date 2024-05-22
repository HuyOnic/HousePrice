# HousePrice
# Dự đoán giá nhà trọ cho sinh viên khu vực Hà Nội
nguồn dữ liệu được crawl từ trong web https://phongtro123.com/ một trang web về thuê nhà trọ với lượng dữ liệu được cập nhập từ năm 2015 cho đến nay
# Cài đặt các libraries cần thiết
Bạn chạy lệnh sau để cài đặt thư viện cần thiết cho chương trình
````
pip install -r requirements.txt
````

Để thực hiện quá trình tự động thu thập dữ liệu, bạn hãy chạy file crawling.py bằng lệnh sau. Qúa trình craw sẽ được diễn ra hoàn toàn tự động
````
python crawling.py
````
Toàn bộ quá trình phân tích, làm sạch, chuẩn hóa,... dữ liệu mình thược hiện trong file data_mining.ipynb
