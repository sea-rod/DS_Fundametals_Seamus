from linked_list import LinkedList

def find_middle_element(linklist):
    slow = linklist
    fast = linklist

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


if "__main__" == __name__:
    linklist = LinkedList()
    linklist.append(1)
    linklist.append(2)
    linklist.append(3)
    linklist.append(4)
    linklist.append(5)
    linklist.append(6)
    linklist.append(7)

    print(find_middle_element(linklist.head).val)

