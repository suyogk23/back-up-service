import os 

def write_log(filename, values):
    # Open the file in append mode with reading ('a+')
    # If the file doesn't exist, it will be created
    with open(filename, 'a+') as file:
        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Read the content of the file
        content = file.read()
        # Check if the file is empty (length is 0)
        if len(content) == 0:
            # File is empty, write the values with newline
            file.write(values)
        else:
            # File is not empty, append newline and then the values
            file.write('\n')
            file.write(values)