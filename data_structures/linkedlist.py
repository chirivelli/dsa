class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def display_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

def has_cycle(node):
    slow, fast = node, node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    # 1 -> 2 -> 3 -> 4
    #      ^_________|

    print(has_cycle(head))

if __name__ == '__main__':
    main()