/*binds NewList to a list formed by interchanging pairs of members of the list.
If the list has an odd number of members, then the final one is left unchanged at the end of the NewList */
%spin2(List, NewList).

%Base cases
spin2([],[]).
spin2([X], [X]).

%Recursive case
spin2([X, Y|L1], [Y, X|L2]) :- spin2(L1, L2).





/* binds MaxItem to the value of the largest number in the list */
%lgst(List, MaxItem).

%Base cases
lgst([], list_is_empty).
lgst([X], X).

%Recursive cases
lgst([X, Y|L1], MAX) :-  X>Y, lgst([X|L1], MAX).
lgst([X, Y|L1], MAX) :-  X=<Y, lgst([Y|L1], MAX).





/*binds MaxPos to the position of the first occurrence of the largest number in the list. The first item has position 1*/
%lgst_pos(List, MaxPos).

%Base cases
lgst_pos([], list_is_empty).
%lgst_pos([X], 1).
lgst_pos([X|L1], 1) :-  lgst([X|L1], X).

%Recursive case
lgst_pos([X|L1], INDEX) :-  \+ lgst([X|L1], X), lgst_pos(L1, INDEX1), INDEX is INDEX1 + 1.





/* binds NewList to a list that consists of the original List with first occurrence of the largest item removed */
%remove_lgst(List, NewList).

%Base cases
remove_lgst([], list_is_empty).
remove_lgst([X], []). %if list only contains one element, return empty list
remove_lgst([X|L1], L1) :- lgst([X|L1], X). %return L1 if largest value is the head

%Recursive case
remove_lgst([X|L1], [X|L2]) :- \+ lgst([X|L1], X), remove_lgst(L1, L2). %if largest value not in head, cut off head to recursively search for it