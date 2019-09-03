#To run the program:
#Have a file named 'links.dat', where
#line 1 contains the name of the .json file. Ex: RankingSquash.json
#line 2 contains the spreedsheet ID. Ex: 1NwVZDsYIb7dNAI6SFI5mSaYdSz3BwrM7UoBW0DG-Pb4


#To change initial month, go to function generate_months_list, line 296


from math import *
import numpy as np
import pandas as pd
import codecs
import csv
import gspread					#Google credentials
from oauth2client.service_account import ServiceAccountCredentials #Google credentials
from datetime import datetime, date #Working with dates



class Player:

	def __init__(self, name, pos_init ,pos18, pos17):
		self.name = name
		self.position = pos_init
		self.initial_pos = pos_init
		self.pos18 = pos18
		self.pos17 = pos17
		self.victory = 0
		self.victory_months = [0] * 12
		self.loss = 0
		self.loss_months = [0] * 12
		self.games_won = 0
		self.games_lost = 0
		self.games_ratio = 0
		self.matches_played = 0
		self.match_ratio = 0
		self.challenged_months = [0] * 12
		self.got_challenged_months = [0] * 12
		self.progress = 0
		self.months_idle = []



	def got_challenged(self, date):					#times that got challenged
		self.got_challenged_months[ -1 + date.month ] += 1



	def challenged(self, date):						#times that challenged
		self.challenged_months[ -1 + date.month ] += 1


	def ratios(self):								#calculate ratios
		self.games_ratio 	= self.games_won - self.games_lost
		self.matches_played = self.victory + self.loss
		self.match_ratio 	= self.victory - self.loss
		self.progress 		= self.position - self.initial_pos


	def won(self, date, winner_score, loser_score):  #account for win
		self.victory 							+= 1
		self.victory_months[ -1 +date.month ] 	+= 1
		self.games_won 							+= winner_score
		self.games_lost 						+= loser_score


	def lost(self, date, winner_score, loser_score):	#account for loss
		self.loss 							+= 1
		self.loss_months[ -1 + date.month ] += 1
		self.games_won 						+= loser_score
		self.games_lost 					+= winner_score


def first(iterable, default=None):
	for item in iterable:
		return item
	return default


#get spreadsheet online, and export it as an array
def get_sheet():

	with open('links.dat', newline='') as csvfile:
	    input_file = list(csv.reader(csvfile))

	# print(input_file)
	scope = ['https://spreadsheets.google.com/feeds']
	credentials = ServiceAccountCredentials.from_json_keyfile_name(input_file[0][0], scope)

	docid = input_file[1][0]

	client = gspread.authorize(credentials)
	ss = client.open_by_key(docid)
	spreadsheet = ss.get_worksheet(0)

	raw_results = spreadsheet.get_all_values()

	for i in range(len(raw_results)):
		print(raw_results[i])

	return raw_results



