#include <Stepper.h>
#include <AccelStepper.h>

// Bounce.pde
// -*- mode: C++ -*-
//
// Make a single stepper bounce from one limit to another
//
// Copyright (C) 2012 Mike McCauley
// $Id: Random.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $
// Define a stepper and the pins it will use
AccelStepper x_axis_stepper(AccelStepper::FULL4WIRE, 8, 11, 12, 13); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
Stepper initStepper(200, 8,11,12,13);            

int val;
int str;

int x_current_pos = 0;
int y_current_pos = 0;

int x_axis_stop = 4;
int y_axis_stop = 3;

int y_axis_motor = 6;

void setup()
{ 
  Serial.begin(9600);
  Serial.println("Power On");
  delay(500);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  digitalWrite(9,HIGH);
  digitalWrite(10,HIGH);
  
  // Change these to suit your stepper if you want
  x_axis_stepper.setMaxSpeed(500);
  x_axis_stepper.setAcceleration(130);
  x_axis_stepper.moveTo(500);
  
  //X Axis Zeroing
  Serial.println("Beginning X Zeroing");
  int begintime = millis();
  while (begintime + 6000 > millis())
  {
  	delay(20);
  	initStepper.step(1);
  }
}

void x_move_to(int move_loc){
  x_axis_stepper.runToNewPosition(move_loc / 0.123);
};

void y_move_to(int move_to, int y_current_pos) {
  int move_amount = 0;
  move_amount = move_to - y_current_pos;
}

void serialEvent(){
	str = Serial.read();
	val = Serial.parseInt();
	
	switch (str) {
    case 'x':
      Serial.print("Moving X to ");
      Serial.println(val);
      x_move_to(val);
      Serial.print("Moved.");
      break;

    case 'y':
      y_move_to(val, y_current_pos);
      break;

    case 'a':
      y_move_to(val, y_current_pos);
      x_move_to(val);
      break;

    case 'c':
      break;

    case 'z':
      x_move_to(val);
      y_move_to(val, y_current_pos);
      break;
}
}

void loop()
{
  if (digitalRead(x_axis_stop) == HIGH)
  {
x_current_pos = 0;
  }
  	if (digitalRead(y_axis_stop) == HIGH)
  {
y_current_pos = 0;
  }
}
