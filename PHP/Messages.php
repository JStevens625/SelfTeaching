<?php

class Person {
  protected $name;
  public function __construct($name)
  {
    $this->name = $name;
  }
}

class Business {
  public function hire(Person $person)
  {
    // code...
  }
}

class Staff {

}

?>
