<?php

class Task{
  public $title;

  public $description;

  public $completed = false;

  public function __construct($title,$description)
  {
    $this->title = $title;
    $this->description = $description;
  }

  public function complete()
  {
    $this->completed = true;
  }

}
$task = new Task('Learn OOP','Do this to learn OOP');
//$task2 = new Task('Pick up groceries');

$task->complete();

var_dump($task)

?>
