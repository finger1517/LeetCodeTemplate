class Node():
    def __init__(self, val):
        self.val = val
        self.isLocked = False
        self.lockedBy = None
        self.parent = None
        self.children = []

class LockingTree:

    def __init__(self, parent: List[int]):
        self.Nodes = [Node(i) for i in range(len(parent)+1)]
        for i,p in enumerate(parent):
            self.Nodes[i].parent = p
            self.Nodes[p].children.append((i))


    def lock(self, num: int, user: int) -> bool:
        if self.Nodes[num].isLocked:
            return False
        self.Nodes[num].isLocked = True
        self.Nodes[num].lockedBy = user
        return True


    def unlock(self, num: int, user: int) -> bool:
        if not self.Nodes[num].isLocked:
            return False
        if self.Nodes[num].lockedBy != user:
            return False
        self.Nodes[num].isLocked = False
        self.Nodes[num].lockedBy = None
        return True


    def upgrade(self, num: int, user: int) -> bool:
        if self.Nodes[num].isLocked:
            return False
        lockedDescendant = False
        lockedAncestors = False

        def checkAncestor(x:int):
            if x==-1:
                return
            nonlocal lockedAncestors
            if self.Nodes[x].isLocked:
                lockedAncestors = True
                return
            if not lockedAncestors:
                checkAncestor(self.Nodes[x].parent)
        def checkDe(x: int):
            nonlocal lockedDescendant
            if self.Nodes[x].isLocked:
                lockedDescendant = True
                return
            for child in self.Nodes[x].children:
                not lockedDescendant and checkDe(child)
        def unlock(x):
            self.Nodes[x].isLocked = False
            self.Nodes[x].lockedBy = None
            for child in self.Nodes[x].children:
                unlock(child)
        
        checkAncestor(num)
        if lockedAncestors: return False

        checkDe(num)
        if not lockedDescendant: return False

        unlock(num)
        self.Nodes[num].isLocked = True
        self.Nodes[num].lockedBy = user

        return True

        

        




# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)