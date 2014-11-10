For running the script open terminal and change directory to foleder "RankingRecommendations"
If folder is inside directory Home->App->eatScrambles

	In Linux or Mac:	
1:		cd ~/Home/App/eatScrambles/RankingRecommendations/

	In windows:
1:		cd Home\App\eatScrambles\RankingRecommendations\

------------------------------
Run list command to see all files where you currently are. You must see the 'tests.py' and 'makeRecommend.py' in local directory.
2:	ls
Readme.txt        data.py           localdata.py      recomends.py
exampleRunLog.txt makeRecomend.py   tests.py ....


------------------------------
The two scripts "tests.py" and "makeRecommend.py" are main scripts. Run them with -h option to see details about them.

3:	python3 tests.py -h

usage: tests.py [-h] [-v] [-t {food,movie}] [-c CRITIC] [-q]

Recomendations and Ranking Tests

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbose mode processing shown
  -t {food,movie}, --test {food,movie}
  						testcase name

  -c CRITIC, --critic CRITIC
                          critic name

  -q, --quit            quit now


-------------------------------
Run tests without any option, will choose critique at random and run for it
4:	python3 tests.py
movie
running test


++++++++++++++++++++++++++++++++++++++++++++++++++++++
Top 3 matches for critic Nutan in % for category movie

Miki Firangi : 96.379568 %
Rajkumar : 41.176471 %
Waheeda Rehman : 39.605902 %

++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++


The answer means Wiki Firangi and Nutan have 96.379568% match in choices with each others.



------------------------------
For giving a critique name use -c option
5:	python3 tests.py -c 'Rajkumar'

++++++++++++++++++++++++++++++++++++++++++++++++++++++
Top 3 matches for critic Rajkumar in % for category movie

Alok : 92.447345 %
Waheeda Rehman : 59.408853 %
Salma Agha : 56.694671 %

++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++


Another way of running is from python terminal, better suited if you want to try your own data
5:	python3

>>>
>>> import argparse, random
>>> from tests import tested, testTopNMatches

test data of movies is under data file import it
>>> from data import *
if you need to work on your personal data, write it in file localdata.py and import it
>>> from localdata import *


Import RModel class and create object for it. This object allows us to recommend and rank or do other things with data
>>> from recomends import RModel as RM
>>> rmnd=RM()

Lets see what is there in our movie data example
Assign it to critics variable
>>> critics=movie_critics

>>> critics
{'Alok': {'Maachis': 4.5, 'Singing in the Rain': 4.0, 'The Bridge on River Kwai': 1.0}, 'Rajkumar': {'Saaheb': 2.0, 'Singing in the Rain': 3.0, 'The Shootist': 3.0, 'Saagar': 3.0, 'The Bridge on River Kwai': 2.0, 'Maachis': 4.0}, 'Salma Agha': {'Saaheb': 3.0, 'Maachis': 3.5, 'The Shootist': 4.5, 'Singing in the Rain': 4.0, 'The Bridge on River Kwai': 2.5}, 'Waheeda Rehman': {'Saaheb': 3.0, 'Singing in the Rain': 3.5, 'The Shootist': 3.0, 'Saagar': 2.5, 'The Bridge on River Kwai': 2.5, 'Maachis': 3.5}, 'Miki Firangi': {'Singing in the Rain': 5.0, 'Maachis': 4.0, 'The Shootist': 3.0, 'Saagar': 3.0, 'The Bridge on River Kwai': 3.5}, 'Nutan': {'Saaheb': 1.5, 'Singing in the Rain': 5.0, 'The Shootist': 3.0, 'Saagar': 3.0, 'The Bridge on River Kwai': 3.5, 'Maachis': 3.5}, 'Puneet Issar': {'Singing in the Rain': 3.5, 'Maachis': 3.0, 'The Shootist': 4.0, 'Saagar': 2.5}}


Whats recommended for critic 'Alok', score is weighted average
>>>
>>> rmnd.getRecommendations(critics, 'Alok')
[(3.3477895267131013, 'The Shootist'), (2.8325499182641614, 'Saagar'), (2.5309807037655645, 'Saaheb')]


Transform data from person to items, providing details items relate with person
>>> movies=rmnd.transformPrefs(critics)
>>> movies
{'Saaheb': {'Waheeda Rehman': 3.0, 'Nutan': 1.5, 'Rajkumar': 2.0, 'Salma Agha': 3.0}, 'Maachis': {'Alok': 4.5, 'Rajkumar': 4.0, 'Salma Agha': 3.5, 'Waheeda Rehman': 3.5, 'Nutan': 3.5, 'Miki Firangi': 4.0, 'Puneet Issar': 3.0}, 'The Shootist': {'Rajkumar': 3.0, 'Salma Agha': 4.5, 'Waheeda Rehman': 3.0, 'Miki Firangi': 3.0, 'Nutan': 3.0, 'Puneet Issar': 4.0}, 'Saagar': {'Waheeda Rehman': 2.5, 'Nutan': 3.0, 'Miki Firangi': 3.0, 'Rajkumar': 3.0, 'Puneet Issar': 2.5}, 'The Bridge on River Kwai': {'Alok': 1.0, 'Rajkumar': 2.0, 'Salma Agha': 2.5, 'Waheeda Rehman': 2.5, 'Nutan': 3.5, 'Miki Firangi': 3.5}, 'Singing in the Rain': {'Alok': 4.0, 'Rajkumar': 3.0, 'Salma Agha': 4.0, 'Waheeda Rehman': 3.5, 'Nutan': 5.0, 'Miki Firangi': 5.0, 'Puneet Issar': 3.5}}
>>>
>>>

What is the top matches for a movie. Score bw(+1 and -1). If someone likes "Maachis" then got least chance of liking movies in -ve values. 
>>> rmnd.topMatches(movies, 'Maachis')
[(0.7637626158259785, 'Saagar'), (0.11180339887498941, 'Singing in the Rain'), (-0.3333333333333333, 'Saaheb'), (-0.5663521139548527, 'The Shootist'), (-0.6454972243679047, 'The Bridge on River Kwai')]


By identifying recommendations for a movie, we can suggest these persons for watching particular movie. Note person name we get here havn't yet seen this movie :) tht's why we recommend them to watch it. 
>>> rmnd.getRecommendations(movies, 'Saagar')
[(3.610031066802183, 'Alok'), (3.44362:41497684494, 'Salma Agha')]
>>>

