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
- Bạn có thể khai báo số lượng tham số truyền vào hàm là bao nhiêu cũng đc. Trong đó, `*args` đươc hiểu là list các tham số truyền vào, `**kwargs` là dict các tham số truyền vào. `args` và `kwargs` là gì không quan trọng, quan trọng là số lượng dấu `*`. 1 dấu `*` là đại diện diện cho list, 2 dấu `*` là đại diện cho dict. **lưu ý là list luôn đứng trước dict, nghĩa là `*args` luôn đứng trước `**kwargs`** . Xem ví dụ:

```
>>> def many(*args, **kwargs):
        print(args)
        print(kwargs)

>>> many(1, 2, 3, name="Mike", job="programmer")
(1, 2, 3)
{'job': 'programmer', 'name': 'Mike'}
```
- **Biến scope và biến globals (private và public)**
- Các biến bạn khai báo đơn thuần trong các hàm bạn định nghĩa, thì ngoài phạm vi hàm đó ra bạn không được sử dụng. ví dụ:
```
def function_a():
    a = 1
    b = 2
    return a+b

def function_b():
    c = 3
    return a+c

print( function_a() )
print( function_b() )
```
- Khi chạy đoạn code trên, sẽ báo lỗi: `NameError: global name 'a' is not defined` bởi vì biến `a` là biến nội bộ trong hàm `function_a`, hàm `function_b` không dùng được. Để hàm `function_b` cũng dùng được, cần khai báo biến a như sau: `global a`. ví dụ:
```
def function_a():
    global a
    a = 1
    b = 2
    return a+b

def function_b():
    c = 3
    return a+c

print(function_a())
print(function_b())
```

