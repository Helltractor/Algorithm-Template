class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: [ListNode], l2: [ListNode]):
    if not l1:
        return l2
    if not l2:
        return l1
    l1.val += l2.val
    if l1.val >= 10:
        l1.next = addTwoNumbers(ListNode(l1.val // 10), l1.next)
        l1.val %= 10
    l1.next = addTwoNumbers(l1.next, l2.next)
    return l1


'''    
def tranlistnode(num: [int], l1: [ListNode]):
    temp = num
    head = l1
    while temp:
        l2 = ListNode(temp%10, l1.next)
        l1.next = l2.next
        temp /= 10
'''

'''
def tranlist(l1):
    res = {}
    i = 0
    while l1:
        res[i] = l1.val
        i += 1
        l1 = l1.next
    return res
'''

if __name__ == '__main__':
    l1 = l2 = res = ListNode()
    num1 = input('first number:')
    num2 = input('second number:')
    tranlistnode(int(num1), l1)
    tranlistnode(int(num2), l2)
    res = addTwoNumbers(l1, l2)
    print(res.val)
    while res:
        print(res.val)
        res = res.next
