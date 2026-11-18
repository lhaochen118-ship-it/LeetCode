# Bài giảng LeetCode Medium (tiếng Việt)

Mỗi notebook giảng một bài theo cẩm nang `huong_dan_phong_cach_day_code_ipynb.pdf`: đề bài và ví dụ, kiến thức Python nền tảng, nhiều cách giải từ dễ đến tối ưu (kèm bảng mô phỏng và hàm `trace_*`), code chuẩn LeetCode kèm test, chứng minh, độ phức tạp, kiểm thử chéo ngẫu nhiên, lỗi hay gặp, mẹo nhận diện, biến thể, 6 bài tập có gợi ý và đáp án ở cuối.

Mọi notebook đã được chạy lại từ đầu trên kernel Python 3 mới, không có cell lỗi.

| # | Bài | Kỹ thuật chính | Các cách giải trong notebook |
|---|---|---|---|
| 4101 | [Find All Numbers Disappeared in an Array III](4101_find_all_numbers_disappeared_in_an_array_iii_intro_vietnamese.ipynb) | Khoảng trống giữa các điểm đã sắp xếp, lính canh | Đi dọc trục số → lính canh + cặp kề nhau → quét với `next_missing` |
| 4102 | [Count Valid Substrings I](4102_count_valid_substrings_i_intro_vietnamese.ipynb) | Đếm substring theo điểm kết thúc | `O(n³)` → dừng sớm `O(n²)` → biến `last` `O(n)` → đếm phần bù |
| 4103 | [Remove Elements by Type and Color](4103_remove_elements_by_type_and_color_intro_vietnamese.ipynb) | Stack khối `[key, count]`, thứ tự xoá không quan trọng | Vét cạn mọi thứ tự → mô phỏng tham lam → stack `O(n)` |
| 4104 | [Count Valid Substrings II](4104_count_valid_substrings_ii_intro_vietnamese.ipynb) | Khớp subsequence tham lam, bảng vị trí kế tiếp | `O(n³)` → máy trạng thái `O(n²)` → bảng `nxt` `O(n)` → chuyền vị trí `O(1)` bộ nhớ |
| 4106 | [Find Mismatched Segments Between Two Strings](4106_find_mismatched_segments_between_two_strings_intro_vietnamese.ipynb) | Tách đoạn liên tiếp tối đa | Dịch định nghĩa `O(n³)` → biến `start` / lính canh → hai con trỏ → `groupby` |
| 4107 | [Count Valid Suffix Sorts I](4107_count_valid_suffix_sorts_i_intro_vietnamese.ipynb) | Tách điều kiện, giao hai khoảng, đa tập | Mô phỏng `O(n² log n)` → mảng logic tiền tố/hậu tố → giao khoảng `[minI, maxI]` → thử một ứng viên |
| 4108 | [Minimum Cost to Make Red Nodes Connected](4108_minimum_cost_to_make_red_nodes_connected_intro_vietnamese.ipynb) | Tree DP, đổi mốc chi phí, tập liên thông có đỉnh cao nhất | Vét cạn `2^n` → thử từng top `O(n²)` → tree DP `O(n)` |
| 4110 | [Find the Maximum Length of Valid Subsequence III](4110_find_the_maximum_length_of_valid_subsequence_iii_intro_vietnamese.ipynb) | Số dư, DP theo số dư, đếm khối xen kẽ | Vét cạn → DP kiểu LIS `O(n²)` → `best[r]` `O(n)` → đếm khối |
| 4112 | [Maximize Score After Zeroing Subtrees](4112_maximize_score_after_zeroing_subtrees_intro_vietnamese.ipynb) | Tree DP từ mảng `parent`, lựa chọn bắt buộc / tùy chọn | Vét cạn kế hoạch → DFS đệ quy → DP lặp theo BFS ngược |
| 4113 | [Game of Divisible Sums](4113_game_of_divisible_sums_intro_vietnamese.ipynb) | DP trò chơi, hiệu điểm (negamax) | Minimax → negamax + `lru_cache` → DP lặp → hai biến `O(1)` |
