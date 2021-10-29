## Aplikacja rozpoznająca postacie w lolu
1. Dane -> przetworzone na obrazy zbierane live w grze screenshoty przerobione na bitmapę
    a) możliwe wprowadzenie filtracji mapy poprzez dodanie skanu całej mapy i wykrywanie miejsca pobytu -> zostanie na bitmapie tylko zapis postaci, wardów, umiejętności i minionów
2. Training set -> modele postaci i skinów do nich pod różnymi kątami,
    a) analogicznie jak wyżej model całego summoners rift włączając te po zmodyfikowaniu przez smoki
    b) modele minionów/wardów/skilli
3. Wyświetlanie -> obrys konturu hitboxa postaci



#Proste kroki:
#step1 -> wykrywanie dowolnej postaci
Paski zdrowia/bez pasków zdrowia

#step 1 - implementacja:
wybór modelu:
neural network for classification,
linear regression for classification,
poly regression for classification,

#step 1 - debugging/optymalizacja
1. wygenerowanie training i test data sets -> zbieranie obrazów różnych postaci + innych elementów,
2. precision and recall,
3. learning curve

#step2 - Training set -> jedna postać
2. Dane -> 1 obraz/s 
3. Wyświetlanie -> zielona kropka gdy wykryta jest postać/czerwona gdy jej nie ma, żólta - pomarańczowej gdy nie ma pewności