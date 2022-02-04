import os
from shutil import copytree, rmtree

root_dir = os.path.join(os.getcwd(), 'my_project')
for root, dirs, files in os.walk(root_dir):
    if root.split('/')[-2] == 'templates':
        r = root
        copytree(root, os.path.join(root_dir, 'templates', root.split('/')[-1]))
        # далее идет блок кода, если исходные папки и файлы необходимо удалить
        rmtree("/".join(root.split('/')[:-1]))
