# 01 — Individual Problem Scan

> Điền theo Phase 1 + Phase 2 trong `01-worksheet.md`. Tự scan trước, dùng AI sau để phản biện. Không copy ví dụ Weekly Report.

## Thông tin cá nhân

- Họ và tên: Nguyen Thuy Linh
- Mã học viên:2A20262497
- Vai trò / bối cảnh (VD: sinh viên năm X, intern PM, ...): nhân viên văn phòng
- Công việc hằng tuần (3-5 gạch đầu dòng để soi problem):
- Thứ 2-7 dậy sớm đi làm
- Đi siêu thị và mua đồ dùng
- Nghỉ ngơi, chơi game sau giờ làm
- Nấu ăn
- Đi cafe với bạn bè
---
## Phase 1 — Scan 5+ problems (tối thiểu 5, khuyến khích 8-10)

**Cách điền:** mỗi dòng = việc gì + ai chịu + đo bằng gì. Cột `Dấu hiệu thật` bắt buộc có số: mất bao lâu (bấm giờ mấy lần), mấy lần/tuần, bao nhiêu người gặp, log/ticket/quote nào.
| # | Lăng kính (Lặp lại / Tốn thời gian / AI có thể tốt hơn / Pain từ người khác) | Problem quan sát được | Ai chịu ảnh hưởng? | Dấu hiệu thật (số + bằng chứng) |
|---|---|---|---|---|
| 1 | Lặp lại | Nhân viên phải trả lời nhiều câu hỏi giống nhau từ khách hàng về giá, sản phẩm và chính sách | Nhân viên CSKH, khách hàng | Các câu hỏi tương tự xuất hiện nhiều lần trong ngày, mỗi lần mất khoảng 3-5 phút để trả lời |
| 2 | Tốn thời gian | Phải đọc từng tin nhắn của khách hàng rồi trả lời thủ công | Nhân viên CSKH | Khi có nhiều tin nhắn cùng lúc, có thể mất 30-60 phút để xử lý hết |
| 3 | AI có thể tốt hơn | Khi khách hỏi bằng nhiều cách khác nhau, nhân viên phải tự hiểu ý và tìm thông tin phù hợp | Nhân viên CSKH | Mỗi câu hỏi khó có thể mất 5-10 phút để tra cứu trước khi trả lời |
| 4 | Pain từ người khác | Khách hàng phải chờ phản hồi khi nhân viên đang bận hoặc ngoài giờ làm việc | Khách hàng | Có trường hợp khách phải chờ vài chục phút hoặc đến hôm sau mới được trả lời |
| 5 | Lặp lại + Tốn thời gian | Nhân viên phải tìm lại thông tin sản phẩm, giá và chính sách nhiều lần trong tài liệu | Nhân viên CSKH | Cùng một loại thông tin phải tra cứu nhiều lần mỗi ngày |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

> Gợi ý tự soi: tuần trước mất nhiều thời gian nhất vào việc gì? Việc gì hay trì hoãn? Người khác hay hỏi lại câu gì? Workflow nào ai cũng biết là chậm?

**AI đã dùng ở Phase 1 (nếu có):**
- Prompt đã hỏi: Nhờ AI gợi ý các vấn đề theo 4 lăng kính: lặp lại, tốn thời gian, AI có thể tốt hơn và pain từ người khác.
- Ý dùng được: Gợi ý cách mô tả các vấn đề liên quan đến chăm sóc khách hàng và chatbot AI.
- Ý bỏ vì không phải pain thật: Các ví dụ/số liệu không đúng với trải nghiệm thực tế của bản thân.

**Self-check Phase 1:**
- [x] Đủ 5+ dòng, mỗi dòng có actor + số đo cụ thể
- [x] Dùng ít nhất 3/4 lăng kính
- [ ] Không có dòng chung chung kiểu "mất nhiều thời gian"

---

## Phase 2 — Top 3 Problem Cards

### 2.1. Chọn top 3

Giữ bài nào: actor cụ thể, workflow vẽ được 3-7 bước, bottleneck ở 1 bước, impact đo được. Loại bài quá rộng.

| Rank | Problem (copy từ bảng scan) | Vì sao chọn (2-3 ý) | Điều còn chưa chắc |
|---|---|---|---|
| 1 | Nhân viên phải trả lời nhiều câu hỏi giống nhau của khách hàng về giá, sản phẩm và chính sách | Vấn đề xảy ra lặp lại nhiều lần và có actor rõ ràng là nhân viên CSKH. Có thể đo thời gian trả lời và số câu hỏi lặp lại. | Chưa chắc số lượng câu hỏi lặp lại thực tế mỗi ngày |
| 2 | Phải đọc từng tin nhắn của khách hàng rồi trả lời thủ công | Workflow hiện tại có thể mô tả rõ từ nhận tin nhắn đến tìm thông tin và trả lời. Có thể đo thời gian xử lý một yêu cầu. | Chưa chắc thời gian xử lý trung bình thực tế |
| 3 | Khách hàng phải chờ phản hồi khi nhân viên bận hoặc ngoài giờ làm việc | Actor và pain rõ ràng, ảnh hưởng trực tiếp tới trải nghiệm khách hàng. Có thể đo bằng thời gian khách phải chờ phản hồi. | Chưa có dữ liệu chính xác về thời gian chờ trung bình |

