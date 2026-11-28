# PHẦN 1 — CƠ SỞ KHOA HỌC CHO LỘ TRÌNH DSA CẤP TỐC 7 NGÀY

> Bước 2 của dự án "Lộ trình DSA 7 ngày dựa trên khoa học thần kinh". Nguồn bài tập: kho notebook trong repo này
> (danh mục 3.711 bài DSA). Tài liệu này chỉ làm phần nghiên cứu: cơ chế học, đánh giá phương pháp, các lộ trình
> tham khảo, rồi ghép thành một hệ thống học dùng cho Phần 2–5 (bản đồ kiến thức, danh sách bài, lịch 7 ngày, ôn tập và kiểm tra).
>
> Quy ước đọc hiệu ứng: **d / g** là chênh lệch giữa nhóm áp dụng phương pháp và nhóm đối chứng, đo bằng độ lệch chuẩn.
> 0,2 là nhỏ, 0,5 là trung bình, 0,8 là lớn. Ví dụ g = 0,5 nghĩa là người học trung bình nhảy từ phân vị 50 lên khoảng phân vị 69.

---

## 0. Tóm tắt (đọc phần này nếu chỉ có 5 phút)

1. **Không có nghiên cứu nào cho thấy một người mới có thể "từ số 0 đến Hard" trong 7 ngày.** Khoa học chỉ giúp tăng
   lượng kiến thức giữ được và dùng được trên mỗi giờ học. Lộ trình này dựa trên việc tối ưu số giờ đó, không dựa trên phép màu.
   Điều kiện đầu vào thực tế: biết Python cơ bản (vòng lặp, hàm, list, dict). Nếu chưa biết, cần thêm 1–2 ngày.
2. **Phần lớn bằng chứng có thể áp dụng được đến từ tâm lý học nhận thức, không phải từ ảnh chụp não.** Khoa học thần kinh
   giải thích *vì sao* (củng cố trí nhớ khi ngủ, truy xuất làm bền vết nhớ). Tâm lý học nhận thức cho biết *làm thế nào*.
3. **Bốn kỹ thuật có bằng chứng mạnh nhất** và là xương sống của lộ trình: **luyện truy xuất** (tự kiểm tra thay vì đọc lại),
   **giãn cách** (ôn rải theo ngày), **học lại liên tiếp đến tiêu chí** (kết hợp hai cái trên), **xen kẽ dạng bài** (trộn các
   dạng dễ nhầm để luyện kỹ năng *chọn* kỹ thuật).
4. **Với người mới, "lời giải mẫu + tự giải thích" hiệu quả hơn tự mày mò**. Nhưng **thử giải 10–15 phút trước khi xem
   lời giải** vẫn có lợi. Khi đã có nền (khoảng từ ngày 4), chuyển dần sang "tự giải trước, xem gợi ý sau" (hiệu ứng đảo ngược
   chuyên môn).
5. **Một bài đại diện là chưa đủ để hình thành schema.** Nghiên cứu về chuyển giao loại suy (Gick & Holyoak 1983; Alfieri và
   cộng sự 2013) cho thấy **so sánh hai bài cùng bản chất nhưng khác bề ngoài** tạo ra schema tốt hơn hẳn so với học kỹ một bài.
   Vì vậy đơn vị chọn bài ở Phần 3 sẽ là **bộ ba: bài Neo + bài Đồng cấu + bài Đối chứng** (bài trông giống nhưng phải giải khác).
6. **Giấc ngủ là một phần của quá trình học, không phải thời gian bị mất.** Thức trắng làm giảm khả năng ghi nhớ cái mới. Giấc
   ngủ sau buổi học củng cố kỹ năng và có thể giúp "ngộ" ra quy luật.
7. **Mục tiêu thật sự của 7 ngày**: xây khoảng 25–30 schema (khuôn mẫu tư duy) cho các dạng bài, kèm một "chỉ mục nhận diện"
   (dấu hiệu trong đề → kỹ thuật) và khả năng **ghép 2 schema** lại với nhau. Bài Hard mở đầu thường chính là sự ghép đó.

---

## 1. Nói rõ trước: khoa học hứa hẹn gì, không hứa hẹn gì

**Khoảng cách giữa khoa học thần kinh và lớp học.** Bruer (1997, *"Education and the brain: A bridge too far"*) đã cảnh báo
rằng rất ít phát hiện ở cấp độ tế bào hay vùng não có thể chuyển thẳng thành phương pháp dạy học. Gần 30 năm sau, nhận định này
vẫn đúng phần lớn. Trong tài liệu này:

- **Khoa học thần kinh** được dùng để giải thích cơ chế: hồi hải mã mã hóa ký ức mới, ký ức được củng cố khi ngủ, truy xuất
  kích hoạt lại và làm bền mạng ký ức, dopamine và sự tò mò.
- **Tâm lý học nhận thức và nghiên cứu giáo dục** (thí nghiệm ngẫu nhiên, phân tích gộp) được dùng để quyết định *làm gì*.

**Phân hạng bằng chứng dùng trong tài liệu:**

| Hạng | Ý nghĩa |
|---|---|
| **A** | Nhiều phân tích gộp và thí nghiệm ngẫu nhiên, lặp lại được ở nhiều loại tài liệu, có cả nghiên cứu trong lớp học thật |
| **B** | Có phân tích gộp hoặc nhiều thí nghiệm tốt nhưng hiệu ứng phụ thuộc điều kiện; hoặc bằng chứng mạnh trong một lĩnh vực hẹp (ví dụ giáo dục lập trình) |
| **C** | Bằng chứng hỗ trợ ở mức vừa hoặc nhỏ; hữu ích như điều kiện nền (ngủ, vận động, nghỉ) |
| **D** | Thiếu bằng chứng, chưa được lặp lại, hoặc đã bị bác bỏ. Không dùng hoặc chỉ dùng như mẹo tổ chức |

**Ngưỡng thực tế.** 7 ngày × khoảng 8 giờ tập trung ≈ 55–60 giờ. Đây là ngân sách cứng. Mọi lựa chọn ở các bước sau phải vừa
trong ngân sách này (xem mục 6.6).

---

## 2. Bộ não học kỹ năng giải thuật như thế nào

### 2.1. Nút thắt cổ chai: trí nhớ làm việc và tải nhận thức

- Trí nhớ làm việc chỉ giữ được khoảng **4 "khối" thông tin** cùng lúc (Cowan 2001).
- **Thuyết tải nhận thức** (Sweller 1988): khi người mới giải bài bằng cách mò mẫm từ đích ngược về (means–ends analysis), gần
  hết dung lượng trí nhớ làm việc bị dùng để tìm đường, không còn chỗ để *học* cấu trúc lời giải.
- **Hệ quả cho DSA:** một bài Hard như *76. Minimum Window Substring* đòi hỏi giữ cùng lúc: hai con trỏ, bảng đếm ký tự, điều
  kiện "cửa sổ hợp lệ", cách cập nhật đáp án, các trường hợp biên. Với người mới đó là 6–8 phần tử, vượt dung lượng. Với người đã
  có schema "cửa sổ trượt" thì cả cụm đó chỉ là **1 khối**, nên còn chỗ để nghĩ về phần khó riêng của bài.

### 2.2. Chunking và schema: chuyên gia "nhìn" thấy cấu trúc sâu

- **Cờ vua:** Chase & Simon (1973) cho thấy kiện tướng nhớ thế cờ thật nhanh hơn hẳn người mới, nhưng với thế cờ xếp ngẫu nhiên
  thì lợi thế gần như biến mất. Họ không có trí nhớ tốt hơn mà có **thư viện khối** (chunk) lớn hơn (Gobet và cộng sự 2001).
- **Vật lý:** Chi, Feltovich & Glaser (1981) cho người mới và chuyên gia phân loại bài cơ học. Người mới xếp theo **bề ngoài**
  ("bài mặt phẳng nghiêng", "bài lò xo"). Chuyên gia xếp theo **nguyên lý** ("bảo toàn năng lượng", "định luật 2 Newton").
- **Lập trình:** Soloway & Ehrlich (1984) đề xuất rằng lập trình viên giỏi nắm hai loại tri thức: **programming plans** (các
  đoạn chương trình chuẩn cho các chuỗi hành động hay gặp) và **quy tắc diễn đạt** (convention).
- **Hệ quả cho DSA:** người mới thấy "bài mảng", "bài chuỗi", "bài cây". Người giỏi thấy "đơn điệu → tìm kiếm nhị phân trên đáp
  án", "cần phần tử lớn hơn gần nhất → ngăn xếp đơn điệu", "tổng đoạn con có số âm → prefix sum + hash map". **Mục tiêu của
  7 ngày là chuyển người học từ cách phân loại thứ nhất sang thứ hai.**

### 2.3. Ba giai đoạn hình thành kỹ năng

| Giai đoạn (Fitts & Posner 1967; Anderson 1982) | Đặc điểm | Trong DSA |
|---|---|---|
| **Nhận thức / khai báo** | Biết *về* kỹ thuật, làm chậm, phải nghĩ từng bước, hay sai | Hiểu ý tưởng hai con trỏ khi đọc lời giải |
| **Liên kết / biên dịch tri thức** | Các bước gộp lại, ít lỗi hơn, bắt đầu nhận ra khi nào dùng | Tự viết được hai con trỏ cho bài mới cùng dạng |
| **Tự động** | Nhanh, ít tốn chú ý, giải phóng trí nhớ làm việc | Viết khung tìm kiếm nhị phân/BFS không cần nghĩ |

**Mục tiêu thực tế trong 7 ngày:** đưa các schema cốt lõi lên giai đoạn **liên kết**. Riêng các **khung code lặp lại** (tìm kiếm
nhị phân với biên trái/phải, khung BFS, Union-Find, khung quay lui) cần đưa lên **tự động** bằng luyện từng phần (drill). Như vậy
khi gặp bài Hard, trí nhớ làm việc dành cho phần thực sự mới.

