import json
import os


if __name__ == '__main__':
    root_list = [41008148, 127413603, 71924100, 185592680, 192562407, 86803240]
    for r in root_list:
        path = os.path.join('across_unique', str(r))
        with open(path, 'r') as fr:
            js = json.load(fr)

        print(len(js))
        if not os.path.exists('across_unique_txt'):
            os.makedirs('across_unique_txt')
        path = os.path.join('across_unique_txt', str(r))
        with open(path, 'w') as fw:
            for i in js:
                fw.write(str(i)+'\n')
