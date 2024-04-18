## Instrukcja obsługi
- Pobieramy folder z plikami projektu
- W terminalu, przechodzimy do lokalizacji w której mamy folder z projektem
- Za pomocą poniższej komendy budujemy obraz Docker
```console
docker build -t weatherimage .
```
- Następnie uruchamiamy zbudowany obraz
```console
docker run -p 8501:8501 weatherimage
```
- W przeglądarce uruchamiamy aplikację pod zdefiniowanym wcześniej portem
- W polu tekstowym wpisujemy nazwę miasta, następnie klikamy przycisk
- Po chwili powinny pojawić się informacje na temat aktualnej pogody z danego miasta
