# 03 — Individual Reflection

> Viết bằng lời của bạn (Phase 7 trong `01-worksheet.md`). Có thể dùng AI gợi ý câu hỏi tự soi, không dùng AI viết thay. 8-12 câu, có chuyện cụ thể.

## Thông tin cá nhân

- Họ và tên: Nguyễn Thùy linh
- Mã học viên:2A202602497
- Nhóm:2A TH-True Mi
- Candidate problem nhóm chọn: Gom và tổng hợp context (ticket, code liên quan, lịch sử thay đổi) khi review PR để nhận ra rủi ro kỹ thuật.

---

## 1. Tôi đã tham gia vào phần nào?

Ghi việc cụ thể + kết quả cụ thể. Không ghi chung chung kiểu "tham gia thảo luận".

| Hoạt động | Tôi đã làm gì? (việc cụ thể) | Kết quả / ảnh hưởng tới nhóm |
|---|---|---|
| Scan cá nhân | Tôi scan các vấn đề xung quanh và viết Problem Card cá nhân, xác định actor, workflow, bottleneck và impact. | Có các candidate problem cụ thể để đưa ra thảo luận với nhóm. |
| Pitch Problem Card | Tôi trình bày các Problem Card của mình và giải thích vấn đề, workflow và điểm nghẽn. | Giúp nhóm có thêm phương án để so sánh khi chọn bài toán chung. |
| Challenge bài của bạn khác | Tôi cùng các thành viên đặt câu hỏi về mức độ lặp lại, impact và khả năng đo lường của các candidate. | Giúp loại bớt các vấn đề quá rộng hoặc chưa đủ bằng chứng. |
| Gom trùng / cluster | Tôi tham gia nhóm các candidate có điểm chung về công việc thủ công, thu thập thông tin và xử lý context. | Giúp nhóm thu gọn các ý tưởng để dễ so sánh. |
| Problem Statement | Tôi hỗ trợ làm rõ actor, vấn đề và bottleneck của bài toán review PR. | Problem Statement cụ thể hơn và tập trung vào một bước có thể đo lường. |
| Rule / Workflow / Agent | Tôi cùng nhóm đề xuất PR Context Copilot: AI tổng hợp PR, ticket, code diff và history thành Review Brief, còn reviewer kiểm tra và quyết định cuối cùng. | Nhóm xác định được vai trò của AI và human boundary. |
| Decision | Tôi tham gia đánh giá giải pháp và thống nhất làm prototype PR Context Copilot để kiểm chứng khả năng giảm thời gian chuẩn bị context. | Nhóm có hướng prototype rõ ràng và metric để đánh giá. |
| Chọn candidate problem | Tôi cùng nhóm so sánh các candidate dựa trên mức độ lặp lại, bottleneck, impact và khả năng đo lường. | Nhóm thống nhất tập trung vào bài toán reviewer phải gom context từ nhiều nguồn khi review PR. |
| Validation / research | Tôi cùng nhóm xác định những dữ liệu còn thiếu như thời gian chuẩn bị context/PR và thời gian chờ review. | Giúp nhóm không coi các giả định hoặc số liệu chưa kiểm chứng là fact và xác định nội dung cần validation tiếp. |
**Dấu tay rõ nhất của tôi trong artifact cuối (1-2 câu):**

Dấu tay rõ nhất của tôi là tham gia xây dựng ý tưởng prototype PR Context Copilot và làm rõ workflow trước/sau khi có AI. Tôi tập trung vào việc giữ reviewer ở bước kiểm tra và quyết định cuối cùng thay vì để AI tự động approve PR.

