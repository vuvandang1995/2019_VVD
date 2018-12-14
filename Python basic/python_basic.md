# Part I - Learning the Basics
#### Chapter 1 - Use IDE
- Lựa chọn trình soạn thảo code. Tôi lựa chọn `Visual studio code`, đơn gián bởi vì nó nhẹ, cũng đầy đủ tiện ích như các tool khác.
#### Chapter 2 - All about Strings
- Khởi tạo một String
    - my_name = "Vu Van Dang"
    - my_name2 = 'Vu Van Dang'
    - my_name = '''Toi ten la Vu Van Dang'''
    - my_name = "I'm Vu Van Dang"
    - my_old = str(24)
- Nối String
    - str1 = "Vu Van"
    - str2 = "Dang"
    - My_name = str1 + str2
- Các phương thức đối với String
    1. Đổi chữ thường thành chữ hoa
        - `my_name = 'vu van dang'`
        - => `my_name.upper()` = 'VU VAN DANG'
    - Sử dụng `dir(my_name)` để show ra các phương thức đối với String
    - <img src='https://i.imgur.com/OQukYjF.png'>
    - Sử dụng `help(my_string.capitalize)` để xem cách sử dụng phương thức nào đó
    2. Chèn dữ liệu và chuỗi String
        - ví dụ: "Python is as simple as {0}, {1}, {2}".format("x", "y", "z")
            `"Python is as simple as x, y, z"`
        - "Python is as simple as {2}, {0, {1}".format("x", "y", "z")
            `"Python is as simple as z, x, y"`
#### Chapter 3 - List, Tuples and Dictionaris
##### - List: Điều đặc biệt của list() trong Python là nó có thể chứa các phần tử khác kiểu dữ liệu (*ví dụ: `my_list` = ["a", 1, "Python", 5]*)
1. Khai báo:
    - my_list = []
    - my_list = list()
    - my_list = [1, 2, 3]
    - my_list2 = ["a", "b", "c"]
    - my_list3 = ["a", 1, "Python", 5]
    - my_list4 = [my_list2, my_list3]
2. Extend list: add dữ liệu của 1 list vào 1 list trống
    - combo_list = []
    - one_list = [4, 5]
    - combo_list.extend(one_list)
    - => combo_list = [4, 5]
3. Cộng list
    - my_list = [1, 2, 3]
    - my_list2 = ["a", "b", "c"]
    - my_list3 = my_list + my_list2
4. Sort() list
    - my_list = [3, 6, 1, 8, 7]
    - my_list_sort = my_list.sort()
    - nhưng my_list_sort = None
    - Giải thích: my_list_sort bằng None bởi vì `my_list.sort()` là 1 phương thức sắp xếp không return là 1 list nên không thể gán `my_list_sort = my_list.sort()`
5. Cắt list
    - my_list = [1, 2, 3]
    - my_list[0:1] sẽ bằng [1, 2]
#### Tuples
    - Sự khác biệt giữa list và tuples là: sau khi khai báo, các phần tử trong list có thể thay đổi, còn trong tuples thì không thể.
    - Giải thích 1 cách rõ ràng hơn: Khi ta khai báo 1 list, thì hệ thống cung cấp bộ nhớ để lưu trữ các phần tử kia một cách rời rạc, bởi vậy nên ta có hàm xóa phần tử của list. ví dụ:
```
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del a[-1]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```