### 2.4. Củng cố trí nhớ: truy xuất, khoảng cách và giấc ngủ

- **Truy xuất là một sự kiện củng cố nhanh.** Antony và cộng sự (2017) lập luận rằng mỗi lần chủ động nhớ lại sẽ kích hoạt lại
  thông tin liên quan và xây dựng biểu diễn trên trục hồi hải mã – vỏ não, giống một phần những gì xảy ra khi ngủ. Đọc lại thì
  không làm được điều này.
- **Giấc ngủ củng cố kỹ năng.** Walker và cộng sự (2002): sau một đêm ngủ, tốc độ gõ chuỗi phím tăng khoảng 20%, còn thời gian
  thức tương đương thì không tăng đáng kể. Diekelmann & Born (2010) tổng quan cơ chế: ký ức được "phát lại" và chuyển dần từ hồi
  hải mã sang vỏ não khi ngủ sóng chậm. Gais và cộng sự (2006): ngủ sớm sau khi học giúp giữ lại tốt hơn.
- **Giấc ngủ có thể giúp phát hiện quy luật ẩn.** Wagner và cộng sự (2004, *Nature*): sau 8 giờ ngủ, số người phát hiện quy tắc
  rút gọn ẩn trong bài toán tăng khoảng gấp 3 so với mức nền khoảng 20%. *Lưu ý:* Schönauer và cộng sự (2018) không thấy hiệu ứng
  này với các bài toán "insight" cổ điển. Hãy coi đây là lợi ích *có thể có*, không phải chắc chắn.
- **Thiếu ngủ làm hỏng việc học cái mới.** Yoo và cộng sự (2007): một đêm thức trắng làm giảm hoạt động hồi hải mã khi ghi nhớ và
  làm kết quả nhớ kém hơn (truyền thông thường trích "kém tới 40%"; con số này là kết quả hành vi, không phải đo "dung lượng" hồi
  hải mã).
- **Khoảng cách theo phút (cơ chế LTP):** nghiên cứu trên động vật cho thấy kích thích lặp lại cách nhau vài phút có thể khởi động
  LTP. Kelley & Whatson (2013) áp dụng thành "spaced learning" (3 lượt học 20 phút xen 10 phút nghỉ) với kết quả tích cực, nhưng
  **chưa được lặp lại độc lập** (hạng D). Lộ trình chỉ mượn ý tưởng nghỉ ngắn giữa các khối học.

### 2.5. Phân biệt "học" và "thể hiện"

Bjork (1994) và Soderstrom & Bjork (2015) chỉ ra: **kết quả trong lúc luyện là chỉ báo kém về việc học thật sự.** Học dồn (cùng
một dạng liên tục, đọc lại lời giải) cho cảm giác trôi chảy và điểm cao ngay lúc đó nhưng quên nhanh. Ngược lại các **"khó khăn có
ích"** (giãn cách, xen kẽ, tự kiểm tra) làm buổi học có vẻ chậm và vất vả hơn nhưng giữ lâu và chuyển giao tốt hơn. Người học
thường đánh giá sai điều này: trong Kornell & Bjork (2008), đa số người tham gia tin rằng học theo khối tốt hơn, dù học xen kẽ
cho kết quả tốt hơn. **Hệ quả:** lộ trình phải có tiêu chí đánh giá khách quan, có độ trễ, không dựa vào cảm giác "mình hiểu rồi".

### 2.6. Hệ quả thiết kế tổng hợp từ cơ chế

> Mục tiêu 7 ngày = **(1)** một thư viện khoảng 25–30 schema/khung code, **(2)** một chỉ mục nhận diện "dấu hiệu → schema", được
> luyện bằng xen kẽ, **(3)** khả năng ghép 2 schema, **(4)** tất cả được củng cố bằng truy xuất giãn cách và giấc ngủ đủ.

---

## 3. Đánh giá từng phương pháp

### 3.0. Bảng tổng quan

| # | Phương pháp | Hạng | Hiệu ứng tiêu biểu | Luyện kỹ năng DSA nào |
|---|---|---|---|---|
| 1 | Luyện truy xuất (testing effect) | A | g ≈ 0,50 (Rowland 2014); chuyển giao d ≈ 0,40 (Pan & Rickard 2018) | Nhớ khung code, bất biến, dấu hiệu nhận diện |
| 2 | Giãn cách (distributed practice) | A | Truy xuất giãn cách so với dồn: g ≈ 0,74 (Latimier và cộng sự 2021) | Giữ kiến thức qua 7 ngày và sau đó |
| 3 | Học lại liên tiếp đến tiêu chí | A | Kết hợp 1 + 2; hiệu quả cao với tài liệu môn học thật | Đảm bảo không "học rồi bỏ" |
| 4 | Xen kẽ (interleaving) | A– | g ≈ 0,42 (Brunmair & Richter 2019); d = 0,83 trong RCT toán lớp 7 (Rohrer và cộng sự 2020) | **Chọn đúng kỹ thuật** cho bài chưa gặp |
| 5 | Lời giải mẫu + giảm dần hỗ trợ | A (với người mới) | Hiệu ứng lời giải mẫu; đảo chiều khi đã giỏi (Kalyuga và cộng sự 2003) | Học dạng mới nhanh, ít quá tải |
| 6 | Tự giải thích (self-explanation) | B+ | g ≈ 0,55 (Bisra và cộng sự 2018) | Hiểu *vì sao* thuật toán đúng |
| 7 | Nhãn mục tiêu con (subgoal labels) | B (mạnh trong CS) | Cải thiện giải bài mới trong lập trình (Margulieux và cộng sự 2012, 2016) | Phân rã khung code thành các bước có tên |
| 8 | So sánh loại suy / ca đối chứng | B+ | d ≈ 0,50 (Alfieri và cộng sự 2013) | Trừu tượng hóa schema từ 2 bài |
| 9 | Thử trước khi học / thất bại có ích | B | g ≈ 0,36 (Sinha & Kapur 2021) | Kích hoạt tri thức cũ, thấy rõ chỗ hổng |
| 10 | Đọc – lần vết – giải thích – viết code | B (CS) | Kỹ năng lần vết code liên quan tới kỹ năng viết code (Lopez và cộng sự 2008); Parsons tiết kiệm thời gian (Ericson và cộng sự 2017) | Nắm cơ chế trước khi code |
| 11 | Luyện tập có chủ đích + phản hồi | B | Luyện tập giải thích 12% phương sai tổng, chỉ 4% trong giáo dục (Macnamara và cộng sự 2014) | Tập trung vào điểm yếu, có phản hồi nhanh |
| 12 | Học đến thành thạo + gợi ý theo bước | B | Kèm cặp 1-1 d ≈ 0,79; hệ thống gia sư theo bước ≈ 0,76 (VanLehn 2011) | Không bước tiếp khi nền chưa vững |
| 13 | Mã hóa kép / trực quan hóa | C+ | Hỗ trợ khi hình minh họa đúng cơ chế | Vẽ con trỏ, cây đệ quy, bảng DP |
| 14 | Giấc ngủ (và ngủ trưa) | B (cơ chế), C (áp dụng) | Xem mục 2.4 | Củng cố kỹ năng, phát hiện quy luật |
| 15 | Ấp ủ / nghỉ có cấu trúc | C | d ≈ 0,29 (Sio & Ormerod 2009); Pomodoro: kết quả trái chiều | Thoát bế tắc khi bị kẹt |
| 16 | Vận động thể chất | C | Vận động cấp tính, trí nhớ dài hạn ES ≈ 0,52 (Roig và cộng sự 2013) | Tỉnh táo, tốc độ học |
| 17 | Tò mò / động lực / đặt cược | C | Tò mò tăng ghi nhớ phụ thuộc hồi hải mã (Gruber và cộng sự 2014) | Duy trì năng lượng trong 7 ngày |

---

### 3.1. Luyện truy xuất (Retrieval practice / testing effect) — Hạng A

- **Nguyên lý:** chủ động lấy thông tin ra khỏi trí nhớ làm vết nhớ bền hơn nhiều so với đưa thông tin vào lại (đọc lại).
- **Bằng chứng:**
  - Roediger & Karpicke (2006): sau 1 tuần, nhóm tự kiểm tra nhiều lần nhớ khoảng 61%, nhóm đọc lại nhiều lần khoảng 40%.
  - Karpicke & Blunt (2011, *Science*): luyện truy xuất đạt 67% so với 45% ở nhóm vẽ sơ đồ tư duy, *kể cả* với câu hỏi suy luận.
  - Phân tích gộp: Rowland (2014) g ≈ 0,50. Adesope và cộng sự (2017) xác nhận hiệu ứng trên nhiều định dạng.
  - **Chuyển giao:** Pan & Rickard (2018): d ≈ 0,40; mạnh nhất với câu hỏi áp dụng và suy luận.
  - Dunlosky và cộng sự (2013) xếp vào nhóm "hiệu quả cao". Câu hỏi **tự tạo câu trả lời** (viết ra) hiệu quả hơn câu hỏi nhận
    diện (trắc nghiệm).
- **Ưu điểm:** rẻ, áp dụng được cho mọi nội dung, vừa học vừa kiểm tra.
- **Hạn chế:** khó chịu hơn đọc lại. Người học tự học thường không dùng nó (Karpicke, Butler & Roediger 2009). Cần phản hồi
  (đối chiếu đáp án) khi tỉ lệ nhớ đúng thấp.
