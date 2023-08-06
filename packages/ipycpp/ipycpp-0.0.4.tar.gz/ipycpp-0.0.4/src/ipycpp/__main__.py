from ipykernel.kernelbase import Kernel
import subprocess, traceback

import asyncio
from asyncio.subprocess import PIPE
from asyncio import subprocess


async def _read_stream(stream, callback):
    while True:
        line = await stream.readline()
        if line: callback(line)
        else: break


async def run(command, stdoutcallback, stderrcallback):
    process = await subprocess.create_subprocess_shell(
        command, stdout=PIPE, stderr=PIPE
    )
    await asyncio.wait(
        [
            _read_stream(process.stdout, stdoutcallback),
            _read_stream(process.stderr, stderrcallback),
        ]
    )
    await process.wait()




emptymain= """
#ifndef IPYCPP_MAIN_METHOD
int main(){ return 0;}
#endif
"""


def find_option(code, option_name):
	# find option in code
	option = None
	option_index = code.find(option_name)
	if option_index != -1:
		option = code[option_index + len(option_name):]
		option = option[:option.index('\n')].strip()
	return option


class CppKernel(Kernel):
	implementation = 'ipycpp'
	implementation_version = '1.0'
	language = 'cpp'
	language_version = '0.1'
	language_info = {
		'name': 'cpp',
		'mimetype': 'text/x-c',
		'file_extension': '.cpp',
	}
	banner = "Custom c++ kernel made by Luca Fabbian"


	known_cells = {}
	stack = []

	def send_error(self, text):
		stream_content = {'name': 'stderr', 'text': '\033[0;31m' + text + '\033[0m'}
		self.send_response(self.iopub_socket, 'stream', stream_content)

		return {'status': 'error',
			'execution_count': self.execution_count,
		}


	async def do_execute(self, code, silent, store_history=True, user_expressions=None,
		allow_stdin=False, *, cell_id=None):
		try:
			ipycpp_options = {
				"ipycpp_file": None,
				"ipycpp_build": None,
				"ipycpp_run": None,
			}

			# remove cell and following from stack
			if cell_id in self.stack:
				self.stack = self.stack[:self.stack.index(cell_id)]

			# iterate over options
			for option in ipycpp_options:
				# find option in previous stack entries
				for cell in self.stack:
					option_value = find_option(self.known_cells[cell], "$$" + option + ":")
					if option_value:
						ipycpp_options[option] = option_value

				# find option in code
				option_value = find_option(code, "$$" + option + ":")
				if option_value:
					ipycpp_options[option] = option_value

			# generate total code by stacking all cells
			totalcode = "#define IPYCPP\n"
			for cell in self.stack:
				totalcode += self.known_cells[cell] + "\n"
			totalcode += "#define IPYCPP_MAIN\n" + code + "\n#undef IPYCPP_MAIN\n" + emptymain

			# return error if no file is specified
			if not ipycpp_options["ipycpp_file"]:
				return self.send_error("No file specified\n"
			   +	"Specify a file with $$ipycpp_file: <file> (e.g. $$ipycpp_file: main.cpp)")
			
			# return error if no build or run command is specified
			if not ipycpp_options["ipycpp_build"] and not ipycpp_options["ipycpp_run"]:
				return self.send_error("No build or run command specified\n"
			  	+ "Either specify a build command with $$ipycpp_build: or a run command with $$ipycpp_run:\n"
					+ "e.g. $$ipycpp_build: g++ -o main main.cpp\n")
				

			# write code to file
			with open(ipycpp_options["ipycpp_file"], 'w') as f:
				f.write(totalcode)

			commands = []
			if(ipycpp_options["ipycpp_build"]):
				commands.append(ipycpp_options["ipycpp_build"])
			
			if(ipycpp_options["ipycpp_run"]):
				commands.append(ipycpp_options["ipycpp_run"])

			self.is_html_mode = False
			self.html_text = ""
			self.is_special_output_disabled = False


			def send_stdout(x):
				text = x.decode("UTF8")
				if self.is_special_output_disabled:
					self.send_response(self.iopub_socket, 'stream', {'name': 'stdout', 'text':  text})
					return
				
				if "$$$ipycppr_disable_special_output$$$" in text:
					self.is_special_output_disabled = True
					return

				if self.is_html_mode:
					if "$$$ipycppr_html_end$$$" in text:
						self.is_html_mode = False
						content = {
							'source': 'kernel',
							'data': {
								'text/html': self.html_text
							},
							'metadata' : {
								'text/html' : {
								}
							}
						}
						self.send_response(self.iopub_socket, 'display_data', content)
					else:
						self.html_text += text
					return

					

				if "$$$ipycppr_html_start$$$" in text:

					self.is_html_mode = True
					self.html_text = ""
					return

				if "$$$ipycppr_image$$$" in text:
					image_path = text[text.index("$$$ipycppr_image$$$") + len("$$$ipycppr_image$$$"):].strip()
					with open(image_path, mode="rb") as png:
						content = {
							'source': 'kernel',
							'data': {
								'image/png': png.read()
							},
							'metadata' : {
								'image/png' : {
								}
							}
						}
						self.send_response(self.iopub_socket, 'display_data', content)
					return

				self.send_response(self.iopub_socket, 'stream', {'name': 'stdout', 'text':  text})

			await run( " && ".join(commands), 
							send_stdout,
							lambda x: print(self.send_response(self.iopub_socket, 'stream', {'name': 'stderr', 'text':  '\033[0;31m' + x.decode("UTF8") + '\033[0m'})),
					)
			
			# store code
			self.known_cells[cell_id] = code
			self.stack.append(cell_id)
			
			return {'status': 'ok',
					'execution_count': self.execution_count,
			}
	
		except Exception as ex:
			return self.send_error(''.join(traceback.TracebackException.from_exception(ex).format()))



if __name__ == '__main__':
	from ipykernel.kernelapp import IPKernelApp
	IPKernelApp.launch_instance(kernel_class=CppKernel)
