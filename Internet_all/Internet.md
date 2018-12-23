# What is the Internet?
- Internet có thể được hiểu là "network of networks". Nơi chia sẻ thông tin trên toàn cầu.

# Thông tin được truyền đi bằng gì? bằng cách nào?
- Khi bạn gửi một hình ảnh, một tin nhắn hay một video cho 1 người bạn ở bên Mỹ, bạn có thắc mắc những thông tin ấy đã được gửi đi như thế nào không? Đó không phải ma thuật, đó là Internet.
- Các thông tin như ảnh, tin nhắn văn bản, video... được chuyển sang bits. Bits là mã nhị phân được biểu diễn bởi 0 và 1.
  - 8 bits = 1 byte
  - 1024 bytes = 1 kilobyte
  - 1024 kilobyte = 1 megabyte
  ...
- Một bài hát vào khoảng 3 - 4 mb, nó cũng được chuyển sang bits và chuyển đi trong môi trường Internet
- Vậy những bit đó được gửi đi bằng gì? có 3 ý tưởng được áp dụng để truyền thông tin bit, đó là điện, ánh sáng và sóng.
  - Để truyền thông tin bằng điện, người ta dùng dây cáp đồng,... nó có ưu điểm là rẻ nhưng lại dễ bị mất mát thông tin
  - Để truyền thông tin bằng ánh sáng, người ta dùng cáp quang... nó có ưu điểm là cực nhanh, không mất thông tin nhưng rất đắt, phức tạp
  - Để truyền thông tin bằng sóng, người ta dùng máy phát sóng như wifi,... có ưu điểm là kết nối không dây nhưng chất lượng càng kém khi khoảng cách đường truyền càng xa. Người ta có thể sử dụng vệ tinh hoặc các thiết bị trung chuyển để cải thiện việc này.
- **Bandwidth** nghĩa là băng thông, là số lượng bit tối đa truyền đi được trong 1 giây. ví dụ như bạn tải 1 bài hát 3 MB mất 3 giây, thì băng thông là 1 MB/s

# IP address and DNS
## IP address
- Internet là mạng của các mạng. Nó liên kết hàng tỷ thiết bị kết nối lại với nhau trên toàn thế giới. 
- Một mô hình cụ thể rằng: bạn có một laptop và 1 chiếc điện thoại cùng kết nối tới wifi và bạn có thể truy cập Internet. Điều đó có nghĩa rằng cục wifi của bạn kết nối với 1 **Internet Service Provider (hay còn gọi là ISP)** (chính là nhà cung cấp dịch vụ mang như VNPT, FPT,...)
- Vậy Laptop, điện thoại di động đó giao tiếp với nhau như thế nào? Phải có một bộ các quy tắc và chuẩn, dùng để giao tiếp giữa chúng, gọi là **Protocol**
- Cũng giống số điện thoại của mỗi người, các thiết bị cũng cần có một địa chỉ duy nhất trong mạng (private hoặc public). Một giao thức ra đời để các thiết bị trong mạng giao tiếp thông qua địa chỉ ấy, đó chính là **Internet Protocol, hay còn gọi là IP**. Địa chỉ của các thiết bị sử dụng **Internet Protocol** gọi là **IP address**. 
- Giải sử bạn biết máy tính của bạn có địa chỉ là 174.129.14.120, Như bạn nhìn thấy, địa chỉ được chia làm 4 phần cách nhau mởi dấu `.`. Mỗi phần mang một ý nghĩa riêng, giống như bạn nhìn vào một địa chỉ: `số nhà 19, đường Cầu giấy, thành phố Hà Nội, quốc gia Việt Nam.`
- Một địa chỉ có độ dài là 32 bits, chia đều cho 4 phần.

<img src="https://i.imgur.com/8ZhvT2Z.png">

- Vậy dựa vào địa chỉ IP đã phân tích, bạn có thể biết được các thông tin như country, region, subnet, device

<img src="https://i.imgur.com/zFIziJx.png">

- Như đã giới thiệu ở trên, địa chỉ IP bạn vừa nghen nói đến là địa chỉ IPv4, được ra đời năm 1973,có thể cung cấp 4 tỷ địa chỉ. Tuy nhiên với tốc độ phát triển hiện này, con số 4 tỷ là không đủ. Người ta nghiên cứu cho ra đời một loại IP khác là IPv6, có độ dài 128 bíts, có thể cung cấp 340 tỷ địa chỉ

