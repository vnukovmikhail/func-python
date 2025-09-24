import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    return root

def print_tree(element, level=0):
    print('   ' * level + f'<{element.tag}>')
    for child in element:
        print_tree(child, level + 1)

def find_tag(root, tag_name):
    return root.findall(f'.//{tag_name}')
  
def get_tag_list(elements):
    return [el.text for el in elements if el.text]

def get_depth(element):
    if len(element) == 0:
        return 1
    return 1 + max(get_depth(child) for child in element)

from collections import deque

def get_width(root):
    queue = deque([root])
    max_width = 0

    while queue:
        level_size = len(queue)
        max_width = max(max_width, level_size)
        for _ in range(level_size):
            node = queue.popleft()
            queue.extend(node)
    return max_width

def count_nodes_at_level(root, level):
    queue = deque([(root, 0)])
    count = 0

    while queue:
        node, depth = queue.popleft()
        if depth == level:
            count += 1
        for child in node:
            queue.append((child, depth + 1))
    return count





ACTIONS_LIST = '''
/tree - to look tree of xml
/tagl - find list of tags
/tree_d - get tree depth
/tree_w - get tree width
/count_n - count nodes at level

/exit - to quit
'''

if __name__ == '__main__':
    xml_file = input('Write xml-file name: ')
    try:
        with open(xml_file, 'r', encoding='utf-8') as f:
            xml_data = f.read()
        
        if xml_data:
            root = parse_xml(xml_data)
            while True:
                print(ACTIONS_LIST)
                action = input()

                match action:
                    case '/tree':
                        print('XML Tree:')
                        print_tree(root)
                    case '/tagl':
                        tag = input('Write tag to find: ')
                        print('Tag list:', get_tag_list(find_tag(root, tag)))
                    case '/tree_d':
                        print('Tree depth: ', get_depth(root))
                    case '/tree_w':
                        print('Tree width', get_width(root))
                    case '/count_n':
                        level = int(input('Choose level to search: '))
                        print(f'Nodes count at level {level}:', count_nodes_at_level(root, level))
                    case '/exit':
                        break
                    case _:
                        print('Something going wrong...')
                
                input('[PRESS ENTER FOR NEXT ACTIONS]')
    except FileNotFoundError as e:
        print(e)
