import os
class read:
    @staticmethod
    def read_line(path_name:str,line_number: int):
        try:
            f = open(path_name).readlines()
            if (line_number>len(f)):
                return "the file '"+path_name+"' only has "+ str(len(f))+ " lines"
                pass
                # comment: 
            return 'the line '+str(line_number)+' of the file \''+path_name+'\' contains the following: \n'+ f[line_number-1] 
                # comment: tru this read function
        except Exception as e:
            return "we encountered the following error\n"+ str(e)
        # end try
        """
        Purpose: allow the agent/user to read a particular line from a particular file 
        """
        # end if
    # end def
    @staticmethod
    
    def read_from_line_to_line(path_name:str,from_line: int, to_line:int):
        """
        Purpose: allow the agent/user to read block of lines they want to read
        """
        try:
            endnote=""
            f = open(path_name).readlines() 
            if (from_line>len(f)):
                return "the file '"+path_name+"' only has "+ str(len(f))+ " lines"
                pass
            # end if
            if (to_line>len(f)):
                endnote = " (the last line of the file is "+str(len(f))+")"
                to_line= len(f)
                pass
            # end if
            combinedlines=""
            for line in f[from_line-1:to_line]:
                combinedlines=combinedlines+ line
                pass
            return 'the line '+str(from_line)+' through line '+str(to_line)+endnote+' of the file \''+path_name+'\' contains the following: \n' + combinedlines
        except Exception as e:
             return "we encountered the following error\n"+ str(e)
    @staticmethod
    def directory_tree(path_name: str, indent: str = "") -> str:
        """
        Purpose: Recursively print a directory tree structure.
        """
        try:
            # Safely get the current folder name (e.g. '.' becomes current folder name, or falls back)
            norm_path = os.path.normpath(path_name)
            output = os.path.basename(norm_path)
            if not output:  # Handles root like '/'
                output = path_name
        except Exception:
            output = path_name

        try:
            entries = os.listdir(path_name)
        except PermissionError:
            return output + "\n\t[Permission Denied]"

        directories = [entry for entry in entries if os.path.isdir(os.path.join(path_name, entry))]
        
        for directory in directories:
            sub_path = os.path.join(path_name, directory)
            output = output + "\n\t" +directory+"\\"
            
        notdirectories = [entry for entry in entries if entry not in directories]
        if notdirectories:
            output = output + "\n\t" + "\n\t".join(notdirectories)
            
        return output

    @staticmethod
    def directory_tree_recursive(path_name: str, indent: str = "") -> str:
        """
        Purpose: Recursively print a directory tree structure.
        """
        try:
            # Safely get the current folder name (e.g. '.' becomes current folder name, or falls back)
            norm_path = os.path.normpath(path_name)
            output = os.path.basename(norm_path)
            if not output:  # Handles root like '/'
                output = path_name
        except Exception:
            output = path_name

        try:
            entries = os.listdir(path_name)
        except PermissionError:
            return output + "\n\t[Permission Denied]"

        directories = [entry for entry in entries if os.path.isdir(os.path.join(path_name, entry))]
        
        for directory in directories:
            sub_path = os.path.join(path_name, directory)
            output = output + "\n\t" + "\n\t".join(read.directory_tree(sub_path).split('\n'))
            
        notdirectories = [entry for entry in entries if entry not in directories]
        if notdirectories:
            output = output + "\n\t" + "\n\t".join(notdirectories)
            
        return output
    @staticmethod 
    def read_file(path_name:str)-> str:
        return "".join(open(path_name).readlines())
        pass
class Write:
    def append_to_file(file_name:str, block:str):
        """
        Purpose: write a block at the end of a file
        """
        with open(file_name, 'a') as f:
            f.write(block+"\n")
        # end def
    @staticmethod
    def overwrite_file(file_name:str, block:str):
        """
        Purpose: delete content and write block
        """
        with open(file_name, 'w') as f:
            f.write(block)
    @staticmethod
    def replace_block_on_a_file(file_name:str, starting_of_block:int, ending_of_block:int, block:str):
        """
        Purpose: replace the block indicated by the indexes the indexes
        """
        new_content:list(str)
        with open(file_name, "r") as file:
            lines = file.readlines()
            new_content= lines[0:starting_of_block-1]+[line+'\n' for line in block.split("\n")]+lines[ending_of_block::]
            pass
        with open(file_name, "w") as file:
            file.write("".join(new_content))
    @staticmethod
    def inset_block_at_line(file_name:str, line_number:str,block:str):
        """
        Purpose: insert a block at a perticular line
        """
        new_content:list(str)
        with open(file_name, "r") as file:
            lines = file.readlines()
            new_content= lines[0:line_number]+[line+'\n' for line in block.split("\n")]+lines[line_number::]
            pass
        with open(file_name, "w") as file:
            file.write("".join(new_content))
