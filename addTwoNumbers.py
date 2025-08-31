class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Empty function body (to be implemented later)
    firstList = []
    secondList = []
    while l1:
        firstList.append(l1.val)
        l1 = l1.next
    while l2:
        secondList.append(l2.val)
        l2 = l2.next

    firstList = firstList[::-1]
    secondList = secondList[::-1]
    print(firstList)
    print(secondList)
    firstNum = int("".join(map(str,firstList)))
    secondNum = int("".join(map(str,secondList)))
    finalSum = firstNum + secondNum
    finalList = list(map(int,str(finalSum)))
    finalList = finalList[::-1]
    sumList = ListNode(finalList[0])
    current = sumList
    for item in finalList[1:]:
        current.next = ListNode(item)
        current = current.next
    return sumList

# -------- Create linked lists --------
# First number: 342 → stored as 2 -> 4 -> 3
l1 = ListNode(2, ListNode(4, ListNode(3)))

# Second number: 465 → stored as 5 -> 6 -> 4
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Pass to function
result = addTwoNumbers(l1, l2)