def subsets(nums):
        res = []
        answer = []
        def backtrack(i: int):
            if i >= len(nums):
                answer.append(res)
                return
            else:
                backtrack(i+1,res)
                res.append(nums[i])
                # print(res)
                res.pop()
                backtrack(i+1,res + nums)

        backtrack(0,res)
        return answer
x = subsets([1,2,3])
print(x)