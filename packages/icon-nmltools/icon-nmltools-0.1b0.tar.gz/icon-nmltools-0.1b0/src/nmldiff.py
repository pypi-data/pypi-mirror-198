#!/usr/bin/python3
import f90nml
import argparse
import re

#global settings
#wspace for the namelist parameter names
paramspace = 36
#wspace for the values
valspace = 24
#indent after the group name
indent = " "*2
#whitespace between columns
wspace = " "*2
#seperator symbol between columns
separator = "|"

#namelists to ignore in display and comparison
ignorenmls = ['output_nml', 'meteogram_output_nml']

#helper functions

def get_defaults_from_logfile(logfile):
    #Returns the default namelist values as a dictionary derived from the icon namelist logfile
    
    #indentation of the namelist values in the logfile
    indval = 48
    
    def convert_to_value(strvals):
        #converts the string namelist value into (a list of) propper types
        #first split by comma
        #this function will fail if there are commas inside a string
        strvals = re.split(', ', strvals)
        vals = []
        for strval in strvals:
            #check for repetition and get the number of repetitions
            if '*' in strval:
                n = int(re.split('\*', strval)[0])
                strval = re.split('\*', strval)[1]
            else:
                n = 1
            #check for bool
            if strval.startswith('T'):
                val = True
            elif strval.startswith('F'):
                val = False
            #check for string
            elif strval.startswith("'"):
                idx = strval.rfind("'")
                val = trim_str(strval[1:idx])
            #set to int of float
            elif '.' in strval or 'E' in strval:
                val = float(strval)
            else:
                val = int(strval)
            vals += [val]*n
        if len(vals)==1:
            vals = vals[0]
        return vals
           
    nmldef = {}
    
    for line in open(logfile):
        #does the line specify the start of a namelist
        if re.fullmatch('NAMELIST [A-Z,_]*\n', line):
            namelist = line.replace('NAMELIST ', '').replace(' ', '').replace('\n', '').lower()
            nmldef[namelist] = {}
        #check if a namelist parameter is specified by checking for 4 whitespaces followed by one non-whitespace
        elif re.match('    [A-Z]', line):
            parameter = re.split(" +", line[4:])[0].lower()
            vals = convert_to_value(line[indval:].replace('\n', ''))
            nmldef[namelist][parameter] = vals
        elif re.match(' *>> DEFAULT: ', line):
            #overwrite with the default if specified
            vals = convert_to_value(line[indval+12:])
            nmldef[namelist][parameter] = vals
            
    return nmldef


def trim_str(string):
    #remove trailing whitespaces, including the [...] if it is precided by whitespaces
    if string.endswith('  [...]'):
        string = string[:-6]
    while len(string)>0 and string[-1]==" ":
        string = string[:-1]
    return string


def values_equal(v1, v2, df, listidx):
    #checks if values v1 and v2 are considered identical. Depends on the existence of a default and on settings for comparing lists
    #if default is given, replace None values with the default
    if df is not None:
        if v1 is None:
            v1 = df
        if v2 is None:
            v2 = df
    #if one or both objects are a list: special treatment
    if isinstance(v1, list) or isinstance(v2, list):
        #convert single values to list
        if not isinstance(v1, list):
            v1 = [v1]
        if not isinstance(v2, list):
            v2 = [v2]
        #as a default compare only elements of the shorter list
        if listidx is None:
            for i in range(min(len(v1), len(v2))):
               if v1[i]!=v2[i]:
                return False
            return True 
        #only compare a specific element
        elif re.fullmatch('[0-9]', listidx):
            idx = int(listidx)
            try:
                eq = v1[idx]==v2[idx]
            except IndexError:
                return False
            return eq
        #compare all elements one by one
        elif listidx == 'a':
            if len(v1)!=len(v2):
                return False
            for i in range(len(v1)):
                if v1[i]!=v2[i]:
                    return False
            return True
    #compare non-list values
    else:
        return v1==v2
      
def add_style(string, style, use_colors):
    #Adds fontstyle and color tags to the string. style='n' (normal), 'e' (emphasize), 'd' (deemphasize)
    
    #define the emphasizie and non-emphasize tags according to color setting
    if use_colors:
        #bold red
        estr = "\033[1;91m"
        #italic gray
        nestr = "\033[3;90m"
    else:
        #bold
        estr = "\033[1m"
        #italic
        nestr = "\033[3m"
    
    #emphasize
    if style=='e':
        return estr + string + "\033[0m"
    #deemphasize
    elif style=='d':
        return nestr + string + "\033[0m"
    #nothing
    else:
        return string