- **Áp dụng vào DSA 7 ngày:**
  - **"Trang trắng" đầu mỗi buổi:** không mở tài liệu, viết lại khung code + bất biến + độ phức tạp của các dạng đã học. Sau đó
    mới đối chiếu.
  - **Giải lại từ editor trống** thay vì đọc lại lời giải. Một bài chỉ được tính là "đã biết" khi gõ lại được từ đầu.
  - **Thẻ ghi nhớ hai chiều:** mặt trước "Mảng đã sắp xếp, tìm cặp có tổng = target, bộ nhớ O(1)?", mặt sau "Hai con trỏ từ hai
    đầu, vì tổng đơn điệu theo từng con trỏ". Chiều ngược lại: "Ngăn xếp đơn điệu dùng khi nào?".
  - **Giải ở mức kế hoạch (plan-only):** đọc đề rồi trong 3–5 phút viết ra dạng bài, ý tưởng, độ phức tạp, *không code*. Đây là
    lượt truy xuất rẻ nhất cho kỹ năng nhận diện.

### 3.2. Giãn cách (Spacing / distributed practice) — Hạng A

- **Nguyên lý:** cùng tổng thời gian, chia thành nhiều lượt cách nhau thì nhớ lâu hơn học dồn một lần.
- **Bằng chứng:**
  - Cepeda và cộng sự (2006): tổng quan 317 thí nghiệm. Cepeda và cộng sự (2008): hơn 1.350 người. **Khoảng cách tối ưu tăng
    theo thời gian cần nhớ**: khoảng **10–20% thời gian cần nhớ** khi mục tiêu là vài tuần, giảm còn khoảng 5% khi mục tiêu là 1 năm.
  - Latimier, Peyre & Ramus (2021): truy xuất giãn cách tốt hơn truy xuất dồn, g ≈ 0,74. **Lịch giãn dần (1-2-4-8…) không tốt hơn
    lịch đều** (g ≈ 0,03).
- **Ưu điểm:** hiệu ứng lớn và ổn định. Dễ lên lịch.
- **Hạn chế:** trong 7 ngày, không thể dùng khoảng cách dài. Nếu muốn nhớ nhiều tháng thì *bắt buộc* phải có lịch duy trì sau 7 ngày.
- **Áp dụng:**
  - **Hai mục tiêu thời gian:** (a) nhớ đến cuối ngày 7, khoảng cách tối ưu ≈ 1 ngày; (b) nhớ 1–3 tháng, khoảng cách ≈ 3–7 ngày.
  - **Lịch:** nội dung học ngày N được ôn vào **tối ngày N → sáng N+1 → N+3 → ngày 7**, rồi duy trì ở **ngày 14 và ngày 30**
    (bảng ở mục 6.5).
  - Vì lịch giãn dần không hơn lịch đều, chọn lịch **đơn giản, dễ tuân thủ**.

### 3.3. Học lại liên tiếp đến tiêu chí (Successive relearning) — Hạng A

- **Nguyên lý:** trong mỗi buổi, truy xuất có phản hồi cho đến khi làm đúng ít nhất 1 lần. Lặp lại ở nhiều buổi cách nhau.
- **Bằng chứng:** Rawson & Dunlosky (2011, 2013); Rawson, Dunlosky & Sciartelli (2013) với bài thi môn học thật. Ghi nhớ lâu dài
  tốt hơn rõ rệt. *Lưu ý:* nhiều nghiên cứu so với "học như thường lệ", không so với nhóm đọc lại có cùng thời gian.
- **Áp dụng (quy tắc vận hành chính của lộ trình):**
  - Mỗi bài trọng điểm có trạng thái: *Chưa đạt → Đạt 1 lần → Đạt 2 lần (cách ≥ 1 ngày) → Vững*.
  - **"Đạt"** = giải lại từ trang trắng, không xem gợi ý, trong giới hạn thời gian, giải thích được bất biến.
  - Bài nào phải xem lời giải sẽ vào **hàng đợi học lại** và được giải lại ở buổi kế tiếp.

### 3.4. Xen kẽ dạng bài (Interleaving) — Hạng A–

- **Nguyên lý:** trộn bài của nhiều dạng thay vì làm liền 10 bài cùng dạng. Người học phải tự quyết định *dùng kỹ thuật nào*.
  Cơ chế chính là **so sánh phân biệt**: nhìn thấy các dạng cạnh nhau giúp nhận ra ranh giới giữa chúng.
- **Bằng chứng:**
  - Rohrer & Taylor (2007): trộn bài toán giúp học tốt hơn.
  - Kornell & Bjork (2008): học xen kẽ tốt hơn, *dù người học tin điều ngược lại*.
  - Brunmair & Richter (2019): 59 nghiên cứu, g ≈ 0,42. **Hiệu ứng lớn hơn khi các dạng giống nhau bề ngoài**. Không hiệu quả
    (thậm chí có hại) với học từ vựng hay văn bản giải thích.
  - Rohrer, Dedrick, Hartwig & Cheung (2020): RCT 54 lớp toán lớp 7, kiểm tra bất ngờ sau 1 tháng: 61% so với 38%, d = 0,83.
- **Hạn chế:** khi mới học một dạng hoàn toàn mới, học theo khối ngắn trước giúp nắm cơ chế. Làm bài xen kẽ tốn thời gian hơn.
- **Áp dụng (đây là phương pháp "đo ni đóng giày" cho DSA):** kỹ năng khó nhất với người mới không phải *thực hiện* hai con trỏ
  mà là *biết khi nào* dùng nó.
  - **Mô hình lai:** học dạng mới theo khối ngắn (bài Neo + Đồng cấu), **ngay chiều cùng ngày** đưa vào bộ bài trộn.
  - **Bộ trộn ẩn nhãn** mỗi chiều: 4–6 bài từ *mọi* dạng đã học, không ghi tên dạng, xáo thứ tự.
  - **Xen kẽ các cặp dễ nhầm** (đúng điều kiện mà Brunmair & Richter thấy hiệu ứng mạnh nhất): cửa sổ trượt ↔ prefix sum;
    hai con trỏ ↔ tìm kiếm nhị phân; BFS ↔ DFS ↔ Dijkstra; tham lam ↔ quy hoạch động; quay lui ↔ quy hoạch động; heap ↔ sắp xếp.
  - Ngày 6–7: gần như toàn bộ là luyện xen kẽ và thi thử.

### 3.5. Lời giải mẫu, giảm dần hỗ trợ và hiệu ứng đảo ngược chuyên môn — Hạng A (với người mới)

- **Nguyên lý:** người mới học một cấu trúc phức tạp qua **lời giải mẫu được giải thích từng bước** hiệu quả hơn tự giải, vì giảm
  tải nhận thức thừa (Sweller 1988; Kirschner, Sweller & Clark 2006). Sau đó **giảm dần hỗ trợ**: lời giải đầy đủ → lời giải
  thiếu vài bước → tự giải (Renkl, Atkinson và cộng sự 2002).
- **Hiệu ứng đảo ngược chuyên môn** (Kalyuga, Ayres, Chandler & Sweller 2003): cái giúp người mới có thể *cản trở* người đã có nền.
  Khi đã có schema, đọc lời giải chi tiết thành thừa, còn tự giải lại hiệu quả hơn.
- **Áp dụng:**
  - Ngày 1–3 (dạng hoàn toàn mới): lời giải mẫu là chủ đạo, nhưng **luôn có một bước thử ngắn trước** (mục 3.9).
  - Ngày 4–7: đảo thứ tự. Tự giải trước, chỉ xem gợi ý theo bậc (mục 3.12).
  - **Kho notebook tiếng Việt của repo chính là nguồn lời giải mẫu chất lượng.** Điều kiện là phải đọc *chủ động* (mục 6.9).
    Đọc thụ động sẽ tạo ra ảo giác trôi chảy.

### 3.6. Tự giải thích và tra hỏi "tại sao" — Hạng B+

- **Nguyên lý:** khi đọc lời giải, tự giải thích *vì sao* mỗi bước đúng giúp nối kiến thức mới với kiến thức cũ và phát hiện chỗ
  không hiểu.
- **Bằng chứng:** Chi và cộng sự (1989): học sinh giỏi tự giải thích nhiều hơn khi học lời giải mẫu. Chi và cộng sự (1994): *nhắc*
  tự giải thích cải thiện hiểu biết. Bisra và cộng sự (2018): 64 nghiên cứu, g ≈ 0,55. Dunlosky (2013) xếp mức "trung bình". Dạy
  lại cho người khác có lợi cho ghi nhớ lâu dài (Fiorella & Mayer 2013).
- **Hạn chế:** tốn thời gian. Chất lượng giải thích quyết định hiệu quả. Cần câu hỏi gợi ý cụ thể.
- **Áp dụng (bộ câu hỏi cố định cho mọi bài trọng điểm):**
  1. *Bất biến là gì?* Điều gì luôn đúng sau mỗi vòng lặp?
  2. *Vì sao không bỏ sót đáp án?* (lập luận đúng đắn, ví dụ vì sao được phép bỏ con trỏ trái)
  3. *Vì sao độ phức tạp là O(…)?* Mỗi phần tử vào/ra bao nhiêu lần?
  4. *Nếu bỏ dòng này, test nào sai?*
  5. *Dấu hiệu nào trong đề gợi ý kỹ thuật này?*

  Cuối mỗi dạng: giải thích lại bằng lời trong 2 phút như đang dạy người khác (kỹ thuật Feynman, thực chất là tự giải thích + dạy lại).

### 3.7. Nhãn mục tiêu con (Subgoal labels) — Hạng B (bằng chứng mạnh riêng cho giáo dục lập trình)

- **Nguyên lý:** gắn nhãn chức năng cho từng cụm bước trong lời giải mẫu. Người học thấy *cấu trúc* thay vì một chuỗi dòng code,
  nhờ đó chuyển giao sang bài mới có bề ngoài khác.
- **Bằng chứng:** Catrambone (1998). Margulieux, Guzdial & Catrambone (2012) và Margulieux, Catrambone & Guzdial (2016): lời giải
  mẫu có nhãn mục tiêu con giúp người học lập trình giải bài mới tốt hơn. Cơ chế được đề xuất: làm nổi bật cấu trúc, giúp tổ chức
  thông tin, kích thích tự giải thích.
