#/usr/bin/python
#MarkYAML v1 04-18-2019
#Written by Joseph Sarro
#This a script to make a YAML file. 
#Uodates: 
#04-23-2019: Changed interactive questions into options
#04-24-2019: Added study protocol functionality
#04-25-2019: Made dictionary lookup non case sensitive.
import os
import argparse
##define options
parser = argparse.ArgumentParser(description='Generate a yaml file. Example usage: python MarkYAML.py -sid "2018-Marion_County_Public_Health_Deparment_surveillance" -st "Marrion_County_data" -t NJLT -a light -y 2018 -s "BLANK,Culex pipiens,Culex restuans,Culex pipiens morphological group,Culex territans,Culiseta inornata,Anopheles punctipennis,Anopheles quadrimaculatus,Aedes vexans,Aedes trivittatus,Aedes grossbecki,Aedes japonicus complex,Aedes triseriatus,Orthopodomyia signifera,Psorophora ferox,Coquillettidia perturbans,Uranotaenia sapphirina,Culex erraticus,Aedes albopictus,Psorophora columbiae,Anopheles crucians,Anopheles barberi,Psorophora howardii,Psorophora ciliata,Anopheles earlei" -i morphological -d adult -x female,male -C n -o name.yaml')
parser.add_argument('-C', type=str,
                   help='Fully specifed config file y/n. (Default: n)')
parser.add_argument('-sid', type=str,
                   help='Study ID.')
parser.add_argument('-st', type=str,
                   help='Study title.')
parser.add_argument('-t', type=str, required=True,
                   help='List of trap types seperated by commas. Please enter within "" if there are spaces  i.e. "this has,a,space"')
#parser.add_argument('-T', type=file,
 #                  help='file containing a comma seperated list of trap types')
parser.add_argument('-a', type=str, required=True,
                   help='List of attractants sperated by commas. Please enter within "" if there are spaces  i.e. "this has,a,space"')
#parser.add_argument('-A', type=file,
 #                  help='file containing a comma seperated list of attractants')
parser.add_argument('-s', type=str, required=True,
                   help='List of species sperated by commas. Please enter within "" if there are spaces  i.e. "this has,a,space"')
#parser.add_argument('-S', type=file,
 #                  help='file containing a comma seprated list of species')
parser.add_argument('-i', type=str, required=True,
                   help='Species identification method. Seperate by commas if there are multiple. Please enter within "" if there are spaces  i.e. "this has,a,space"')
parser.add_argument('-d', type=str, required=True,
                   help='Developmental stage. Seperate by commas if there are multiple.')
parser.add_argument('-g', type=str,
                   help='Feeding and gonotrophic status. Usage example:"freshly fed female insect"')
parser.add_argument('-x', type=str, required=True,
                   help='Sex. Seperate by commas if there are multiple.')
parser.add_argument('-y', type=int, required=True,
                   help='Year.')
parser.add_argument('-o', type=str, required=True,
                   help='Output file name.')
