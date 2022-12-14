# Quiz App

Projekt aplikacji mobilnej na Androida, tworzona w Pythonie. 

## Technologie
* [Python](https://www.python.org/)
* [Kivi](https://kivy.org/)

## Jak zacząć?

Poniższe instrukcje zapewnią Ci kopię projektu uruchomioną na komputerze (pliki lokalnie) do celów programistycznych i testowych. Zobacz kroki poniżej, aby zapoznać się z uwagami dotyczącymi uruchamiania projektu.

### Wymagania wstępne

* Musisz posiadać na swoim komputerze skonfigurowanego [Git'a](https://git-scm.com/). 
* Zainstaluj na swoim komputerze IDE do programowania w Pythonie np. PyCharm, VS Code. 
* Skonfiguruj Pythona na swoim komputerze (+3.8).

### Instalowanie

1. Sklonuj projekt

```
git clone https://github.com/AGH-Narzedzia-Informatyczne-2022-2023/PanDaPiec.git
```

2. Przejdź do sklonowanego repo, utwórz venv i aktywuj go:

```
py -3 -m venv .venv
.venv\scripts\activate
```

3. (opcjonalnie) Jeśli Powershell wyrzuci błąd:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

4. Ustaw jako interpreter ten z nowo utworzonego venv'a.

    W przypadku VS Code:

    Będąc w katalogu z projektem, `CTRL + SHIFT + P`, wpisz `Python: Select Interpreter`, wybierz z listy ten, który znajduje się w .venv

5. Zainstaluj moduły:
```
pip install -r requirements.txt
```

## Uruchamianie projektu
```
python main.py
```

## Uruchamianie testów

W tym akapicie wyjaśmimy jak uruchomić testy.

### Testowanie widzetów

```
python3 widget_test
```

### Testy przejrzystości kodu

```
python3 cleancode_test
```
## Autorzy

* **Arkadiusz Mika** - - [Arkadiusz4](https://github.com/Arkadiusz4)
* **Filip Kowalski** - - [Spookyless](https://github.com/Spookyless)
* **Krzysztof Czerenko** - - [Krzysiek899](https://github.com/Krzysiek899)
* **Jakub Retajczyk** - - [Jakubret](https://github.com/jakubret)
* **Maciej Michałek** - - [McMichalek](https://github.com/McMichalek)
* **Michał Broś** - - [MBrosik](https://github.com/MBrosik)

Zobacz pełną listę [współtwórców PanDaPięć](https://github.com/orgs/AGH-Narzedzia-Informatyczne-2022-2023/teams/pandapiec/members)

## Licencja

Projekt oparty jest na licencji Creative Commons Zero - zobacz [LICENSE.md](LICENSE.md)

## Podziękowania

* [AGH](https://www.agh.edu.pl/), za darmowe GitHub PRO
* Wszystkim użytkownikom Quiz App