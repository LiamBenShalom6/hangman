def my_mp4_playlist(file_path, new_song):

    with open(file_path, 'r+') as f:
        cd_data = f.read()
        cd_splitted_lines = cd_data.split("\n")

        # If the file has less than three lines, add empty lines
        if len(cd_splitted_lines) < 3:
            for i in range(len(cd_splitted_lines), 3):
                cd_splitted_lines[i].append('\n')
            
        singer = cd_splitted_lines[2].split(";")[1]
        time = cd_splitted_lines[2].split(";")[2]
        
        cd_splitted_lines[2] = new_song + ";" + singer + ";" + time + ";"
        
        
        f.seek(0)
        
        for lines in cd_splitted_lines:
            f.write(lines + "\n")

        f.seek(0)
        print(f.read())
		
def main():
    songs_file = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\songs.txt"
    my_mp4_playlist(songs_file, "Python Love Story")

if __name__ == "__main__":
    main()