# Web Scraper za Baze podataka

Ovaj projekat je **web scraper** koji automatski prati i beleži nove objave sa određenog sajta, a zatim obaveštava korisnike putem Discord aplikacije.

## Funkcionalnosti
- **Praćenje novih obaveštenja:** Program koristi Selenium za scraping i prikupljanje podataka sa sajta.
- **Čuvanje novosti:** Forkovani repozitorijum [git-auto-commit-action](https://github.com/stefanzweifel/git-auto-commit-action) omogućava automatsko otkrivanje novih objava i njihovo čuvanje u `.md` fajlu.
- **Automatsko slikanje:** Generiše se screenshot relevantne objave koristeći Python.
- **Deljenje informacija:** Uz pomoć Discord webhook linka, slika i link ka novoj objavi šalju se korisnicima.
- **Automatizacija:** GitHub Actions periodično pokreće scraper i ažurira podatke.

## Korišćene tehnologije
- **Selenium:** Za scraping i interakciju sa sadržajem sajta.
- **Python:** Za generisanje screenshot-ova.
- **GitHub Actions:** Za automatizaciju pokretanja scrapper-a i ažuriranje `.md` fajla.
- **Discord Webhook:** Za slanje obaveštenja korisnicima.
- **Kod iz forka:** Za poređenje i otkrivanje novih objava koristi se [git-auto-commit-action](https://github.com/stefanzweifel/git-auto-commit-action), forkovan u [automatic-changes](https://github.com/studentAutomations/automatic-changes).

## Kako funkcioniše
1. **Periodično pokretanje:** GitHub Actions aktivira skriptu u unapred definisanim intervalima.
2. **Scraping:** Selenium pretražuje sajt i prikuplja podatke o objavama.
3. **Otkrivanje novosti:** Forkovani kod proverava da li postoje nove objave i, ako postoje, automatski ih dodaje u `.md` fajl.
4. **Slanje obaveštenja:** Screenshot i link ka objavi šalju se putem Discord webhook-a svim korisnicima.

## Kako koristiti
1. Fork-ujte ovaj repozitorijum.
2. Dodajte svoj Discord webhook URL u konfiguraciju.
3. Aktivirajte GitHub Actions.
4. Pogledajte `.md` fajl za sačuvane novosti i pratite obaveštenja na Discord-u.

## Doprinos
Slobodno otvorite **issue** ili pošaljite **pull request** za predloge ili poboljšanja.

## Licence
[MIT Licence](./LICENSE)
