class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    queue = [self.root]

    while queue:
      curr = queue.pop(0)
      if curr['id'] == id: return curr
      for node in curr['children']:
        queue.append(node)
    
    return None