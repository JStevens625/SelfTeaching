<?php

class Person {
  private $name;
  private $age;

  public function __construct($name)
  {
    $this->name = $name;
  }

  public function getAge()
  {
    return $this->age;
  }

  public function setAge($age)
  {
    if ($age < 18) {
      throw new Exception("Not old enough");
    }

    $this->age = $age;
  }

}
$john = new Person("John Doe");
$john->setAge(18);

var_dump($john->getAge())
?>