### 2.2. Problem Cards chi tiết (lặp lại cho cả 3 cards)

---

#### Problem Card #1 – Trả lời câu hỏi lặp lại của khách hàng

Problem 1 câu:
Nhân viên CSKH phải trả lời thủ công nhiều câu hỏi lặp lại của khách hàng về giá, sản phẩm và chính sách.

Actor:
Nhân viên CSKH.

Thời điểm / bối cảnh:
Khi khách hàng nhắn tin hỏi về giá, thông tin sản phẩm hoặc chính sách.

Current workflow 3-7 bước:
1. Khách hàng gửi câu hỏi.
2. Nhân viên đọc và xác định nội dung khách đang hỏi.
3. Nhân viên tìm thông tin liên quan.
4. Nhân viên soạn câu trả lời.
5. Nhân viên gửi câu trả lời cho khách hàng.

Bottleneck:
Bước 3 và 4: Nhân viên phải tìm thông tin và soạn lại câu trả lời dù nhiều câu hỏi có nội dung giống nhau.

Impact:
Mỗi câu hỏi lặp lại mất khoảng 3-5 phút để xử lý; khi có nhiều khách cùng hỏi, thời gian xử lý tăng và khách phải chờ lâu hơn.

Success metric:
Giảm thời gian xử lý một câu hỏi lặp lại từ khoảng 3-5 phút xuống dưới 1 phút.

Non-AI alternative:
Tạo FAQ và bộ câu trả lời mẫu để nhân viên tìm và gửi nhanh cho khách.

AI hypothesis:
AI có thể hiểu câu hỏi của khách dù được diễn đạt theo nhiều cách, tìm thông tin phù hợp và đề xuất câu trả lời tự động.
Quick gut:
[ ] No AI / process fix
[ ] Rule
[x] Workflow
[ ] Agent
[ ] Chưa biết

**Draft workflow Card #1** (ASCII / Mermaid / ảnh đính kèm):

```text
CURRENT STATE — 3-5 phút

[1 Nhận câu hỏi] → [2 Hiểu câu hỏi] → [3 Tìm thông tin] → [4 Soạn và gửi câu trả lời] <-- bottleneck

FUTURE STATE — dưới 1 phút

[1 Nhận câu hỏi] → [2 AI tìm thông tin và tạo câu trả lời] → [3 Nhân viên review/gửi] <-- human boundary

Fallback: nếu AI không chắc chắn hoặc trả lời sai thì chuyển cho nhân viên CSKH kiểm tra và trả lời.
```

File đính kèm (nếu vẽ riêng): `01-individual-problem-scan-workflow-card-1.png`

---

#### Problem Card #2 – Xử lý tin nhắn khách hàng thủ công

```text
Problem 1 câu:
Nhân viên CSKH phải đọc, phân loại và xử lý từng tin nhắn khách hàng thủ công nên mất nhiều thời gian khi lượng tin nhắn tăng.

Actor:
Nhân viên CSKH.

Thời điểm / bối cảnh:
Khi có nhiều khách hàng nhắn tin hỏi thông tin hoặc yêu cầu hỗ trợ cùng lúc.

Current workflow 3-7 bước:
1. Khách hàng gửi tin nhắn.
2. Nhân viên đọc nội dung.
3. Nhân viên xác định khách đang cần hỗ trợ vấn đề gì.
4. Nhân viên tìm thông tin cần thiết.
5. Nhân viên soạn và gửi câu trả lời.

Bottleneck:
Bước 2-4: Nhân viên phải đọc, hiểu và tìm thông tin cho từng tin nhắn một cách thủ công.

Impact:
Khi có nhiều tin nhắn cùng lúc, nhân viên mất nhiều thời gian xử lý và khách hàng phải chờ phản hồi.

Success metric:
Giảm thời gian xử lý tin nhắn và giảm số tin nhắn đơn giản cần nhân viên xử lý thủ công.

Non-AI alternative:
Phân loại sẵn các nhóm câu hỏi và tạo FAQ/câu trả lời mẫu cho từng nhóm.

AI hypothesis:
AI có thể đọc nội dung tin nhắn, xác định nhu cầu của khách và tìm thông tin phù hợp để hỗ trợ nhân viên tạo câu trả lời.

Quick gut:
[ ] No AI / process fix
[ ] Rule
[x] Workflow
[ ] Agent
[ ] Chưa biết
```

**Draft workflow Card #2:**

