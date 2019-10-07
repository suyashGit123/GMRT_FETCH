# GMRT_FETCH

The Classifier is divided into 2 modules:</br>
1.) FETCH</br>
2.) Pysigproc</br>
</br>
Both of these modules and their dependencies have been installed on the GPU server.</br>
The generation of the candidates(.h5 files) is done using candmaker command .For avoiding memory errors we have modified the candmaker</br> command to :</br>
candmaker.py -n 1 --frequency_size 256 --time_size 256 --cand_param_file cands.csv --plot --fout /data/candidates/</br>
The h5 files are saved to the directory /data/candidates  (This is output of candmaker command)</br>
The input of candmaker script is a csv file (which contains path to filterbank file, and other parameters of FRB: start time, width, snr and dm)</br>
The pysigproc  notebook  creates these candidates , which means it does the job of candmaker script except the fact that it doesn’t  rebin and decimate them. To summarise this discussion the pysigproc module only creates candidate objects and dedisperses them by using candidate script [ This is present in Pysigproc repo and is used by both candmaker as well as the notebook itself].</br>
The pysigproc notebook is more for simulation and understanding , which is why the candidates should be generated using candmaker only. At no point should the pysigproc notebook [titles as pysigproc_demo.ipynb] be confused with pysigproc module which cannot be bypassed [it is executed by candmaker command].</br>
As of now we have generated candidates using pysigproc, doing the same with candmaker has failed due to memory errors. Suggestions by Devansh and Kshitij to resolve it are :</br>
1.	Use High Performance Computer ( done)</br>
2.	Use FRB with smaller DM</br>Training   ( Optional ) :</br>
# Train
The train.py command can be used to finetune the models  which are present in FETCH module.</br>
INPUT:  1.) model index [ refer file models_list.csv]</br>
        2.)A training dataset [ A csv file with headers candidate h5’s and their labels ]</br>
# Predict :
Predicts candidates living in directory /data/candidates </br>
INPUT:  1.) model index [ refer file models_list.csv]</br>
        2.) Path to directory </br>