## DNS
- Tình huống với một người sử dụng web bình thường, bạn không thể bắt họ nhớ địa chỉ IP dài loằng ngoằng của web server để truy câp,thay vào đó họ dùng domain để truy cập, ví dụ như `google.com`, `facebook.com`. Việc người dùng nhập domain, thay vì địa chỉ IP như vậy, đó là công nghệ **DNS**, viết tắt của **Domain Name System**.
- Vậy, DNS server có tác dụng phân giải tên miền thành địa chỉ IP và phản hồi lại cho người dùng. Ví dụ như bạn nhập vào trình duyệt với tên miền là: `facebook.com`, thì sẽ có 1 request từ máy tính của bạn được gửi tới DNS server gần nhất để hỏi rằng `facebook.com` có địa chỉ là bao nhiêu? DNS sẽ phản hồi lại cho bạn nếu nó biết. Nếu nó không biết, nó sẽ đi hỏi các DNS server xung quanh nó. 
- Mỗi DNS server sẽ có một bảng danh sách địa chỉ IP và tên miền tương ứng, mỗi khi nó biết thêm thông tin về tên miền và IP nào mới, nó sẽ update vào bảng này.
- Bạn có tự hỏi vậy hệ thống DNS như thế nào mới có thể đáp ứng được các yêu cầu liên tục của hàng tỷ thiết bị? Câu trả lời là các DNS server được kết nối với một `Distributed Hierarchy`, hiểu nôm na nó là ông vua. Các ông vua nằm ở các vùng lớn khác nhau. 
- Mỗi một `Distributed Hierarchy` sẽ phụ trách phản hồi tùy vào loại domain như `.org`, `.com`, `.net`,...

<img src="https://i.imgur.com/fGKUgsL.png">

- DNS là một giao thức mở và công khai, bởi thế, sẽ có rất nhiều nguy cơ bị tấn công bởi các hacker. đó là **DNS spoofing**
- Một giả thiết cho một vụ tấn công giả mạo DNS: Đó là khi một hacker xâm nhập vào DNS server, sửa thông tin địa chỉ IP của domain `xyz.com` thành một địa chỉ IP của 1 web server giả mạo, thì khi người dùng truy cập `xyz.com` sẽ không vào được đúng trang `xyz.com` thật nữa, mà chuyển sang trang giả mạo.

# Packets, router and reliability
- Ok, một tình huống khi bạn gửi một đoạn video 1 gb cho người khác. Như chúng ta đã tìm hiểu, 1 GB dữ liệu đó sẽ được chuyển thành bits để gửi đi. 1 GB ~ 1073741824 bits, là một con số quá lớn để gửi thông tin đi 1 lần duy nhất. Giải pháp được đưa ra là chia dữ liệu thành các gói tin nhỏ hơn, gọi là **packet**. Giống như bạn có 1 chiếc máy bay muốn gửi sang Mỹ cho 1 người bạn, bạn sẽ phải tháo nhỏ nó ra và gửi đi từng phần, bên nhận sẽ ghép lại thành sản phẩm máy bay. 
- Các **packet** khi được gửi ra network, làm thể nào để nó có thể tới đúng nơi mà nó cần đến? Mỗi **packet** sẽ chứa thông tin như địa chi IP người gửi, người nhận.
- Một mạng sẽ bao gồm rất nhiều các **Router**, là thiết bị định tuyến, kết nối với nhau và có nhiệm vụ định tuyến đường đi cho các **packet**. Các **Router** có bảng định tuyến lưu thông tin các địa chỉ đi qua nó và các **router** hàng xóm của nó. **router** có được trang bị thuật toán tìm đường đi ngắn nhất.
- Mỗi **packet** sẽ đi theo con đường riêng, thời gian tới khác nhau
- Trong thực tế, trong quá trình 1 **packet** trong mạng có thể gặp cái lỗi như đứt dây cáp, hỏng ***router**,... dẫn đến việc mất gói tin, vậy nơi nhận dữ liệu sẽ không có đủ số lượng các ***packet** để ghép lại thành dữ liệu ban đầu. Tôi đang nói đến vấn đề độ tin cậy **Reliability**. **TCP (Transmission Control Protocol)** sẽ giúp chúng ta vấn đề này.
- TCP là một giao thức quản lý việc gửi và nhận dữ liệu của bạn. Khi bạn muốn tải 1 bài hát ở ZingMp3, ZingMp3 server sẽ gửi cho bạn các gói tin là dữ liệu về bài hát đó bằng giao thức TCP. Khi các gói tin đó tới máy tính của bạn, TCP phía máy tính của bạn sẽ kiểm tra số lượng các **packet** đã đủ chưa. Nếu nó thấy đã đủ, nó sẽ xác nhận rằng ok, nếu nó phát hiện có một số **packet** bị mất, nó sẽ không xác nhận ok và thông tin tới nơi gửi những **packet** bị mất và đề nghị gửi lại.
- Việc giao tiếp giữa client và server sử dung TCP phải có cơ chế  bắt tay 3 bước.