- **Áp dụng:** mọi khung code trong lộ trình viết dưới dạng **các bước có tên**. Ví dụ cửa sổ trượt (độ dài thay đổi):

  ```text
  [1] Mở rộng: đưa nums[right] vào cửa sổ, cập nhật trạng thái
  [2] Kiểm tra vi phạm: trạng thái còn hợp lệ không?
  [3] Co lại: khi vi phạm, bỏ nums[left], left += 1, cập nhật trạng thái
  [4] Ghi nhận: cập nhật đáp án từ cửa sổ hợp lệ hiện tại
  ```

  Người học tự viết nhãn trước, sau đó so với nhãn chuẩn. Khi gặp bài lạ, câu hỏi là "trạng thái là gì, vi phạm là gì", không
  phải "code bài nào giống".

### 3.8. So sánh loại suy và ca đối chứng — Hạng B+

- **Nguyên lý:** schema trừu tượng hình thành khi **so sánh** các ví dụ, không phải khi học kỹ một ví dụ.
- **Bằng chứng:**
  - Gick & Holyoak (1983): với *một* ví dụ, cả tóm tắt, nêu nguyên lý hay vẽ sơ đồ đều không giúp trừu tượng hóa schema. Với *hai*
    ví dụ được so sánh, người học hình thành schema, và **chất lượng schema dự đoán khả năng chuyển giao**.
  - Alfieri, Nokes-Malach & Schunn (2013): 57 thí nghiệm, d ≈ 0,50. Hiệu quả hơn khi yêu cầu tìm điểm chung và khi nguyên lý được
    nêu *sau* khi so sánh.
  - Schwartz & Bransford (1998): phân tích các ca đối chứng trước giúp người học tiếp thu bài giảng sau đó tốt hơn.
- **Áp dụng (điểm điều chỉnh quan trọng cho yêu cầu "chỉ cần học sâu một bài"):** một bài đại diện là điều kiện cần nhưng chưa đủ.
  Đơn vị tối thiểu là **bộ ba**:
  - **Neo:** bài kinh điển, sạch, thể hiện schema rõ nhất.
  - **Đồng cấu:** bề ngoài khác, *bản chất giống*. Sau khi giải, viết 2–3 câu "hai bài này giống nhau ở…". Ví dụ
    *704. Binary Search* ↔ *875. Koko Eating Bananas* (tìm kiếm nhị phân trên chỉ số ↔ trên không gian đáp án).
  - **Đối chứng:** *bề ngoài giống*, bản chất khác. Ví dụ *209. Minimum Size Subarray Sum* (số dương → cửa sổ trượt được) ↔
    *560. Subarray Sum Equals K* (có số âm → cửa sổ trượt sai, phải dùng prefix sum + hash map). Bài đối chứng dạy **ranh giới
    áp dụng**, đúng thứ mà kỹ năng nhận diện cần.
  - Phần 3 sẽ chọn bài theo cấu trúc này. Các bài tương tự khác chỉ được thêm khi chúng dạy một *biến thể* hoặc *ghép* mới.

### 3.9. Thử trước khi học, tạo sinh, thất bại có ích — Hạng B

- **Nguyên lý:** cố gắng trả lời hoặc giải *trước* khi được dạy, kể cả khi sai, giúp tiếp thu lời giải sau đó tốt hơn. Lý do:
  kích hoạt tri thức cũ, thấy rõ chỗ hổng, chú ý vào đúng phần quan trọng.
- **Bằng chứng:**
  - Richland, Kornell & Kao (2009): làm bài kiểm tra trước khi đọc giúp nhớ tốt hơn, và lợi ích đến từ việc *cố trả lời*, không
    phải từ việc đã thấy câu hỏi. Kornell, Hays & Bjork (2009): đoán sai rồi được sửa vẫn nhớ đáp án đúng tốt hơn.
  - Kapur (2008); Sinha & Kapur (2021): 53 nghiên cứu, giải trước rồi học tốt hơn học trước rồi giải, g ≈ 0,36. Hiệu ứng mạnh hơn
    (0,37–0,58) khi tuân thủ nguyên tắc "productive failure". Ngược lại với học sinh nhỏ tuổi và kỹ năng chung chung.
- **Mâu thuẫn bề ngoài với mục 3.5 và cách hòa giải:** lời giải mẫu tốt hơn *tự mò hoàn toàn*. Nhưng *thử ngắn có giới hạn thời
  gian rồi học lời giải* tốt hơn *học lời giải ngay*. Hai kết quả này khớp nhau nếu giới hạn thời gian thử.
- **Áp dụng:** với mỗi dạng mới, **thử bài Neo 10–15 phút**: viết brute force, ước lượng độ phức tạp, ghi lại *vì sao* nó chậm
  hoặc sai. Rồi mới học lời giải mẫu. Tối hôm trước, đọc đề các bài Neo của ngày mai (nghĩ thử, không giải) để tạo "câu hỏi treo"
  cho não xử lý.

### 3.10. Lần vết code, giải thích, rồi mới viết (nghiên cứu giáo dục lập trình) — Hạng B

- **Bằng chứng:** Lopez, Whalley, Robbins & Lister (2008): có thứ bậc kỹ năng *biết cú pháp → lần vết / giải thích code → viết
  code*. Khả năng lần vết code lặp liên quan đến khả năng viết code (tương quan thực sự nhưng chỉ ở mức vừa phải). Ericson,
  Margulieux & Rick (2017): **bài Parsons** (sắp xếp lại các dòng code bị xáo) cho kết quả học tương đương viết code từ đầu nhưng
  **nhanh hơn**.
- **Áp dụng:**
  - Với mỗi thuật toán mới: **lần vết bằng tay** trên input nhỏ (vẽ mảng, vị trí con trỏ, ngăn xếp, hàng đợi, bảng DP) → **giải
    thích bằng lời** → mới **viết code**.
  - **Khởi động bằng bài Parsons tự chế:** xáo các dòng của khung code (BFS, Union-Find, quay lui) rồi sắp lại. Nhanh hơn gõ lại
    toàn bộ, dùng xen với gõ lại từ trang trắng.

### 3.11. Luyện tập có chủ đích và phản hồi — Hạng B

- **Bằng chứng:** Ericsson, Krampe & Tesch-Römer (1993): luyện tập *có chủ đích* (nhắm điểm yếu, ở rìa năng lực, có phản hồi) mới
  tạo ra tiến bộ. Người luyện tốt nhất hiếm khi luyện có chủ đích quá khoảng 4 giờ/ngày. Macnamara, Hambrick & Oswald (2014):
  luyện tập chỉ giải thích khoảng 12% khác biệt thành tích nói chung, khoảng 4% trong giáo dục. **Luyện tập quan trọng nhưng không
  phải tất cả; chất lượng và thiết kế luyện tập quan trọng hơn số giờ.**
- **Áp dụng:**
  - **Sổ lỗi có phân loại** (mục 6.8): mỗi lỗi dẫn tới một bài drill riêng.
  - **Phản hồi tức thì:** chạy test và nộp lên judge của LeetCode. Tự nghĩ test biên trước khi nộp.
  - **Giới hạn cường độ:** khoảng 4–5 giờ/ngày cường độ cao (học mới, giải độc lập, bộ trộn). Phần còn lại là cường độ thấp hơn
    (ôn, drill khung, phản tư).

### 3.12. Học đến thành thạo và gợi ý theo bước — Hạng B

- **Bằng chứng:** Bloom (1984): "2 sigma" của kèm cặp 1-1 kết hợp học đến thành thạo. VanLehn (2011) đánh giá lại: kèm cặp người
  thật d ≈ 0,79, hệ thống gia sư thông minh **theo từng bước** ≈ 0,76, hệ thống chỉ chấm đáp án ≈ 0,31. Phản hồi ở **từng bước**
  là yếu tố then chốt, không phải đưa đáp án. Koedinger và cộng sự (2023, *PNAS*): trên 1,3 triệu lượt tương tác, **tốc độ học
  của học sinh giống nhau đến bất ngờ**, khoảng **+0,1 log-odds (~2,5 điểm % độ chính xác) mỗi lượt luyện có phản hồi**. Khác
  biệt chủ yếu đến từ *kiến thức ban đầu*. Nghĩa là: muốn thành thạo cần **đủ số lượt luyện có phản hồi** cho mỗi đơn vị kiến
  thức, không có đường tắt.
- **Áp dụng:**
  - **Cổng thành thạo:** không chuyển sang dạng phụ thuộc khi dạng tiên quyết chưa qua cổng (ví dụ chưa vững duyệt cây/đệ quy thì
    chưa sang quay lui và DP).
  - **Thang gợi ý 5 bậc** (mô phỏng gia sư theo bước; dùng được với AI hoặc phần "Hint" của LeetCode):
    0 tự làm 15–20 phút → 1 chỉ xem *tên dạng/dấu hiệu* → 2 xem *ý tưởng* (không code) → 3 xem *mã giả* → 4 xem *lời giải đầy đủ*.
    Dùng bậc 3–4 thì bài tự động vào hàng đợi học lại.
  - Khi dùng AI làm gia sư: yêu cầu **gợi ý từng bước**, cấm đưa code hoàn chỉnh.

### 3.13. Mã hóa kép và trực quan hóa — Hạng C+

- **Bằng chứng:** Paivio (1986); Mayer (2009, học đa phương tiện): lời + hình đúng cơ chế giúp hiểu tốt hơn chỉ lời. **Không
  liên quan đến "phong cách học"** (mục 4).
- **Áp dụng:** mỗi schema có **một hình chuẩn**: hai con trỏ trên mảng, cửa sổ co giãn, ngăn xếp đơn điệu, cây đệ quy, bảng DP
  2 chiều, đồ thị với hàng đợi BFS. Vẽ tay khi lần vết.

### 3.14. Điều kiện sinh lý: ngủ, nghỉ, vận động, động lực — Hạng B/C

