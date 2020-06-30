
function httpGet(theUrl) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", theUrl, false );
	xmlHttp.send( null );
	return xmlHttp.responseText;
}

function search() {
	var city = document.getElementById('city').value
	var country = document.getElementById('country').value
	if(city === '' || country === '') {
		alert('Error')
		return
	}
	httpGet('request.php?city=' + city + '&country=' + country)

	var frameWrapper = document.getElementById('frameWrapper')
	frameWrapper.innerHTML = '<iframe src="http://localhost:5601/app/kibana#/dashboard/db84aa70-b6d7-11ea-b975-5dab1aa0a23d?embed=true&_a=(description:\'\',filters:!((\'$state\':(store:appState),meta:(alias:!n,disabled:!f,index:\'11f2b600-b6bb-11ea-b975-5dab1aa0a23d\',key:city,negate:!f,params:(query:\'' + city.replace(' ', '%20') + '\'),type:phrase),query:(match_phrase:(city:\'' + city.replace(' ', '%20') + '\')))),fullScreenMode:!f,options:(hidePanelTitles:!f,useMargins:!t),panels:!((embeddableConfig:(),gridData:(h:14,i:ac87578c-e9f5-4e3f-8fc9-0f70992d257a,w:11,x:0,y:0),id:\'0ffa5250-b6c4-11ea-b975-5dab1aa0a23d\',panelIndex:ac87578c-e9f5-4e3f-8fc9-0f70992d257a,type:visualization,version:\'7.7.0\'),(embeddableConfig:(colors:(\'Current%20temperature\':%230A437C),timeRange:(from:now-15m,to:now),vis:(colors:(\'Current%20temperature\':%230A437C,\'Predicted%20temperature\':%2382B5D8))),gridData:(h:14,i:\'5b9a5442-73bd-4812-b3ea-3ef9576f8c9d\',w:37,x:11,y:0),id:e5aaed80-b6bd-11ea-b975-5dab1aa0a23d,panelIndex:\'5b9a5442-73bd-4812-b3ea-3ef9576f8c9d\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(colors:(\'Current%20humidity\':%23F2C96D),timeRange:(from:now-15m,to:now),vis:(colors:(\'Current%20humidity\':%23F2C96D,\'Predicted%20humidity\':%23E0752D))),gridData:(h:14,i:\'86569159-d0b8-4a86-994e-37e4655bd6b1\',w:37,x:0,y:14),id:d2681390-b70f-11ea-bee8-d74fc47318bd,panelIndex:\'86569159-d0b8-4a86-994e-37e4655bd6b1\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(vis:!n),gridData:(h:14,i:\'47e60591-8a99-477e-bcb1-9e5cb58bdd4d\',w:11,x:37,y:14),id:ff56c2b0-b6c5-11ea-b975-5dab1aa0a23d,panelIndex:\'47e60591-8a99-477e-bcb1-9e5cb58bdd4d\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(vis:!n),gridData:(h:15,i:ac3a9cf8-2ebb-48a2-8aa0-97d6b347af3f,w:13,x:0,y:28),id:\'2c39a7d0-b6c5-11ea-b975-5dab1aa0a23d\',panelIndex:ac3a9cf8-2ebb-48a2-8aa0-97d6b347af3f,type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:15,i:\'6556449a-d961-4168-b8fd-0120a83def87\',w:11,x:13,y:28),id:\'694e3b60-b6d7-11ea-b975-5dab1aa0a23d\',panelIndex:\'6556449a-d961-4168-b8fd-0120a83def87\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:15,i:\'4dd4cf36-c23c-433f-89c4-437c08d65e5a\',w:11,x:24,y:28),id:af04ad30-b6d5-11ea-b975-5dab1aa0a23d,panelIndex:\'4dd4cf36-c23c-433f-89c4-437c08d65e5a\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:15,i:de4e6823-220a-4bc7-aa97-d76f6c16771d,w:13,x:35,y:28),id:eb1f04a0-b71b-11ea-bee8-d74fc47318bd,panelIndex:de4e6823-220a-4bc7-aa97-d76f6c16771d,type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:8,i:dca55a5d-5f98-47aa-ad92-329e85619dd8,w:9,x:0,y:43),id:\'67e6bfc0-b8d2-11ea-959c-1397c5fe66fa\',panelIndex:dca55a5d-5f98-47aa-ad92-329e85619dd8,type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:16,i:\'28592803-4d28-4c46-aa21-d8b2a7b44c58\',w:15,x:9,y:43),id:f80b5f10-b8ce-11ea-959c-1397c5fe66fa,panelIndex:\'28592803-4d28-4c46-aa21-d8b2a7b44c58\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:16,i:\'8dde254e-8f66-4508-a27c-4183a1789a93\',w:15,x:24,y:43),id:\'9c3520d0-b8cf-11ea-959c-1397c5fe66fa\',panelIndex:\'8dde254e-8f66-4508-a27c-4183a1789a93\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:8,i:\'9063c002-55ea-4323-ac6a-eda351b51f45\',w:9,x:39,y:51),id:\'43d03430-b8d3-11ea-959c-1397c5fe66fa\',panelIndex:\'9063c002-55ea-4323-ac6a-eda351b51f45\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:8,i:\'31b82cc2-43ad-4053-87bd-ae9d1d7c653e\',w:9,x:0,y:51),id:e0dc0520-b8d2-11ea-959c-1397c5fe66fa,panelIndex:\'31b82cc2-43ad-4053-87bd-ae9d1d7c653e\',type:visualization,version:\'7.7.0\'),(embeddableConfig:(),gridData:(h:8,i:aad9ef5b-a523-4901-86ce-682ebcbd8d19,w:9,x:39,y:43),id:\'32a7cf10-b8d3-11ea-959c-1397c5fe66fa\',panelIndex:aad9ef5b-a523-4901-86ce-682ebcbd8d19,type:visualization,version:\'7.7.0\'),(embeddableConfig:(timeRange:(from:now-15m,to:now)),gridData:(h:18,i:\'6896c451-79d8-4436-846b-0bc3ac9a9fbe\',w:48,x:0,y:59),id:\'3983cae0-b6d1-11ea-b975-5dab1aa0a23d\',panelIndex:\'6896c451-79d8-4436-846b-0bc3ac9a9fbe\',type:visualization,version:\'7.7.0\')),query:(language:kuery,query:\'\'),timeRestore:!f,title:Weather,viewMode:view)&_g=(filters:!(),refreshInterval:(pause:!f,value:5000),time:(from:now-15m,to:now))" frameborder="0" style="overflow:hidden;overflow-x:hidden;overflow-y:hidden;height:100%;width:100%;" height="100%" width="100%"></iframe>'
}

var city = document.getElementById("city");

city.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("search").click();
  }
});

var country = document.getElementById("country");

country.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("search").click();
  }
});