# HTTP and HTTPS
## HTTP là gì?
- Khi bạn truy cập 1 trang web, việc đầu tiên là bạn  phải mở web browser
- Web browser là ứng dụng để bạn truy cập vào các trang web. Tiếp theo là nhập URL
- URL (Uniform Resource Locator) là chuẩn địa chỉ của 1 website.
### Điều gì xảy ra khi bạn truy cập facebook.com?
- Khi đó trình duyệt sẽ gửi request lên web server của facebook, sau đó server sẽ response lại cho trình duyệt rất nhiều thông tin như văn bản, hình ảnh,... Giao thức được sử dụng giữa web server và browser chính là **HTTP (Hypertext Transfer Protocol)**, dịch là giao thức trao đổi siêu văn bản =)) 
- Thực tế, khi bạn truy vào đường dẫn `facebook.com` như vậy, nghĩa là browser vừa thực hiện một **GET request** lên server. Ví dụ cụ thể hơn là bạn truy cập vào trang `xxx.com/login`, nghĩa là bạn vừa gửi một request để lấy giao diện đăng nhập vào ứng dụng, web server gửi response cho bạn là trang html gồm các form thông tin đăng nhập. 
- Sau khi bạn điền thông tin đăng nhập và bấm submit, hành động đó được gọi là **POST request**.
- Ok, sau khi bạn đăng nhập thành công, bạn có thể tắt trình duyệt và bật lại, truy cập vào trang `xxx.com` đã thấy trạng thái được login rồi??? vì sao lại thế? Lí do là: Khi bạn gửi thông tin đăng nhập cho web server, web server kiểm tra thông tin hợp lệ sẽ gửi về cho web browser trang đã đăng nhập và **cookie data**. **cookie data** đó chứa id đại diện cho thông tin đăng nhập của bạn được lưu ở phía web browser, ví dụ như (**cookie data** là `#123456`). Và những lần sau đó, khi bạn truy cập vào trang `xyz.com`, web browser sẽ gửi id đó lên server và tự động đăng nhâp cho bạn. Tóm lại, **cookies** có tác dụng là nói cho server biết bạn là ai trong những lần truy cập sau.
## HTTPS
- Quá trình trao đổi của client với server, nếu dữ liệu không được bảo vệ, sẽ rất dễ bị đánh cắp trên đường truyền, việc này vô cùng nguy hiểm nếu lộ những thông tin nhạy cảm. **HTTPS** sẽ giải quyết vấn đề này.
- Trước hết chúng ta cần tìm hiểu **SSL** và **TLS** là gì. **SSL** là `Secure Sockets Layer`, **TLS** là `Transport Layer Security`. Bạn có thể hiểu **SSL**và **TLS** là lớp bảo vệ bao quanh các cuộc trao đổi của bạn, là giải pháp hoàn hảo để tránh việc bị đánh cắp và giả mạo thông tin. 
- **SSL** và **TLS** sẽ được thể hiện khi bạn truy cập 1 trang web: `https://xxx.com`
- **HTTPS** là `HyperText Text Protocol Secure`. Nghĩa là giao thức **HTTP** sẽ được bảo vệ.
- Khi bạn truy cập 1 website bằng **HTTPS**, kết nối giữa web browser và web server sẽ giống như thế này: 

<img src="https://i.imgur.com/Moxj7Xk.png">

- Lúc này, nó sẽ cung cấp 1 **digital certificate** dịch là chứng chỉ số, nó sẽ công nhân danh tính cho website đó. Bạn cần phải đăng kí chứng chi này.

# Tổng kết

<img src="https://i.imgur.com/kDRUPMs.png">

1. **HTTP** và **DNS** quản lý việc gửi và nhận các file của websie
2. **TCP/IP** và **Routing** sẽ chia nhỏ những file đó thành các **packet**
3. Các **packet** sẽ được chuyển thành bits và được gửi đi bởi tầng vật lý như cáp điện, cáp quang, wifi
























