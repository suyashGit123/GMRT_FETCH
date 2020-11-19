import csv
import os
import time
import math
import multiprocessing
import logging
import pandas as pd
from multiprocessing import Process, current_process
from multiprocessing import log_to_stderr,get_logger

import argparse



if __name__ == '__main__':
  
  parser = argparse.ArgumentParser()
 #logging info
  log_to_stderr()
  logger = get_logger()
  logger.setLevel(logging.INFO)
  
 #optional arguments
  parser.add_argument('--pout', help='Output file directory for candidate h5', type=str,default = '/home/guest/suyash/default_cand/')
  parser.add_argument('--pin', help='input csv file for candmaker', type=str,default='/home/guest/suyash/fetch/cands.csv')
  parser.add_argument('--clean',help='deletes contents of default',default = 0)
  args =parser.parse_args()

  in_path= str(args.pin)
  out_path= str(args.pout)
  clean = int(args.clean)
  
  if (clean == 1):
    print("cleaning folder")
    os.system(f"find {out_path} -type f -delete")
  
  start_time = time.time()


 # os.system(f"candmaker.py  --nproc 10 --frequency_size 256 --time_size 256 --cand_param_file {in_path}  --plot --fout {out_path} --src1 {s1} --src2 {s2}")
  os.system(f"candmaker.py  --nproc 50 --frequency_size 256 --time_size 256 --cand_param_file {in_path}  --plot --fout {out_path} ")
  os.system(f"predict.py --data_dir {out_path} --model a")
  print("displaying results")
  end_time = time.time()
  total_time = end_time - start_time
  logging.info(f'End to End time: {total_time}')
  print (f'End to End time: {total_time}')
  if (os.path.exists(f"{out_path}auto_output_level0")==False): 
   os.system(f"mkdir {out_path}auto_output_level0")
  if (os.path.exists(f"{out_path}auto_output_level1")==False): #check for folder
   os.system(f"mkdir {out_path}auto_output_level1")
  df=pd.read_csv(f'{out_path}results_a.csv')
  for ind in df.index:
    if(df['label'][ind]==1):
        fil=df['candidate'][ind]
        ret=fil.split('/')[-1]
        target=ret.split('.h5')[0]
        img= target+'.png'
        os.system(f"mv {out_path}/{ret} {out_path}auto_output_level1/")
        os.system(f"mv {out_path}/{img} {out_path}auto_output_level1/")
    if(df['label'][ind]==0):
        fil=df['candidate'][ind]
        ret=fil.split('/')[-1]
        target=ret.split('.h5')[0]
        img= target+'.png'
        os.system(f"mv {out_path}/{ret} {out_path}auto_output_level0/")
        os.system(f"mv {out_path}/{img} {out_path}auto_output_level0/")
       # print(img)
       # print(ret)
    


