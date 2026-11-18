# LeetCode

Bộ notebook Jupyter (.ipynb) tiếng Việt giảng giải bài LeetCode cho người nhập môn, theo cẩm nang
`huong_dan_phong_cach_day_code_ipynb.pdf`. Danh mục ID và độ khó của toàn bộ bài nằm trong
`LeetCode_Danh_Muc_4114_Theo_Do_Kho.pdf`.

Mỗi notebook đi theo cùng một trình tự: đề bài → kiến thức nền → các cách giải từ đơn giản đến tối ưu →
mô phỏng từng bước → code `class Solution` + test → vì sao đúng / độ phức tạp → lỗi thường gặp →
bài tập (TODO + gợi ý) → đáp án ở cuối → template và checklist.

## Notebook mẫu (Easy)

| # | Bài | Notebook |
|---|-----|----------|
| 1 | Two Sum | [two_sum_hashmap_intro_vietnamese.ipynb](two_sum_hashmap_intro_vietnamese.ipynb) |
| 9 | Palindrome Number | [palindrome_number_python_intro_vietnamese.ipynb](palindrome_number_python_intro_vietnamese.ipynb) |
| 13 | Roman to Integer | [roman_to_integer_intro_vietnamese(1).ipynb](roman_to_integer_intro_vietnamese(1).ipynb) |

## Hard (thư mục `hard/`)

| # | Bài | Các cách giải được giảng | Notebook |
|---|-----|--------------------------|----------|
| 4 | Median of Two Sorted Arrays | Gộp + sort → merge hai con trỏ (đi tới giữa) → phần tử thứ k (loại k/2) → binary search vách ngăn | [0004](hard/0004_median_of_two_sorted_arrays_intro_vietnamese.ipynb) |
| 10 | Regular Expression Matching | Đệ quy → đệ quy + memo → DP bảng → DP 2 hàng | [0010](hard/0010_regular_expression_matching_intro_vietnamese.ipynb) |
| 23 | Merge k Sorted Lists | Gom + sort → merge lần lượt → so k đầu → min-heap → chia để trị | [0023](hard/0023_merge_k_sorted_lists_intro_vietnamese.ipynb) |
| 25 | Reverse Nodes in k-Group | Chép giá trị (baseline) → stack → đệ quy → lặp với dummy, O(1) nhớ | [0025](hard/0025_reverse_nodes_in_k_group_intro_vietnamese.ipynb) |
| 30 | Substring with Concatenation of All Words | Hoán vị (brute force) → so Counter từng vị trí → sliding window theo offset | [0030](hard/0030_substring_with_concatenation_of_all_words_intro_vietnamese.ipynb) |
| 32 | Longest Valid Parentheses | Brute force → DP → stack chỉ số với mốc -1 → hai lượt quét O(1) nhớ | [0032](hard/0032_longest_valid_parentheses_intro_vietnamese.ipynb) |
| 37 | Sudoku Solver | Backtracking quét → backtracking + set → MRV → bitmask + MRV | [0037](hard/0037_sudoku_solver_intro_vietnamese.ipynb) |
| 41 | First Missing Positive | Thử từng k → sort → set → đánh dấu bằng dấu âm → cyclic sort | [0041](hard/0041_first_missing_positive_intro_vietnamese.ipynb) |
| 42 | Trapping Rain Water | Brute force → prefix/suffix max → monotonic stack → two pointers | [0042](hard/0042_trapping_rain_water_intro_vietnamese.ipynb) |
| 44 | Wildcard Matching | Đệ quy → memo → DP bảng → DP 1 chiều → greedy + quay lui về `*` gần nhất | [0044](hard/0044_wildcard_matching_intro_vietnamese.ipynb) |
| 51 | N-Queens | Hoán vị + lọc → backtracking quét → backtracking 3 set → bitmask | [0051](hard/0051_n_queens_intro_vietnamese.ipynb) |
| 52 | N-Queens II | Hoán vị → backtracking quét → 3 set → bitmask → đối xứng gương | [0052](hard/0052_n_queens_ii_intro_vietnamese.ipynb) |
| 60 | Permutation Sequence | Sinh hoán vị (dừng sớm) → itertools → next permutation k-1 lần → hệ đếm giai thừa | [0060](hard/0060_permutation_sequence_intro_vietnamese.ipynb) |
| 65 | Valid Number | `float()` (vì sao sai) → tách theo e/E → một lượt quét với cờ → DFA → regex | [0065](hard/0065_valid_number_intro_vietnamese.ipynb) |
| 68 | Text Justification | Tách hàm rõ ràng (greedy chia dòng + divmod) → round-robin → bản gọn ljust/join | [0068](hard/0068_text_justification_intro_vietnamese.ipynb) |
