str1="chuỗi ký tự (string) là một kiểu dữ liệu rất hay dùng trong Python, một từ, một đoạn văn bản đều là kiểu chuỗi "
str2="Chuỗi trong Python được đánh dấu bằng dấu nháy đơn  hoặc nháy kép , tuy nhiên nếu bắt đầu bằng dấu nào thì phải kết thúc bằng dấu đấy"

result = " "
for i in range(len(str1)):
    for j in range(len(str1), i - 1, -1):
        if str1[i:j] in str2:
            if len(str1[i:j]) > len(result):
                result = str1[i:j]
print("Chuỗi ký tự con chung của", str1, "và", str2, "là:", result)

    
    
    
