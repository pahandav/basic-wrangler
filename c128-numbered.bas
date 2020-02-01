0input"80-Columns?";a$:z=rnd(-ti):ifa$<>"y"then2
1graphic5:fast
2printchr$(147):z=0:y=1:a=z:t=z:v=13:c=44:d=z:e=z:r=z:x=2:i=z:j=z:dima(c):g=100:h=4:k=512:l=32:u=16:n=255:o=99:f=65535:q=6:s=3841:b=4096:m=39:p=y:w=z:fori=ztoc:reada(i):nexti:print"welcome to the battle system test!":print:print
3print"Two soldiers approach.":print
4ifa(v*a)=zthen7
5ifa=zthen23
6t=z:goto45
7ifa(z)=zthen94
8a=a+y:ifa<>zthent=z
9ifa(v*a)=zthena=a+y
10ifa>xthena=z
11d=z:ifa(v*y)=zthend=d+y
12ifa(v*x)=zthend=d+y
13ifd=xthen15
14goto4
15print"You are victorious.":print:w=w+y:a=z:t=z:ifw>=10thengosub21
16fori=ytox:a(i*v)=a(i*v+y):nexti:gosub82:ifr<12.5thenprint"You obtained a Potion!"
17ifr<12.5thenprint
18ifr<12.5thenp=p+y
19ifp>othenp=o
20goto3
21gosub82:ifr>=25thenreturn
22fori=vtom-y:a(i)=a(i)*1.5:nexti:print"The enemies have powered up!":print:return
23print:printa(z);"/";a(y);"hp":printa(x);"/";a(3);"mp":print:print"(A) Attack":print"(M) Magic":print"(I) Items":print"(Q) Quit"
24geta$:ifa$=""then24
25ifa$="a"ora$="a"then30
26ifa$="m"ora$="m"then34
27ifa$="i"ora$="i"then40
28ifa$="q"ora$="q"then95
29goto23
30gosub83:ifc=zthen23
31ifc>xthen30
32ifc<zthen30
33goto45
34print:print"(1) Lightning -";a(m);"mp":print"(2) cure -";a(m+3);"mp":print"which spell do you want to cast?":print"type (0) to go back."
35geta$:ifa$=""then35
36c=val(a$):ifc=ythen64
37ifc=xthen74
38ifc=zthen23
39goto34
40print:print"(1) potion -";p:print"which item do you wish to use?":print"type (0) to go back."
41geta$:ifa$=""then41
42c=val(a$):ifc=ythen77
43ifc=zthen23
44goto40
45c=((a(a*v+10)/h)+(a(a*v+5)))+a(a*v+7)-a(t*v+7):gosub82:i=a(a*v+11):gosub90:ifd>rthenc=n
46i=a(t*v+11):gosub90:ifd>rthenc=n
47ifr<cthen51
48ift>zthenprint"your attack missed!"
49ift=zthenprint"soldier";a;"missed you!"
50print:goto7
51d=a(a*v+h):e=a(a*v+12):c=d+((d+e)/l)*((d*e)/l):d=((u*(k-a(t*v+q)))*c)/(u*k):c=(a(a*v+11)+a(a*v+12)-a(t*v+12))/h:gosub91:ifr<=cthen53
52goto54
53d=int(d*x)
54d=int(d*(s+(rnd(y)*n))/b):ifd=zthend=y
55a(t*v)=a(t*v)-d:ifa(t*v)<=zthena(t*v)=z
56ifa<>zthen60
57print"you hit soldier";t;"for";d;"hp.":print:ifa(t*v)<>zthen59
58print"you defeated soldier";t:print
59goto7
60ifd>zthengosub92
61print"soldier";a;"hit you for";d;"hp.":print:ifa(z)<>zthen63
62print"you died.":print
63goto7
64e=z:d=z:ifa(m)>a(x)then73
65a(x)=a(x)-a(m):gosub83:ifc=zthen34
66ifc>xthen64
67ifc<zthen64
68c=a(m+x)+a(a*v+12)-((a(t*v+12))/x)-y:gosub82:ifr<cthengosub93
69ifr>cthen71
70d=(a(m+y)*(k-a(t*v+9))*c)/(u*k)
71ifd>zthen54
72print"your spell missed.":print:goto7
73print:print"you don't have enough mp to cast that spell.":goto34
74e=3:ifa(m+3)>a(x)then73
75a(x)=a(x)-a(m+3):gosub93:d=c+22*a(m+y+e):d=int(d*(s+(rnd(y)*n))/b):print:print"you have been healed for";d;"hp.":print:a(z)=a(z)+d:ifa(z)>a(y)thena(z)=a(y)
76goto7
77ifp=zthenprint
78ifp=zthenprint"you have no potions."
79ifp=zthen23
80a(z)=a(z)+g:ifa(z)>a(y)thena(z)=a(y)
81p=p-y:print:print"you have been healed for 100 hp.":print:goto7
82r=int(rnd(y)*g):return
83print:fori=ytox:ifa(v*i)>zthenprint"(";i;")";" soldier";i
84nexti:print"which enemy do you want to target?":print"(0) to go back."
85geta$:ifa$=""then85
86c=val(a$):ifc=zthenreturn
87e=z:ifa(v*c)<=zthene=n
88ife=nthen83
89t=c:print:return
90d=i/h:return
91r=((rnd(y)*f)*o/f)+y:return
92forj=ztog:nextj:printchr$(7):return
93c=q*(a(8)+a(12)):return
94print:print"game over":print:fori=ztoy:gosub92:nexti
95print:print"you won";w;"times.":print:end:data314,314,54,54,38,96,24,1,21,17,6,14,6,30,30,0,0,6,1,4,1,1,1,50,4,2,30,30,0,0,6,1,4,1,1,1,50,4,2,4,8,100,5,5,255
