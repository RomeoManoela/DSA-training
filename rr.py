from collections import deque

from Problems.LinkedList.reverse import LinkedList


def areAlmostEqual( s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    nbr = []
    if s1 == s2:
        return True
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            nbr.append(i)
        if len(nbr) != 2:
            return False
    i, j = nbr[0], nbr[1]
    s = list(s2)
    s[i], s[j] = s[j], s[i]
    s2 = ''.join(s)
    if s2 == s1:
        return True
    return False

print(areAlmostEqual("aac", "aab"))


def addTwoNumbers( l1: LinkedList, l2: LinkedList ) -> LinkedList:
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    l1_dq = deque()
    l1_tmp = l1.head
    while l1_tmp is not None:
        l1_dq.appendleft(l1_tmp.data)
    sum_l1 = int(''.join(map(str, l1_dq)))

    l2_dq = deque()
    l2_tmp = l2.head
    while l2_tmp is not None:
        l1_dq.appendleft(l2_tmp.data)
    sum_l2 = int(''.join(map(str, l2_dq)))
    sum = sum_l1 + sum_l2
    l = [int(nbr) for nbr in str(sum)]
    ll: LinkedList = LinkedList(l[0])
    for n in l:





