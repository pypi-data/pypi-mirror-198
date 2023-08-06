# ipycpp
Simple and hackable jupyter kernel for running c++ (c plus plus) codes inside a python notebook.

Rather than providing a true interactive experience, this kernel would just extract the cpp code from the notebook, compile it on the fly and print the result. It is meant as a drop-in replacement for your main cpp file.

Install with:
```
pip install ipycpp
```

The package itself is in pure python, and will just call the cpp compiler already installed in your system. Of course, you have to provide a suitable cpp compiler, such as `g++` in order to make it work. Advanced build tools such as `make` should work as well.

## Motivation
Other packages, such as `xeus-cling` provide a better interactive experience when working with cpp, yet they introduce a lot of magic behind the scene. While developing algorithms with `cpp`, you usually care more about speed and low level control. This package guarantees no overhead - it just transpiles your notebook into a plain `.cpp` file: you may even check the result by yourself. Moreover, since this package is just a ~300lines pure python script, it's way easier to setup.

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
You may provide non-textual data to the notebook, such as html or images, by printing some special tags. This feature is enabled by default, and let you create interactive notebooks.

### disable
To disable any kind of special data for the rest of the cell, just print `$$$ipycppr_disable_special_output$$$` at the beginning of your main.

For example:
```cpp
printf("$$$ipycppr_disable_special_output$$$\n");
```
In this way, you will be sure that any further output will be printed "as is".

### images
You may display an image by printing the special tag `$$$ipycppr_image$$$` followed by the image path. For example:
```cpp
printf("$$$ipycppr_image$$$%s\n", "myfolder/myimage.png");
```

### html
Mark html regions with `$$$ipycppr_html_start$$$` and `$$$ipycppr_html_end$$$` (newline required). You may also add some javascript logic to create interactive widgets.

Basic example:
```cpp
printf("$$$ipycppr_html_start$$$\n%s\n$$$ipycppr_html_end$$$\n", "<b>some bold text</b>");
```

Advanced example (this will create an interactive widget using the [PetiteVue library](https://github.com/vuejs/petite-vue); the widget will display a number and two buttons to increment or decrement it):
```cpp
auto html = R""""(

<div class="widgetcontainer">
	<div class="widget" v-scope="{ count: 0 }">
		<button @click="count--">-</button>
		{{ count }}
		<button @click="count++">+</button>
	</div>

	<script>
	if(!window.INSTALL_PETITE_VUE){
		let resolve = null;
		window.INSTALL_PETITE_VUE = new Promise(r => resolve = r);
		var script = document.createElement('script');
		script.src = 'https://unpkg.com/petite-vue';
		script.onload = resolve;
		document.head.appendChild(script);
	}

	{
		// get current element right now, and mount it as soon as petite-vue is loaded
		let element = document.currentScript.previousElementSibling;
		window.INSTALL_PETITE_VUE.then(() => PetiteVue.createApp().mount(element));
	}

	</script>
</div>
)"""";

#ifdef IPYCPP_MAIN
#define IPYCPP_MAIN_METHOD
int main(){
	printf("$$$ipycppr_html_start$$$\n%s\n$$$ipycppr_html_end$$$\n", html);
}
#endif
```


## Authors and license

Main author: Luca Fabbian <luca.fabbian.1999@gmail.com>

Freely distributed under MIT license.

Feel free to open a github issue to report bugs or submit feature requests!