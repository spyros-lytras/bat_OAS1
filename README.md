# Online supplementary for [A Prenylated dsRNA Sensor Protects Against Severe COVID-19 and is Absent in Horseshoe Bats](https://www.medrxiv.org/content/10.1101/2021.05.05.21256681v1.full-text)

(this repository contains supplementary material for the following sections of the above paper: <i>Synteny analysis</i>, <i>In silico genome screening</i>, <i>PDE analysis</i>)

## Synteny analysis

Genomic synteny between humans and the greater horseshoe bat (<i>R. ferrumequinum</i>) was assessed using the [ensembl genome synteny browser](https://www.ensembl.org/Homo_sapiens/Location/Synteny?g=ENSG00000089127&t=ENST00000680189&r=12%3A112905856-112919898&db=core&otherspecies=Rhinolophus_ferrumequinum).

- [synteny alignment between genomes (retrieved from ensembl)](https://github.com/spyros-lytras/bat_OAS1/blob/master/synteny_analysis/alignment_Homo_sapiens_12_112918751_112941483_Rf.fas).
- [580bp <i>R. ferrumequinum</i> sequence span up to where synteny resumes to the human genome](https://github.com/spyros-lytras/bat_OAS1/blob/master/synteny_analysis/Rf_insert.fas).
- [hmmscan Dfam hits](https://github.com/spyros-lytras/bat_OAS1/blob/master/synteny_analysis/hmmscan_hits.csv).


## <i>In silico</i> genome screening

This analysis was performed using the [DIGS tool](https://giffordlabcvr.github.io/DIGS-tool/).

List of [44 Chiroptera genome assemblies](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/digs_bat_assemblies.csv) used.

- Screen 1: bat LTR insertion search
	- [DIGS control file](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen1.ctl)
	- [DIGS probes](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen1_probes.fas)
	- [DIGS curated output](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen1_digsout.csv)

- Screen 2: CaaX terminal search
	- [DIGS control file](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen2.ctl)
	- [DIGS probes](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen2_probes.fas)
	- [DIGS curated output](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen2_digsout.csv)

- Screen 3: OAS1 C-terminal domain search
	- [DIGS control file](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen3.ctl)
	- [DIGS probes](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen3_probes.fas)
	- [DIGS curated output](https://github.com/spyros-lytras/bat_OAS1/blob/master/genome_screening/screen3_digsout.csv)

	
## PDE analysis

The custom PDE HMM profile used in this study is available [here](https://github.com/spyros-lytras/bat_OAS1/blob/master/pde_analysis/CoV_AKAP7_VP3_PDE.hmm), along with the [curated alignment](https://github.com/spyros-lytras/bat_OAS1/blob/master/pde_analysis/al_CoV_AKAP7_VP3_cur.fas) used to create it.

The [pde_search python script](https://github.com/spyros-lytras/bat_OAS1/blob/master/pde_analysis/pde_search.py) contains all filtering/parsing steps and commands used for the analysis.

- [CoVs with PDE detected](https://github.com/spyros-lytras/bat_OAS1/blob/master/pde_analysis/CoV_dat2_fn_PDE.csv)
- [CoVs with no PDE detected](https://github.com/spyros-lytras/bat_OAS1/blob/master/pde_analysis/CoV_dat2_fn_noPDE.csv)

NB: the <i>Bat_host</i> column has been manually added to the dataframes.