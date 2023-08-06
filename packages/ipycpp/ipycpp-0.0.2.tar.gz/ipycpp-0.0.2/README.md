# ipycpp
Simple and hackable jupyter kernel for running c++ (c plus plus) codes inside a python notebook.

Rather than providing a true interactive experience, this kernel would just extract the cpp code from the notebook, compile it on the fly and print the result.

Install with:
```
pip install ipycpp
```

The package itself is in pure python, but you have to install a cpp compiler, such as `g++` in order to make it work

## Usage

*Note: you may find a complete example here, [example.ipynb](https://github.com/lucafabbian/ipycpp/blob/main/example.ipynb)*

First, you have to provide some configuration.
- `$$ipycpp_file`: this is the location where your code would be extracted
- `$$ipycpp_build`: this is the command ipycpp should use to compile your code
- `$$ipycpp_run`: this is the command ipycpp should use to compile your code

Create a cell with:
```cpp
// $$ipycpp_file: src/main.cpp
// $$ipycpp_build: g++ src/main.cpp -o bin/main
// $$ipycpp_run: bin/main


/* you may also declare global variables and include directives */

#include <stdio.h>

auto hello = "hello world!";

```

Then, you may add other cells with some shared functions, for example:
```cpp

void printHelloWorld(){
	printf("%s\n", hello);
}

```

Finally, when you want to show some output value, you may declare the usual main function, just remembed to surround it with the special `#ifdef IPYCPP_MAIN` guard

```cpp
#ifdef IPYCPP_MAIN
#define IPYCPP_MAIN_METHOD
int main(){
	printHelloWorld();
}
#endif

```

Keep in mind that the notebook is stateless. Everything will be recompiled EVERY time. If you change a variable inside a main function and then run another cell, the change will be overwritten.


## Special formatting
You may display an image by printing the special tag `$$$ipycppr_image$$$` followed by the image path. For example:
```cpp
printf("$$$ipycppr_image$$$%s\n", "myfolder/myimage.png");
```


## Authors and license

Main author: Luca Fabbian <luca.fabbian.1999@gmail.com>

Freely distributed under MIT license.

Feel free to open a github issue to report bugs or submit feature requests!