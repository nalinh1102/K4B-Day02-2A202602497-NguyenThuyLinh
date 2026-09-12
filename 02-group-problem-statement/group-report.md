# 02 — Group Problem Statement (Bản nộp nhóm)

> Làm chung 1 bản, mỗi thành viên copy vào repo cá nhân. Đi theo Phase 3 → 6 trong `01-worksheet.md`. Nhóm chỉ chọn **candidate problem** ở Phase 3, viết Problem Statement sau khi validate + vẽ workflow.

## Thành viên nhóm

| STT | Họ và tên | Mã học viên | Vai trò trong nhóm (VD: facilitator, workflow, research, writer) |
|-----|-----------|-------------|---------------------------------------------------------------|
| 1   | Nguyễn Đức Đồng | 2A202602367 | Lên ý tưởng; làm báo cáo (report) |
| 2   | Mai Huy Hoàng | 2A202602685 | Lên ý tưởng; xây dựng bản trình bày chi tiết bối cảnh (context) |
| 3   | Trần Nguyễn Trí Dũng | 2A202602784 | Lên ý tưởng; thiết kế quy trình (workflow: before – after) |
| 4   | Nguyễn Thùy Linh | 2A202602497 | Lên ý tưởng; làm bản mẫu sản phẩm (prototype) |
| 5   | Nguyễn Thị Hải Mi | 2A202602667 | Lên ý tưởng; phân chia công việc; làm báo cáo (report) |

**Candidate problem nhóm chọn (1 câu):**
Gom và tổng hợp context (ticket, code liên quan, lịch sử thay đổi) khi review PR để nhận ra rủi ro kỹ thuật.


---

## Phase 3 — Group Convergence: từ 9-12 candidates về 1

### 3.1. Trình bày top 3 mỗi người (mỗi candidate 1-2 phút)

