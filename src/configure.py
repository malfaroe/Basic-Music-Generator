DATA_PATH = r"C:\Users\malfaro\Desktop\mae_code\Basic-Music-Generator\data\Jazz" #folder of midi songs dataset
MAPPING_JSON_NAME = "mapping_modular.json" #name of the dictionary with mappings symbol/integer
SEQUENCE_LENGTH = 100 #length of input sequence of elements 
TRAINING_DATA_PATH = r"C:\Users\malfaro\Desktop\mae_code\Basic-Music-Generator\src\training_data.pkl"

#####TRAINING UNIT
OUTPUT_UNITS = None #to be obtained as vocab_size variable from generate_training_sequences
NUM_UNITS = [256] #Hidden layer units
LOSS = "sparse_categorical_crossentropy"
LEARNING_RATE = 0.001
EPOCHS = 30
BATCH_SIZE = 128
SAVED_MODEL_NAME = r"C:\Users\malfaro\Desktop\mae_code\Basic-Music-Generator\src\weights-FINAL.hdf5"