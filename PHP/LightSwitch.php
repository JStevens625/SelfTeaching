<?php
class LightSwitch {
  public function on()
  {
    // code...
  }

  public function off()
  {
    // code...
  }
  private function connect()
  {
    // code...
  }
  private function activate()
  {
    // code...
  }
}

$switch = new LightSwitch;
$switch->connect() //Will not work as it is a private method

?>