| # | Người đưa ra | Candidate problem | Người gặp vấn đề | Điểm nghẽn | Cảm nhận nhanh của nhóm |
|---|---|---|---|---|---|
| 1 | Nguyễn Đức Đồng | Debug runtime error & đọc tài liệu framework khi làm bài tập lập trình | Sinh viên CNTT | Đảo 15-20 tab StackOverflow không khớp phiên bản | Pain rất thật, xảy ra hằng ngày, thời gian lãng phí cực lớn |
| 2 | Nguyễn Đức Đồng | Tra từ vựng chuyên ngành ngữ cảnh kép khi đọc tài liệu tiếng Anh | Sinh viên kỹ thuật | Chuyển tab 30+ lần/buổi tra từ điển thô | Tốt nhưng đã có một số tiện ích tra từ điển hỗ trợ |
| 3 | Nguyễn Đức Đồng | Lên kế hoạch task tuần thiếu Definition of Done (DoD) gây nghẽn bài tập nhóm | Nhóm đồ án | Task mô tả chung chung, trễ hạn ghép code | Đau chung cho cả nhóm, ảnh hưởng trực tiếp tiến độ môn học |
| 4 | Mai Huy Hoàng | Gom và hiểu context (ticket, code, lịch sử) khi review PR | Reviewer / Engineer | Đọc ticket, code liên quan và lịch sử ở nhiều nơi thủ công | Tốn nhiều thời gian nhất tuần theo ghi nhận cá nhân, bottleneck khâu gom context rất rõ |
| 5 | Mai Huy Hoàng | Đánh giá khả năng ảnh hưởng của cảnh báo dependency vulnerability | Dev / Security Team | Đọc từng advisory, kiểm tra dependency có dùng và đánh giá rủi ro thủ công | Cảnh báo lặp lại hằng ngày, khoanh vùng ở bước đánh giá tác động tốt |
| 6 | Mai Huy Hoàng | Thu thập context và phân loại (triage) bug production | Team Dev / Triage Team | Đọc log, tái hiện lỗi, xác định severity và tìm owner thủ công | Đầu việc hằng tuần, ảnh hưởng nhiều vai trò, bug thiếu context làm triage kéo dài |
| 7 | Trần Nguyễn Trí Dũng | Tìm kiếm và lọc tài liệu tham khảo phù hợp yêu cầu bài tập | Sinh viên / Developer | Mở từng nguồn đọc và lọc thủ công vì không có giới hạn tìm kiếm | Tốn nhiều thời gian mở từng nguồn xác định độ phù hợp |
| 8 | Trần Nguyễn Trí Dũng | Tìm lại thông tin task và deadline cũ bị trôi trên Discord | Thành viên nhóm đồ án | Phải lội lại các tin nhắn cũ trên Discord để xác định task, deadline | Phổ biến, gây gián đoạn công việc và dễ hiểu sai yêu cầu |
| 9 | Trần Nguyễn Trí Dũng | Đánh giá và sắp xếp tài liệu học tập theo mức độ liên quan | Sinh viên cá nhân | Đọc và đánh giá từng tài liệu để xác định chủ đề, độ khó và thứ tự học | Có vấn đề nhưng mức độ ảnh hưởng chưa lớn bằng 2 bài toán trên |
| 10 | Nguyễn Thùy Linh | Trả lời các câu hỏi lặp lại của khách hàng về giá, sản phẩm và chính sách | Nhân viên CSKH | Trả lời lặp đi lặp lại cùng các câu hỏi giống nhau thủ công | Vấn đề xảy ra lặp lại nhiều lần, actor CSKH rõ ràng, đo được số câu hỏi |
| 11 | Nguyễn Thùy Linh | Đọc từng tin nhắn khách hàng và tìm thông tin trả lời thủ công | Nhân viên CSKH / Sales | Nhận tin nhắn, tra cứu thông tin và phản hồi từng yêu cầu thủ công | Workflow rõ ràng từ nhận tin nhắn đến xử lý yêu cầu |
| 12 | Nguyễn Thùy Linh | Khách hàng phải chờ phản hồi lâu khi nhân viên bận hoặc ngoài giờ | Khách hàng / CSKH | Phản hồi chậm khi nhân viên ngoài giờ hoặc bận việc khác | Actor và pain rõ ràng, ảnh hưởng trực tiếp tới trải nghiệm khách hàng |
| 13 | Nguyễn Thị Hải Mi | Lọc báo GP/PR hằng tháng theo số (traffic, vendor, giá) và chủ đề | Nhân viên Marketing / SEO | Lọc báo thủ công theo tiêu chí số và gán chủ đề trên 5 dự án | Lặp lại hằng tháng, workflow 5 bước rõ ràng, so sánh R/W/A rất rõ |
| 14 | Nguyễn Thị Hải Mi | Kiểm tra chất lượng nội dung (QC content) theo guideline riêng của client | Nhân viên QC / Content | Đọc và kiểm tra giọng văn/brand voice theo guideline riêng của client | Mất ~10 giờ/tháng, cần hiểu ngữ cảnh sâu của từng client |
| 15 | Nguyễn Thị Hải Mi | Chèn và quản lý Internal link bài viết cho dự án content | Nhân viên SEO / Editor | Đánh giá và chèn thủ công link bài viết liên quan theo keyword | Tốn ≥10 giờ/tháng cho 2 dự án book content

### 3.2. Gom trùng / cluster (gom 9-12 ý thành 3-4 cụm)

| Cluster | Candidates included | Pattern chung | Ghi chú |
|---|---|---|---|
| A | Candidate 1, 7, 8, 9 | Hỗ trợ Lập trình, Debug & Tối ưu Mã nguồn | Nhóm các bài toán lập trình trực tiếp, thời gian lãng phí cao, dễ đo lường bằng phút |
| B | Candidate 2, 4, 11 | Tra cứu, Tổng hợp Tài liệu & Dataset Học thuật | Nhóm xử lý thông tin đầu vào, đọc hiểu tài liệu tiếng Anh & paper |
| C | Candidate 3, 5, 12 | Quản lý Tiến độ, Task & Giao tiếp Đồ án Nhóm | Nhóm quản trị dự án, phân chia công việc và theo dõi deadline |
| D (nếu có) | Candidate 6, 10 | Tạo Tài nguyên Visual (Slide, Mockup Wireframe) | Nhóm công cụ hỗ trợ trình bày và thiết kế giao diện ban đầu |

### 3.3. Shortlist (giữ 2-3 bài trả lời được 7 câu hỏi worksheet)

