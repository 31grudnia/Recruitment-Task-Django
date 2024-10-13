## Zadanie 1: Aplikacja Django do Przetwarzania Tekstu
Cel: Utwórz aplikację Django, która pozwala użytkownikowi przesłać plik tekstowy. Aplikacja powinna przeczytać plik, przemieszać litery w środku każdego wyrazu (pozostawiając pierwszą i ostatnią literę na swoich miejscach) i wyświetlić zmodyfikowany tekst użytkownikowi.

Funkcjonalności:
Strona główna zawiera formularz do przesyłania pliku tekstowego.
Po przesłaniu pliku, użytkownik jest przekierowywany na stronę z wynikiem, gdzie zmodyfikowany tekst jest wyświetlany.

empty file 


---
## Zadanie 2: Walidator PESEL w Aplikacji Django
Cel: Utwórz aplikację Django, która pozwala użytkownikowi wprowadzić numer PESEL do formularza. Aplikacja powinna zweryfikować numer PESEL zgodnie z oficjalną specyfikacją i wyświetlić użytkownikowi informację o poprawności numeru.

Funkcjonalności:
Strona główna zawiera formularz do wprowadzania numeru PESEL.
Po wprowadzeniu numeru, aplikacja wyświetla informacje o tym, czy numer PESEL jest poprawny czy nie, a także dodatkowe informacje, takie jak data urodzenia i płeć.

---

<!-- {"pesel": "00323106070"} -->

<!-- 1*0 + 3*0 + 7*3 + 9*2 + 1*3 + 3*1 + 7*0 + 9*6 + 1*0 + 3*7 =21+18+3+3+54+21--> 

@TODO:                                                                  
- Contenerization
- Test
- DB?
- Frontend?
- Celery?
- CI?