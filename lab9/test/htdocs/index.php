<!DOCTYPE html>
 
 <html>
 <body>
   <h1>Hello</h1>
  
    <?php
        $sth = $_GET["name"];
        // $allowedLetters = "abcde";
        // $whitelisted = "";
        // for ($i=0; $i < strlen($sth); $i++)
        // {
        //     if (str_contains($allowedLetters, $sth[$i]))
        //     {
        //         $whitelisted = $whitelisted . $sth[$i];
        //     }
        // }
        $sth = str_replace("<script>", "", $sth);
        echo 'Hello ' . $sth . '!';
    ?>
 </body>
 </html>
