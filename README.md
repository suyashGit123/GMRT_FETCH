# GMRT_FETCH

## FETCH for GMRT Filterbank Data

The candidate preparation of FETCH is divided into 3 scripts:</br>
1.) pysigproc.py ( Contains definition of functions for generating a sigproc file)</br>
2.) candidate.py(function definitions for generating H5 files)</br>
3.) candmaker.py( calls functions defined  in candidate.py and h5plotter.py)</br>

The machine learning stage comprisesof 2 scripts i.e. train.py and predict.py
___

**Note** : The changes for the raw file variation of FETCH are different and the below listed changes ar only for the GMRT filterbank file processing 

The generation of the candidates(.h5 files) is done using candmaker command .For avoiding memory errors we have modified the candmaker command to :</br>
>candmaker.py -n 1 --frequency_size 256 --time_size 256 --cand_param_file cands.csv --plot --fout /data/candidates/</br>

The input of candmaker script is a csv file which contains parameters of FRB in the order: 

>/path/to/filterbank/myfilterbank.fil,S/N,start_time,dm,width(in number ofsamples)

The numpy errors for the GMRT filterbank files have been removed by altering the candidate.py and changing the mode parameter of pad_along_axis function
The original package can be found at [FETCH](https://github.com/devanshkv/fetch)

**Note** : Multiple instancesof filterbank files can be passed to FETCH inside the input csv file </br>

### Automating the process

The output of the first stage of candidate preparation resides in the path to directory passed in the input csv file. and then run the command shown below for running the CNN on the candidate files .</br>
>predict.py --data_dir /data/candidates/ --model index

The index is an letter from 'a-h' (lower case) and it chooses the CNN for FRB classifcation .We suggest setting it to 'a'</br>

---
Instead of using the above sequential approach we have automated the process of candidate preparation and prediction using the auto.py script.</br>
The input and output file directories can be set explicitly in the script, but can also be set using the command :

>python auto.py --pin /pathto/input/directory --pout /path to/output/directory

It also logs in the time taken for end to end processing and also the binary result of classification. Other options like cleaning the directory before writing the candidates to it can be accessed by settig the 'clean'flag

---
### Estimated time taken
Below is the estimated time for bandwise change in processing for file with 6 samples and 2K channels:</br>

| Band          | Are           |
| ------------- |:-------------:|
| Band 3        |  5min         |
| Band 4        |  ~1 to 2 min  |
| Band 5        |  < 1 min      | 







