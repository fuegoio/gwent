# Gwent

This project is a Gwent game developped in Python for the back-end and VueJS for the front-end.

## How to lauch the project

To launch this project, you can either launch the back-end and the front-end or just the back-end, as we have a live version of the front-end running polling your localhost server.

#### Back-end

To launch the backend, we need first to create a virtualenv and install the requirements once :

```
$ cd back/
$ virtualenv --python=python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Then to launch it everytime :

```
$ cd back/
$ source venv/bin/activate
(venv) $ python run.py
```

#### Front-end

The front-end is developped in VueJS and needs Node to run. If you don't want to launch the local front-end, you can access a deployed one at [https://gwent-pooa.netlify.com/](https://gwent-pooa.netlify.com/).

To launch the front, we need first to install the requirements once :

```
$ cd front/
$ npm install
```

Then to launch it everytime :

```
$ cd front/
$ npm run serve
```

#### Pycharm configuration

In this project, Pycharm is already configured with the right run configurations : the backend and
the frontend ones.

#### Play

You can now play ! As the server is on your computer, you need to play against yourself, and therefore open two tabs
on your browser with two different names.

## How to play

Your deck has been drawn randomly from available cards of your faction, and you can re-draw (mulligan) two cards prior to the start of the game.
Each game contains three rounds and the first player to win two rounds wins the game.
To end a round from your perspective, pass on your turn
One of the important things to remember is that the 10 cards you start a Gwent game with must last you through the duration of the three rounds. You do not get a full, 10 card deck each round. This is where strategy really comes into play.

There are several different types of Gwent cards to be concerned with, and each card you play gets placed into one of the rows on the board. The most common card types that you'll run into are Close Combat, Long Range and Siege. Each of these cards has a value, and that value helps to determine your overall score. Your combined score between all of your rows is matched against your opponent's combined score to determine who wins the round.

You're not just trying to win individual rows (Close Combat, Long Range and Siege), but end each round with an overall score higher than your opponent. You could be winning the Siege row by a score of eight to six, but if your opponent is winning the Close Combat row eight to five, they are winning the overall round by a score of 14 to 13.

### Special Abilities Explained

* Morale Boost - Adds +1 to all of the cards in the row
* Scorch - Will destroy all of the highest value cards in play on either side of the board
* Scorch: Close Combat - Destroys all of the highest value Close Combat cards in play
* Spy - Place it on your opponent's side of the board in exchange for drawing two cards from your deck
* Hero - Immune to any special effects or other card's abilities
* Tight Bond - Place it next to a card with the same name to double their values
* Medic - After playing this card, choose one from your discarded pile and play it instantly
* Agile - Place this card in either the Close Combat or Long Range row
* Muster - Find any cards with the same name in your deck and play them instantly

### Weather Cards Explained
* Biting Frost - Power of all Close Combat cards set to 1
* Impenetrable Fog - Power of all Long Range cards set to 1
* Torrential Rain - Power of all Siege cards set to 1
* Clear Weather - Will clear all weather effects on the board
* You might be asking when you would play a Weather card. Well, imagine that you have two Close Combat Cards on the board, both with a value of two (for a total of four in the Close Combat row). Your opponent then plays a single Close Combat card with a value of five. You could play the Biting Frost card, setting all Close Combat cards to a value of one. This would mean that you are now winning that row with a score of two, while your opponent only has one point.


