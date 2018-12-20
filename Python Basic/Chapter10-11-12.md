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
- Trong ví dụ trên, hàm truyền vào 2 tham số là a=1, b=2, return kết quả là tổng 2 tham số. Khi gọi tới hàm, nếu không truyền vào tham số nào thì nó sẽ lấy tham số mặc định để tính, nếu truyền vào tham số mới, hàm sẽ tính tham số mới.

```
>>> def keyword_function(a, b=None):
        if b is not None:
            return a+b
        else:
            return a

>>> keyword_function(b=4, a=5)
9
>>> keyword_function(a = 8)
8
```
- Trong ví dụ trên, khai báo tham số b = None có nghĩa là nếu gọi tới hàm `keyword_function`,tham số truyền vào hàm có thể có b hoặc không. **lưu ý: các tham số khai báo là None khi định nghĩa hàm, luôn luôn phải nằm ở cuối cùng trong dãy tham số**

- `*args và ** kwargs`
- Bạn có thể khai báo số lượng tham số truyền vào hàm là bao nhiêu cũng đc. Trong đó, `*args` đươc hiểu là list các tham số truyền vào, `**kwargs` là dict các tham số truyền vào. `args` và `kwargs` là gì không quan trọng, quan trọng là số lượng dấu `*`. 1 dấu `*` là đại diện diện cho list, 2 dấu `*` là đại diện cho dict. **lưu ý là list luôn đứng trước dict, nghĩa là `*args` luôn đứng trước `**kwargs`**
