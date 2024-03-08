
from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.pipeline.batch_prediction import start_batch_prediction

file_path= r"C:\Users\sahus\project\aps_fault_detection\aps_failure_training_set1.csv"
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)


'''def test_logger_and_exception():
     try:
        logging.info('starting the test_logger_and_exception')
        res = 3/0
        print(res)
        logging.info('stopping the test_logger_and_exception')
     except Exception as e:
        logging.debug('stopping the test_logger_and_exception')
        raise SensorException(e, sys)
    
if __name__=="__main__":
     try:
         test_logger_and_exception()
     except Exception as e:
         print(e)'''