# shutil_extra
extra utils

# Usage

## dirtree
```python
from shutil_extra.dirtree import generate_dirtree

tree_cnf = f'''
folder1
    folder2_1,folder2_2
        folder3_1->folder4
        folder3_2->folder4->folder5_1,folder5_2
        folder3_3->folder4
        folder3_4->folder4
'''
generate_dirtree('./folder_tree', tree_cnf)
```