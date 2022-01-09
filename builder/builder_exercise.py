

class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.parts = [f'class {root_name}:', '  def __init__(self):']

    def add_field(self, type, name):
        self.parts.append(
            f'      self.{type} = {name}'
            )
        return self

    def __str__(self):  
        return '\n'.join(self.parts)

cb = CodeBuilder('Person')\
    .add_field('name','""')\
    .add_field('age', '0')
print(cb)