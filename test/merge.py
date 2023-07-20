import trim

def merge_audio(result, cnt):
    ret = []
    for i in range(cnt):
        start_time = result[i][-1][0]
        if (trim.timing - start_time <= 0.2):
            for sentence in result[i][:-1]:
                ret.append(sentence)
        else:
            for sentence in result[i]:
                ret.append(sentence)
    
    return ret