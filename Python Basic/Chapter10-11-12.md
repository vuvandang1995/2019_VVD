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

#### Chapter 11: Class
- Mọi thứ trong Python đều là object
- Xét một ví dụ sau ở Python3:

```
class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"
```

- Giải thích: Tạo một class trong python.
        - Từ khóa `class` dùng để định nghĩa 1 class
        - `Vahicle` là tên của class, theo quy ước, tên class thì chữ cái đầu phải được viết hoa.
        - Tiếp theo là method `__init__`, hay còn gọi là phương thức khởi tao (initialization). có thể bạn sẽ thắc mắc các function trong class lại được gọi là method. Bởi vì các method trong class để mô tả hành động hay thuộc tính của class và nó luôn chứa tham số `self`(trong function bình thường thì không có `self`).
        - Cụ thể method `-__init__` để định nghĩa các thuộc tính của class. `def __init__(self, color, doors, tires):` có nghĩa là các attribute truyền vào class `Vahicle` là `color`, `doors`, `tires`.
        - `self` tương đương với `this` ở các ngôn ngữ khác. Nó có ý nghĩa là chỉ chính bản thân class đó. Trong các dòng `self.color = color`, tương đương `Vahicle.color = color`, có ý nghĩ rằng định nghĩa `color` của class `Vahicle` đặt bằng tham số color được truyền vào.

- Xét thêm 1 ví dụ khác:
```
class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s!" % (self.color, self.vtype)

if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())
```

- Kết quả là:
```
car braking
I'm driving a blue car!
I'm driving a red truck!
truck braking
```
        
## 12.2 Kế thừa
```
class Con1(Cha):
  def ptCon1():
    print('phuong thuc con')
```
python hỗ trợ đa kế thừa 
```
class ConNgua:
    chan = 'Dai'
    bay = True

    def __init__(self, gioi_tinh='Duc'):
        self.gioi_tinh = gioi_tinh
       
    def chay(self):
        print('Nhanh')


class ConLua:
    chan = 'Ngan'
    boi = True

    def __init__(self, gioi_tinh='Cai'):
        self.gioi_tinh = gioi_tinh
    
    def chay(self):
        print('Cham')

class ConLa(ConNgua, ConLua):
    pass
----------------------------------------
la1 = ConLa()
la1.chan
>> Dai
la1.gioi_tinh
>> Duc
la1.bay
>> True
la1.boi
>> True
la1.chay()
>> Nhanh
```
* Lớp con sẽ kế thừa tất cả các thuộc tính và phương thức của các lớp cha. Mặc định nếu các phương thức và thuộc tính của các lớp cha trùng nhau thì lớp con sẽ kế thừa của lớp cha nào khai báo trước trong trường hợp trên là ConNgua

## 12.3 Ghi đè
```
class Con2(Cha):
  def ptCha():
    print('phuong thuc cha bi ghi de boi con 2')
```
* lớp Con2 kế thừa lớp Cha cả thuộc tính và phương thức ptCha, tuy nhiên phương thức ptCha ở lớp Con2 được định nghĩa khác
## 12.4 Ẩn dữ liệu
Các thuộc tính bình thường có thể gọi ra ở bên ngoài lớp thông qua cú pháp
<tên lơp>.<thuộc tính> hoặc <tên đối tượng thuộc lơp>.<thuộc tính>
Khi ta không muốn bên nguoài nhìn thấy thuộc tính nào thì tên thuộc tính ta thêm __ trước tương tụ cho phương thức
```
class Vidu:
  __thuocTinhAn=100
```
Tuy nhiên ta vẫn có thể gọi được bằng cú pháp
<đối tượng>._<tên lớp>__<tên thuộc tính>

## 12.5 Các thuộc tính mặc định
`__dict__`: Là Dictionary chứa namespace của lớp.
`__doc__`: Được sử dụng để truy cập Documentation String của lớp nếu có.
`__name__`: Là tên lớp.
`__module__`: Là tên Module trong đó lớp được định nghĩa. Thuộc tính là `__main__` trong chế độ tương tác.
`__bases__`: Là một Tuple chứa các lớp cơ sở.
```
class Sinhvien:
   'Class co so chung cho tat ca sinh vien'
   svCount = 0

   def __init__(self, ten, hocphi):
      self.ten = ten
      self.hocphi = hocphi
      Sinhvien.svCount += 1
   
   def displayCount(self):
     print "Tong so Sinh vien %d" % Sinhvien.svCount

   def displaySinhvien(self):
      print "Ten : ", self.ten,  ", Hoc phi: ", self.hocphi
-----------------------------------------------------------
Sinhvien.__doc__: Class co so chung cho tat ca sinh vien
Sinhvien.__name__: Sinhvien
Sinhvien.__module__: __main__
Sinhvien.__bases__: ()
Sinhvien.__dict__: {'__module__': '__main__', 'displayCount':
<function displayCount at 0xb7c84994>, 'svCount': 2, 
'displaySinhvien': <function displaySinhvien at 0xb7c8441c>, 
'__doc__': 'Class co so chung cho tat ca sinh vien', 
'__init__': <function __init__ at 0xb7c846bc>}
```

## 12.6 Một số phương thức mặc định
|Phương thức|chức năng|Lời gọi mẫu|
|-----------|---------|-----------|
|`__init__`( self [,args...]|Là constructor (với bất kỳ tham số tùy ý nào)|obj = tenLop(args)|
|`__del__`( self )|Là destructor, xóa một đối tượng| del obj|
|`__repr__`( self )| Biểu diễn chuỗi hiển thị khi gọi đối tượng(<Sinhvien: chuoigido>)|repr(obj)|
|`__str__`( self )| Biểu diễn chuỗi sau khi convert đối tượng sang string|str(obj)|
|`__cmp__`( self, x )|So sánh đối tượng|cmp(obj, x)|

## 12.7 Một số toán tử
|Phương thức|chức năng|Toán tử|
|-----------|---------|-------|
|`__add__`( self, other) |Cộng hai đối tượng| + |
|`__sub__`( self, other)|Trừ hai đối tượng| - |
|`__mul__`( self, other )| Nhân hai đối tượng|x|
|`__div__`( self )| Chia đối tượng sang string|:|
        
