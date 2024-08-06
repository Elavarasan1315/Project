import os

def main():
    i = 0
    path = 'C:/Users/user/Pictures/Screenshots/'
    
    for filename in os.listdir(path):
        if filename.endswith('.png'):  # Check if the file is a PNG
            new_filename = 'img' + str(i) + '.png'
            source = os.path.join(path, filename)
            destination = os.path.join(path, new_filename)
            os.rename(source, destination)
            i += 1

if __name__ == '__main__':
    main()
