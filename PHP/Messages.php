<?php

require 'autoloading/Person.php';
require 'autoloading/Business.php';
require 'autoloading/Staff.php';
//Instead of requireing files we can autoload using composer for now we will manually import them.
$person1 = new Person('Joe Smith');

$person2 = new Person('Jane Doe');

$staff = new Staff([$person1]);

$business = new Business($staff);

$business->hire($person2);

var_dump($business->getStaffMembers());

?>
