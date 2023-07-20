def format_time(time):
    s, ms = str(time).split('.')
    s = int(time)
    ms = int(time)
    
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    
    return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2) + ',' + str(ms).zfill(3)

def list_to_srt(result):
    srt = ""
    for i, sentence in enumerate(result):
        start_time = format_time(sentence[0])
        end_time = format_time(sentence[1])
        text = sentence[2]
        
        srt += str(i + 1) + "\n" + start_time + " --> " + end_time + "\n" + text + "\n\n"
    return srt