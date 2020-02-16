import TreeNode


class LC:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement], i]            
            dic[nums[i]] = i
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return root.left == root.right
        self.isSymmetric(root.left)
        self.isSymmetric(root.right)
        return (root.left == root.right)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = []
        left = -1
        right = -1
        if root:
            current_val = root.val
            stack.append((root,current_val))
        else: 
            return False
        while stack != []:
            expand = stack.pop()  
            current_node = expand[0]
            current_val = expand[1]
            if current_val == sum and current_node.left == None and current_node.right == None :
                return True
            if current_node.left:                                
                left = current_val + current_node.left.val
                stack.append((current_node.left, left))
            if current_node.right:                   
                right = current_val + current_node.right.val
                stack.append((current_node.right, right))
        return False
            

    def maxDepth_104(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth_104(root.left), self.maxDepth_104(root.right))

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor > 0:
            if xor & 1 :
                count += 1
            xor >>= 1
        return count

    def canWinNim_292(self, n: int) -> bool:
        return n % 4 != 0
    def fizzBuzz(self, n: int):
        res = []
        for i in range(1,n+1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 5 == 0:
                res.append('Buzz')
            elif i % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(i))
        return res
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(0, len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count
    def containsDuplicate(self, nums):
        me_set = set(nums)
        return len(me_set) != len(nums)
    def containsDuplicate_v2(self, nums): #works but slow
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    def reverse_integer(self, x: int) -> int:
        res = 0
        isNegative = False
        if x < 0:
            x *= -1
            isNegative = True       
        while x > 0:
            mod = x % 10
            res *= 10
            res += mod
            x = int(x/10)
        if isNegative:
            res *= -1
        # so dumb sine the max val is 2^31 that why i need this if below
        if abs(res) > (1<<31)-1:
            return 0
        return res
    def intersect(self, nums1, nums2):
        L = []
        if len(nums1) <= len(nums2):
            for item in nums1:
                if item in nums2:
                    L.append(item)
        else:
            for item in nums2:
                if item in nums1:
                    L.append(item)
        return L
    #39/68 this is a 'hard question'
    def longestConsecutive(self, nums):
        sorted_list = sorted(nums)
        sorted_list = list(set(sorted_list))
        count = 1
        me_max = 1
        print(sorted_list)
        for i in range(1,len(sorted_list)):
            if sorted_list[i] - sorted_list[i-1] == 1:
                count += 1
                print('yeah')
            else:
                count = 1
            me_max = max(me_max, count)
        print('me_maax: ',me_max)
        return me_max





