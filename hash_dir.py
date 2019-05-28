"""Module used to hash a directory
"""
import hashlib
import os
import sys


def get_hash_of_dir(directory, extensions_filter):
    """Compute the hash of a dir

    Arguments:
        directory {str} -- Path of the dir
        extensions_filter {list} -- Filter the files to math this extensions (no filter if the list is empty)

    Returns:
        ? -- The hash of the dir
    """
    # Get the filter if the list is not empty
    tuple_filter = None
    if extensions_filter:
        tuple_filter = tuple(extensions_filter)
    # Create the MD5 hash
    md5 = hashlib.md5()
    # Check if the dir exist
    if not os.path.exists(directory):
        return None
    # Check in the entire directory recursively
    for root, _, files in os.walk(directory):
        for filename in files:
            # Use the extension filter is one was given
            if tuple_filter and not filename.lower().endswith(tuple_filter):
                continue
            filepath = os.path.join(root, filename)
            try:
                file_reader = open(filepath, 'rb')
            except IOError:
                # Can't open the file for some reason
                file_reader.close()
                continue

            while 1:
                # Read file in as little chunks
                buf = file_reader.read(4096)
                if not buf:
                    break
                # Update the MD5 hash
                md5.update(buf)
            file_reader.close()
    # Return the complete hash
    return md5.hexdigest()

if __name__ == "__main__":
    # Change to true to print only the Hash
    SIMPLE = False
    def main():
        """ Main """
        # Check if there is enough args or display the help
        if len(sys.argv) < 2:
            print(f"Usage {sys.argv[0]} [Folder Path] (Extentions filter...)")
            return
        # Get the extensions filter if at least one arg is provided
        extensions_filter = list()
        if len(sys.argv) >= 3:
            for i in range(2, len(sys.argv)):
                extensions_filter.append(sys.argv[i])
        # Print the result hash of the folder
        if not SIMPLE:
            print("Hash of {}{} :".format(
                sys.argv[1],
                f" with filter {extensions_filter}" if extensions_filter else ""
            ))
        print(get_hash_of_dir(sys.argv[1], extensions_filter))
    main()
