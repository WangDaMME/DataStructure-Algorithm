class FileNode(object):
    def __init__(self,name,type='dir'):
        self.name=name # 文件名
        self.type=type   #'dir' or 'file'
        self.children=[]
        self.parent=None

    def __repr__(self):
        return self.name

class FileSystemTree(object):
    def __init__(self):
        self.root=FileNode("/")
        self.now=self.root

    def mkdir(self,name):
        if name[-1]!='/':
            name+='/'
        node=FileNode(name)
        self.now.children.append(node)
        node.parent=self.now

    # 展示当前目录下所有目录
    def ls(self):
            return self.now.children

    def cd(self,name):
        if name[-1]!='/':
            name+='/'
        if name=='../':
            self.now= self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now=child
                return

        raise ValueError('invalid dir')


tree=FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
print(tree.ls())
tree.cd('bin/')
tree.mkdir('python/')
print(tree.ls())