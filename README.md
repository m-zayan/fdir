# **fdir**
A fidir is a C optimized module for python provide functions for iterating OS files and directories.<br>
Functions similar to (eg: os. listdir) but much faster.

> # **Module Setup** 
----
``git clone https://github.com/m-zayan/fdir.git``<br>
 Unzip file then open it<br>
 Open terminal (**Linux**) or cmd (**Windows command prompt**)<br>
Type ``python setup.py build && python setup.py install`` 
> # *Modes*

1 - ``./`` Dirctories (Folders) <br>
2 - ``.``  Files <br>
3 - ``.*`` Files with specific extension (eg : ``.csv`` or ``.pdf``)
4 - ``//`` Files and Directories
> # **Module Functions**
----
## **``listdir(str path,str mode)``**<br>
The Function takes two arguments ``path`` and ``mod (1 , 2 , 3 or 4)`` and return List of pathes from given ``path``<br>
> **Ex**
------
```python
import fdir
pathes_list = fdir.listdir(path,'./') # return path of all folders at the current directory as same as (os.listdir)

```

## **``itrAll(list paths,str mode)``**<br>
The Function takes two arguments list of ``paths`` and ``mod (1 , 2 , 3 or 4)`` and return dictionary (str key,list paths)``<br>
> **Ex** 
------
```python
import fdir
sub_files = fdir.itrAll(pathes_list,'./') # return paths of all folders for each path at list

```

## **``itrDict(dict paths,str mode)``**<br>
The Function takes two arguments dictionary of ``paths`` and ``mod (1 , 2 , 3 or 4)`` and return dictionary (str key,dict paths)``<br>
> **Ex** 
------
```python
import fdir
sub_files = fdir.itrAll(sub_files,'.pdf') # return paths of all pdf files for each list of paths at dictionary

```
