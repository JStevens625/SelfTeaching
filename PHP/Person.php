<?php
class person {

  public $name;

  private $age;

  public function __construct($name)
  {
      $this->name=$name;
  }
  public function getAge()
  {
    return $this->age;
  }
  public function setAge($age){
    if ($age < 21) {
      throw new Exception("Not Allowed to Drink");
    }
    $this->age=$age;
  }
}
$Jake = new person("Jacob");
$Jake->setAge(21);
var_dump($Jake->getAge())
?>
