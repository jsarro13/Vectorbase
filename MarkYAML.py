#/usr/bin/python
#MarkYAML v1 04-18-2019
#Written by Joseph Sarro
#This is an interactive script to make a YAML file. To run type "python MarkYAML.py"
#Last edit 04-18-2019
import os
#f = open('2017_full_Data.txt', 'r')
print "Enter a file name."
G= open('SAF_2017.out.txt','w')
file = raw_input("")
G= open(file,'w')
#being dictionary creations#
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
"  Aedes campestris : VBsp:0000994",
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
"  Anopheles quadrimaculatus s.l. ",
"  Anopheles quadrimaculatus s.s. ",
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
"  Culex pipiens-restuans (Mixed) ",
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
print "Will this be a fully specified config file?"
full=raw_input("(y/n)")
#print full
#Note: This does not work on first input. Look into this.
if (full !="y") or (full !="n"):
	FULL = False
	while FULL == False:
		print "please enter y or n."
		full=raw_input("(y/n)")
		if full =="y" or full =="n":
			FULL=True
if full=="y":
	print "Yes"
elif full=="n":
	#print "No"
	#print >> G, "tester"
	print >> G, "#"
	print >> G, "# minimal config file"
	print >> G, "#"
	print >> G, "# not enough to make a fully functional i_investigation sheet"
	print >> G, "# see test-01-full-inv.yaml for that"
	print >> G, "#"
	print >> G, ""
	print "Enter study indentifier."
	study_id=raw_input("")
	print >> G, "study_identifier :",study_id
	print "Enter study title."
	study_title=raw_input("")
	print >> G, "study_title :",study_title
	print >> G, ""
	print >> G, ""
	print >> G, "#"
	print >> G, "# list the species expected to be identified"
	print >> G, "# and their VBsp:nnnnnnn ontology term accessions"
	print >> G, "#"
	print >> G, "study_species :"
	print "Enter comma seperated list of species. Do not add spaces in between."
	species_list=raw_input("")
	sp_split=species_list.split(",")
	for sp in sp_split:
		#print(sp)
		for spdic in species_dic:
			if sp in spdic:
				print >> G, spdic
G.close()
