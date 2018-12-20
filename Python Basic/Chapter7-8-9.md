#### Chapter 7: Exception Handling
- Exception handling là xử lý các trường hợp ngoại lệ, ví dụ như trong lệnh `try/except` hay dùng.
1. Common Exceptions: một số exception đã được định nghĩa sẵn trong python như:
  - Exception (this is what almost all the others are built off of)
  - AttributeError - Raised when an attribute reference or assignment fails.
  - IOError - Raised when an I/O operation (such as a print statement, the built-in open() function or a method of a file object) fails for an I/O-related reason, e.g., “file not found” or “disk full”.
  - ImportError - Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
  - IndexError - Raised when a sequence subscript is out of range.
  - KeyError - Raised when a mapping (dictionary) key is not found in the set of existing keys.
  - KeyboardInterrupt - Raised when the user hits the interrupt key (normally Control-C or Delete).
  - NameError - Raised when a local or global name is not found.
  - OSError - Raised when a function returns a system-related error.
  - SyntaxError - Raised when the parser encounters a syntax error.
  - TypeError - Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
  - ValueError - Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
  - ZeroDivisionError - Raised when the second argument of a division or modulo operation is zero.
- Ví dụ:
```
>>> my_dict = {"a":1, "b":2, "c":3}
>>> try:
        value = my_dict["d"]
    except KeyError:
        print("That key does not exist!")

That key does not exist!
>>> my_list = [1, 2, 3, 4, 5]
>>> try:
        my_list[6]
    except IndexError:
        print("That index is not in the list!")

That index is not in the list!
```

```
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")
```

```
try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occurred!")
```

```
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")
```
- Trong ví dụ trên, hàn sau finally dù có bắt đc exception hay không nó đều chạy

```
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
```

- Trong ví dụ trên, lệnh sau else chỉ chạy khi không bắt được exception

#### Chapter 8: Working with files
- Đọc 1 file, nên thêm "r" vào trước đường dẫn file để tránh các kí tự đặc biệt. ví dụ:
```
handle = open("test.txt")
handle = open(r"C:\Users\mike\py101book\data\test.txt", "r")
```

- Các kiểu đọc file:
  - .read() : đọc tất cả trong file, đọc từng kí tự
  - .readline() : đọc dòng đầu tiên trong file
  - .readlines(): đọc tất cả các dòng trong file, đọc từng dòng

1. Đọc file theo số kí tự truyền vào 
```
handle = open("test.txt", "r")

while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break
```
- Trong ví dụ trên, `.read(1024)` có nghĩa là chế độ `r`cho phép đọc file theo dung lượng (cụ thể ở đây là 1024 bytes), như chúng ta đã biết, 1 kilobyte bằng 1024 byte, tương đương với 1024 kí tự. Hiểu nôm na ở ví dụ trên, chế độ đọc "r" cho phép đọc số lượng kí tự tùy chọn.

2. Đọc file theo kiểu nhị phân
- Việc đọc file kiểu này là chế độ "rb" (`handle = open("test.txt", "rb")`) nghĩa là **read-binary**. Chế độ này cần thiết trong trường hợp bạn viết chương trình tải 1 file từ internet xuống hoặc chương trình gửi file từ PC này sang PC khác.

3. Ghi vào file
- Cũng tương tự như đọc file, ghi file cũng có 2 chế độ là "w" và "wb". Hàm .write("...") sẽ tạo ra file mới nếu file đó chưa tồn tại. **Một lưu ý là chế độ "w" hay "wb" cho phép bạn ghi vào file nhưng nó sẽ ghi đè dữ liệu cũ trong file trong trường hợp file đó đã tồn tại**.  Ví dụ:

```
handle = open("test.txt", "w")
handle.write("This is a test!")
handle.close()
```
- Chế độ ghi file thứ 2 là `"a"`, với chế độ này nó cũng sẽ tạo ra file mới nếu nó chưa tồn tại. Trong trường hợp file đã tồn tại, chế độ `"a"` sẽ ghi dữ liệu thêm vào file đó mà không làm mất dữ liệu cũ.

4. Sử dụng câu lệnh `with`
- Khi sử dụng câu lệnh `with`, file sẽ tự động đóng lại sau khi câu lệnh `with` kết thúc. Xem ví dụ sau để hiểu hơn:
```
with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)
```
- trong ví dụ trên, dòng `with open("test.txt") as file_handler:` tương đương với `file_handler = open("test.txt")`

5. Catching Error (bắt lỗi)
```
try:
    file_handler = open("test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
    file_handler.close()
```

#### Chapter 9: Importing
- Một module là những đoạn code được viết sẵn trong Python hoặc do người lập trình tự định nghĩa. Để sử dụng các module đó ở nhiều nơi khác nhau trong 1 project, bạn chỉ cần import module đó.
1. Import
- Ví dụ bạn muốn import thư viện `math` vào chương trình của bạn để sử dụng hàm `sqrt()`:
```
>>> import math
>>> math.sqrt(4)
2.0
```
2. Sử dụng from to import
- Việc sử dụng `import math` như ví dụ trên có nghĩa rằng bạn import tất cả mọi thứ có trong thư viện `math`. Đó là 1 ý tưởng không tốt. Bạn cũng có thể import những hàm cụ thể muốn dùng thôi. ví dụ:
```
>>> from math import sqrt
>>> sqrt(16)
4.0
```
3. Một số lưu ý:
- Cho 1 ví dụ:
```
>>> from math import *
>>> sqrt = 5
>>> sqrt(16)
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: 'int' object is not callable
```
- Trong ví dụ trên, bạn import * nghĩa la bạn import tất cả mọi thứ có trong thư viện `math`, nhưng trong chương trình lại sử dụng 1 biến tên là sqrt, trùng với 1 hàm trong thư viện `math`, vậy nếu bạn sử dụng hàm `sqrt` sẽ bị lỗi. Để tránh điều này, bạn có thể import hàm từ thư viện và nhưng thay cho nó 1 cái tên khác. ví dụ:
```
>>> from math import sqrt as sqrt_ok
>>> sqrt = 5
>>> sqrt_ok(16)
4
```