#Create players list
def create_players():
	pl_list = []

	ailton = 			Player('Ailton'				,7 		,7, 12); 				pl_list.append(ailton)
	akira = 			Player('Akira'				,35		,18,15 ); 				pl_list.append(akira)
	alaim = 			Player('Alaim'				,15 	,15, 20); 				pl_list.append(alaim)
	alexandre = 		Player('Alexandre'			,31		,10,10);				pl_list.append(alexandre)
	andre = 			Player('André' 				,27 	,100 ,100 );			pl_list.append(andre)
	baltazar = 			Player('Baltazar'			,2 		,3 , 3); 				pl_list.append(baltazar)
	bateli= 			Player('Bateli'				,12 	,13 , 11); 				pl_list.append(bateli)
	carlao = 			Player('Carlão'				,14 	,22 ,21 ); 				pl_list.append(carlao)
	cezinha  = 			Player('Cezinha'			,38		,29, 100);				pl_list.append(cezinha)
	claudio = 			Player('Claudio'			,21 	,100, 100);				pl_list.append(claudio)
	coquinho = 			Player('Coquinho'			,32		,11 ,9 ); 				pl_list.append(coquinho)
	eduardo = 			Player('Eduardo'			,24 	,33 ,33 ); 				pl_list.append(eduardo)
	eleazar = 			Player('Eleazar'			,40		,32 ,31 ); 				pl_list.append(eleazar)
	enrico = 			Player('Enrico'				,20 	,28 ,28 ); 				pl_list.append(enrico)
	evandro = 			Player('Evandro'			,39		,30,29 ); 				pl_list.append(evandro)
	fabio = 			Player('Fabio'				,28 	,35, 35); 				pl_list.append(fabio)
	fabioMaia = 		Player('Fabio Maia'			,18 	,27, 27); 				pl_list.append(fabioMaia) 
	fellipo = 			Player('Fellipo' 			,26 	,100 ,100);				pl_list.append(fellipo)
	fernando = 			Player('Fernando'			,25 	,31 ,30 );				pl_list.append(fernando)
	graciano = 			Player('Graciano'			,33		,12, 16 );				pl_list.append(graciano)
	gustavo = 			Player('Gustavo'			,1 		,1 ,1 );				pl_list.append(gustavo)
	gustavoBazani = 	Player('Gustavo Bazani'		,43		,38 ,100 );				pl_list.append(gustavoBazani)
	israel = 			Player('Israel'				,10 	,21 ,100 );				pl_list.append(israel)
	joseIlton = 		Player('Jose Ilton'			,6 		,6 ,6 );				pl_list.append(joseIlton)
	joseLuis = 			Player('Jose Luis'			,4 		,5 ,5 ); 				pl_list.append(joseLuis)
	julio = 			Player('Julio'				,17 	,24, 22);				pl_list.append(julio)
	leandro = 			Player('Leandro'			,13 	,16, 13);				pl_list.append(leandro)
	leandroMedeiros = 	Player('Leandro Medeiros'	,37		,23, 24);				pl_list.append(leandroMedeiros)
	leonardoFinoti = 	Player('Leonardo Finoti'	,41		,36, 100);				pl_list.append(leonardoFinoti)
	lindomar = 			Player('Lindomar'			,22 	,34, 34);				pl_list.append(lindomar)
	luisMiro = 			Player('Luis Miró'			,34		,17, 14);				pl_list.append(luisMiro)
	mario = 			Player('Mario'				,9 		,26, 26);				pl_list.append(mario)
	paje = 				Player('Pajé'				,42		,37, 101);				pl_list.append(paje)
	pascoal  = 			Player('Pascoal'			,3 		,2, 2);					pl_list.append(pascoal)
	paulinho = 			Player('Paulinho'			,36		,19, 17);				pl_list.append(paulinho)
	robinson = 			Player('Robinson'			,30		,9, 8);					pl_list.append(robinson)
	rodrigoArgento  = 	Player('Rodrigo Argento'	,19 	,25, 25);				pl_list.append(rodrigoArgento)
	rodrigoPaulino = 	Player('Rodrigo Paulino'	,11 	,14, 19);				pl_list.append(rodrigoPaulino)
	rogerio = 			Player('Rogerio'			,29		,4, 4);					pl_list.append(rogerio)
	romanholli = 		Player('Romanholli'			,5 		,100,100 );				pl_list.append(romanholli)
	romani = 			Player('Romani'				,8 		,8, 7);					pl_list.append(romani)
	rosiane = 			Player('Rosiane' 			,23 	,100, 100); 			pl_list.append(rosiane)
	vanderlei  = 		Player('Vanderlei'			,16 	,20, 23);				pl_list.append(vanderlei)

	#Ivo 2017 = 2018: 36
	#Chicão - 2017: 18; 2018: 21
	#"Giovanni":pldata(29,32),
   
	return pl_list




#analyze each match individidualy. The import is a line from the resuts array.
def new_game(match, players_list):											
	date = datetime.strptime(match[0], '%m/%d/%Y %H:%M:%S')					#Gets the date of the match in correct format
	winner = first(x for x in players_list if x.name == match[1])	#Retrieves the object with attribute .name == winner name
	loser = first(x for x in players_list if x.name == match[2])		#Retrieves the object with attribute .name == loser name
	if match[3] == '3 a 0':
		winner_score = 3
		loser_score =  0
	elif match[3] == '3 a 1':
		winner_score = 3
		loser_score = 1
	else:
		winner_score = 3
		loser_score = 2

	return [date, winner, winner_score, loser, loser_score]			#returns formated list with data



def arrange_results(match_list, players_list):						#iterates the function new_game for all results
	results = []
	for i in range(1, len(match_list)):
		results.append( new_game(match_list[i], players_list) )

	return results




#analyse each match
def points_change(match, players_list):								
	date, winner, winner_score, loser, loser_score = match 							#gets the formated results array
	winner.won(date, winner_score, loser_score) 			#accounts for win
	loser.lost(date, winner_score, loser_score)				#accounts for loss

	if winner.position > loser.position: 					#if the winner is the challenger
		winner.challenged(date)
		loser.got_challenged(date)


		diff = winner.position - loser.position 			#calculates diference in position
		for i in range(1, 1+diff): 							#reduces 1 position for the loser and everyone in between the winner and loser
			middle_player = first(x for x in players_list if x.position == winner.position - i)
			middle_player.position += 1

			middle_player.ratios()
		winner.position -= diff
	
	else:
		winner.got_challenged(date)
		loser.challenged(date)

	winner.ratios()
	loser.ratios()




