import trim

def merge_audio(result, cnt):
    ret = []
    for i in range(cnt):
        start_time = result[i][-1][0]
        if (trim.timing - start_time <= 0.2):
            ret.append(result[i][:-1])
        else:
            ret.append(result[i])
    
    return ret