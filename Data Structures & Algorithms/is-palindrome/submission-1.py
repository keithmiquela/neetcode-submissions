class Solution:
    def isPalindrome(self, s: str) -> bool:
        included = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijjklmnopqrstuvwxyz0123456789'
        check = []
        for char in s:
            if char in included:
                check.append(char.lower())
        return check == check[::-1]