#returns a list of all the player that did not challenged in the last month, and another for all that challenged
def generate_idle_player_list(month, players):
	idle_list = []
	challenger_list = []

	for i in range(len(players)):
		if players[i].challenged_months[month - 1] > 0:
			challenger_list.append(players[i])

	for i in range(1 , len(players)):
		if players[i].challenged_months[month-1] == 0: #idle don't last players, and the first player
			idle_list.append(players[i])

	
	return idle_list, challenger_list  #returns list of all players (except #1) that did no challenge this month



#after all the idles get downgraded, calculates the empty positions
def generate_empty_positions(players, idles):
	empty_positions = []
	

	for pos in range(2, idles[-1].position): 	#iterates for all players from #2
		pos_empty = True
		for j in range(len(idles)):
			if idles[j].position == pos:
				pos_empty = False

		if pos_empty:
			empty_positions.append(pos)
	return empty_positions 						#Return all positions that are empty, after the idles got downgraded





def is_there_empty_pos(players): 				#After idle reordering, checks if there is any empty positions
	
	for pos in range(len(players), 1, -1):
		empty = True
		for i in range(len(players)):
			if players[i].position == pos:
				empty = False

		if empty:
			return True, pos


	return False, 0				#Returns if there is empty position, and what is the empty position


def reorders(players, empty_pos):					#Reorders the players, to fill all the empty positions
	for i in range(len(players)):
		if players[i].position > empty_pos:
			players[i].position -= 1






def idle_points_change(month, players):
	idles, challengers  = generate_idle_player_list(month, players)


	for i in range(len(idles)): 									#reduces idle points
			idles[i].position += 2
			idles[i].months_idle.append(month)


	empty_positions = generate_empty_positions(players, idles)
	print(empty_positions)


	for i in range(len(challengers)):
		up_challenger = first(x for x in challengers if x.position > empty_positions[i])		#increases challenger points
		up_challenger.position = empty_positions[i]




	empty_bol, empty_pos = is_there_empty_pos(players)						#Reorders to fill empty positions
	while empty_bol:
		reorders(players, empty_pos)
		empty_bol, empty_pos = is_there_empty_pos(players)
		

	'''
	para um challenger, procurar o proximo idle acima
	Quem não jogou perde 2 pontos


'''




#Do a months process
def month_process(results, month, players_list):
	for i in range(len(results)):
		if results[i][0].month == month:
			points_change(results[i], players_list)			#Matches from a month
			

	players_list.sort(key=lambda x:x.position, reverse=False)	#Orders players

	idle_points_change(month, players_list)						#Idle reordering

	players_list.sort(key=lambda x:x.position, reverse=False)

	return players_list


def generate_months_list():
	initial_month = 8
	today = date.today()
	end_month = today.month

	return range(initial_month, end_month) #returns list with every month until the month previous with the actual month



#Does it for every month
def rank(results, players_list):
	for i in generate_months_list():
		players_list = month_process(results, i, players_list)

	return players_list






def print_rank(players):
	with open('updated_rank.csv', 'w') as rankfile:
		print('Posição , Nome , Saldo de jogos , Jogos jogados , Jogos ganhos , Saldo de games , Games ganhos , Progresso no ranking , Posição inicial , Desafios Total, Meses que não desafiou, Desafios no último mês ', file=rankfile)
		for i in range(len(players)):
			print('{} , {} , {} , {} , {} , {} , {} , {} , {}, {} , {} , {} '.format(players[i].position, 	players[i].name, 			players[i].match_ratio, 
				players[i].matches_played, 				players[i].victory, 					players[i].games_ratio, 	players[i].games_won,
				players[i].progress, 					players[i].initial_pos, 				np.sum(players[i].challenged_months), 	len(players[i].months_idle),
				players[i].challenged_months[date.today().month - 1] ), file=rankfile)

			print('{} , {} , {} , {} , {} , {} , {} , {} , {}, {} , {} , {} '.format(players[i].position, 	players[i].name, 			players[i].match_ratio, 
				players[i].matches_played, 				players[i].victory, 					players[i].games_ratio, 	players[i].games_won,
				players[i].progress, 					players[i].initial_pos, 				np.sum(players[i].challenged_months), 	len(players[i].months_idle),
				players[i].challenged_months[date.today().month - 1]    ))





def main():
	match_list = get_sheet()
	players_list = create_players()

	results = arrange_results(match_list, players_list)
	ranking = rank(results, players_list)
	print_rank(ranking)


main()