```

---

## 2. Bảng dùng AI (mỗi dòng 1 phase có dùng AI — 2 cột cuối bắt buộc)

| Phase | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai / hời hợt ở đâu? | Tôi sửa gì bằng nhận định của mình? |
|---|---|---|---|---|
| Scan | Tôi dùng AI để gợi ý cách nhìn các vấn đề theo actor, workflow, bottleneck và impact. | AI giúp tôi biết cách tách một vấn đề chung thành các vấn đề cụ thể để đưa vào Problem Card. | Một số ví dụ và số liệu AI gợi ý không đúng với trải nghiệm thực tế và chưa có bằng chứng. | Tôi bỏ các ví dụ không phù hợp, không coi số liệu chưa kiểm chứng là fact và chỉ giữ những vấn đề có thể giải thích rõ. |
| Problem Card | Tôi dùng AI để hỗ trợ cấu trúc Problem Card gồm actor, workflow, bottleneck, impact, metric và AI hypothesis. | AI giúp tôi trình bày từng candidate problem rõ ràng và dễ so sánh. | AI có xu hướng đề xuất giải pháp AI khá sớm trong khi vấn đề chưa được kiểm chứng đầy đủ. | Tôi bổ sung Non-AI alternative, fallback và yêu cầu có human review thay vì để AI xử lý toàn bộ. |
| Workflow | Tôi dùng AI để gợi ý cách mô tả current state và future state của quy trình review PR. | AI giúp tôi nhìn rõ bottleneck nằm ở bước reviewer phải gom và hiểu context từ nhiều nguồn. | AI có thể đơn giản hóa workflow và khiến phần AI trông như có thể thay reviewer. | Tôi giữ reviewer là người kiểm tra và quyết định cuối cùng; AI chỉ hỗ trợ tổng hợp context thành Review Brief. |
| Research | Tôi dùng AI để gợi ý những dữ liệu cần kiểm chứng cho candidate problem. | AI giúp tôi nhận ra cần đo thời gian chuẩn bị context/PR và thời gian engineer chờ review. | AI không có dữ liệu thực tế của team nên không thể khẳng định chính xác mức thời gian tiết kiệm. | Tôi coi các con số chưa có bằng chứng là giả thuyết cần validation thay vì kết luận. |
| Problem Statement | Tôi dùng AI để hỗ trợ diễn đạt vấn đề ngắn gọn theo actor, pain, workflow và bottleneck. | AI giúp Problem Statement tập trung hơn vào việc reviewer phải tìm context ở nhiều nơi trước khi review PR. | Một số gợi ý ban đầu còn rộng và dễ chuyển sang mô tả giải pháp thay vì mô tả vấn đề. | Tôi thu hẹp vào reviewer, bước gom context và impact về thời gian chuẩn bị review. |
| Rule / Workflow / Agent | Tôi dùng AI để gợi ý prototype PR Context Copilot và phân chia nhiệm vụ giữa AI với con người. | AI giúp hình dung luồng tạo Review Brief từ PR, ticket, code diff và history. | AI có xu hướng tự động hóa nhiều bước, có thể gây rủi ro nếu context bị thiếu hoặc tóm tắt sai. | Tôi đặt human boundary: reviewer phải kiểm tra Review Brief và vẫn là người quyết định approve hoặc request changes. |
| Decision | Tôi dùng AI để hỗ trợ so sánh hướng giải pháp và xác định metric cho prototype. | AI giúp tôi xác định metric chính là thời gian reviewer cần để chuẩn bị đủ context cho một PR. | AI chưa thể chứng minh prototype chắc chắn giảm thời gian nếu chưa thử nghiệm thực tế. | Tôi coi hiệu quả của prototype là hypothesis cần kiểm chứng bằng cách so sánh thời gian trước và sau khi sử dụng. |

> Nếu phase nào không dùng AI, ghi `Không dùng` và vì sao tự làm.

---

## 3. Reflection câu hỏi mở

Chọn 3-4 câu trong 6 câu dưới để viết thành đoạn 8-12 câu (không trả lời bullet 1 dòng):
- Tôi học được gì khi nghe top 3 problems của các bạn khác?
- Nhóm có lúc nào bị solution-first, đòi làm Agent cho ngầu không?
- Tôi có thay đổi ý kiến sau khi bị challenge không, vì sao đổi?
- Tôi đóng góp gì thật sự vào artifact cuối, phần nào có dấu tay của tôi?
- Điều khó nhất khi viết Problem Statement là gì, metric hay boundary?
- Nếu làm lại, tôi sẽ challenge nhóm mạnh hơn ở điểm nào?

Qua bài này, tôi nhận ra một vấn đề phù hợp để phát triển không chỉ cần gây mất thời gian mà còn phải có actor, workflow, bottleneck và impact đủ rõ để kiểm chứng. Khi nghe và challenge các candidate problem, tôi thấy bài toán review PR đáng chú ý vì reviewer phải tìm và đọc context từ nhiều nguồn trước khi có thể đánh giá code. Tuy nhiên, nhóm hiện chưa có số liệu thực tế về thời gian chuẩn bị context trên từng PR nên tôi cho rằng đây vẫn là phần cần validation thêm. Trong quá trình thảo luận, có lúc chúng tôi nghĩ khá sớm đến việc dùng AI để tự động hóa quy trình review. Sau khi xem lại workflow, tôi nhận ra AI không nên thay thế reviewer mà phù hợp hơn với vai trò hỗ trợ gom và tóm tắt thông tin. Phần tôi đóng góp rõ nhất là tham gia xây dựng ý tưởng prototype PR Context Copilot và làm rõ workflow trước và sau khi có AI. Tôi đề xuất AI tổng hợp PR, ticket, code diff và history thành một Review Brief để reviewer có context nhanh hơn. Tôi cũng giữ human boundary ở bước reviewer kiểm tra thông tin và đưa ra quyết định approve hoặc request changes cuối cùng. Điều khó nhất khi viết Problem Statement là tránh chuyển quá sớm từ việc mô tả vấn đề sang mô tả giải pháp AI. Nếu làm lại, tôi sẽ cùng nhóm thu thập thêm dữ liệu về thời gian review PR thực tế và challenge kỹ hơn giả thuyết rằng bước gom context là bottleneck lớn nhất trước khi quyết định phát triển prototype.
```text



```

---

## 4. Tự kiểm cuối bài (check trước khi nộp repo)

- [x] [12đ] Cá nhân có 5+ problems + top 3 Problem Cards
- [x] [12đ] Tôi đã pitch rõ + challenge nhóm đúng trọng tâm (ghi ở bảng mục 1)
- [x] Nhóm có nhật ký hội tụ từ candidates về 1 bài
- [x] [15đ] Nhóm có workflow trước/sau
- [x] [20đ] Nhóm có PS v0/v1 với metric + boundary rõ
- [x] [15đ] Nhóm có so sánh No AI / Rule / Workflow / Agent
- [x] [10đ] Nhóm có Go / Not Yet / No-Go + lý do rõ
- [x] [10đ] Reflection này có vai trò thật + AI giúp/sai ở đâu + điều học được + nếu làm lại đổi gì
- [x] [6đ] Tôi tự giải thích được mạch problem → workflow → metric → boundary → độ phù hợp AI

