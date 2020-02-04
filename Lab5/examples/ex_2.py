def countOccurences(s):
	ans = [0]*26
	for i in range(0, len(s)):
		ans[ord(s[i]) - ord('a')] = ans[ord(s[i]) - ord('a')] + 1
	return ans

print(countOccurences("felicity"))
