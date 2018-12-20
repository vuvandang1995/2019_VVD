#### Chapter 10: Functions
- Một functions của bạn là một hàm mà bạn tự định nghĩa. ví dụ:
```
>>> def a_function():
        print("You just created a function!")
```
- Định nghĩa hàm có tham số truyền vào:
```
>>> def keyword_function(a=1, b=2):
        return a+b

>>> keyword_function(b=4, a=5)
9
>>> keyword_function()
3
```
- Trong ví dụ trên, hàm truyền vào 2 tham số là a=1, b=2, return kết quả là tổng 2 tham số. Khi gọi tới hàm, nếu kh