def print_line(param, v1, v2, df=None, style=None, use_colors=False):
    #prints a line with namelist parameters
    #replace style with default style (n: normal)
    if style is None:
        style = {0: 'n', 1: 'n', 2: 'n'}
    #default always normal
    style[3] = 'n'
    paramstr = add_style(param.ljust(paramspace)[:paramspace], style[0], use_colors)
    line = indent + paramstr + wspace
    for iv, v in enumerate([v1, v2] if df is None else [v1, v2, df]):
        if iv>0:
            #put in separator
            line += wspace + separator + wspace
        if isinstance(v, str):
            vstr = ("'"+v+"'").ljust(valspace)
        else:
            vstr = str(v).ljust(valspace)
        if len(vstr)>valspace:
            if isinstance(v, str):
                vstr = vstr[:valspace-4] + "...'"
            else:
                vstr = vstr[:valspace-3] + "..."
        line += add_style(vstr, style[iv+1], use_colors)
    print(line)

#main function
def nmldiff(args):
    nmls = {1: f90nml.read(args.file1), 2:f90nml.read(args.file2)}
    
    #read defaults
    if args.defaults is not None:
        defaults = get_defaults_from_logfile(args.defaults)
    else:
        defaults = None
    
    
    
    #get all namelist that are given in the two files
    namelists = sorted(list(set(list(nmls[1].keys())+list(nmls[2].keys()))))
    
    #by default remove output and meteogram namelists
    for inml in ignorenmls:
        if inml in namelists:
            namelists.remove(inml)
        
    #dictionary to store the given values of both namelists and the default
    nmldict = {namelist: {} for namelist in namelists}
    
    #store the given values in the dictionary
    for namelist in namelists:
        
        #get all mentioned parameters in the namelist in any file
        params = []
        for i, nml in nmls.items():
            try:
                params += sorted(list(set(list(nml[namelist].keys()))))
            except KeyError:
                pass
        params = sorted(list(set(params)))
        
        #get the specified values
        for param in params:
            if args.ignorepaths and ('path' in param or 'file' in param):
                continue
            p = {}
            for i in [1, 2]:
                #get the value, replace with None if not given
                try:
                    p[i] = nmls[i][namelist][param]
                except KeyError:
                    p[i] = None
                if isinstance(p[i], str):
                    p[i] = trim_str(p[i])
            #store in dictionary, together with default (None if not given)
            if defaults is None:
                nmldict[namelist][param] = (p[1], p[2], None)
            else:
                nmldict[namelist][param] = (p[1], p[2], defaults[namelist][param])
                
    #print table header
    header = "\n" + " "*paramspace + indent + wspace + "Namelist-1 value".ljust(valspace) + wspace + separator + wspace + "Namelist-2 value".ljust(valspace)
    if args.printdefs:
        header += wspace + separator + wspace + "default".ljust(valspace)
    header += "\n" + "-"*len(header)
    print(header)
    
    #go through the namelists in alphabetic order
    for namelist in namelists:
        print(f"\033[1m&{namelist}\033[0m")
        for param in sorted(nmldict[namelist].keys()):
            #normal style settings
            style = {i: 'n' for i in range(3)}
            #check if values are equal
            eq = values_equal(*nmldict[namelist][param], args.listidx)
            #if verbose option not set, don't print equal values
            if eq and not args.verbose:
                continue
            if not eq and args.verbose:
                #emphasize the parameter
                style[0] = "e"
            #get the two values and analyze how they should be printed
            v = {1: nmldict[namelist][param][0], 2:nmldict[namelist][param][1]}
            #deemphasize if a value is not specified
            #if the default is given and the value is not, insert it
            for i in [1, 2]:
                if v[i] is None:
                    style[i] = 'd'
                    if defaults is not None:
                        v[i] = defaults[namelist][param]
            #set default for printing if requested
            df = defaults[namelist][param] if args.printdefs else None
            
            print_line(param, v[1], v[2], df, style=style, use_colors=~args.nocolors)
            
        print()
    
#main function command line interface    
def nmldiff_cli():
    #parse the arguments
    description = """Prints the difference between two icon namelists. Output and Meteogram namelists will be ignored."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("file1", help="First namelist file")
    parser.add_argument("file2", help="Second namelist file")
    parser.add_argument("-l", "--listidx", metavar="idx", help="Compare lists by picking one element (idx=0-9) or all elements (idx=a). If not given, the common elements are compared.")
    parser.add_argument("-i", "--ignorepaths", help="Ignores namelist parameters that contain 'file' or 'path' in their name.", action="store_true")
    parser.add_argument("--nocolors", help="Turn off colors to highlight differences (in verbose mode).", action="store_true")
    parser.add_argument("-v", "--verbose", help="Shows all the given parameters with differences highlighted.", action="store_true")
    parser.add_argument("-d", "--defaults", metavar="logfile", help="Specify defaults by providing a namelist log file. These will be considered in the comparison.")
    parser.add_argument("-f", "--printdefs", help="Print the default values as additional column.", action="store_true")
    args = parser.parse_args()
    
    nmldiff(args)
    

              
if __name__=='__main__':
    nmldiff_cli()
    
