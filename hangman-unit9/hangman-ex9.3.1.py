def my_mp3_playlist(file_path):
    f = open(file_path, "r")
    cd_data = f.read()
    cd_splitted_lines = cd_data.split("\n")
    cd_items = []
    count_songs = len(cd_splitted_lines)
    for element in cd_splitted_lines:
        cd_items.append(element.split(";"))
    
    save_name_dict = {}
    save_song_time_dict = {}
    time_list = []
    singer = ""
    for item in cd_items:
        singer = item[1]
        time_list = item[2].split(":")
        time = (".").join(time_list)
        save_song_time_dict[item[0]] = float(time)
        
        if singer in save_name_dict.keys():
            save_name_dict[singer] += 1
        else:
            save_name_dict[singer] = 1
    
    max_time = max(save_song_time_dict.values())
    max_time_apper = max(save_name_dict.values())
    
    max_song = ""
    for i in save_song_time_dict.keys():
        if save_song_time_dict[i] == max_time:
            max_song = i
    
    max_singer = ""
    for i in save_name_dict.keys():
        if save_name_dict[i] == max_time_apper:
            max_singer = i
    
    f.close()
    my_cd_tuple = (max_song, count_songs, max_singer)
    return my_cd_tuple
    
        



def main():
    songs_file = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\songs.txt"
    print(my_mp3_playlist(songs_file))

if __name__ == "__main__":
    main()