
<?php
    function createFile($file_name, $txt) {
        $myfile = fopen("service", "w") or die("Unable to open file!");
        fwrite($myfile, $txt);
        fclose($myfile);
    }

    function FileToString($file_name) {
        if ( !file_exists($file_name) ) {
            return "null null";
        }
        $file = fopen($file_name, "r") or die("Unable to open file!");
        $filesize = filesize($file_name);
        $txt = "";
        if($filesize > 0)
            $txt = fread($file, filesize($file_name));
        fclose($myfile);
        return $txt;
    }

    $data = explode(' ', FileToString("service"));

    $city = $data[0];
    $country = $data[1];

    if(strcmp ( $city, $_GET['city']) != 0 || strcmp ( $country, $_GET['country']) != 0) {
        shell_exec('gnome-terminal -- sh -c "cd ../wrappers/; ./start_gnome \'' . $_GET['city'] . ' ' . $_GET['country'] . '\'"');
        createFile("service", $_GET['city'] . ' ' . $_GET['country']);
    }
?>