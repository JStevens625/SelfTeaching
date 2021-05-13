<?php

abstract class Shape{
  protected $color;
  public function __construct($color = 'red') //Given a default color of red.
  {                                           //If default was not given then
    $this->color = $color;                    //shape could not be used till color was defined.
  }

  public function getColor()
  {
      return $this->color;
  }

  abstract protected function getArea();
}

class Square extends Shape {
  protected $length = 4;

  public function getArea()
  {
    return pow($this->length,2);
  }
}

class Triangle extends Shape {
  protected $base = 4;
  protected $height = 7;

  public function getArea(){
    return .5 * $this->base * $this->height; //Overrides the parent method
  }
}

class Circle extends Shape {
  protected $radius = 5;
  public function getArea()
  {
    return pi * pow($this->radius,2);
  }
}

//echo (new Triangle)->getArea();
//echo (new Square)->getColor(); //default red
//echo (new Circle('green'))->getColor(); //green
//new Shape; //Cannot be done because it is abstract. But will have requirements
//new Circle;
?>
