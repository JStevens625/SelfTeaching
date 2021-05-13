<?php

interface Animal
{
  public function communicate();
}

class Dog implements Animal {
  public function communicate()
  {
    return 'Bark';
  }
}

class Dog implements Animal {
  public function communicate()
  {
    return 'Meow';
  }
}

?>
