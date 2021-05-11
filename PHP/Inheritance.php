<?php

  class Mother{
    public function getEyeCount()
    {
      return 2;
    }
  }

  class Child extends Mother{

  }

//$Son = new Child();
//$Son->getEyeCount();
(new Child)->getEyeCount(); //short-hand
?>
