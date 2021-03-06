## **Install** <br>
----

```
$ pip install fdir==1.0
```

## **Modes** <br>
-------
 1 - ``./`` Dirctories (Folders) <br>
 2 - ``.``  Files <br>
 3 - ``.*`` Files with specific extension (eg : ``.csv`` or ``.pdf``)<br>
 4 - ``//`` Files and Directories <br><br>

## **Module Functions**<br>
----
## **``listdir(str path,str mode)``**<br>
The Function takes two arguments ``path`` and ``mode (1 , 2 , 3 or 4)`` <br>
return List of pathes from given ``path``<br>
> **Ex**
------
```python
import fdir
pathes_list = fdir.listdir(path,'./') # return path of all folders at the current directory as same as (os.listdir)

```

## **``itrAll(list paths,str mode)``**<br>
The Function takes two arguments list of ``paths`` and ``mode (1 , 2 , 3 or 4)`` <br>
return dictionary ``(str key,list paths)``<br>
> **Ex** 
------
```python
import fdir
sub_files = fdir.itrAll(pathes_list,'./') # return paths of all folders for each path at list

```

## **``itrDict(dict paths,str mode)``**<br>
The Function takes two arguments dictionary of ``paths`` and ``mode (1 , 2 , 3 or 4)`` <br>
return dictionary ``(str key,dict paths)``<br>
> **Ex** 
------
```python
import fdir
dict_sub_files = fdir.itrDict(sub_files,'.pdf') # return paths of all pdf files for each list of paths at dictionary

```
## **``walk(str paths,str mode)``**<br>
The Function takes two arguments dictionary of ``paths`` and ``mode (1 , 2 , 3 or 4)`` <br>
Recursively iterating through all files from initial path , Return List of all files which match ``mode`` <br>
> **Ex** 
------
```python
import fdir
pdf_files = fdir.walk(path,'.pdf') # return paths of all pdf files.
```
