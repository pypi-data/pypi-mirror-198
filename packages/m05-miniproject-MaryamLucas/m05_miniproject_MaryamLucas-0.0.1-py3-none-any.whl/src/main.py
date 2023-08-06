"""

"""

from utils import reg,load_data
import argparse 
 
parser = argparse.ArgumentParser()

parser.add_argument('--data_type', help="select data type ", required=True)
parser.add_argument('--model_type', help="select model", required=True)

args = parser.parse_args()

if __name__ == "__main__":
    
    print("running model: ",args.model_type,"with data: " , args.data_type)
    X_tr, X_ts, y_tr, y_ts = load_data(args.data_type)
    reg(args.model_type,X_tr,y_tr,X_ts,y_ts)
    
