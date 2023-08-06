import random


class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class PyLinkList():
    def __init__(self, data=None, length=None, reverse=False):
        self.data = data
        self.length = length
        self.reverse = reverse

    def _limit_length(self, data):  # 长度限制
        if len(data) > 10000:
            raise "The length of data cannot exceed 10000."

    def generate_single_with_headnode(self):
        """
            生成带头结点的单向链表。
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
        if self.data:
            if self.reverse:
                print('将data反转')
                self._limit_length(self.data)

                root = Node(val=None, next=None)  # 生成头节点

                for i in self.data:
                    node = Node(val=i, next=None)
                    node.next = root.next
                    root.next = node
                return root
            else:
                print('生成data')
                self._limit_length(self.data)

                root = Node(val=None, next=None)  # 生成头节点
                data_reverse = self.data.copy()  # 先反转data，再用"头插法"构造链表
                data_reverse.reverse()

                for i in data_reverse:
                    node = Node(val=i, next=None)
                    node.next = root.next
                    root.next = node
                return root
        elif self.data == []:
            print('欲构造空链表')
            root = Node(val=None, next=None)
            return root
        elif self.length:
            print('生成length的随机数链表')
            if self.length > 10000:
                raise "The length of data cannot exceed 10000."
            root = Node(val=None, next=None)
            count = 1
            while count != self.length:
                node = Node(val=random.randint(0, 200), next=None)
                node.next = root.next
                root.next = node
                count += 1
            return root
        else:
            print('全随机')
            root = Node(val=None, next=None)  # 生成头节点
            self.length = random.randint(0, 10)  # 长度为0~10
            if not self.length:
                return root, self.length

            count = 1
            while count != self.length:
                node = Node(val=random.randint(0, 200), next=None)  # 数值为0~200
                node.next = root.next
                root.next = node
                count += 1
            return root, self.length - 1

    def generate_single_with_no_headnode(self):  # 不带头节点的单向链表
        if self.data:
            if self.reverse:
                print('将data反转')
                self._limit_length(self.data)

                root = Node(val=None, next=None)  # 生成头节点

                for i in self.data:
                    node = Node(val=i, next=None)
                    node.next = root.next
                    root.next = node
                return root.next
            else:
                print('生成data')
                self._limit_length(self.data)

                root = Node(val=None, next=None)  # 生成头节点
                data_reverse = self.data.copy()  # 先反转data，再用"头插法"构造链表
                data_reverse.reverse()

                for i in data_reverse:
                    node = Node(val=i, next=None)
                    node.next = root.next
                    root.next = node
                return root.next
        elif self.data == []:
            print('欲构造空链表')
            root = Node(val=None, next=None)
            return root
        elif self.length:
            print('生成length的随机数链表')
            if self.length > 10000:
                raise "The length of data cannot exceed 10000."
            root = Node(val=None, next=None)
            count = 1
            while count != self.length:
                node = Node(val=random.randint(0, 200), next=None)
                node.next = root.next
                root.next = node
                count += 1
            return root.next
        else:
            print('全随机')
            root = Node(val=None, next=None)  # 生成头节点
            self.length = random.randint(0, 10)  # 长度为0~10
            if not self.length:
                return root.next, self.length

            count = 1
            while count != self.length:
                node = Node(val=random.randint(0, 200), next=None)  # 数值为0~200
                node.next = root.next
                root.next = node
                count += 1
            return root.next, self.length - 1


def print_link_list(root: Node, have_head=True):
    # 打印链表，默认有头节点
    if have_head:
        while root.next:
            root = root.next
            print(root.val)
    else:
        while root:
            print(root.val)
            root = root.next


def pprint_link_list(root: Node, have_head=True):
    # 按->的方式打印链表，其输出在一行，默认有头节点
    if have_head:
        while root.next:
            root = root.next
            # 控制`->`的输出
            if root.next:
                print(root.val, end="->")
            else:
                print(root.val)
    else:
        while root:
            if root.next:
                print(root.val, end="->")
                # 控制`->`的输出
            else:
                print(root.val)
            root = root.next


def get_length(root: Node, have_head=True):
    # 获取链表长度，默认有头节点，头节点不计入长度
    count = 0
    if have_head:
        while root.next:
            root = root.next
            count += 1
        return count
    else:
        while root:
            count += 1
            root = root.next
        return count


pylinklist = PyLinkList(data=[1, 2, 3, 4, 5])
a = pylinklist.generate_single_with_no_headnode()
print_link_list(a)
pprint_link_list(a, have_head=False)
print(get_length(a))