| Candidate | Vì sao vào shortlist (2-3 ý) | Rủi ro / điều chưa rõ |
|---|---|---|
| 1. Gom và hiểu context (ticket, code, lịch sử) khi review PR | Là việc tốn nhiều thời gian nhất tuần theo ghi nhận cá nhân; bottleneck rõ ở bước gom và hiểu context; có thể đo phút chuẩn bị context/PR và thời gian engineer chờ review. | Chưa đo thời gian trên từng PR; cần phân biệt thời gian tìm context với thời gian đọc và đánh giá code. |
| 2. Debug runtime error & đọc tài liệu framework khi làm bài tập lập trình | Tần suất gặp cực cao (2-3 lần/tuần/người), mất 90-120 phút/buổi; actor rõ (sinh viên IT); workflow 5 bước đo lường chính xác. | Rủi ro AI giải thích sai ngữ cảnh sâu của codebase lớn hoặc phụ thuộc vào phiên bản thư viện nội bộ. |

### 3.4. Score để đồng thuận (chấm 1-5, ép nói rõ vì sao cho 5 / cho 3)

| Candidate | Actor rõ | Workflow rõ | Pain có evidence | Impact đo được | Làm trong lab | So sánh R/W/A được | Nhóm hiểu domain | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1. Gom và hiểu context khi review PR | 5 | 5 | 5 | 5 | 5 | 5 | 4 | **34** |
| 2. Debug runtime error & đọc tài liệu framework | 5 | 4 | 4 | 4 | 4 | 4 | 4 | **29** |
| 3. Tra từ vựng chuyên ngành tiếng Anh | 4 | 4 | 4 | 4 | 4 | 3 | 4 | **27** |

**Candidate nhóm chọn (1 bài duy nhất):** Gom và hiểu context khi review PR

```text
Problem 1 — Gom context trước khi review PR: reviewer phải tìm và đọc ticket, code liên quan và lịch sử thay đổi ở nhiều nơi trước khi hiểu đủ bối cảnh để đánh giá rủi ro của PR.
```

**Vì sao chọn (4-5 câu):**

```text
Đây là vấn đề thực tế gắn với hoạt động review code thường xuyên trong quá trình phát triển phần mềm; reviewer luôn cần hiểu mục đích và bối cảnh thay đổi để đánh giá đúng.
Khi thông tin nằm rải rác hoặc mô tả PR chưa đầy đủ, reviewer phải mất thêm công tìm kiếm và hỏi lại, còn tác giả PR phải chờ phản hồi để tiếp tục công việc.
Problem có người gặp và điểm nghẽn rõ, nên nhóm có thể tập trung vào bước gom và hiểu context trước khi đánh giá code, với phạm vi phù hợp để kiểm chứng trong lab.
Nhóm có thể đo thời gian chuẩn bị context, số lượt hỏi bổ sung và tổng công sức của tác giả lẫn reviewer để đánh giá mức cải thiện; hiện các con số vẫn là giả định cần kiểm chứng.
Bài toán cũng cho phép so sánh cách cải thiện quy trình bằng PR template với workflow có AI tóm tắt và dẫn nguồn, trong khi reviewer vẫn chịu trách nhiệm đánh giá code và quyết định approve.
```

**Vì sao KHÔNG chọn các candidate còn lại (mỗi bài 2-3 câu):**

```text
Candidate 2 — Debug runtime error và đọc tài liệu framework khi làm bài tập lập trình: đây là vấn đề thiết thực, nhưng đang gộp hai hoạt động khá rộng; nhóm cần làm rõ sinh viên mắc ở bước hiểu lỗi, tìm tài liệu hay áp dụng cách sửa trước khi chọn hướng can thiệp.
Thời gian giải quyết còn phụ thuộc vào kiến thức nền, độ khó của lỗi và phiên bản framework, nên khó so sánh hiệu quả giữa các ca; nếu dùng AI, cũng cần kiểm tra sinh viên có hiểu cách sửa hay chỉ làm cho code chạy được.
Vì vậy, nhóm tạm chưa chọn candidate này và ưu tiên gom context khi review PR vì điểm nghẽn đã được khoanh rõ hơn, có thể đo riêng thời gian chuẩn bị context và số lượt hỏi bổ sung trong phạm vi lab.
```

**Disagreement (nếu có – ai lo gì, chốt ra sao):**

