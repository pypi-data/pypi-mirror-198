import random


class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def generate(data=[], length=None, reverse=False):
    """
        生成链表。
        参数：
            data:
                type: list
                作为生成链表的数据，根据参数`reverse`是否为True决定是否反转。
                默认为空，随机生成1~10个以内的值为0~200的数据。
            length:
                type: int
                生成链表的长度，若传入`data`，则`length`自动获得，传入的数值无效。
                若不传入`data`，则需要两个接收值，一个是头节点，另一个是长度
                范围：0~10000
            reverse:
                type: bool
                为True则反转`data`的顺序，默认为False。
                若不传入`data`，则此参数无效。
    :return: 链表头
    """
    if data and reverse:  # 给出data，并要求反转
        print("data and reverse")
        if len(data) > 10000:
            raise "The length of data cannot exceed 10000."
        root = Node(val=-1, next=None)  # 生成头节点
        for i in data:
            node = Node(val=i, next=None)
            node.next = root.next
            root.next = node
        return root
    elif data:  # 给出data，不反转
        print("data")
        if len(data) > 10000:
            raise "The length of data cannot exceed 10000."
        root = Node(val=-1, next=None)  # 生成头节点
        data_reverse = data.copy()  # 先反转data，再构造链表
        data_reverse.reverse()
        for i in data_reverse:
            node = Node(val=i, next=None)
            node.next = root.next
            root.next = node
        return root
    elif (not data) and (not length):  # 没有data，并不指定长度，则随机生成，reverse无效，需要两个接收值
        print("(not data) and (not length)")
        root = Node(val=-1, next=None)  # 生成头节点
        length_ = random.randint(0, 10)  # 长度为0~10
        if not length_:
            return root, length_
        count = 1
        while count != length_:
            node = Node(val=random.randint(0, 200), next=None)  # 数值为0~200
            node.next = root.next
            root.next = node
            count += 1
        return root, length_ - 1
    elif (not data) and length:  # 没有`data`，指定长度
        print("(not data) and length")
        if length > 10000:
            raise "The generated linked list cannot exceed 10000 in length."
        root = Node(val=-1, next=None)  # 生成头节点
        if not length:  # 长度为0
            return root
        count = 1
        while count != length:
            node = Node(val=random.randint(0, 200), next=None)  # 数值为0~200
            node.next = root.next
            root.next = node
            count += 1
        return root
    return -1


def print_link_list(root: Node):
    while root.next:
        root = root.next
        print(root.val)


def pprint_link_list(root: Node):
    """
        按->的方式打印链表，其输出在一行
    """
    while root.next:
        root = root.next
        # 控制`->`的输出
        if root.next:
            print(root.val, end="->")
        else:
            print(root.val)


def get_length(root: Node):
    count = 0
    while root.next:
        root = root.next
        count += 1
    return count


a, l = generate(data=[])
print_link_list(a)
pprint_link_list(a)
print(get_length(a))
