from sys import argv


def file_overwrite(n=20):

    filename = "example1.txt"
    with open(filename, 'r+') as f:
        content = f.read()
        print (content)
        # ask user to overwrite the file
        while True:
            feedback = input("Type 'y' to overwrite the file or 'n' to exit: ")
            if feedback.lower() == 'y':
                # move the file pointer back to the start and then truncate the file
                f.seek(0)
                f.truncate()
                break
            elif feedback.lower() == 'n':
                # return instantly, another advantage of using a function
                return
            else:
                print ("Please enter either 'y' or 'n'.")


        # Loop n times and ask for user input and save it in the list.
        lines = []
        for line_num in range(1, n+1):
            line = input()
            lines.append(line)

        f.write('\n'.join(lines))

        # After writing the file pointer is again at the end of the file.
        # To read the content again move it back to the start and then
        # read file's content.
        f.seek(0)
        print( f.read())

#

