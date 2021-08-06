from Bio import SeqIO, SearchIO, Entrez
import pandas as pd
import random
import subprocess

Entrez.email = # add email

file = 'Coronaviridae_nuccomplete.csv'#

outp = 'CoV_dat1'



####    Download fasta seqs    ####

#parse
alldf = pd.read_csv(file)

#remove human SARS viruses
alldf = alldf.loc[(alldf["Species"] != 'Severe acute respiratory syndrome-related coronavirus') & (alldf["Host"] != 'Homo sapiens')]

#drop rows without a host
hostdf = alldf.dropna(subset=['Host'])

#filter by sequence length
lenhostdf = hostdf.loc[hostdf['Length'] >= 25000]

#get accessions to list
idez = list(lenhostdf.Accession)

allfas = outp + '.fas'

#efetch fetches the genome information in fasta format
net_handle = Entrez.efetch(db="nucleotide", id=idez, rettype='fasta', retmode="text")
#opens a writable file with the output file name
out_handle = open(allfas, "w")
#writes the fasta record in the opened file
out_handle.write(net_handle.read())
out_handle.close()
net_handle.close()



#### getorf - make aa file with all possible proteins ####

orffile = allfas.replace('.fas', '_orfout.fas')
getorf = 'getorf -sequence %s -outseq %s -find 1 -flanking 0 -minsize 100'%(allfas, orffile)
subprocess.Popen([getorf], shell = True,close_fds=True).wait()



#### now search everything with the custom HMM profile  ####

profile = 'CoV_AKAP7_VP3_PDE.hmm'
resfile = orffile.replace('_orfout.fas', '_hmm.out')
hmmscan = 'hmmscan --tblout %s %s %s'%(resfile, profile, orffile)
subprocess.Popen([hmmscan], shell = True,close_fds=True).wait()



#resfile has the results in hmmer out format
    #make list of accessions with PDEs
pdeids = []
for res in SearchIO.parse(resfile, 'hmmer3-tab'):
    pdeids.append(res.id.split('_')[0])
    

#accessions without detected PDE
nopdeids = list(set(list(lenhostdf.Accession)) - set(pdeids))    


lenhostdf.sort_values(by = ['Species'], inplace = True)


#make final result files
         
lenhostdf = lenhostdf[['Accession', 'Host', 'Species', 'Genus', 'Length','Collection_Date']]

pdefn = lenhostdf.loc[lenhostdf["Accession"].isin(pdeids)]

print(pdefn)

pdefn.to_csv('CoV_dat2_fn_PDE.csv', index = False)

nopdefn = lenhostdf.loc[lenhostdf["Accession"].isin(nopdeids)]

print(nopdefn)

nopdefn.to_csv('CoV_dat2_fn_noPDE.csv', index = False)
