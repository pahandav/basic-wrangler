0POKE 82,0:? CHR$(125):Z=0:Y=1:A=Z:T=Z:V=13:C=44:D=Z:E=Z:R=Z:X=2:I=Z:J=Z:DIM A(C):G=100:H=4:K=512:L=32:U=16:N=255:O=99:F=65535
1Q=6:S=3841:B=4096:M=39:P=Y:W=Z:DIM A$(Y):F. I=Z TO C:READ R:A(I)=R:N. I:? "WELCOME TO THE BATTLE SYSTEM TEST!":?:?
2? "TWO SOLDIERS APPROACH.":?
3IF A(V*A)=Z THEN 6
4IF A=Z THEN 22
5T=Z:G. 40
6IF A(Z)=Z THEN 89
7A=A+Y:IF A<>Z THEN T=Z
8IF A(V*A)=Z THEN A=A+Y
9IF A>X THEN A=Z
10D=Z:IF A(V*Y)=Z THEN D=D+Y
11IF A(V*X)=Z THEN D=D+Y
12IF D=X THEN 14
13G. 3
14? "YOU ARE VICTORIOUS.":?:W=W+Y:A=Z:T=Z:IF W>=10 THEN GOS. 20
15F. I=Y TO X:A(I*V)=A(I*V+Y):N. I:GOS. 79:IF R<12.5 THEN ? "YOU OBTAINED A POTION!"
16IF R<12.5 THEN ?
17IF R<12.5 THEN P=P+Y
18IF P>O THEN P=O
19G. 2
20GOS. 79:IF R>=25 THEN RET.
21F. I=V TO M-Y:A(I)=A(I)*1.5:N. I:? "THE ENEMIES HAVE POWERED UP!":?:RET.
22?:? A(Z);"/";A(Y);" HP":? A(X);"/";A(3);" MP":?:? "(A) ATTACK":? "(M) MAGIC":? "(I) ITEMS":? "(Q) QUIT":I. A$
23IF A$="A" THEN 28
24IF A$="M" THEN 32
25IF A$="I" THEN 37
26IF A$="Q" THEN 90
27G. 22
28GOS. 80:IF C=Z THEN 22
29IF C>X THEN 28
30IF C<Z THEN 28
31G. 40
32?:? "(1) LIGHTNING - ";A(M);" MP":? "(2) CURE - ";A(M+3);" MP":? "WHICH SPELL DO YOU WANT TO CAST?":? "TYPE (0) TO GO BACK."
33I. A$:C=VAL(A$):IF C=Y THEN 60
34IF C=X THEN 70
35IF C=Z THEN 22
36G. 32
37?:? "(1) POTION - ";P:? "WHICH ITEM DO YOU WISH TO USE?":? "TYPE (0) TO GO BACK.":I. A$:C=VAL(A$):IF C=Y THEN 74
38IF C=Z THEN 22
39G. 37
40C=((A(A*V+10)/H)+(A(A*V+5)))+A(A*V+7)-A(T*V+7):GOS. 79:I=A(A*V+11):GOS. 85:IF D>R THEN C=N
41I=A(T*V+11):GOS. 85:IF D>R THEN C=N
42IF R<C THEN 46
43IF T>Z THEN ? "YOUR ATTACK MISSED!"
44IF T=Z THEN ? "SOLDIER ";A;" MISSED YOU!"
45?:G. 6
46D=A(A*V+H):E=A(A*V+12):C=D+((D+E)/L)*((D*E)/L):D=((U*(K-A(T*V+Q)))*C)/(U*K):C=(A(A*V+11)+A(A*V+12)-A(T*V+12))/H:GOS. 86
47IF R<=C THEN 49
48G. 50
49D=INT(D*X)
50D=INT(D*(S+(RND(Y)*N))/B):IF D=Z THEN D=Y
51A(T*V)=A(T*V)-D:IF A(T*V)<=Z THEN A(T*V)=Z
52IF A<>Z THEN 56
53? "YOU HIT SOLDIER ";T;" FOR ";D;" HP.":?:IF A(T*V)<>Z THEN 55
54? "YOU DEFEATED SOLDIER ";T:?
55G. 6
56IF D>Z THEN GOS. 87
57? "SOLDIER ";A;" HIT YOU FOR ";D;" HP.":?:IF A(Z)<>Z THEN 59
58? "YOU DIED.":?
59G. 6
60E=Z:D=Z:IF A(M)>A(X) THEN 69
61A(X)=A(X)-A(M):GOS. 80:IF C=Z THEN 32
62IF C>X THEN 60
63IF C<Z THEN 60
64C=A(M+X)+A(A*V+12)-((A(T*V+12))/X)-Y:GOS. 79:IF R<C THEN GOS. 88
65IF R>C THEN 67
66D=(A(M+Y)*(K-A(T*V+9))*C)/(U*K)
67IF D>Z THEN 50
68? "YOUR SPELL MISSED.":?:G. 6
69?:? "YOU DON'T HAVE ENOUGH MP TO CAST THAT SPELL.":G. 32
70E=3:IF A(M+3)>A(X) THEN 69
71A(X)=A(X)-A(M+3):GOS. 88:D=C+22*A(M+Y+E):D=INT(D*(S+(RND(Y)*N))/B):?:? "YOU HAVE BEEN HEALED FOR ";D;" HP.":?:A(Z)=A(Z)+D
72IF A(Z)>A(Y) THEN A(Z)=A(Y)
73G. 6
74IF P=Z THEN ?
75IF P=Z THEN ? "YOU HAVE NO POTIONS."
76IF P=Z THEN 22
77A(Z)=A(Z)+G:IF A(Z)>A(Y) THEN A(Z)=A(Y)
78P=P-Y:?:? "YOU HAVE BEEN HEALED FOR 100 HP.":?:G. 6
79R=INT(RND(Y)*G):RET.
80?:F. I=Y TO X:IF A(V*I)>Z THEN ? "(";I;") ";" SOLDIER ";I
81N. I:? "WHICH ENEMY DO YOU WANT TO TARGET?":? "(0) TO GO BACK.":I. A$:C=VAL(A$):IF C=Z THEN RET.
82E=Z:IF A(V*C)<=Z THEN E=N
83IF E=N THEN 80
84T=C:?:RET.
85D=I/H:RET.
86R=((RND(Y)*F)*O/F)+Y:RET.
87F. J=Z TO G:N. J:? CHR$(253):RET.
88C=Q*(A(8)+A(12)):RET.
89?:? "GAME OVER":?:F. I=Z TO Y:GOS. 87:N. I
90?:? "YOU WON ";W;" TIMES.":?:END
91D. 314,314,54,54,38,96,24,1,21,17,6,14,6,30,30,0,0,6,1,4,1,1,1,50,4,2,30,30,0,0,6,1,4,1,1,1,50,4,2,4,8,100,5,5,255
