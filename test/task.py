import subtitle as st
# result of task
result = []
def process_audio_file(path):
    global result
    print(f'Processing: {path}')
    result.append(st.get_subtitle(path))