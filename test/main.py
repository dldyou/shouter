import findspark
findspark.init() 
from pyspark import SparkConf, SparkContext
import upload
import task_file
import hdfsPath as hp

def main():
    # configuration spark API
    conf = SparkConf().setAppName("Shouter").setMaster("local")
    sctx = SparkContext(conf = conf)
    # file upload to hdfs like audio0.mp3, audio1.mp3, ..., audio{n}.mp3
    upload.file_processing()
    # file read from hdfs 
    audio_files = hp.get_path()
    # set RDD 
    audio_files_rdd = sctx.parallelize(audio_files)
    # Map (apply subtitle.get_subtitle() for every audio{n}.mp3 files)
    result_rdd = audio_files_rdd.map(task_file.process_audio_file)
    print(result_rdd)
    # Reduce (collect results)
    results = result_rdd.collect()
    # transform to subtitle file form
    
    # start download subtitle file
    
if __name__ == '__main__':
    main()