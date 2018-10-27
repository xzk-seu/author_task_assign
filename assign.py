import os


if __name__ == '__main__':
    root_dict = {'Engineering': 127413603,
                 'Medicine': 71924100,
                 'Computer Science': 41008148,
                 'Materials Science': 192562407,
                 'Biology': 86803240,
                 'Chemistry': 185592680}
    root_list = [192562407, 127413603, 71924100, 41008148, 86803240, 185592680]
    i = int(input('input 0-5: '))
    root_id = root_list[i]
    path = os.path.join('all', str(root_id))
    total_author = set()
    with open(path, 'r') as fr:
        for line in fr:
            total_author.add(int(line))
    print('total: %d' % len(total_author))

    path = os.path.join('10-23', str(root_id))
    existing = set()
    with open(path, 'r') as fr:
        for line in fr:
            existing.add(int(line))
    print('existing: %d' % len(existing))

    remain = total_author - existing
    if not os.path.exists('new'):
        os.makedirs('new')
    path = os.path.join('new', str(root_id))
    with open(path, 'w') as fw:
        for line in remain:
            fw.write(str(line)+'\n')
    print('remain: %d' % len(remain))
