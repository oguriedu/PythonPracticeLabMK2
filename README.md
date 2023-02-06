**CHÚ Ý ĐỌC VÀ LÀM CHÍNH XÁC THEO HƯỚNG DẪN TRƯỚC KHI THỰC HIỆN BẤT KÌ MỘT HÀNH ĐỘNG NÀO TRÊN GIT**

## Các phần mềm cần có
- Link tải gitbash: https://git-scm.com/downloads
  **LƯU Ý:** Khi cài đặt gitbash, Select Components chọn Window Explorer intergration nếu chưa được chọn

- Link tải github desktop: https://desktop.github.com/


## Thực hiện clone repository
- Chọn 1 folder rỗng chuột phải chọn gitbash để clone git repository về máy với dòng lệnh bên dưới

```
git clone https://github.com/oguriedu/PythonPracticeLabMK2.git
```

**LƯU Ý:** Nếu chưa sử dụng Gitbash trên máy bao giờ, Gitbash lúc này sẽ yêu cầu đăng nhập vào tài khoản git. Bắt buộc phải sử dụng tài khoản git gắn với gmail sinh viên được nhà trường cấp
**KHUYÊN:** Trong trường hợp không chắc chắn về tài khoản git hiện đang sử dụng trên máy:
- B1: Logout toàn bộ tài khoản git trên tất cả các trình duyệt.
- B2: Nhấn window, tìm kiếm **Credential Manager**.
- B3: Chọn **Window Credentials**.
- B4: Ở mục **Generic Credentials** tìm tất cả mục sử dụng git và chọn **Remove**.
- B5: Clone repository về máy và đăng nhập lại github


## Thực hiện tạo nhánh chính của bản thân

- Sau khi clone repository về máy thành công tiến hành tạo **NHÁNH CHÍNH** theo **ĐÚNG** format: `<lớp-họtên-msv>`. Format phải **CHÍNH XÁC** giống như dưới đây:

```
git checkout -b DHTI10A1HN-NgoQuangDai-1122334455
```
**LƯU Ý:** Nhánh chính làm không chính xác sẽ bị xóa, nếu mất bài sinh viên tự chịu trách nhiệm

- Sau khi tạo nhánh chính vào **folder lab01** chỉnh sửa lại file README.md thêm `<lớp-họtên-msv>` vào file README
- Sau khi chỉnh sửa file thực hiện commit đầu tiên cho **NHÁNH CHÍNH**:

```
git add .

git commit -m "first commit"

```

- Push **NHÁNH CHÍNH** lên remote repository. Ví dụ:

```
git push origin DHTI10A1HN-NgoQuangDai-1122334455
```
**LƯU Ý:** Kiểm tra kĩ nhánh hiện tại xem mình có đúng đang ở **NHÁNH CHÍNH** của mình không trước khi thực hiện. Nếu push vào nhánh **MAIN** hoặc **NHÁNH CỦA SINH VIÊN KHÁC**, vi phạm sinh viên sẽ bị trừ điểm quá trình.

## Thực hiện làm các bài tập trong lab
- Tạo nhánh mới theo lab mà bạn đang làm từ nhánh chính theo **ĐÚNG** format: `<họtên-msv/lab-đang-thực-hiện>`. Ví dụ:

```
git checkout -b NgoQuangDai-1122334455/lab01
```

- Làm các bài tập trên nhánh theo lab, `add` thay đổi, `commit` rồi push lên đúng nhánh đang thực hiện

```
git add .

git commit -m "thuc hanh lab01 da hoan thanh bai01/bai02/bai03"

git push origin NgoQuangDai-1122334455/lab01
```
- Sinh viên làm xong bài nào, trong commit ghi rõ bài mình đã hoàn thành giống như ví dụ trên

**LƯU Ý:** Kiểm tra kĩ nhánh hiện tại xem mình có đúng đang ở nhánh làm bài tập của mình không trước khi thực hiện. Nếu push trực tiếp vào nhánh **MAIN**, **NHÁNH CHÍNH** hoặc **NHÁNH CỦA SINH VIÊN KHÁC**, vi phạm sinh viên sẽ bị trừ điểm quá trình.
**LƯU Ý:** Mỗi lab yêu cầu sinh viên làm một nhánh riêng và push commit mỗi bài lab chính xác vào nhánh đó 

## Tạo pull request gửi yêu cầu merge vào NHÁNH CHÍNH CỦA BẢN THÂN
- Sau khi đã hoàn thành bài và commit đầy đủ lên nhánh lab của mình. Sinh viên truy cập github và tạo pull request vào **NHÁNH CHÍNH** của mình. Ghi rõ nội dung nộp bài Pull Request Title.

- Thầy và các bạn cùng khóa sẽ review code và comment góp ý. **Comment "Done"** sau khi đã fix xong comment.

**LƯU Ý:** Không tạo pull request vào **MAIN** hoặc bất kỳ **NHÁNH CỦA SINH VIÊN KHÁC**, vi phạm sẽ bị trừ điểm quá trình

## Cập nhập bài tập trên git
- Mỗi buổi học thầy cô sẽ gửi bài lên git
- Sinh viên checkout lại về **NHÁNH CHÍNH** của bản thân và pull lại từ nhánh main để cập nhập bài học

```
git checkout DHTI10A1HN-NgoQuangDai-1122334455

git pull origin main
```
- Sau khi đã pull về thành công, sinh viên tạo nhánh bài tập mới giống như được hướng dẫn ở phần **Thực hiện làm các bài tập trong lab**

## Lưu ý trong quá trình thực hành
- **KHÔNG PULL REQUEST VÀO MAIN**
- **KHÔNG PULL REQUEST VÀO NHÁNH CỦA SINH VIÊN KHÁC**
- **KHÔNG PUSH LÊN NHÁNH MAIN**
- **KHÔNG PUSH TRỰC TIẾP LÊN NHÁNH CHÍNH CỦA BẢN THÂN**
- **ĐẶT TÊN NHÁNH THEO ĐÚNG FORMAT**
- **HOÀN THÀNH BÀI TẬP ĐÚNG HẠN**
- Bài tập được giao trên lớp yêu cầu nộp đầy đủ trước khi học lab tiếp theo 3 ngày để thầy kiểm tra và đánh giá quá trình học tập.

- Có bất kì vấn đề gì liên quan đến git có thể nhắn tin hỏi lại thầy.

- Học thêm về git:
  - https://git-scm.com/book/en/v2
  - https://learngitbranching.js.org/?locale=vi
  DHKL16A1HN-NguyenKhang-22174600062