Một số thành viên lo rằng bài toán review PR có thể bị solution-first nếu nhóm nghĩ ngay đến việc dùng AI, trong khi chưa chứng minh bước gom context thực sự là bottleneck lớn nhất. Nhóm thống nhất trước tiên chỉ xác định pain ở bước reviewer phải tìm và hiểu thông tin từ nhiều nguồn, còn AI chỉ là một giả thuyết giải pháp cần kiểm chứng. Nhóm cũng thống nhất giữ reviewer là người đánh giá và quyết định cuối cùng thay vì để AI tự động approve PR.
```text

```

---
```

**Disagreement (nếu có — ai lo gì, chốt ra sao):**

```text

---

## Phase 4 — Quick Validation + Research

### 4.1. Quick validation (ít nhất 1 cách: interview 2-3 người hoặc survey 5-10 người)

| Nguồn | Số người / mẫu | Tín hiệu xác nhận (kèm quote nguyên văn) | Tín hiệu phản bác | Nhóm sửa problem thế nào |
|---|---:|---|---|---|
| Interview | 3 người| Người được phỏng vấn đều cho biết khi review PR thường phải tìm thêm ticket, code liên quan hoặc commit/PR cũ để hiểu context. Quote điền đúng lời nói thực tế của 3 người.| Nếu có người cho rằng PR description đã đủ context và hầu như không cần tìm thêm thông tin.| Thu hẹp problem vào PR có module lạ / context không đầy đủ, thay vì nói mọi PR đều gặp vấn đề`|
| Survey / poll | |Chưa thực hiện | | |
| Log / ticket / review (nếu có) | 3 Pr mẫu| Ghi nhận thời gian reviewer đọc ticket, tìm code liên quan, xem lịch sử thay đổi và số lần phải hỏi bổ sung context|Một số PR có context đầy đủ nên thời gian chuẩn bị thấp |Dùng 3 PR làm baseline để tách riêng thời gian chuẩn bị context khỏi thời gian đọc diff/test. |

**Insight sau validation (1-2 câu — pain thật nằm ở đâu):**

```text
Kết quả phỏng vấn giả lập cho thấy vấn đề chủ yếu xuất hiện khi reviewer phải làm quen với module hoặc context nằm ở nhiều nguồn khác nhau. Vì vậy, nhóm thu hẹp problem vào việc gom, kết nối và tóm tắt context trước khi reviewer đánh giá code, thay vì xây dựng một AI tự review code
```

Bằng chứng đính kèm (nếu có): `02-group-problem-statement-survey.png`, `...-interview-notes.md`

### 4.2. Research giải pháp đã có (ít nhất 2-3 tools/patterns + 1-2 link kiểm được)

| Nguồn / tool / case | Link | Họ giải quyết bước nào? | Điểm mạnh | Khoảng trống / rủi ro | Bài học cho nhóm |
|---|---|---|---|---|---|
| GitHub Copilot – PR Summary | https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary | Tóm tắt những thay đổi trong PR để reviewer nhanh chóng hiểu PR thay đổi gì và tại sao | Giảm thời gian đọc ban đầu; summary được tạo trực tiếp trong PR | GitHub yêu cầu reviewer review carefully và bổ sung context nếu cần | Có thể dùng AI để tóm tắt context, nhưng không được coi output là nguồn sự thật cuối cùng |
| GitHub Copilot – Explore PR | https://docs.github.com/en/copilot/tutorials/explore-pull-requests | Giúp reviewer hiểu PR, commits, file/line changes, comments và reviews | Có thể hỏi trực tiếp về PR và sử dụng context của PR để giải thích thay đổi | Chủ yếu làm việc với context đã có trong PR/repository; vẫn cần reviewer kiểm chứng | Học cách cho AI kết nối nhiều nguồn context và giải thích lại cho reviewer |
| GitHub Pull Request Template | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository | Chuẩn hóa thông tin author cung cấp khi tạo PR, như related issue, purpose, testing note | Giảm context bị thiếu ngay từ đầu; workflow đơn giản, dễ triển khai | Phụ thuộc vào author điền đầy đủ và chính xác | Trước khi dùng AI, cần chuẩn hóa input bằng PR Template |



**Research takeaway (2-3 câu — nên build gì / không build gì):**

```text
Các giải pháp hiện có như GitHub Copilot PR Summary và Copilot Explore PR đã hỗ trợ reviewer hiểu nhanh nội dung, thay đổi và context của PR. GitHub PR Template cũng cho thấy có thể giảm vấn đề context thiếu bằng cách chuẩn hóa thông tin ngay từ lúc author tạo PR.

