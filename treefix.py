from sqlalchemy import *

db = create_engine('mysql://redmine:redmine@localhost/redmine_test')

metadata = MetaData(db)

issues = Table('issues', metadata,
    Column('id', Integer, primary_key=True),
    Column('parent_id', Integer),
    Column('root_id', Integer),
    Column('lft', Integer),
    Column('rgt', Integer)
)

iss = issues.select().execute()

for i in iss:
    n = Node()
    n.id = i.id
    n.parent_id = i.parent_id
    n.root_id = i.root_id
    n.lft = i.lft
    n.rgt = i.rgt
    nodes[i.id] = n



nodes = {}

def walk_children(node, c):
    c += 1
    node.lft = c
    for child in node.children():
        c = walk_children(child, c=c)
    c += 1
    node.rgt = c
    return c


class Node():
    
    def children(self):
        cs = []
        # troche nieladne, ale trudno
        for ch in nodes.values():
            if ch.parent_id == self.id:
                cs.append(ch)
        
        return cs

    


for node in nodes.values():
    if node.parent_id is None: # root
        walk_children(node, c=0)


for node in nodes.values():
    print node.id, node.lft, node.rgt

    issues.update().where(issues.c.id==node.id).values(lft=node.lft, rgt=node.rgt).execute()

