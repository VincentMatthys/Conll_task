from keras.models import load_model
from utils import *
import pickle
from process import *

# This function is used to print the Performance Metrics using the Testing Data
def find_metrics(X_teste, y_teste,model_path1,all_words,all_tags):
    # load model
    
    model = load_model(model_path1)
    
    model.evaluate(X_teste, y_teste, verbose=1)
    
    preds, y_true = np.argmax(model.predict(X_teste), axis=-1), np.argmax(y_teste, -1)
    pred_tag, true_tag = parser2categorical(preds, y_true, all_tags) 
    print(metrics(pred_tag, true_tag))
    
# This Function is for loading the pickle files of the POS Model's embedded files and some variables.
def POS_EVAL():
    with open('encoding/X_teste_POS.pkl', 'rb') as f:
        X_teste = pickle.load(f)
    with open('encoding/y_teste_POS.pkl', 'rb') as f:
        y_teste = pickle.load(f)
    with open('encoding/all_words_POS.pkl', 'rb') as f:
        all_words = pickle.load(f)
    with open('encoding/all_tags_POS.pkl', 'rb') as f:
        all_tags = pickle.load(f)
    with open('encoding/MAX_LEN_POS.pkl', 'rb') as f:
        MAX_LEN = pickle.load(f)
    # FOR THE POS MODEL
    PATH1A="checkpoints/model_POS.h5"
    find_metrics(X_teste, y_teste,PATH1A,all_words,all_tags)
# This Function is for loading the pickle files of the Syntactic Chunk Model's embedded files and some variables.
def PAR_EVAL():
    with open('encoding/X_teste_PAR.pkl', 'rb') as f:
        X_teste = pickle.load(f)
    with open('encoding/y_teste_PAR.pkl', 'rb') as f:
        y_teste = pickle.load(f)
    with open('encoding/all_words_PAR.pkl', 'rb') as f:
        all_words = pickle.load(f)
    with open('encoding/all_tags_PAR.pkl', 'rb') as f:
        all_tags = pickle.load(f)
    with open('encoding/MAX_LEN_PAR.pkl', 'rb') as f:
        MAX_LEN = pickle.load(f)    

    # FOR THE POS MODEL
    PATH1A="checkpoints/model_PAR.h5"
    
    find_metrics(X_teste, y_teste,PATH1A,all_words,all_tags)
# This Function is for loading the pickle files of the NER Model's embedded files and some variables.
def NER_EVAL():
    with open('encoding/X_teste_NER.pkl', 'rb') as f:
        X_teste = pickle.load(f)
    with open('encoding/y_teste_NER.pkl', 'rb') as f:
        y_teste = pickle.load(f)
    with open('encoding/all_words_NER.pkl', 'rb') as f:
        all_words = pickle.load(f)
    with open('encoding/all_tags_NER.pkl', 'rb') as f:
        all_tags = pickle.load(f)
    with open('encoding/MAX_LEN_NER.pkl', 'rb') as f:
        MAX_LEN = pickle.load(f)      

    # FOR THE POS MODEL
    PATH1A="checkpoints/model_NER.h5"
    
    find_metrics(X_teste, y_teste,PATH1A,all_words,all_tags)



