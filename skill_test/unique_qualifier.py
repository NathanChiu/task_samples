import sys;

class CustomNode:
    def __init__(self, title, parent):
        self.title = title
        self.parent = parent
        self.children = {}
        if parent is not None:
            parent.children[title] = self

    def find(self, path):
        if path == self.title:
            return self
        next = self.children[path.split('/')[1]]
        return next.find(path.split('/', 1)[1])

def main():
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

    # custom1 = CustomNode('Custom1', root)
    # custom2 = CustomNode('Custom2', custom1)
    # custom3 = CustomNode('Custom3', custom2)
    custom1 = CustomNode('Root', root)
    custom2 = CustomNode('b', custom1)
    custom3 = CustomNode('c', custom2)
    # custom1 = CustomNode('a', root)
    # custom2 = CustomNode('b', custom1)
    # custom3 = CustomNode('Root', custom2)
    # target = root.find('Root/Programs/Notepad')
    # target = root.find('Root/Programs/Word')
    # target = root.find('Root/a/b/Root')
    target = root.find('Root/Root')
    # target = root.find('Root/UserData/Private/Word')
    # target = root.find('Root/Programs/Browser')
    print(getShortestUniqueQualifier(root, target))
    # print(programs.find('Programs/Word').title)
    # sys.stdout.write(getShortestUniqueQualifier(root, target))

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

def getShortestUniqueQualifier(root, target):
    #traverse every node of tree, get the ones with the matching title.
    candidates = traverseTree(root, target.title)
    parent_names = []
    i = 0
    while len(candidates) > 1:
        i += 1
        # print(i)
        temp_cand = []
        for cand in candidates:
            #get the ith parent name
            p = getNthParent(cand, i)
            if p:
                parent_name = p.title
            #keep candidacy if name matches
                if parent_name == getNthParent(target, i).title:
                    temp_cand += [cand]
        candidates = temp_cand
    names = [target.title]
    for j in range(i):
        parent = getNthParent(candidates[0], j+1)
        names = [parent.title] + names
    return "/".join(names)
    # return ""
# def getShortestUniqueQualifier(root, target):
#     #first find all nodes that match the title.
#     candidates = getCandidates(root, target)
#     return target.title
#     # return ;

main()

#
# Succeeded for Root
# Succeeded for Root/Programs
# Succeeded for Root/Programs/Notepad
# 1
# Succeeded for Root/Programs/Browser
# 1
# Succeeded for Root/UserData/Browser
# Failed for Root/a/b/Root: Failed with [exception] rather than [b/Root]
# Failed for Root/Root: Failed with [exception] rather than [Root/Root]
# Failed for Root/a: Failed with [exception] rather than [Root/a]
# Failed for Root/a/a: Failed with [exception] rather than [Root/a/a]
# Failed for Root/a/a/a: Failed with [exception] rather than [a/a/a]
# Failed for Root/Root/UserData/Word: Failed with [exception] rather than [Root/Root/UserData/Word]
# Failed for Root: Failed with [Root] rather than [/Root]
# 1
# Failed for Root/UserData/Word: Failed with [UserData/Word] rather than [/Root/UserData/Word]
