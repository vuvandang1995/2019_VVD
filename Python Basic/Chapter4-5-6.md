#### Chapter4: Conditional statements
- Các ví dụ:
```
empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list!")

if empty_tuple:
    print("It's not an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if not nothing:
    print("Then it's nothing!")
```
- Có thể chèn một số kí tự đặc việt vào string. ví dụ:
```
>>> print("I have a \n new line in the middle")
I have a
 new line in the middle
>>> print("This sentence is \ttabbed!")
This sentence is    tabbed!
```
- sử dụng `if __name__ == “__main__”`:
    - Bạn thường nhìn thấy dòng này ở cuối file, nhưng không phải file .py nào cũng có. Dòng `if __name__ == “__main__”` hiểu nôm na rằng bạn chỉ muốn chạy các dòng code trong file đó, các file khác không thể import file này được. Hiểu nôm na hơn file chứa `if __name__ == “__main__”` là file chính, các file khác không thể import nó.
    
#### Chapter 5: Loops
- Có 2 loại vòng lặp phổ biến nhất hiện nay là `for`và `while`
- Hàm range(x) là hàm sinh ra các dãy số integer liên tiếp. Nếu chỉ có 1 đối số, nó sẽ bắt đầu từ số 0, kết thúc là x. Ví dụ:
```
>>> range(5)
range(0, 5)
```
- Một ví dụ khác của range():
```
>>> range(5,10)
range(5, 10)
>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]
```
- Trong ví dụ trên, hàm `range(5, 10)` nó sẽ sinh ra một dãy số bắt đầu từ 5, kết thúc là 10. Hàm `list(range(1, 10, 2))` có nghĩa là hàm `range(1, 10, 2)` sẽ sinh ra một dãy số không âm bắt đầu từ 1, kết thúc là 10, khoảng cách giữa 2 số là 2. Sử dụng hàm `list()` để in ra dãy số trên. 
- Sử dụng vòng lặp trong dict:
```
>>> a_dict = {"one":1, "two":2, "three":3}
>>> for key in a_dict:
       print(key)

three
two
one
```
#### Chapter 6: Python comprehensions
- Có thể lồng ghép nhiều lệnh. ví dụ:
```
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> print( {i: str(i) for i in range(5)} )
{0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}
```
 - hàm set() dùng để xóa các phần từ xuất hiện nhiều hơn 1 lần trong list. Ví dụ:
 ```
 >>> my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
>>> my_set = set(my_list)
>>> my_set
set([1, 2, 3, 4, 5, 7, 8])
 ```
 - Một ví dụ khác của set():
 ```
 >>> my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
>>> my_set = {x for x in my_list}
>>> my_set
set([1, 2, 3, 4, 5, 7, 8])
 ```
 