args = parser.parse_args()
#print(args.accumulate(args.integers))
#print args.t
#end define options
#f = open('2017_full_Data.txt', 'r')
#print "Enter a file name."
G= open(args.o,'w')
#file = raw_input("")
#G= open(file,'w')
#being dictionary creations#
gon_dic={
"  unfed female insect : VSMO:0000210",
"  fed female insect : VSMO:0000218",
"  fed and gravid female insect : VSMO:0000208",
"  freshly fed female insect : VSMO:0000207"
}
stage_dic={
"  adult : IDOMAL:0000655",
"  larva : IDOMAL:0000653"
}
id_dic={
"  - study_protocol_name : MORPHO\n"
   "    study_protocol_type : morphological identification\n"
   "    study_protocol_type_term_source_ref : MIRO\n"
   "    study_protocol_type_term_accession_number : 30000039\n"
   "    study_protocol_description :\n"
   "      Mosquitoes were identified using morphological identification**\n"
}
trap_dic={
"  - study_protocol_name : NJLT\n"
   "    study_protocol_type : new jersey trap catch\n"
   "    study_protocol_type_term_source_ref : IRO\n"
   "    study_protocol_type_term_accession_number : 0000031\n"
   "    study_protocol_description :\n"
   "      Mosquitoes were caught using a New Jersey light trap**\n",

"  - study_protocol_name : CDCLIGHT\n"
    "    study_protocol_type : CDC light trap\n"
    "    study_protocol_type_term_source_ref : VSMO\n"
    "    study_protocol_type_term_accession_number : 0000727\n"
    "    study_protocol_description :\n"
    "      Mosquitoes were caught using a CDC light trap\n", 

"  - study_protocol_name : GRAVID\n"
    "    study_protocol_type : CDC gravid trap\n"
    "    study_protocol_type_term_source_ref : VSMO\n"
    "    study_protocol_type_term_accession_number : 0001510\n"
    "    study_protocol_description :\n"
    "      Mosquitoes were caught using a gravid trap\n",

"  - study_protocol_name : BGSENT\n"
    "    study_protocol_type : BG-Sentinel trap\n"
    "    study_protocol_type_term_source_ref : VSMO\n"
    "    study_protocol_type_term_accession_number : 0001906\n"
    "    study_protocol_description :\n"
    "      Mosquitoes were caught using a Biogents BG-Sentinel trap\n" 
}
att_dic={
"  light : IRO:0000139",
"  CO2 : IRO:0000035",
"  BG-lure : IRO:0001060",
"  No attractant used : IRO:0000153",
"  hay or grass infusion: IRO:0000037",
"  alfalfa infusion : IRO:0001059",
"  octenol : IRO:0000036"
}
sex_dic={
"  female : PATO:0000383",
"  male : PATO:0000384",
"  mixed sex : PATO:0001338"
}
species_dic={
"  Aedes aboriginis : VBsp:0000961",
"  Aedes abserratus : VBsp:0000962",
"  Aedes albopictus : VBsp:0000522",
"  Aedes aloponotum : VBsp:0000969",
"  Aedes atlanticus : VBsp:0000976",
"  Aedes atropalpus : VBsp:0000977",
"  Aedes aurifer : VBsp:0000979",
"  Aedes bahamensis : VBsp:0000895",
"  Aedes bicristatus : VBsp:0000984",
"  Aedes bimaculatus : VBsp:0000985",
"  Aedes brelandi : VBsp:0001178",
"  Aedes burgeri : VBsp:0001180",
"  Aedes c. canadensis : VBsp:0000996",
"  Aedes c. mathesoni : VBsp:0000997",

"  Aedes cantator : VBsp:0001000",
"  Aedes cataphylla : VBsp:0001004",
"  Aedes churchillensis : VBsp:0001007",
"  Aedes cinereus : VBsp:0000255",
"  Aedes clivis : VBsp:0001009",
"  Aedes communis : VBsp:0001011",
"  Aedes decticus : VBsp:0001018",
"  Aedes aegypti ",
"  Aedes deserticola : VBsp:0001020",
"  Aedes diantaeus : VBsp:0001022",
"  Aedes dorsalis VSMO:0000674",
"  Aedes dupreei : VBsp:0001024",
"  Aedes epactius : VBsp:0001028",
"  Aedes euedes : VBsp:0001030",
"  Aedes excrucians : VBsp:0001033",
"  Aedes fitchii : VBsp:0001035",
"  Aedes flavescens : VBsp:0001036",
"  Aedes fulvus : VBsp:0001039",
"  Aedes grossbecki : VBsp:0001041",
"  Aedes hemiteleus : VBsp:0000255",
"  Aedes hendersoni : VBsp:0001188",
"  Aedes hexodontus : VBsp:0001047",
"  Aedes impiger : VBsp:0001053",
"  Aedes implicatus : VBsp:0001055",
"  Aedes increpitus : VBsp:0001057",
"  Aedes infirmatus : VBsp:0001059",
"  Aedes intrudens : VBsp:0001061",
"  Aedes j. japonicus : VBsp:0000761",
"  Aedes japonicus : VBsp:0000761",
"  Aedes japonicus complex : VBsp:0000761",
"  Aedes melanimon : VBsp:0001077",
"  Aedes mercurator : VBsp:0001079",
"  Aedes mitchellae : VBsp:0001081",
"  Aedes monticola : VBsp:0001083",
"  Aedes muelleri : VBsp:0001084",
"  Aedes nevadensis : VBsp:0001085",
"  Aedes nigripes : VBsp:0001087",
"  Aedes nigromaculis : VBsp:0001090",
"  Aedes niphadopsis : VBsp:0001091",
"  Aedes papago : VBsp:0000664",
"  Aedes pionips : VBsp:0001106",
"  Aedes provocans : VBsp:0001108",
"  Aedes pullatus : VBsp:0001112",
"  Aedes punctodes : VBsp:0001113",
"  Aedes punctor : VBsp:0001114",
"  Aedes purpureipes : VBsp:0003670",
"  Aedes rempeli : VBsp:0001120",
"  Aedes riparius : VBsp:0001122",
"  Aedes s. idahoensis : VBsp:0001140",
"  Aedes s. spencerii : VBsp:0001139",
"  Aedes scapularis : VBsp:0001126",
"  Aedes schizopinax : VBsp:0001127",
"  Aedes sierrensis : VBsp:0001134",
"  Aedes sollicitans : VBsp:0001138",
"  Aedes sp. : VBsp:0000253",
"  Aedes squamiger : VBsp:0001142",
"  Aedes sticticus : VBsp:0001144",
"  Aedes stimulans : VBsp:0001146",
"  Aedes taeniorhynchus : VBsp:0001152",
"  Aedes tahoensis : VBsp:0001153",
"  Aedes thelcter : VBsp:0001154",
"  Aedes thibaulti : VBsp:0001156",
"  Aedes togoi : VBsp:0003875",
"  Aedes tormentor : VBsp:0001157",
"  Aedes tortilis : VBsp:0001158",
"  Aedes triseriatus : VBsp:0001206",
"  Aedes trivittatus : VBsp:0001159",
"  Aedes varipalpus : VBsp:0001162",
"  Aedes ventrovittis : VBsp:0001163",
"  Aedes vexans : VBsp:0000372",
"  Aedes washinoi : VBsp:0001167",
"  Aedes zoosophus : VBsp:0001209",
"  Anopheles albimanus : VBsp:0000071",
"  Anopheles atropos : VBsp:0000033",
"  Anopheles barberi : VBsp:0000040",
"  Anopheles bradleyi : VBsp:0000047",
"  Anopheles bradleyi/crucians ",
"  Anopheles crucians : VBsp:0003876",
"  Anopheles crucians complex : VBsp:0000072",
"  Anopheles diluvialis : VBsp:0000077",
"  Anopheles earlei : VBsp:0000079",
"  Anopheles franciscanus : VBsp:0000089",
"  Anopheles freeborni : VBsp:0000090",
"  Anopheles georgianus : VBsp:0000094",
"  Anopheles hermsi : VBsp:0000108",
"  Anopheles inundatus : VBsp:0000114",
"  Anopheles judithae : VBsp:0000115",
"  Anopheles maverlius : VBsp:0000135",
"  Anopheles occidentalis : VBsp:0003409",
"  Anopheles perplexens : VBsp:0003416",
"  Anopheles pseudopunctipennis : VBsp:0003429",
"  Anopheles punctipennis : VBsp:0003439",
"  Anopheles quadrimaculatus : VBsp:0003441",
"  Anopheles smaragdinus : VBsp:0003441",
"  Anopheles sp. : VBsp:0000015",
"  Anopheles walkeri : VBsp:0003469",
"  Coquillettidia perturbans : VBsp:0002347",
"  Coquillettidia sp. : VBsp:0002312",
"  Culex abominator : VBsp:0002996",
"  Culex anips : VBsp:0003005",
"  Culex apicalis : VBsp:0003195",
"  Culex arizonensis : VBsp:0003196",
"  Culex atratus : VBsp:0003008",
"  Culex bahamensis : VBsp:0002516",
"  Culex biscaynensis : VBsp:0003691",
"  Culex boharti : VBsp:0003197",
"  Culex cedecei : VBsp:0003020",
"  Culex chidesteri : VBsp:0002539",
"  Culex coronator : VBsp:0002544",
"  Culex declarator : VBsp:0002549",
"  Culex erraticus : VBsp:0003050",
"  Culex erythrothorax : VBsp:0002561",
"  Culex interrogator : VBsp:0002588",
"  Culex iolambdis : VBsp:0003071",
"  Culex mulrennani : VBsp:0003090",
"  Culex nigripalpus : VBsp:0002622",
"  Culex peccator : VBsp:0003103",
"  Culex pilosus : VBsp:0003110",
"  Culex pipiens : VBsp:0002641",
"  Culex pipiens morphological group : VBsp:0003847",
"  Culex quinquefasciatus : VBsp:0002654",
"  Culex reevesi : VBsp:0003216",
"  Culex restuans : VBsp:0002657",
"  Culex salinarius : VBsp:0002661",
"  Culex sp. : VBsp:0002423",
"  Culex stigmatosoma : VBsp:0002682",
"  Culex tarsalis : VBsp:0002687",
"  Culex territans : VBsp:0003218",
"  Culex thriambus : VBsp:0002694",
"  Culiseta alaskaensis : VBsp:0002401",
"  Culiseta impatiens : VBsp:0002407",
"  Culiseta incidens : VBsp:0002408",
"  Culiseta inornata : VBsp:0002409",
"  Culiseta melanura : VBsp:0002381",
"  Culiseta minnesotae : VBsp:0002390",
"  Culiseta morsitans : VBsp:0002391",
"  Culiseta particeps : VBsp:0002412",
"  Culiseta sp. : VBsp:0002373",
"  Deinocerites cancer : VBsp:0002287",
"  Deinocerites mathesoni : VBsp:0000997",
"  Deinocerites pseudes : VBsp:0002300",
"  Deinocerites sp. : VBsp:0002283",
"  Haemagogus equinus : VBsp:0003276",
"  Haemagogus sp. : VBsp:0003257",
"  Mansonia dyari : VBsp:0001257",
"  Mansonia sp. : VBsp:0001252",
"  Mansonia titillans : VBsp:0001265",
"  Orthopodomyia alba : VBsp:0001302",
"  Orthopodomyia kummi : VBsp:0000498",
"  Orthopodomyia signifera : VBsp:0003681",
"  Orthopodomyia sp. : VBsp:0001301",
"  Psorophora ciliata : VBsp:0001345",
"  Psorophora columbiae : VBsp:0001307",
"  Psorophora confinnis : VBsp:0001308",
"  Psorophora cyanescens : VBsp:0001326",
"  Psorophora discolor : VBsp:0001310",
"  Psorophora ferox : VBsp:0001328",
"  Psorophora horrida : VBsp:0001331",
"  Psorophora howardii : VBsp:0001348",
"  Psorophora johnstonii : VBsp:0001332",
"  Psorophora longipalpus : VBsp:0001334",
"  Psorophora mathesoni : VBsp:0000997",
"  Psorophora mexicana : VBsp:0001338",
"  Psorophora pygmaea : VBsp:0001317",
"  Psorophora signipennis : VBsp:0001318",
"  Psorophora sp. : VBsp:0001304",
"  Toxorhynchites moctezuma : VBsp:0001487",
"  Toxorhynchites r. rutilus : VBsp:0001484",
"  Toxorhynchites r. septentrionalis : VBsp:0001485",
"  Toxorhynchites sp. : VBsp:0001489",
"  Uranotaenia a. anhydor : VBsp:0001933",
"  Uranotaenia a. syntheta : VBsp:0001934",
"  Uranotaenia lowii : VBsp:0002089",
"  Uranotaenia sapphirina : VBsp:0002128",
"  Uranotaenia sp. : VBsp:0001927",
"  Wyeomyia mitchellii : VBsp:0001869",
"  Wyeomyia smithii : VBsp:0001879",
"  Wyeomyia sp. : VBsp:0001772",
"  Wyeomyia vanduzeei : VBsp:0001884",
"  Mosquito  "
}
#End dictionary creations
#line = f.readline()
#print >> G, "tester"
#print "Will this be a fully specified config file?"
#full=raw_input("(y/n)")
#print full
#Note: This does not work on first input. Look into this.
#if (full !="y") or (full !="n"):
#	FULL = False
#	while FULL == False:
#		print "please enter y or n."
#		full=raw_input("(y/n)")
#		if full =="y" or full =="n":
#			FULL=True
full=args.C
if full=="y":
	print "Yes"