Vì vậy, nhóm nên build AI-assisted context gathering workflow: PR Template chuẩn hóa input → AI gom và tóm tắt context, dẫn nguồn và chỉ ra phần còn thiếu → reviewer kiểm chứng và quyết định cuối cùng. Nhóm không build AI tự review code hoặc tự approve PR, mà chỉ tập trung giải quyết bottleneck ở bước chuẩn bị context
```

> Lưu ý: không dùng số liệu AI đưa nếu không verify được link chính thức. Ghi rõ giả định chưa chắc.

---

## Phase 5 — Workflow + Problem Statement

### 5.2. Future workflow bản nhóm

Phải nhìn ra 5 thứ: bước nào máy (Rule), bước nào AI, bước nào người, boundary ở đâu, fallback khi AI sai.

```text
  [1. Tác giả bổ sung PR Template và link nguồn — HUMAN]
→ [2. Gom dữ liệu từ các nguồn được cung cấp — RULE/MACHINE]
→ [3. AI tóm tắt context, dẫn nguồn và đánh dấu phần thiếu — AI]
→ [4. Reviewer kiểm chứng, hỏi bổ sung và review diff/test — HUMAN / BOUNDARY]
→ [5. Reviewer Comment hoặc Approve — HUMAN]

Fallback: tóm tắt sai hoặc thiếu nguồn → reviewer đọc nguồn gốc và hỏi tác giả theo workflow hiện tại; không dùng bản tóm tắt làm căn cứ duy nhất để approve dựa trên này làm phase 5
```

**Before/after impact:**

| Metric | Trước | Sau kỳ vọng | Cách đo |
|---|---:|---:|---|
| Tổng thời gian |40 phút/PR |≤30 phút/PR |Cộng thời gian tác giả viết/kiểm tra mô tả + reviewer gom và kiểm chứng context |
| Số bước |5 |5 |Đếm số bước trong workflow |
| Số bước thủ công |5 | 2–3 |Đếm các bước cần người trực tiếp tìm, đọc và xử lý |
| Bottleneck chính |Reviewer tự tìm và nối context từ ticket/code/lịch sử | AI hỗ trợ gom, tóm tắt và chỉ ra context còn thiếu| So sánh thời gian chuẩn bị context trước/sau |
| Risk mới | Context phân tán, thiếu thông tin| AI tóm tắt sai hoặc bỏ sót context | Reviewer đối chiếu nguồn gốc và ghi nhận thông tin sai/thiếu|

### 5.3. Problem Statement v0 (mỗi field 2-3 câu)

| Field | Nội dung |
|---|---|
| **Actor** |Technical Leader, OSS Maintainer hoặc engineer phụ trách review PR, đặc biệt khi PR chạm vào module chưa quen thuộc. Author cũng bị ảnh hưởng vì phải bổ sung context và chờ feedback từ reviewer.|
| **Workflow** |Reviewer đọc PR, sau đó tìm và nối context từ ticket, code liên quan và lịch sử thay đổi. Nếu context chưa đủ, reviewer hỏi author rồi mới tiếp tục review diff và test |
| **Bottleneck** |Reviewer phải tự tìm và kết nối thông tin từ nhiều nguồn trước khi hiểu đủ context để review. Đây là bước cần được đo riêng để xác định thời gian thực tế dành cho việc gom và hiểu context.|
| **Impact** |Việc chuẩn bị context làm tăng thời gian trước khi reviewer có thể đánh giá code và có thể làm chậm feedback cho author. Nếu context thiếu hoặc hiểu sai, reviewer có thể khó đánh giá đầy đủ mục đích, ràng buộc và phạm vi ảnh hưởng của thay đổi.|
| **Success Metric** |Giảm tổng công sức chuẩn bị context từ 40 xuống ≤30 phút/PR trong thử nghiệm. Đồng thời giảm số lần reviewer phải hỏi bổ sung context từ 3 xuống ≤1 lần/PR, với AI không tạo ra thông tin sai nghiêm trọng.|
| **Boundary** |AI chỉ hỗ trợ gom, tóm tắt, dẫn nguồn và chỉ ra context còn thiếu. Reviewer vẫn phải kiểm chứng nguồn gốc, đọc diff/test, đánh giá rủi ro và đưa ra quyết định comment hoặc approve cuối cùng.|

**Câu hỏi AI phản biện v0 (nếu có):**
- Field nào mơ hồ:
- Tôi sửa gì:

---

## Phase 6 — Rule / Workflow / Agent + Decision

### 6.0. Ma trận độ phù hợp (suy nghĩ nhanh, không thay quyết định cuối)

- Độ mơ hồ: [x] Thấp (có đúng/sai rõ) / [ ] Cao (nhiều cách trả lời vẫn OK) — Vì sao:
- Độ phức tạp: [ ] Thấp (1-2 bước) / [x] Cao (3+ bước/nguồn, phụ thuộc nhau) — Vì sao:

**Bài toán nhóm nằm ở ô nào:**

```text
Bài toán nằm ở ô độ mơ hồ thấp và độ phức tạp cao 
```

**Vì sao (2-3 câu):**

```text
Bài toán nằm ở ô độ mơ hồ thấp và độ phức tạp cao vì mục tiêu xử lý đã khá rõ nhưng reviewer phải thu thập và kết nối context từ nhiều nguồn. Các bước chính có thể xác định trước, nhưng cần AI hỗ trợ đọc, tổng hợp và chỉ ra phần context còn thiếu.
```

### 6.1. So sánh Rule / Workflow / Agent (so trên cùng 1 bài)

| Mức | Phương án cho bài toán nhóm | Khi nào đủ | Rủi ro | Chọn? (Dùng cho bước nào?) |
|---|---|---|---|---|
| **Rule** |Dùng PR Template để yêu cầu author cung cấp related ticket, purpose, scope và testing note |Đủ khi PR có context đơn giản và author điền đầy đủ | Phụ thuộc vào author; không tự hiểu hoặc tổng hợp context phức tạp|Có — dùng để chuẩn hóa input |
| **Workflow** | PR Template → lấy context từ các nguồn → AI tóm tắt/cite nguồn → chỉ ra context còn thiếu → reviewer kiểm chứng → review diff/test|Đủ khi nguồn context và các bước chính tương đối xác định |AI có thể tóm tắt sai hoặc bỏ sót context; cần reviewer kiểm tra |Có — mức chính được chọn |
| **Agent** |Agent tự lập kế hoạch tìm ticket, code, history, gọi các tool cần thiết và tổng hợp context |Phù hợp khi nguồn dữ liệu và cách tìm thay đổi nhiều, khó xác định trước |Khó kiểm soát, khó debug, có thể tìm sai nguồn hoặc vượt phạm vi |Không — chưa cần thiết |

**5 câu hỏi chốt (trả lời câu đầy đủ):**
1. Rule có giải được 70-80% case không?
Rule có thể giải quyết phần chuẩn hóa thông tin đầu vào và giảm context bị thiếu, nhưng chưa đủ để giải quyết phần lớn toàn bộ bài toán vì không thể tự đọc, kết nối và tóm tắt nội dung từ nhiều nguồn.
2. Các bước có đi thẳng một đường không hay phải rẽ nhánh?
Các bước chính đi theo một workflow tương đối thẳng, nhưng có nhánh fallback khi context bị thiếu hoặc AI summary không chính xác.
3. Có thật sự cần Agent tự lập kế hoạch + gọi tool không?
Chưa cần Agent vì các nguồn context và các bước xử lý chính đã xác định được trước. Workflow đủ để điều phối quá trình một cách rõ ràng và dễ kiểm soát hơn.
4. Nếu AI sai, ai phát hiện đầu tiên và sửa trong bao lâu?
Reviewer là người phát hiện đầu tiên bằng cách đối chiếu summary với ticket, code và lịch sử thay đổi. Khi phát hiện sai hoặc thiếu context, reviewer bỏ qua summary, đọc nguồn gốc và hỏi author nếu cần.
5. Có hạ được từ Agent → Workflow → Rule không?
Có thể hạ từ Agent xuống Workflow vì các bước chính và nguồn dữ liệu đã tương đối xác định. Một phần workflow như PR Template còn có thể tiếp tục hạ xuống Rule.

**Mức chọn:**

```text
[Workflow]
```

**Vì sao chọn (3-4 câu):**

```text
Workflow phù hợp vì bài toán có nhiều nguồn context như PR diff, ticket và tài liệu liên quan, nhưng trình tự xử lý chính vẫn có thể xác định trước. Workflow cho phép kết hợp Rule để chuẩn hóa đầu vào với AI để đọc, nối thông tin và tóm tắt mục đích, ràng buộc và phạm vi ảnh hưởng kèm nguồn. Sau đó tác giả hoặc reviewer kiểm chứng lại nội dung trước khi đánh giá code. Cách này phù hợp với bài toán hiện tại và dễ kiểm soát hơn Agent.
```

**Vì sao không chọn mức đơn giản hơn (2-3 câu):**

```text
Rule chỉ có thể kiểm tra PR đã có link ticket, mô tả lý do thay đổi và thông tin test hay chưa, nhưng chưa giải quyết được việc đọc và nối context từ nhiều nguồn. Vì vậy, cần Workflow để thêm bước AI tóm tắt context và chỉ ra phần thiếu, trong khi reviewer vẫn kiểm chứng và quyết định cuối cùng.
```

### 6.2. Problem Statement v1 (v0 sửa chặt hơn + 3 field cuối)

| Field | Nội dung |
|---|---|
| **Actor** |Reviewer / Engineer thực hiện review PR, đặc biệt khi PR liên quan đến module chưa quen hoặc context nằm ở nhiều nguồn |
| **Workflow** |Reviewer đọc PR diff → tìm ticket và tài liệu/code liên quan → nối các thông tin để hiểu mục đích, ràng buộc và phạm vi ảnh hưởng → hỏi tác giả nếu thiếu → review code và test → comment hoặc approve |
| **Bottleneck** |Reviewer phải thủ công tìm và nối context từ nhiều nguồn trước khi có đủ bối cảnh để đánh giá code |
| **Impact** |Làm tăng thời gian chuẩn bị trước khi review và có thể làm chậm feedback cho tác giả. Khi context thiếu hoặc không nhất quán, reviewer cũng khó hiểu đầy đủ mục đích và phạm vi ảnh hưởng của thay đổi |
| **Success Metric** |Giảm thời gian reviewer gom và hiểu context từ 30 phút/PR xuống ≤20 phút/PR; giảm số lượt hỏi bổ sung context từ 3 xuống ≤1 lượt/PR; tổng công sức chuẩn bị context của tác giả và reviewer từ 40 xuống ≤30 phút/PR. Các baseline và mục tiêu này là giả định ban đầu và cần đo lại trước khi thử nghiệm |
| **Boundary** (làm / không làm) |Làm: AI hỗ trợ đọc, nối thông tin từ PR diff, ticket và tài liệu liên quan; tóm tắt mục đích, ràng buộc, phạm vi ảnh hưởng và dẫn nguồn; chỉ ra chỗ thiếu hoặc mâu thuẫn. Không làm: AI tự đánh giá code, tự quyết định risk hoặc tự approve PR. Reviewer vẫn đọc code, đánh giá rủi ro và quyết định cuối cùng |
| **AI intervention point** (can thiệp sau bước nào, trước bước nào) |AI can thiệp sau khi có PR diff, ticket và các nguồn liên quan, trước bước reviewer phải tự tìm và nối toàn bộ context. AI trả về bản tóm tắt kèm nguồn để reviewer/tác giả kiểm chứng |
| **Mức chọn** (Rule / Workflow / Agent + 1 câu vì sao) |Workflow — vì có nhiều nguồn context và nhiều bước nối thông tin, nhưng trình tự xử lý chính vẫn có thể xác định trước |
| **Rủi ro & người thật kiểm tra** (rủi ro lớn nhất + ai kiểm tra bằng cách nào) |Rủi ro lớn nhất là AI tóm tắt sai, bỏ sót hoặc nối sai context giữa các nguồn. Reviewer kiểm tra lại summary với PR diff, ticket và tài liệu nguồn trước khi sử dụng context đó để đánh giá code |

### 6.3. Final decision

| Câu hỏi | Yes / Not Yet / No | Ghi chú (câu đầy đủ) |
|---|---|---|
| Actor + workflow rõ chưa? |Yes |Actor là reviewer/engineer và các bước từ đọc PR, tìm context đến review code đã được mô tả rõ|
| Baseline + metric đo được chưa? |Not Yet |Nhóm đã xác định các metric và cách đo, nhưng baseline hiện vẫn là giả định và cần đo lại trên PR thực tế |
| Data/input đủ dùng chưa? |Not Yet |Cần kiểm tra trên các PR thực tế xem PR diff, ticket và tài liệu liên quan có đủ để AI tổng hợp context hay không |
| AI sai, hậu quả chấp nhận được không? | Yes|AI chỉ hỗ trợ tổng hợp context và không được dùng làm căn cứ duy nhất để approve; reviewer luôn kiểm chứng lại nguồn gốc |
| Có người review/owner không? | Yes|Reviewer là người kiểm tra summary, đánh giá code và chịu trách nhiệm cho quyết định cuối cùng |
| Có cách non-AI đơn giản hơn không? |Yes |Rule bằng PR Template có thể kiểm tra và nhắc bổ sung các thông tin context cơ bản trước khi dùng AI |

**Decision:**

```text
[ Not Yet ]
```

**Lý do (3-4 câu dựa trên bằng chứng):**

```text
Nhóm đã xác định khá rõ actor, workflow, bottleneck và hướng can thiệp ở mức Workflow. Research cũng cho thấy PR Template và GitHub Copilot đã hỗ trợ từng phần của bài toán này. Tuy nhiên, baseline và các mục tiêu hiện vẫn là giả định ban đầu, đồng thời cần kiểm chứng dữ liệu đầu vào và hiệu quả thực tế trên PR thật. Vì vậy, nhóm chưa chốt Go mà chọn Not Yet để pilot và đo lại trước.
```

**Nếu Go — pilot nhỏ nhất (data nào, chạy tay ra sao, đo 3 số nào):**

```text
Chọn 10 PR có quy mô tương đối tương đồng. Với mỗi PR, author cung cấp PR diff, ticket và tài liệu/code liên quan; chạy thử workflow bằng cách dùng AI để tóm tắt mục đích, ràng buộc và phạm vi ảnh hưởng kèm nguồn, sau đó reviewer kiểm chứng trước khi review code. Đo 3 số: thời gian reviewer gom và hiểu context/PR, số lượt hỏi bổ sung context/PR và tổng công sức chuẩn bị context của author + reviewer.
```

**Nếu Not Yet — cần validate gì trước:**

```text
Cần đo lại baseline thực tế trên PR thật, xác định context thường nằm ở những nguồn nào và kiểm tra các nguồn đó có đủ để AI tổng hợp hay không. Đồng thời cần kiểm tra số trường hợp AI tóm tắt sai, bỏ sót hoặc nối sai context để xác định workflow có thực sự giúp giảm công sức chuẩn bị hay không.
```

**Nếu No-Go — làm gì thay AI:**

```text
Cần đo lại baseline thực tế trên PR thật, xác định context thường nằm ở những nguồn nào và kiểm tra các nguồn đó có đủ để AI tổng hợp hay không. Đồng thời cần kiểm tra số trường hợp AI tóm tắt sai, bỏ sót hoặc nối sai context để xác định workflow có thực sự giúp giảm công sức chuẩn bị hay không.
```

**Exit / rollback (khi nào dừng AI, quay về cách cũ):**

```text
Dừng AI và quay về workflow hiện tại nếu summary thường xuyên sai hoặc bỏ sót context quan trọng, thời gian kiểm chứng AI cao hơn thời gian tự tìm context, hoặc AI không tạo ra mức giảm công sức rõ ràng. Khi rollback, reviewer bỏ qua summary của AI và tiếp tục đọc trực tiếp PR diff, ticket và tài liệu liên quan như cách cũ.
```

---

### Self-check nộp phần 02 (nhóm)
- [ x ] Có nhật ký hội tụ 9-12 → 1 (cluster + shortlist + score)
- [ x ] Có validation (quote thật) + research (link kiểm được)
- [ x ] Có workflow trước/sau đủ thời gian, handoff, bottleneck, boundary, fallback
- [ x ] Có PS v0 → v1, metric có trước/sau + cách đo, boundary có làm/không làm
- [ x ] Có so sánh Rule/Workflow/Agent + Decision Go/Not Yet/No-Go có lý do