| Yếu tố | Bằng chứng | Quy tắc trong lộ trình |
|---|---|---|
| **Ngủ đêm** | Mục 2.4: củng cố kỹ năng (Walker 2002), có thể giúp phát hiện quy luật (Wagner 2004), thiếu ngủ làm hỏng ghi nhớ (Yoo 2007) | **7,5–9 giờ/đêm, tuyệt đối không thức trắng.** Ôn nhẹ 15–20 phút trước khi ngủ, không học nội dung mới căng thẳng ngay trước giờ ngủ |
| **Ngủ trưa** | Mednick và cộng sự (2003): giấc ngủ trưa 60–90 phút cho cải thiện học tri giác tương đương một đêm | Tùy chọn: 20–30 phút để hồi tỉnh táo, hoặc 60–90 phút nếu có điều kiện |
| **Caffeine** | Drake và cộng sự (2013): caffeine 6 giờ trước khi ngủ vẫn làm giảm giấc ngủ | Chỉ dùng buổi sáng |
| **Ấp ủ khi bế tắc** | Sio & Ormerod (2009): 117 nghiên cứu, d ≈ 0,29. Mạnh hơn khi đã chuẩn bị kỹ trước và khi khoảng nghỉ là hoạt động *nhẹ nhàng* | Kẹt quá 25–30 phút: ghi lại chỗ kẹt, đi bộ 10 phút, rồi quay lại. Nếu vẫn kẹt thì lên thang gợi ý |
| **Nghỉ có cấu trúc** | Biwer và cộng sự (2023): nghỉ theo lịch tốt hơn tự nghỉ về mệt mỏi và động lực; Smits và cộng sự (2025): kết quả ngược lại hoặc không khác | Khối 50–90 phút + nghỉ 10–15 phút. Pomodoro dùng tùy thích, không có phép màu |
| **Vận động** | Roig và cộng sự (2013): vận động cấp tính cải thiện trí nhớ dài hạn ES ≈ 0,52. Winter và cộng sự (2007): học từ vựng nhanh hơn 20% sau chạy cường độ cao, nhưng không giữ lâu hơn | 20–30 phút vận động vừa đến mạnh trước khối học sáng. Đi bộ trong giờ nghỉ |
| **Tò mò, động lực** | Gruber, Gelman & Ranganath (2014): trạng thái tò mò tăng ghi nhớ phụ thuộc hồi hải mã qua mạch dopamine | Mở đầu mỗi dạng bằng một câu đố "vì sao brute force chậm?". Thi thử có tính giờ ở ngày 6–7 tạo áp lực vừa phải |

---

## 4. Loại bỏ hoặc dùng thận trọng

| Phương pháp / niềm tin | Đánh giá | Lý do |
|---|---|---|
| **Phong cách học** (người học "thị giác", "thính giác"…) | **D, loại bỏ** | Pashler, McDaniel, Rohrer & Bjork (2008): không có bằng chứng đầy đủ cho việc dạy theo phong cách học. Một số kiểm chứng còn cho kết quả ngược |
| **Đọc lại, tô sáng, tóm tắt** | **D** (Dunlosky 2013: hiệu quả thấp) | Tạo cảm giác trôi chảy nhưng ít củng cố. Đọc lại notebook lời giải là cái bẫy lớn nhất của repo này nếu dùng sai |
| **"Kim tự tháp học tập"** (nhớ 10% khi đọc, 90% khi dạy…) | **D** | Không có dữ liệu gốc (Lalley & Miller 2007). Ý "dạy lại có ích" đúng, nhưng các con số là bịa |
| **"10.000 giờ" như quy luật** | **Thận trọng** | Macnamara và cộng sự (2014): luyện tập chỉ giải thích một phần khác biệt. Chất lượng luyện tập mới là yếu tố chính |
| **Học dồn liên tục 12–14 giờ/ngày, thức khuya** | **Loại bỏ** | Đi ngược bằng chứng về giãn cách, giới hạn luyện tập có chủ đích và giấc ngủ. "Thể hiện" tăng, "học" giảm |
| **"Spaced learning" 20-10-20 phút** (Kelley & Whatson 2013) | **D (hứa hẹn)** | Dựa trên cơ chế LTP, kết quả ban đầu tốt nhưng chưa được lặp lại độc lập. Chỉ mượn ý nghỉ ngắn giữa các khối |
| **Nhạc sóng não, nootropics, "học trong khi ngủ"** | **D** | Không có bằng chứng cho việc học kỹ năng phức tạp. Kích hoạt lại ký ức khi ngủ chỉ củng cố cái đã học khi thức |
| **Ultralearning, "20 giờ đầu tiên", DiSSS** | **Khung thực hành, không phải nghiên cứu** | Hữu ích để *tổ chức* việc học. Phần cốt lõi có thể quy về các phương pháp hạng A/B (mục 5.1) |
| **Giải thật nhiều bài theo danh sách dài** | **Thận trọng** | Không có xen kẽ, giãn cách hay chọn lọc thì nhiều bài trùng bản chất chỉ thêm "thể hiện", không thêm schema mới |

---

## 5. Các lộ trình và khung học cấp tốc đáng tham khảo

### 5.1. Khung thực hành học thần tốc

| Khung | Ý chính | Bằng chứng tương ứng | Mượn gì cho DSA 7 ngày |
|---|---|---|---|
| **Ultralearning** (Scott Young 2019; thử thách tự học chương trình khoa học máy tính MIT trong khoảng 1 năm) | Metalearning, tập trung, *trực tiếp* (luyện đúng kỹ năng đích), *drill* điểm yếu, truy xuất, phản hồi, ghi nhớ, trực giác, thử nghiệm | Trực tiếp ≈ xử lý phù hợp với hình thức kiểm tra; drill ≈ luyện từng phần trong 4C/ID; truy xuất ≈ testing effect | Chu trình "giải bài thật → tìm điểm yếu → drill → quay lại bài thật" |
| **The First 20 Hours** (Josh Kaufman 2013) | Phân rã kỹ năng, học vừa đủ để tự sửa sai, loại bỏ rào cản, luyện ≥ 20 giờ | Phân rã ≈ phân tích nhiệm vụ; tự sửa sai ≈ phản hồi | Chuẩn bị môi trường trước ngày 1 (editor, tài khoản LeetCode, mẫu thẻ ghi nhớ) |
| **DiSSS** (Tim Ferriss 2012) | Phân rã, chọn lọc 80/20, sắp thứ tự, đặt cược | Chọn lọc ≈ ưu tiên tri thức có tần suất cao | Lọc kiến thức theo tần suất xuất hiện trong 3.711 bài (Phần 2–3) |
| **A Mind for Numbers** (Barbara Oakley 2014) | Chế độ "tập trung" và "lan tỏa", chunking, tự kiểm tra | "Lan tỏa" ≈ ấp ủ (d ≈ 0,29); chunking ≈ Chase & Simon | Luân phiên tập trung sâu và nghỉ nhẹ khi bế tắc |

### 5.2. Mô hình thiết kế giảng dạy cho kỹ năng phức tạp

- **4C/ID** (van Merriënboer 1997; van Merriënboer, Clark & de Croock 2002): 4 thành phần cho kỹ năng phức tạp:
  1. **Nhiệm vụ học trọn vẹn** (bài LeetCode thật, từ dễ đến khó, hỗ trợ giảm dần);
  2. **Thông tin hỗ trợ** (mô hình tư duy, "vì sao", tức thẻ schema);
  3. **Thông tin quy trình đúng lúc** (cú pháp, API như `heapq`, `bisect`, `collections.deque`, tra khi cần);
  4. **Luyện từng phần** cho kỹ năng lặp lại đến mức tự động (khung tìm kiếm nhị phân, BFS, Union-Find), *luôn đặt trong bối
     cảnh bài trọn vẹn*.

  Đây là khung kiến trúc tốt nhất cho một ngày học DSA.
- **Học nghề nhận thức** (Collins, Brown & Newman 1989): làm mẫu → kèm cặp → hỗ trợ rồi rút dần → diễn đạt thành lời → phản tư →
  khám phá. Ánh xạ: lời giải mẫu → gợi ý theo bậc → giảm dần hỗ trợ → giải thích lại → sổ lỗi → bài Hard ghép.
- **Học đến thành thạo / gia sư nhận thức** (Bloom; Anderson và cộng sự 1995; Koedinger): chia thành đơn vị kiến thức, luyện có
  phản hồi theo bước, chỉ đi tiếp khi thành thạo.

### 5.3. Bài học từ các lĩnh vực đòi hỏi tư duy cao

| Lĩnh vực | Cách chuyên gia được đào tạo | Ánh xạ sang DSA |
|---|---|---|
| **Cờ vua** | Học các motif chiến thuật (đòn chĩa, ghim…) qua rất nhiều bài tập ngắn, phân tích ván của kiện tướng. Chunking (Chase & Simon 1973; Gobet 2001) | Motif ↔ dạng bài; bài tập chiến thuật ↔ "plan-only" (nhận dạng nhanh) |
| **Toán** | Pólya (1945): hiểu đề → lập kế hoạch → thực hiện → nhìn lại. Schoenfeld (1985): người giỏi dành thời gian *phân tích và giám sát*, người mới lao vào tính ngay. Xen kẽ bài (Rohrer) | Quy trình 4 bước cố định cho mọi bài (dùng trong Phần 4–5), đặc biệt bước "nhìn lại": liên hệ với schema nào |
| **Vật lý** | Phân loại theo nguyên lý (Chi 1981) | Bài tập *phân loại đề* (không giải) theo dạng, có xen kẽ |
| **Lập trình** | Programming plans (Soloway & Ehrlich 1984); lần vết rồi mới viết (Lister, Lopez); nhãn mục tiêu con (Margulieux); bài Parsons (Ericson) | Khung code có nhãn mục tiêu con; lần vết bằng tay; Parsons để khởi động |

### 5.4. Các lộ trình DSA phổ biến: điểm mạnh và điểm yếu

