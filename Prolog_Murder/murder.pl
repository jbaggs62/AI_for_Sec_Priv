main :- write('This Prolog program solves a murder.'),
write(' This Prolog program is written into the murderer.pl file').


/* Rules and Facts. */

person( allan, 25, m, football_player).
person( allan, 25, m, butcher).
person( barbara, 22, f, hairdresser).
person( bert, 55, m, carpenter).
person( john, 25, m, pickpocket).

had_affair( barbara, john).
had_affair( barbara, bert).
had_affair( susan, john).

killed_with( susan, club).
motive( money).
motive( jealousy).
    
smeared_in( catherine, blood).
smeared_in( allan, mud).
     
owns( bert, wooden_leg).
owns( john, pistol).

/* Background knowledge for murder. */

operates_identically( wooden_leg, club).
operates_identically( bar, club).
operates_identically( pair_of_scissors, knife).
operates_identically( football_boot, club).

owns_probably(X, football_boot) :- person(X,_,_,football_player).
owns_probably(X, pair_of_scissors) :- person(X,_,_,_).
owns_probably(X, Object) :- owns(X, Object).


/* Suspect all those who own a weapon with which susan could possibly have been killed. */

suspect(X) :- killed_with( susan, Weapon), operates_identically(Object, Weapon), owns_probably( X, Object).
    
/*Suspect some that have had affair with susan. */
               
suspect(X) :- motive( jealousy), person(X,_,m,_), had_affair( susan,X).

/* Suspect females who have had an affair with a man susan knew.*/

suspect(X) :- motive( jealousy), person( X,_,f,_), had_affair(X,Man), had_affair(susan,Man).

/* Suspect pickpockets whose motive could be money.*/

suspect(X) :- motive(money), person(X,_,_,pickpocket).    


% Commands to see who is the person
% write('This Prolog program solves a murder.').
% write('Is allan a suspect?'),  suspect(allan).
% write('Is barbara a suspect?'),  suspect(barbara).
% write('Is bert a suspect?'),  suspect(bert).
% write('Is john a suspect?'),  suspect(john).
