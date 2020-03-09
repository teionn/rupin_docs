# Install
Copy the entire `rupin` folder to`Documents/maya/scripts` or `Documents/maya/<version>/scripts`.

# Run
Execute the following command in `python` or drag and drop` rupin.mel` to launch the tool.

### mel
`rupin.mel`をMayaにドラッグアンドドロップします。

### command-line
```python
from rupin import rupin
rupin.run_maya()
```

# Option

### GUI
- [x] Remove unknown nodes used
    - If you check this box, you can delete unknown nodes that are used forcibly and cannot be deleted.

### command-line

#####
- [x] Remove unknown nodes used
    - The GUI can be started with `Remove unknown nodes used` checked.
```python
from rupin import rupin
rupin.run_maya(force=True)
```

##### Force removal of unknown nodes.
```python
rupin.forceRemoveUnknownNode()
```

##### Force removal of unknown plugins.
```python
rupin.forceRemoveUnknownPlugin()
```