| Lộ trình | Điểm mạnh | Điểm yếu nhìn từ khoa học học tập |
|---|---|---|
| **Blind 75 / NeetCode 150 + roadmap** ([neetcode.io/roadmap](https://neetcode.io/roadmap)) | Có cây phụ thuộc chủ đề rõ; bài được chọn lọc kỹ; nhóm theo dạng (tốt cho schema) | Học theo khối từng chủ đề, ít xen kẽ; không có lịch giãn cách; không phân biệt bài Neo / Đồng cấu / Đối chứng |
| **Grind 75** (Yangshun Tay, [techinterviewhandbook.org/grind75](https://www.techinterviewhandbook.org/grind75)) | Tự điều chỉnh theo số tuần và giờ mỗi tuần; trộn chủ đề trong tuần | Thiết kế cho 2–6 tháng; ít hướng dẫn về truy xuất hay tiêu chí thành thạo |
| **Grokking the Coding Interview (patterns)** | Dạy theo *mẫu tư duy* (khoảng 28 đến hơn 40 mẫu tùy phiên bản), rất gần khái niệm schema | Nhiều mẫu chồng lấn; thiên về khối; mang tính thương mại |
| **LeetCode Patterns** (Sean Prashad, [seanprashad.com/leetcode-patterns](https://seanprashad.com/leetcode-patterns/)) | Gắn nhãn mẫu cho từng bài, tiện chọn bài | Chỉ là danh sách, không có thứ tự học |
| **USACO Guide / CSES / Competitive Programmer's Handbook** ([usaco.guide](https://usaco.guide), [cses.fi/book](https://cses.fi/book/book.pdf)) | Thứ tự kiến thức chặt chẽ (Bronze → Platinum), lý thuyết vững | Rộng và sâu hơn mục tiêu (cây phân đoạn, luồng…); khung thời gian vài tháng đến vài năm |

**Kết luận từ các lộ trình:** các lộ trình phổ biến làm tốt việc **chọn bài và chia chủ đề** (tương ứng schema) nhưng gần như
**bỏ trống phần "cách học"**: thiếu truy xuất, giãn cách, xen kẽ, tiêu chí thành thạo, ca đối chứng. Lộ trình 7 ngày sẽ lấy cây
phụ thuộc chủ đề từ NeetCode/USACO làm khung, rồi thêm lớp phương pháp học từ mục 3.

---

## 6. Tổng hợp: hệ thống học DSA 7 ngày

### 6.1. Đơn vị kiến thức: Thẻ Schema

Mỗi dạng bài được nén thành **một thẻ** (thông tin hỗ trợ trong 4C/ID). Đây vừa là thứ để học, vừa là thứ để truy xuất hằng ngày:

```text
TÊN SCHEMA: Cửa sổ trượt (độ dài thay đổi)
DẤU HIỆU NHẬN DIỆN: đoạn con/chuỗi con liên tiếp; "dài nhất/ngắn nhất thỏa điều kiện";
                    điều kiện ĐƠN ĐIỆU khi mở rộng (thêm phần tử chỉ làm "tệ hơn" hoặc chỉ làm "tốt hơn")
Ý TƯỞNG + BẤT BIẾN: cửa sổ [left, right] luôn hợp lệ sau bước co; mỗi phần tử vào 1 lần, ra 1 lần
KHUNG (nhãn mục tiêu con): [1] Mở rộng → [2] Kiểm tra vi phạm → [3] Co lại → [4] Ghi nhận
ĐỘ PHỨC TẠP: O(n) thời gian, O(k) bộ nhớ cho trạng thái
BẪY: điều kiện không đơn điệu (có số âm) → KHÔNG dùng được, chuyển sang prefix sum + hash map
BÀI: Neo 3 · Đồng cấu 424 · Đối chứng 560 · Ghép Hard 76
```

### 6.2. Đơn vị bài tập: bộ ba (+1)

| Vai trò | Mục đích khoa học | Số lượng |
|---|---|---|
| **Neo** | Lời giải mẫu chuẩn, hình thành schema lần đầu (3.5, 3.6, 3.7) | 1 cho mỗi schema |
| **Đồng cấu** | Trừu tượng hóa qua so sánh (3.8); lượt truy xuất đầu tiên (3.1) | 1 (tối đa 2 nếu schema rộng như DP) |
| **Đối chứng** | Dạy ranh giới áp dụng; nguyên liệu cho xen kẽ (3.4, 3.8) | 1, có thể dùng chung cho 2 schema dễ nhầm |
| **Ghép (Hard mở đầu)** | Kết hợp 2 schema đã ở giai đoạn liên kết | Khoảng 8–12 cho cả lộ trình, đặt *sau* khi các schema thành phần qua cổng |

Phân loại bài ôn tập theo yêu cầu đề bài ánh xạ như sau: **củng cố = Đồng cấu**, **biến thể = Đối chứng / biến thể có điều kiện
khác**, **nâng cao = Ghép**.

### 6.3. Chu trình học một dạng bài mới (khoảng 75–100 phút)

| Bước | Thời gian | Hoạt động | Cơ sở |
|---|---|---|---|
| 1. Thử trước | 10–15' | Thử bài Neo: brute force, độ phức tạp, ghi lại vì sao chậm hoặc sai | 3.9 |
| 2. Học lời giải mẫu chủ động | 15–20' | Đọc notebook *từng đoạn*, che code và dự đoán trước, trả lời 5 câu hỏi tự giải thích, lần vết bằng tay | 3.5, 3.6, 3.10, 3.13 |
| 3. Truy xuất ngay | 10–15' | Đóng tài liệu, viết lại từ trang trắng kèm nhãn mục tiêu con, chạy test | 3.1, 3.7 |
| 4. Đồng cấu | 20–25' | Giải độc lập bài Đồng cấu (thang gợi ý nếu cần), rồi viết "điểm chung của 2 bài" | 3.8, 3.12 |
| 5. Đối chứng | 15–20' | Giải bài Đối chứng, viết "vì sao schema này *không* dùng được / phải sửa gì" | 3.4, 3.8 |
| 6. Đóng gói | 5' | Hoàn thiện Thẻ Schema + 2–3 thẻ ghi nhớ "dấu hiệu → kỹ thuật"; đưa vào lịch ôn | 3.2, 3.3 |

Từ ngày 4 trở đi (hiệu ứng đảo ngược chuyên môn): gộp bước 1–2 thành "tự giải bài Neo 20–25 phút, chỉ xem lời giải để *so sánh*
sau khi giải xong hoặc khi đã lên bậc gợi ý 3".

### 6.4. Nhịp một ngày học (khoảng 8 giờ tập trung, khoảng 4,5–5 giờ cường độ cao)

| Giờ | Khối | Nội dung | Cường độ |
|---|---|---|---|
| 06:30–07:00 | Vận động | 20–30 phút vận động vừa đến mạnh | — |
| 07:30–08:15 | **R: Khởi động truy xuất** | Trang trắng các schema cũ + thẻ ghi nhớ đến hạn + 1–2 bài Parsons | Thấp–vừa |
| 08:15–09:45 | **Khối 1** | Chu trình dạng mới A | **Cao** |
| 10:00–11:30 | **Khối 2** | Chu trình dạng mới B | **Cao** |
| 11:30–13:30 | Nghỉ trưa | Ăn, đi bộ, ngủ trưa (tùy chọn) | — |
| 13:30–15:00 | **Khối 3** | Dạng mới C *hoặc* bài Ghép từ các schema đã qua cổng | **Cao** |
| 15:15–16:15 | **Khối 4: Drill** | Luyện từng phần theo sổ lỗi: khung code tính giờ, bài tập biên, ước lượng độ phức tạp | Vừa |
| 16:15–17:00 | Ấp ủ | Đi bộ hoặc nghỉ nhẹ, không màn hình | — |
| 17:00–18:15 | **Khối 5: Bộ trộn** | 4–6 bài ẩn nhãn, xen kẽ mọi dạng đã học: 2–3 bài giải đầy đủ, còn lại plan-only | **Cao** |
| 20:00–21:00 | **Khối 6: Phản tư** | Sổ lỗi; giải lại bài trong hàng đợi học lại; giải thích lại 1 schema bằng lời; đọc đề Neo của ngày mai | Thấp–vừa |
| 22:30 | Ngủ | 7,5–9 giờ | — |

**Tỉ lệ thời gian thay đổi qua các ngày (giảm dần hỗ trợ):**

| Loại hoạt động | Ngày 1–2 | Ngày 3–5 | Ngày 6–7 |
|---|---|---|---|
| Học mới có hướng dẫn (thử trước + lời giải mẫu) | ~40% | ~25% | ~5–10% |
| Giải độc lập (Đồng cấu, Đối chứng, Ghép) | ~30% | ~35% | ~30% |
| Xen kẽ / thi thử | ~10% | ~20% | ~40% |
| Ôn giãn cách / truy xuất | ~12% | ~12% | ~15% |
| Phản tư / sổ lỗi | ~8% | ~8% | ~8% |

### 6.5. Lịch ôn giãn cách

| Học ở ngày | Ôn 1 (tối cùng ngày, Khối 6) | Ôn 2 (sáng hôm sau, Khối R) | Ôn 3 | Kiểm tra tổng | Duy trì |
|---|---|---|---|---|---|
| N1 | N1 | N2 | N4 | N7 | N14, N30 |
| N2 | N2 | N3 | N5 | N7 | N14, N30 |
| N3 | N3 | N4 | N6 | N7 | N14, N30 |
| N4 | N4 | N5 | N6 hoặc N7 | N7 | N14, N30 |
| N5 | N5 | N6 | N7 | N7 | N14, N30 |
| N6 | N6 | N7 | — | N7 | N14, N30 |

- **Hình thức ôn** (không bao giờ là đọc lại): trang trắng khung code → thẻ ghi nhớ → giải lại 1 bài từ đầu → plan-only 2–3 bài lạ cùng dạng.
- Ngoài lịch trên, mỗi schema còn xuất hiện ngẫu nhiên trong **bộ trộn buổi chiều**: đó là các lượt truy xuất xen kẽ "miễn phí".

### 6.6. Ngân sách thời gian và kiểm tra tính khả thi

- **Ngân sách:** khoảng 56 giờ tập trung (7 × 8).
- **Số lượt luyện cần thiết (suy luận từ dữ liệu, cần thận trọng):** theo Koedinger và cộng sự (2023), mỗi lượt luyện có phản
  hồi tăng khoảng 0,1 log-odds. Sau khi được dạy, đi từ khoảng 65% lên 80% đúng cần cỡ 7–8 lượt cho *mỗi đơn vị kiến thức chi
  tiết*. Một dạng DSA gồm nhiều đơn vị như vậy (nhận diện dấu hiệu, định nghĩa trạng thái, giữ bất biến, xử lý biên). *Đây là phép
  ngoại suy từ hệ thống gia sư sang DSA, chỉ dùng để định hướng.*
- **Hệ quả:** nếu mỗi lượt luyện là một bài giải đầy đủ 30–40 phút thì 25–30 schema × 7 lượt ≈ 90–140 giờ, **vượt ngân sách**.
  Giải pháp là **nhân số lượt luyện bằng các lượt truy xuất nhỏ nhắm đúng đơn vị kiến thức**: thẻ ghi nhớ (1'), trang trắng khung
  code (3–5'), plan-only (3–5'), Parsons (2–3'), drill biên (5'). Một bài Neo cộng các lượt nhỏ có thể cung cấp 6–10 lượt luyện
  cho cùng một schema trong khoảng 1,5–2 giờ.
- **Ước lượng phân bổ:** khoảng 26–30 schema × trung bình 1,5 giờ ≈ 40–44 giờ; bài Ghép (Hard mở đầu) ≈ 6–8 giờ; thi thử và kiểm
  tra tổng ≈ 5–6 giờ. Tổng ≈ 52–58 giờ, **vừa khít ngân sách**.
- **Ràng buộc chuyển cho Phần 2–3:** khoảng **25–30 schema**, khoảng **70–100 bài** tổng cộng (khoảng 30 Neo, Đồng cấu/Đối chứng
  dùng chung khi có thể, 8–12 bài Ghép). Một phần đáng kể bài trong bộ trộn làm ở mức plan-only. Schema nhỏ (hash map, prefix sum)
  khoảng 45–60 phút; schema lớn (DP, đồ thị) 3–4 giờ, chia cho nhiều ngày.

### 6.7. Tiêu chí thành thạo và cổng chuyển tiếp

**Cổng cùng ngày (qua thì được học dạng phụ thuộc):**
- Giải bài Đồng cấu độc lập, tối đa bậc gợi ý 1, trong khoảng ≤ 15 phút (Easy) hoặc ≤ 25–30 phút (Medium).
- Nói được dấu hiệu nhận diện, bất biến và độ phức tạp.

**Cổng có độ trễ (sáng hôm sau, quyết định "vững"):**
- Viết khung từ trang trắng ≤ 5 phút, chạy đúng.
- Nhận diện đúng ≥ 80% bài plan-only có dạng này trong bộ trộn.

**Không qua cổng:** đưa vào hàng đợi học lại, giải lại tối nay và sáng mai. Không mở dạng phụ thuộc cho đến khi qua.

Phần 5 (chiến lược kiểm tra) sẽ chi tiết hóa các cổng này thành bài kiểm tra cụ thể.

### 6.8. Sổ lỗi có phân loại

| Loại lỗi | Ví dụ | Cách chữa (luyện có chủ đích) |
|---|---|---|
| **(a) Không nhận ra dạng** | Không nghĩ tới ngăn xếp đơn điệu cho bài 739 | Thêm thẻ "dấu hiệu → kỹ thuật"; thêm cặp đối chứng vào bộ trộn |
| **(b) Nhận ra dạng nhưng sai trạng thái hoặc bất biến** | Định nghĩa `dp[i]` sai nghĩa | Tự giải thích + lần vết bằng tay trên input nhỏ |
| **(c) Lỗi biên / off-by-one** | `while l < r` hay `l <= r`, `mid` lệch | Drill khung code có tính giờ; thuộc một phiên bản khung duy nhất |
| **(d) Sai độ phức tạp (TLE)** | O(n²) với n = 10⁵ | Drill "ràng buộc → độ phức tạp mục tiêu" (n ≤ 20 → 2ⁿ; n ≤ 10³ → n²; n ≤ 10⁵–10⁶ → n log n hoặc n) |
| **(e) Lỗi cú pháp / API Python** | Quên `heapq` là min-heap | Bảng tra "thông tin đúng lúc" (4C/ID); không học thuộc trước |

### 6.9. Cách dùng kho notebook của repo cho đúng

Repo có các notebook tiếng Việt giảng giải từng bài: hiện có 2.446/3.711 bài DSA (Easy đầy đủ 833/833; Medium 1.164/1.958; Hard
449/920). Đây là kho **lời giải mẫu** rất giá trị, với điều kiện:

1. **Luôn thử trước** 10–15 phút, sau đó mới mở notebook.
2. **Đọc từng ô, dự đoán trước:** che ô code, tự đoán bước tiếp theo rồi mới xem.
3. **Trả lời 5 câu hỏi tự giải thích** (mục 3.6) ngay trên notebook (thêm ô markdown riêng).
4. **Đóng notebook rồi viết lại từ trang trắng.** Không chép.
5. **Không bao giờ "ôn" bằng cách đọc lại notebook.** Ôn bằng truy xuất.

*Ghi chú cho Phần 3:* một số bài Medium và Hard được chọn có thể chưa có notebook. Phần 3 sẽ đánh dấu những bài này.

---

## 7. Bảng ánh xạ: phương pháp → hành động → vị trí trong lộ trình

| Phương pháp | Hành động cụ thể | Ở đâu trong ngày / lộ trình |
|---|---|---|
| Luyện truy xuất | Trang trắng, giải lại từ editor trống, thẻ ghi nhớ, plan-only | Khối R, bước 3 của chu trình, Khối 5, Khối 6 |
| Giãn cách | Lịch N → tối N → N+1 → N+3 → N7 → N14 → N30 | Khối R và Khối 6 hằng ngày; duy trì sau 7 ngày |
| Học lại đến tiêu chí | Trạng thái bài Chưa đạt → Vững; hàng đợi học lại | Khối 6 và cổng sáng hôm sau |
| Xen kẽ | Bộ trộn ẩn nhãn; cặp dễ nhầm | Khối 5 hằng ngày; ngày 6–7 chủ đạo |
| Lời giải mẫu + giảm dần hỗ trợ | Notebook repo → bài Đồng cấu độc lập; đảo thứ tự từ ngày 4 | Bước 2 của chu trình; tỉ lệ ở mục 6.4 |
| Tự giải thích | 5 câu hỏi cố định; giải thích lại bằng lời | Bước 2 và Khối 6 |
| Nhãn mục tiêu con | Khung code chia bước có tên | Thẻ Schema; bước 3 của chu trình |
| So sánh loại suy / đối chứng | Bộ ba Neo – Đồng cấu – Đối chứng; viết "điểm chung / khác biệt" | Bước 4–5 của chu trình; tiêu chí chọn bài ở Phần 3 |
| Thử trước | Brute force 10–15'; đọc đề Neo tối hôm trước | Bước 1 của chu trình; cuối Khối 6 |
| Lần vết → giải thích → viết | Vẽ trạng thái trên input nhỏ trước khi code; bài Parsons | Bước 2; Khối R |
| Luyện có chủ đích | Sổ lỗi 5 loại → drill | Khối 4 |
| Học đến thành thạo + gợi ý theo bước | Cổng chuyển tiếp; thang gợi ý 0–4 | Mọi bài; thứ tự phụ thuộc ở Phần 2 |
| Mã hóa kép | Một hình chuẩn cho mỗi schema | Thẻ Schema |
| Ngủ, vận động, nghỉ, ấp ủ | 7,5–9 giờ ngủ; vận động sáng; nghỉ sau khối; quy tắc kẹt 25–30' | Khung ngày (mục 6.4) |

---

## 8. Hệ quả cho các bước tiếp theo

- **Phần 2 – Bản đồ kiến thức:** sắp xếp khoảng 25–30 schema theo đồ thị phụ thuộc. Gom các "cặp dễ nhầm" để lên kế hoạch xen kẽ.
- **Phần 3 – Danh sách bài trọng điểm:** chọn theo **bộ ba Neo / Đồng cấu / Đối chứng + bài Ghép**. Tiêu chí phụ: tính kinh điển, ghép được
  nhiều kỹ thuật, có notebook trong repo, độ khó vừa sức theo ngày. Phân tích 3.711 bài để kiểm tra độ bao phủ.
- **Phần 4 – Lộ trình chi tiết 7 ngày:** đặt schema vào các khối theo mục 6.4. Tuân thủ lịch giãn cách 6.5 và ngân sách 6.6.
- **Phần 5 – Ôn tập và kiểm tra:** cụ thể hóa các cổng (6.7), bài kiểm tra có độ trễ, đề thi thử xen kẽ ngày 7, lịch duy trì ngày 14 và 30.

---

## Tài liệu tham khảo

**Tổng quan và phương pháp hạng A**
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. — [Tóm tắt APS](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science, 17*(3), 249–255.
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*, 772–775. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/21252317/)
- Karpicke, J. D., Butler, A. C., & Roediger, H. L. (2009). Metacognitive strategies in student learning. *Memory, 17*(4), 471–479.
- Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review. *Psychological Bulletin, 140*(6), 1432–1463.
- Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. *Review of Educational Research, 87*(3), 659–701. — [PDF](https://education.wsu.edu/documents/2018/01/rethinking-use-tests.pdf/)
- Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. *Psychological Bulletin, 144*(7), 710–756. — [PDF](https://sc-pan.github.io/pdf/PR_2018.pdf)
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin, 132*(3), 354–380.
- Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/19076480/)
- Latimier, A., Peyre, H., & Ramus, F. (2021). A meta-analytic review of the benefit of spacing out retrieval practice episodes on retention. *Educational Psychology Review, 33*, 959–987. — [Springer](https://link.springer.com/10.1007/s10648-020-09572-8)
- Rawson, K. A., Dunlosky, J., & Sciartelli, S. M. (2013). The power of successive relearning. *Educational Psychology Review, 25*(4), 523–548. — [Hướng dẫn thực hành của Dunlosky và cộng sự](https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-successive-relearning-dunlosky-greve-badali-wissman-rawson.pdf)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*, 481–498.
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/18578849/)
- Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/31556629/)
- Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. *Journal of Educational Psychology, 112*(1), 40–52. — [Đánh giá WWC](https://ies.ed.gov/ncee/wwc/Study/88770)

**Tải nhận thức, lời giải mẫu, schema, chuyển giao**
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285.
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work. *Educational Psychologist, 41*(2), 75–86.
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. — [UOW](https://ro.uow.edu.au/edupapers/136)
- Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R. (2002). From example study to problem solving: Smooth transitions help learning. *Journal of Experimental Education, 70*(4), 293–315.
- Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences, 24*(1), 87–114.
- Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology, 4*(1), 55–81.
- Gobet, F., et al. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236–243.
- Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science, 5*, 121–152. — [ASU](https://education.asu.edu/lcl/publications/chi-m-t-h-feltovich-p-glaser-r-1981-categorization-and-representation-physics)
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations. *Cognitive Science, 13*, 145–182.
- Chi, M. T. H., de Leeuw, N., Chiu, M.-H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science, 18*, 439–477.
- Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*, 703–725. — [Tóm tắt BPS](https://www.bps.org.uk/research-digest/self-explanation-powerful-learning-technique-according-meta-analysis-64-studies)
- Fiorella, L., & Mayer, R. E. (2013). The relative benefits of learning by teaching and teaching expectancy. *Contemporary Educational Psychology, 38*(4), 281–288.
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. — [Deep Blue](https://deepblue.lib.umich.edu/items/196ea13e-fb69-4a74-a6f9-864c81aed465)
- Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. *Educational Psychologist, 48*(2), 87–113. — [PDF](https://www.lrdc.pitt.edu/Schunn/papers/ContrastingCasesMeta-AlfieriEtAl2013.pdf)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522.
- Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect. *Journal of Experimental Psychology: Applied, 15*(3), 243–257. — [PDF](https://learninglab.uchicago.edu/Pre-Testing_files/RichlandKornellKao.pdf)
- Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *JEP: Learning, Memory, and Cognition, 35*(4), 989–998.
- Kapur, M. (2008). Productive failure. *Cognition and Instruction, 26*(3), 379–424.
- Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction works: Evidence for productive failure. *Review of Educational Research, 91*(5). — [Tin tóm tắt](https://phys.org/news/2021-09-productively-wiser.html)
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In *Metacognition: Knowing about knowing*. MIT Press.
- Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: An integrative review. *Perspectives on Psychological Science, 10*(2), 176–199.

**Hình thành kỹ năng, luyện tập, thành thạo**
- Fitts, P. M., & Posner, M. I. (1967). *Human Performance*. Brooks/Cole.
- Anderson, J. R. (1982). Acquisition of cognitive skill. *Psychological Review, 89*, 369–406.
- Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review, 100*(3), 363–406.
- Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). Deliberate practice and performance in music, games, sports, education, and professions: A meta-analysis. *Psychological Science, 25*(8), 1608–1618. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/24986855/)
- Bloom, B. S. (1984). The 2 sigma problem. *Educational Researcher, 13*(6), 4–16.
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. — [ERIC](https://eric.ed.gov/?id=EJ946764)
- Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023). An astonishing regularity in student learning rate. *PNAS, 120*(13). — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10068755) · [Tin CMU](https://www.cmu.edu/news/stories/archives/2023/march/the-myth-of-the-fast-learner)
- van Merriënboer, J. J. G., Clark, R. E., & de Croock, M. B. M. (2002). Blueprints for complex learning: The 4C/ID-model. *ETR&D, 50*(2), 39–64. — [MIT Open Learning](https://openlearning.mit.edu/mit-faculty/research-based-learning-findings/four-component-instructional-design-4cid)
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship. In *Knowing, learning, and instruction*. Erlbaum.

**Giáo dục lập trình**
- Soloway, E., & Ehrlich, K. (1984). Empirical studies of programming knowledge. *IEEE Transactions on Software Engineering, SE-10*(5), 595–609.
- Lopez, M., Whalley, J., Robbins, P., & Lister, R. (2008). Relationships between reading, tracing and writing skills in introductory programming. *ICER '08*. — [UTS](https://opus.lib.uts.edu.au/handle/10453/10806)
- Catrambone, R. (1998). The subgoal learning model. *Journal of Experimental Psychology: General, 127*(4), 355–376.
- Margulieux, L. E., Catrambone, R., & Guzdial, M. (2016). Employing subgoals in computer programming education. *Computer Science Education, 26*(1), 44–67. — [GSU](https://scholarworks.gsu.edu/ltd_facpub/3)
- Ericson, B. J., Margulieux, L. E., & Rick, J. (2017). Solving Parsons problems versus fixing and writing code. *Koli Calling '17*, 20–29.

**Khoa học thần kinh: giấc ngủ, củng cố, sinh lý**
- Bruer, J. T. (1997). Education and the brain: A bridge too far. *Educational Researcher, 26*(8), 4–16.
- Antony, J. W., Ferreira, C. S., Norman, K. A., & Wimber, M. (2017). Retrieval as a fast route to memory consolidation. *Trends in Cognitive Sciences, 21*(8), 573–576. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/28583416/)
- Diekelmann, S., & Born, J. (2010). The memory function of sleep. *Nature Reviews Neuroscience, 11*, 114–126.
- Walker, M. P., Brakefield, T., Morgan, A., Hobson, J. A., & Stickgold, R. (2002). Practice with sleep makes perfect. *Neuron, 35*, 205–211. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/12123620/)
- Wagner, U., Gais, S., Haider, H., Verleger, R., & Born, J. (2004). Sleep inspires insight. *Nature, 427*, 352–355. — [Nature](https://www.nature.com/articles/nature02223) · [Tổng quan của Verleger và cộng sự](https://pmc.ncbi.nlm.nih.gov/articles/PMC3902672)
- Yoo, S.-S., Hu, P. T., Gujar, N., Jolesz, F. A., & Walker, M. P. (2007). A deficit in the ability to form new human memories without sleep. *Nature Neuroscience, 10*, 385–392. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/17293859/)
- Gais, S., Lucas, B., & Born, J. (2006). Sleep after learning aids memory recall. *Learning & Memory, 13*, 259–262.
- Mednick, S., Nakayama, K., & Stickgold, R. (2003). Sleep-dependent learning: A nap is as good as a night. *Nature Neuroscience, 6*, 697–698.
- Drake, C., Roehrs, T., Shambroom, J., & Roth, T. (2013). Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed. *Journal of Clinical Sleep Medicine, 9*(11), 1195–1200.
- Kelley, P., & Whatson, T. (2013). Making long-term memories in minutes: A spaced learning pattern from memory research in education. *Frontiers in Human Neuroscience, 7*, 589. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3782739)
- Gruber, M. J., Gelman, B. D., & Ranganath, C. (2014). States of curiosity modulate hippocampus-dependent learning via the dopaminergic circuit. *Neuron, 84*(2), 486–496.
- Sio, U. N., & Ormerod, T. C. (2009). Does incubation enhance problem solving? A meta-analytic review. *Psychological Bulletin, 135*(1), 94–120. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/19210055/)
- Biwer, F., et al. (2023). Understanding effort regulation: Comparing "Pomodoro" breaks and self-regulated breaks. *British Journal of Educational Psychology*. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/36859717/); Smits, Wenzel & de Bruin (2025) — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12292963/)
- Roig, M., Nordbrandt, S., Geertsen, S. S., & Nielsen, J. B. (2013). The effects of cardiovascular exercise on human memory: A review with meta-analysis. *Neuroscience & Biobehavioral Reviews, 37*(8), 1645–1666.
- Winter, B., et al. (2007). High impact running improves learning. *Neurobiology of Learning and Memory, 87*(4), 597–609. — [Münster](https://cris.uni-muenster.de/portal/en/publication/21610319)

**Ngộ nhận và khung thực hành**
- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest, 9*(3), 105–119. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/26162104/)
- Lalley, J. P., & Miller, R. H. (2007). The learning pyramid: Does it point teachers in the right direction? *Education, 128*(1), 64–79.
- Young, S. H. (2019). *Ultralearning*. Harper Business. · Kaufman, J. (2013). *The First 20 Hours*. Portfolio. · Ferriss, T. (2012). *The 4-Hour Chef*. · Oakley, B. (2014). *A Mind for Numbers*. TarcherPerigee.
- Pólya, G. (1945). *How to Solve It*. Princeton University Press. · Schoenfeld, A. H. (1985). *Mathematical Problem Solving*. Academic Press.
- Lộ trình DSA: [NeetCode Roadmap](https://neetcode.io/roadmap) · [Grind 75](https://www.techinterviewhandbook.org/grind75) · [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/) · [USACO Guide](https://usaco.guide) · [Competitive Programmer's Handbook](https://cses.fi/book/book.pdf)

> **Ghi chú độ tin cậy:** các hiệu ứng và số liệu ở trên được đối chiếu với tóm tắt, PubMed hoặc bản tác giả công bố khi có thể.
> Một số con số (ví dụ hiệu ứng tổng của Adesope 2017) chỉ được trích ở mức định tính vì các nguồn thứ cấp không thống nhất. Phép
> tính số lượt luyện ở mục 6.6 là **suy luận định hướng**, không phải kết quả nghiên cứu trực tiếp về DSA.
