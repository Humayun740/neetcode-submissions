from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        target_counts = Counter(t)
        window_counts = {}

        # Number of unique characters in t that are fully satisfied in current window
        have = 0
        need = len(target_counts)

        # Stores (length, left_idx, right_idx)
        best_len = float("inf")
        best_range = (-1, -1)

        l = 0
        for r, char in enumerate(s):
            # Expand window to the right
            window_counts[char] = window_counts.get(char, 0) + 1

            # Check if this character meets the target requirement
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # Contract window from the left while it satisfies all requirements
            while have == need:
                # Update best window if smaller
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best_range = (l, r)

                # Pop left character
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                l += 1

        start, end = best_range
        return s[start : end + 1] if best_len != float("inf") else ""