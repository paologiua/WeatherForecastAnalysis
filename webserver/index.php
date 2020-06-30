<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WeatherForecastAnalysis</title>
    <link rel="icon" href="/assets/img/icon.png">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body style="margin:0px;padding:0px;overflow:hidden;position:absolute;top:0px;left:0px;right:0px;bottom:0px">
    <nav class="navbar navbar-light bg-light justify-content-between">
        <a class="navbar-brand">WeatherForecastAnalysis</a>
        <div class="form-inline">
            <input id="city" class="form-control mr-sm-2" type="search" placeholder="City" aria-label="City">
            <input id="country" class="form-control mr-sm-2" type="search" placeholder="Country" aria-label="Country">
            <button id="search" class="btn btn-outline-success my-2 my-sm-0" type="submit" onclick="console.log('sdsd');search()">Search</button>
        </div>
    </nav>    
    <div id="frameWrapper" style="overflow:hidden;overflow-x:hidden;overflow-y:hidden;height:100%;width:100%;">
    
    </div>
    
    <script src="/assets/js/main.js"></script>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>
