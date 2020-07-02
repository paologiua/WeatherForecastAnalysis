# WeatherForecastAnalysis
## Cos'è?
WeatherForecastAnalysis è il progetto universitario dello studente Giua Paolo (X81000576) della facoltà di informatica dell'Università di Catania.
Consiste nell'acquisizione dei dati meteo al fine di fare previsioni.
Le previsioni ottenute vengono poi associate ai dati reali e valutate.
## Obiettivo
Visualizzare i dati ottenuti in una dashboard, così da essere facilmente consultabili e confrontabili.
La dashboard viene visualizzata da una piccola applicazione Web.

# Guida d'uso
## Premessa
Per la corretta esecuzione di WeatherForecastAnalysis è necessario:
* Docker;
* Netcat;
* Php;
* Scaricare [kafka_2.12-2.4.1.tgz](https://drive.google.com/file/d/1xXGH_Ee8MhI0GUlSUVHK_k2sEPxpaEDj/view?usp=sharing) nella cartella kafka/src/setup del progetto;
* Scaricare [spark-2.4.5-bin-hadoop2.7.tgz](https://drive.google.com/file/d/1QPWhdRXWD3SJ6pSYOk1ZUfIL0k9_SM_X/view?usp=sharing) nella cartella spark/src/setup del progetto.
Facoltativo:
* Gnome Terminal.
Infine occore eseguire il file script 'build' posizionato nella cartella principale del progetto.
```
$ ./build
```
## Prima esecuzione
Soddisfatta la premessa, si potrà decidere se eseguire il progetto in background o meno.
## Background
Per questa modalità di esecuzione, basterà eseguire il file script 'start', posizionato nella cartella principale del progetto.
```
$ ./start
```
## In Terminale (occorre Gnome Terminal)
Per questa modalità di esecuzione, basterà eseguire il file script 'start_gnome', posizionato nella cartella principale del progetto.
```
$ ./start_gnome
```
## Stop esecuzione
Per fermare l'esecuzione di Weather Forecast Analysis, richiamare il comando sottostante nella cartella principale del progetto e CTRL + C sul terminale del web server PHP.
```
$ ./stop
```
