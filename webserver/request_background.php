
<?php
    function createFile($file_name, $txt) {
        $myfile = fopen("service", "w") or die("Unable to open file!");
        fwrite($myfile, $txt);
        fclose($myfile);
    }

    function FileToString($file_name) {
        if ( !file_exists($file_name) ) {
            return "";
        }
        $file = fopen($file_name, "r") or die("Unable to open file!");
        $filesize = filesize($file_name);
        $txt = "";
        if($filesize > 0)
            $txt = fread($file, filesize($file_name));
        fclose($myfile);
        return $txt;
    }

    if(strcmp ( FileToString("service"), $_GET['city']) != 0) {
        shell_exec('bash -c "cd ../wrappers/; ./start \'' . $_GET['city'] .'\'" > /dev/null 2>/dev/null &');
        createFile("service", $_GET['city']);
    }
?>