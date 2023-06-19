# convert to binary
positive = 95601

positive_binary = "{0:b}".format(positive)

print(f"{positive_binary=}")


class Solution(object):
    def hammingWeight(self, n):

        n = n

        one_count = 0
        for i in n:
            if i == "1":
                one_count += 1
        return one_count


num = positive_binary
result = Solution()
print(f"The hamming weight of 95,601 is {result.hammingWeight(num)}")
