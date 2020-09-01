# GMRT_FETCH

## FETCH for GMRT Filterbank DATA

The candidate preparation of FETCH is divided into 3 scripts:</br>
1.) pysigproc.py ( Contains definition of functions for generating a sigproc file)..
2.) candidate.py(function definitions for generating H5 files)..
3.) candmaker.py( calls functions defined  in candidate.py and h5plotter.py)..

The machine learning stage comprisesof 2 scripts i.e. train.py and predict.py
___

**Note** : The changes for the raw file variation of FETCH are different and the below listed changes ar only for the GMRT filterbank file processing ..

The generation of the candidates(.h5 files) is done using candmaker command .For avoiding memory errors we have modified the candmaker command to :</br>
>candmaker.py -n 1 --frequency_size 256 --time_size 256 --cand_param_file cands.csv --plot --fout /data/candidates/</br>

The input of candmaker script is a csv file which contains parameters of FRB in the order: 

>/path/to/filterbank/myfilterbank.fil,S/N,start_time,dm,width(in number ofsamples)

The numpy errors for the GMRT filterbank files have been removed by altering the candidate.py and changing the mode parameter of pad_along_axis function..
The original package can be found at [FETCH](https://github.com/devanshkv/fetch)

**Note** : Multiple instancesof filterbank files can be passed to FETCH inside the input csv file ..