```text
CURRENT STATE — chưa có số đo chính xác

[1 Nhận tin nhắn] → [2 Đọc và phân loại] → [3 Tìm thông tin] → [4 Soạn và trả lời] <-- bottleneck

FUTURE STATE — mục tiêu giảm thời gian xử lý

[1 Nhận tin nhắn] → [2 AI phân loại + tìm thông tin] → [3 Nhân viên review/gửi] <-- human boundary

Fallback: nếu AI không xác định được nhu cầu hoặc không tìm được thông tin phù hợp thì chuyển cho nhân viên xử lý.
```

File đính kèm: `01-individual-problem-scan-workflow-card-2.png`

---

#### Problem Card #3 – Khách hàng phải chờ phản hồi

```text
Problem 1 câu:
Khách hàng phải chờ phản hồi khi nhân viên CSKH đang bận hoặc ngoài giờ làm việc.

Actor:
Khách hàng.

Thời điểm / bối cảnh:
Khi khách hàng gửi câu hỏi nhưng nhân viên CSKH chưa thể tiếp nhận và xử lý ngay.

Current workflow 3-7 bước:
1. Khách hàng gửi câu hỏi.
2. Tin nhắn chờ nhân viên tiếp nhận.
3. Nhân viên đọc và xác định yêu cầu.
4. Nhân viên tìm thông tin cần thiết.
5. Nhân viên trả lời khách hàng.

Bottleneck:
Bước 2: Khách hàng phải chờ đến khi nhân viên có thể tiếp nhận và xử lý tin nhắn.

Impact:
Khách hàng phải chờ phản hồi, đặc biệt khi nhân viên bận hoặc ngoài giờ làm việc, làm giảm trải nghiệm khách hàng.

Success metric:
Giảm thời gian chờ phản hồi đối với các câu hỏi phổ biến của khách hàng.

Non-AI alternative:
Tạo FAQ, tin nhắn trả lời tự động và hướng dẫn để khách hàng có thể tự tìm thông tin.

AI hypothesis:
AI có thể trả lời ngay các câu hỏi phổ biến dựa trên dữ liệu của doanh nghiệp và chuyển những trường hợp khó cho nhân viên.

Quick gut:
[ ] No AI / process fix
[ ] Rule
[x] Workflow
[ ] Agent
[ ] Chưa biết
```

**Draft workflow Card #3:**

```text
CURRENT STATE — chưa có số đo chính xác

[1 Khách gửi câu hỏi] → [2 Chờ nhân viên] → [3 Nhân viên tìm thông tin] → [4 Trả lời khách] <-- bottleneck

FUTURE STATE — mục tiêu giảm thời gian chờ

[1 Khách gửi câu hỏi] → [2 AI xử lý câu hỏi phổ biến] → [3 Nhân viên review/xử lý câu khó] <-- human boundary

Fallback: nếu AI không chắc chắn, không tìm được thông tin hoặc khách yêu cầu gặp người thật thì chuyển cho nhân viên CSKH.
```

File đính kèm: `01-individual-problem-scan-workflow-card-3.png`

---

### 2.3. Card muốn pitch nhất (chuẩn bị 2 phút)

**Card tôi muốn pitch nhất:**

Card #1 – Trả lời câu hỏi lặp lại của khách hàng.

```

**Vì sao (2-3 câu: workflow gì, số đo gì, impact gì):**

Workflow hiện tại gồm nhận câu hỏi → hiểu nội dung → tìm thông tin → soạn và gửi câu trả lời, trong đó bottleneck nằm ở bước tìm thông tin và soạn câu trả lời lặp lại. Có thể đo bằng thời gian xử lý trung bình cho một câu hỏi và số lượng câu hỏi lặp lại. Nếu cải thiện được, nhân viên CSKH sẽ giảm thời gian xử lý và khách hàng nhận phản hồi nhanh hơn.

```

**Câu hỏi tôi muốn nhóm challenge (1-2 câu hỏi đúng chỗ yếu):**

1. Vấn đề này có thực sự cần AI hay chỉ cần FAQ và câu trả lời mẫu là đủ?
2. Làm thế nào để kiểm chứng AI giúp giảm thời gian xử lý mà vẫn đảm bảo câu trả lời chính xác?

```

**AI phản biện Card (nếu có):**
- Điểm yếu AI chỉ ra: Chưa có dữ liệu thực tế về số lượng câu hỏi lặp lại và thời gian xử lý trung bình; một số câu hỏi đơn giản có thể chỉ cần FAQ hoặc rule thay vì AI.
- Tôi sửa gì: Không khẳng định các số liệu chưa được kiểm chứng, bổ sung Non-AI alternative và giữ nhân viên review trong workflow để giảm rủi ro AI trả lời sai.

### Self-check nộp phần 01
- [x] Có 5+ problems + top 3 Cards đủ field
- [x] Mỗi Card có workflow trước/sau + bottleneck + metric + fallback
- [x] Đã chọn 1 card pitch + câu hỏi challenge
