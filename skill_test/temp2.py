import sys;

class CustomNode:
    def __init__(self, title, parent):
        self.title = title
        self.parent = parent
        self.children = {}
        if parent is not None:
            parent.children[title] = self

    def changeTitle(self, new_title):
        del self.parent.children[self.title]
        self.title = new_title
        if self.parent is not None:
            self.parent.children[self.title] = self

    def find(self, path):
        if path == self.title:
            return self
        # for child in self.children.values():
        #     print(child.title)
        next = self.children[path.split('/')[1]]
        return next.find(path.split('/', 1)[1])

def Main():
    root = CustomNode("Root", None)
    userData = CustomNode("UserData", root)
    ud_browser = CustomNode("Browser", userData)
    ud_word = CustomNode("Word", userData)
    priv = CustomNode("Private", userData)
    priv_word = CustomNode("Word", priv)

    windows = CustomNode("Windows", root)
    programs = CustomNode("Programs", root)
    notepad = CustomNode("Notepad", programs)
    prog_word = CustomNode("Word", programs)
    prog_browser = CustomNode("Browser", programs)

    custom1 = CustomNode("Custom1", root)
    custom2 = CustomNode("Custom2", custom1)
    custom3 = CustomNode("Custom3", custom2)

    RunTests(root, custom1, custom2, custom3);

def TestGetShortestUniqueQualifier(root, targetAbsPath, expected):
    # try:
    output = GetShortestUniqueQualifier(root, root.find(targetAbsPath))
    # except:
    #     output = "exception"

    if output == expected or (expected is None and output == ""):
        print("Succeeded for " + targetAbsPath)
    else:
        print("Failed for " + targetAbsPath + ": Failed with [" + ("" if output is None else output) + "] rather than [" + ("" if expected is None else expected) + "]")

def RunTests(root, custom1, custom2, custom3):

    #They are unique
    TestGetShortestUniqueQualifier(root, "Root", "Root")
    TestGetShortestUniqueQualifier(root, "Root/Programs", "Programs")
    TestGetShortestUniqueQualifier(root, "Root/Programs/Notepad", "Notepad")

    #They have duplicate names
    TestGetShortestUniqueQualifier(root, "Root/Programs/Browser", "Programs/Browser")
    TestGetShortestUniqueQualifier(root, "Root/UserData/Browser", "UserData/Browser")

    #Root has a duplicate name
    # custom
    # custom1.title = "a"
    # custom2.title = "b"
    # custom3.title = "Root"
    custom1.changeTitle("a")
    custom2.changeTitle("b")
    custom3.changeTitle("Root")
    TestGetShortestUniqueQualifier(root, "Root/a/b/Root", "b/Root")

    #Edge cases
    custom1.changeTitle("Root")
    custom2.changeTitle("b")
    custom3.changeTitle("c")
    # custom1.title = "Root"
    # custom2.title = "b"
    # custom3.title = "c"
    TestGetShortestUniqueQualifier(root, "Root/Root", "Root/Root")

    custom1.changeTitle("a")
    custom2.changeTitle("a")
    custom3.changeTitle("a")
    # custom1.title = "a"
    # custom2.title = "a"
    # custom3.title = "a"
    TestGetShortestUniqueQualifier(root, "Root/a", "Root/a")
    TestGetShortestUniqueQualifier(root, "Root/a/a", "Root/a/a")
    TestGetShortestUniqueQualifier(root, "Root/a/a/a", "a/a/a")


    custom1.changeTitle("Root")
    custom2.changeTitle("UserData")
    custom3.changeTitle("Word")
    # custom1.title = "Root"
    # custom2.title = "UserData"
    # custom3.title = "Word"
    TestGetShortestUniqueQualifier(root, "Root/Root/UserData/Word", "Root/Root/UserData/Word")

    TestGetShortestUniqueQualifier(root, "Root", "/Root")
    TestGetShortestUniqueQualifier(root, "Root/UserData/Word", "/Root/UserData/Word")

def traverseTree(root, title):
    candidates = []
    if root:
        for child in root.children.values():
            candidates += traverseTree(child, title)
    if root.title == title:
        candidates += [root]
    return candidates

def getNthParent(node, N):
    for _ in range(N):
        node = node.parent
    return node

def GetShortestUniqueQualifier(root, target):
    #traverse every node of tree, get the ones with the matching title.
    candidates = traverseTree(root, target.title)
    parent_names = []
    i = 0
    while len(candidates) > 1:
        i += 1
        temp_cand = []
        for cand in candidates:
            #get the ith parent name
            p = getNthParent(cand, i)
            if p:
                parent_name = p.title
            else:
                parent_name = ""
            #keep candidacy if name matches
            if getNthParent(target, i):
                if parent_name == getNthParent(target, i).title:
                    temp_cand += [cand]
            elif parent_name == "":
                temp_cand = [cand]
        candidates = temp_cand
    names = [target.title]
    for j in range(i):
        parent = getNthParent(candidates[0], j+1)
        if parent:
            names = [parent.title] + names
    return "/".join(names)


Main()


Failed for Root: Failed with [exception] rather than [Root]
Failed for Root/Programs: Failed with [exception] rather than [Programs]
Failed for Root/Programs/Notepad: Failed with [exception] rather than [Notepad]
Failed for Root/Programs/Browser: Failed with [exception] rather than [Programs/Browser]
Failed for Root/UserData/Browser: Failed with [exception] rather than [UserData/Browser]
Failed for Root/a/b/Root: Failed with [exception] rather than [b/Root]
Failed for Root/Root: Failed with [exception] rather than [Root/Root]
Failed for Root/a: Failed with [exception] rather than [Root/a]
Failed for Root/a/a: Failed with [exception] rather than [Root/a/a]
Failed for Root/a/a/a: Failed with [exception] rather than [a/a/a]
Failed for Root/Root/UserData/Word: Failed with [exception] rather than [Root/Root/UserData/Word]
Failed for Root: Failed with [exception] rather than [/Root]
Failed for Root/UserData/Word: Failed with [exception] rather than [/Root/UserData/Word]
