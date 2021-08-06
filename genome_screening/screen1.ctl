Begin SCREENDB;
	db_name=gene_oas1_bats_fn;
	mysql_server=localhost;
ENDBLOCK;

BEGIN SCREENSETS;
	query_na_fasta=screen1_probes.fas
	reference_na_fasta=screen1_probes.fas
	output_path=./tmp/;
	bitscore_min_blastn=30;
	seq_length_minimum=30;
	defragment_range=100;
	blast_threads=1;
ENDBLOCK;

BEGIN TARGETS;

	Mammalia/Pipistrellus_pipistrellus
	Mammalia/Miniopterus_natalensis
	Mammalia/Micronycteris_hirsuta
	Mammalia/Rhinolophus_sinicus
	Mammalia/Eidolon_helvum
	Mammalia/Myotis_brandtii
	Mammalia/Miniopterus_schreibersii
	Mammalia/Myotis_davidii
	Mammalia/Antrozous_pallidus
	Mammalia/Pteronotus_parnellii
	Mammalia/Megaderma_lyra
	Mammalia/Pteropus_alecto
	Mammalia/Eonycteris_spelaea
	Mammalia/Myotis_lucifugus
	Mammalia/Phyllostomus_discolor
	Mammalia/Macrotus_californicus
	Mammalia/Rhinolophus_ferrumequinum
	Mammalia/Lasiurus_borealis
	Mammalia/Mormoops_blainvillei
	Mammalia/Eptesicus_fuscus
	Mammalia/Noctilio_leporinus
	Mammalia/Rousettus_aegyptiacus
	Mammalia/Macroglossus_sobrinus
	Mammalia/Murina_aurata_feae
	Mammalia/Hipposideros_galeritus
	Mammalia/Carollia_perspicillata
	Mammalia/Cynopterus_brachyotis
	Mammalia/Hipposideros_armiger
	Mammalia/Nycticeius_humeralis
	Mammalia/Craseonycteris_thonglongyai
	Mammalia/Tonatia_saurophila
	Mammalia/Anoura_caudifer
	Mammalia/Pteropus_vampyrus
	Mammalia/Desmodus_rotundus	
	Mammalia/Aeorestes_cinereus
	Mammalia/Artibeus_jamaicensis
	Mammalia/Molossus_molossus
	Mammalia/Myotis_myotis
	Mammalia/Pipistrellus_kuhlii
	Mammalia/Pteropus_giganteus
	Mammalia/Pteropus_pselaphon
	Mammalia/Rousettus_leschenaultii
	Mammalia/Sturnira_hondurensis
	Mammalia/Tadarida_brasiliensis		

ENDBLOCK;



BEGIN SKIPINDEX;

ENDBLOCK;
