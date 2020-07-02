# WeatherForecastAnalysis
## Cos'è?
WeatherForecastAnalysis è il progetto universitario dello studente **Giua Paolo** (X81000576) della facoltà di informatica dell'Università di Catania.
Consiste nell'acquisizione dei dati meteo al fine di fare previsioni.
Le previsioni ottenute vengono poi associate ai dati reali e valutate.
## Obiettivo
Visualizzare i dati ottenuti in una dashboard, così da essere facilmente consultabili e confrontabili.
La dashboard viene visualizzata da una piccola applicazione Web.

# Guida d'uso
#### Requisiti
Per la corretta esecuzione di WeatherForecastAnalysis è necessario:
* Docker;
* Netcat;
* Php;
* Scaricare [kafka_2.12-2.4.1.tgz](https://drive.google.com/file/d/1xXGH_Ee8MhI0GUlSUVHK_k2sEPxpaEDj/view?usp=sharing) nella cartella **kafka/src/setup** del progetto;
* Scaricare [spark-2.4.5-bin-hadoop2.7.tgz](https://drive.google.com/file/d/1QPWhdRXWD3SJ6pSYOk1ZUfIL0k9_SM_X/view?usp=sharing) nella cartella **spark/src/setup** del progetto;
* Eseguire il file script **'build'** posizionato nella cartella principale del progetto.
```
$ ./build
```
Facoltativo:
* Gnome Terminal.

## Esecuzione
**Soddisfa i requisiti prima di eseguire WeatherForecastAnalysis**
L'esecuzione può avvenire in due modalità:
#### Background
Usa lo script **'start'**, posizionato nella cartella principale del progetto, per l'esecuzione in background.
```
$ ./start
```
Nel terminale sarà visibile solo il log del server integrato di Php.
#### Terminale (Gnome Terminal necessario)
Questa modalità crea più schede di Gnome Terminal per visualizzare cosa accade in ciascun container.
Usa lo script **'start_gnome'**, posizionato nella cartella principale del progetto.
```
$ ./start_gnome
```
## Stop esecuzione
Per fermare l'esecuzione di WeatherForecastAnalysis, richiamare il comando sottostante nella cartella principale del progetto e CTRL + C sul terminale del web server PHP.
```
$ ./stop
```
