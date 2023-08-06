# CSTL : The C++ Standard Template Library (STL) for Python

In the `CSTL` tool, we wrap several C++ STL containers for use in Python. The containers use native C++ implementation and will not have the Copy on write problem like native `list`, `dict` in Python.

## Install
Install from `pip`:
```
pip install CSTL
```
Build from source:
```
git clone https://github.com/fuzihaofzh/CSTL
cd CSTL
./build.sh
python setup.py install
```

## Usage 
```python
import CSTL
vec = CSTL.VecInt([1,2,3,4,5,6,7])
print(vec[2])      #3
vec[2] = 1
print(vec[2])      #1
vec.append(10)
print(vec[-1])     #10
print(list(vec))   #[1, 2, 1, 4, 5, 6, 7, 10]
```

## Supported Datatype

We support the following data types as the elements in the containers
|Python Type|C++ Type| Can be dict key|
|---|---|---|
|int|int|Yes|
|int|std::int64|Yes|
|str|std::string|Yes|
|float|float|No|
|double|double|No|
|bool|bool|No|

## Supported Containers
The supported containers are listed as follows
|Python Structure|C++ Container| 
|---|---|
|list|std::vector|
|dict|std::unordered_map|
|set|std::unordered_set|

We also support nested container, namely, structure like `std::unordered_map< std::string,std::unordered_map< std::string,std::vector< bool > > >` is supported. Currently, at most 3 nested layers are supported.






