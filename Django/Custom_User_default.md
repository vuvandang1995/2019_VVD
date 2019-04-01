- Tạo project: `django-admin startproject openid`
- Tạo app:
```
cd openid
django-admin startapp superadmin
```
- Tạo class user trong file `models.py` trong app vừa tạo

[models.py](https://github.com/vuvandang1995/2019_VVD/blob/master/Django/config/models.py)

- Sửa file `settings.py`:
  - Thêm app vừa tạo vào chỗ `INSTALLED_APPS`
  - Thêm `AUTH_USER_MODEL = 'superadmin.MyUser'`
  - Chỉnh sửa thông tin database
  - Sửa `TIME_ZONE = 'Asia/Ho_Chi_Minh'`
  
- Run commans:

```
python3 manage.py makemigrations
python3 manage.py migrate
```