#elif full=="n":
else:
	#print "No"
	#print >> G, "tester"
	print >> G, "#"
	print >> G, "# minimal config file"
	print >> G, "#"
	print >> G, "# not enough to make a fully functional i_investigation sheet"
	print >> G, "# see test-01-full-inv.yaml for that"
	print >> G, "#"
	print >> G, ""
	#print "Enter study indentifier."
	#study_id=raw_input("")
	study_id=args.sid
	print >> G, "study_identifier :",study_id
	#print "Enter study title."
	#study_title=raw_input("")
	study_title=args.st
	print >> G, "study_title :",study_title
	print >> G, "study_submission_date :",args.y
	print >> G, "study_description :"
	print >> G, ""
	print >> G, "study_protocols :"
	trap_list=args.t
	t_split=trap_list.split(",")
        for sp in t_split:
                #print(sp)
                found=False
                for tdic in trap_dic:
                	if sp.lower() in tdic.lower():
                        	found=True
                        	print >> G, tdic
				break
		if found==False:
                	print "Warning:",sp, "not found in trap dictionary."
	id_list=args.i
        idmeth_split=id_list.split(",")
        for sp in idmeth_split:
                #print(sp)
                found=False
                for idic in id_dic:
                        if sp.lower() in idic.lower():
                                found=True
                                print >> G, idic
                if found==False:
                        print "Warning:",sp, "not found in identification method dictionary."
	print >> G, "#"
	print >> G, "# list the species expected to be identified"
	print >> G, "# and their VBsp:nnnnnnn ontology term accessions"
	print >> G, "#"
	print >> G, "study_species :"
	#print "Enter comma seperated list of species. Do not add spaces in between."
	#species_list=raw_input("")
	species_list=args.s
	sp_split=species_list.split(",")
	for sp in sp_split:
		#print(sp)
		found=False
		for spdic in species_dic:
			if sp.lower() in spdic.lower():
				found=True
				print >> G, spdic
		if found==False:
				print "Warning:",sp, "not found in species dictionary."
	print >> G, ""
	print >> G, "#"
	print >> G, "# list the expected sexes, with ontology term accessions"
	print >> G, "#"
	print >> G, "study_sexes :"
	sex_list=args.x
	sp_sex=sex_list.split(",")
	for sp in sp_sex:
		found=False
                #print(sp)
                for sxdic in sex_dic:
                        if sp.lower() in sxdic.lower():
				found=True
                                print >> G, sxdic
				break
		if found==False:
                	print "Warning:",sp, "not found in sex dictionary."
	print >> G, ""
	print >> G, "#"
	print >> G, "# list the expected developmental stages, with ontology term accessions"
	print >> G, "#"
	print >> G, "study_developmental_stages :"
	stage_list=args.d
	sp_stage=stage_list.split(",")
	for sp in sp_stage:
                #print(sp)
		found=False
                for stdic in stage_dic:
                        if sp.lower() in stdic.lower():
				found=True
                                print >> G, stdic
		if found==False:
                	print "Warning:",sp, "not found in stage dictionary."
	print >> G, ""
	print >> G, "#"
	print >> G, "# list any ontology terms used in the data sheet"
	print >> G, "# for location_{country,ADM1,ADM2,description}, attractant"
	print >> G, "# also the 'pool' term must be provided"
	print >> G, "#"
	print >> G, "study_terms :"
	print >> G, "  pool : EFO:0000663"
	att_list=args.a
	sp_att=att_list.split(",")
	for sp in sp_att:
                #print(sp)
		found=False
                for attdic in att_dic:
                        if sp.lower() in attdic.lower():
				found=True
                                print >> G, attdic
		if found==False:
			print "Warning:",sp, "not found in attractant dictionary."
	gon_list=args.g
	if gon_list is not None:
		sp_gon=gon_list.split(",")
        	for sp in sp_gon:
                	#print(sp)
			found=False
                	for gondic in gon_dic:
                        	if sp.lower() in gondic.lower():
					found=True
                                	print >> G, gondic
		if found==False:
                	print "Warning:",sp, "not found in feeding and gonotrophic dictionary."
G.close()
