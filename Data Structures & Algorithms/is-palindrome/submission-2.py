class Solution:
    def isPalindrome(self, s: str) -> bool:
        yo = ""
        for c in s:
            if c.isalnum():
                yo = yo + c
        yo = yo.lower()
        if yo == yo[::-1]:
            return True
        return False
        