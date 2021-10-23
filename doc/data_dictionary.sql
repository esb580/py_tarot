-- Run this script
-- mysql>source ~/git_repos/scripts/py_tarot/doc/data_dictionary.sql;

-- Create Database
create database py_tarot;

-- Change to New Database
use py_tarot;

-- Create Tables
create table suits (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
suit_name varchar(20),
suit_element int
);

create table cards (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
card_name varchar(20),
card_arcana char(5),
card_number char(5),
card_suit int,
card_meaning_upright text,
card_meaning_reversed text
);

create table symbols (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
symbol_name varchar(50),
symbol_meaning text
);

create table elements (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
element_name char(5),
element_properties text
);

-- Load Data
insert into elements (element_name) values ('Fire');
insert into elements (element_name) values ('Water');
insert into elements (element_name) values ('Air');
insert into elements (element_name) values ('Earth');
insert into suits (suit_name, suit_element) values ('Wands', 1);
insert into suits (suit_name, suit_element) values ('Cups', 2);
insert into suits (suit_name, suit_element) values ('Swords', 3);
insert into suits (suit_name, suit_element) values ('Pentacles', 4);
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Fool', 'Major', '0', 'Beginnings; Innocence; Clear Conscience', 'Vanity; Foolishness; Indiscretion; Inanity'); 
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Magician', 'Major', 'I', 'Power; Adroitness; Construction', 'Destruction; Bane; Untapped Potential');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('High Priestesss', 'Major', 'II', 'Inner Voice; Intuition; Divine Truth; Wisdom; Unconscious', 'Loss of Self; Repression; Secrets; Hidden Agendas');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Empress', 'Major', 'III', 'Beauty; Fertility; Nurturing; Luxury; Creativity', 'Smothering; Excess; Selfishness');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Emporor', 'Major', 'IV', 'Structure; Ambition; Authority; Rationality', 'Chaos; Anger; Tyranny; Domination');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Hierophant', 'Major', 'V', 'Tradition; Legacy; Society; Organized Religion', 'Servitude; Convention; Blind Faith');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
('Lovers', 'Major', 'VI', 'Choices; Union; Love; Relationship', 'Indecision; Ending of Relationship; Conflict');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Chariot', 'Major', 'VII', 'Self Discipline; Success', 'Loss of Direction; Loss of Will; Lack of Discipline');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Strength', 'Major', 'VIII', 'Courage; Inner Strengh; Conviction; Compassion', 'Doubt; Pride; Weakness; Cowardice');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Hermit', 'Major', 'IX', 'Contemplation; Solitude; Insight; Awareness', 'Isolation; Withdrawl; Loneliness; Rejection');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Wheel of Fortune', 'Major', 'X', 'Fate; Karma, Destiny; Fortune; Cycles', 'Bad Luck; Lack of Control; Clinging to Control');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Justice', 'Major', 'XI', 'Truth; Fairness; Law; Clarity; Cause and Effect', 'Dishonesty Unaccountability; Unfairmess');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Hanged Man', 'Major', 'XII', 'Sacrifice; Suspension; Release; Martyrdom', 'Stalling; Fear of Scrifice; Needless Sacrifice');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Death', 'Major', 'XIII', 'End of Cycle; New Beginnings; Change; Metamorphosis', 'Fear of Change; Holding On; Stagnation; Decay');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Temperance', 'Major', 'XIV', 'Middle Path; Patience; Finding Meaning', 'Extremes; Excess Lack of Balance; Lack of Harmony');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Devil', 'Major', 'XV', 'Materialism; Playfulness; Pleasure; Addiction', 'Freedom; Release; Restoring Control');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Falling Tower', 'Major', 'XVI', 'Upheaval; Disaster; Foundational Shift', 'Disaster Avoided; Delaying Disaster; Fear of Suffering');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Star', 'Major', 'XVII', 'Hope; Faith; Rejuvenation; Rebuilding; Healing', 'Discouragement; Faithlessness; Insecurity');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Moon', 'Major', 'XVIII', 'Unconscious; Illusions; Intuition; Unclarity', 'Confusion; Fear; Misinterpretation');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Sun', 'Major', 'XIX', 'Joy; Success; Celebration; Pleasure', 'Negativity; Depression; Sadness');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('Judgement', 'Major', 'XX', 'Reflection; Reckoning; Awakening', 'Lack of Self Awareness; Doubt; Self Loathing');
insert into cards (card_name, card_arcana, card_number, card_meaning_upright, card_meaning_reversed) values 
	('World', 'Major', 'XXI', 'Fulfillment; Harmony; Completion', 'Incompletion; Lack of Closure; Emptiness');


