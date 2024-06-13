# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>

def get_file_names():
	from argparse import ArgumentParser
	parser = ArgumentParser(
			prog='python boldify.py',
			description='Make the first 3 characters of every word in a file \
					bold',
			epilog='CC0. No rights reserved.')
	parser.add_argument('-if',
				nargs=1,
				metavar='input file',
				dest='infile',
				default=None, 
				help='Specify the full path of the input file')
	parser.add_argument('-of',
				nargs=1,
				metavar='output file',
				dest='outfile',
				default=None,
				help='Specify the full path of the output file') 
	args = parser.parse_args()
	
	if (infile := args.infile) == None:
		exit("***Abort***: No input file specified")
	if (outfile := args.outfile) == None:
		outfile = infile
	
	return (infile, outfile)

def insert_b(string):
 return f"<b>{string[:3]}</b>{string[3:]}"

def boldify_strings(strings):
	return map(insert_b, 
			strings.replace("\n", " ").split(" "));

if __name__ == "__main__":
	infile, outfile = get_file_names()
	infile = open(infile[0], "r")
	outfile = open(outfile[0], "w")
	strings = boldify_strings(infile.read())
	outfile.write(" ".join(strings))
