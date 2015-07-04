#include <Stepper.h>

  int val;
  int str;
  
Stepper x_axis_stepper = Stepper(200, 5, 6);

void setup() {
  //When Turned on, move y axis until it hits the stop

  //When Turned on, move x axis until it hits the stop

  //Set current X and Y pos to 0
  int x_current_pos = 0;
  int y_current_pos = 0;

  Serial.begin(9600);
  Serial.write("Power On");
}

int mm_to_steps(int mm) { //Convert input mm into steps for stepper
  int mm_per_step = 0.123;

  int no_of_steps = round(mm / mm_per_step);

  return no_of_steps;
}

void move_x_axis_mm(int mm, int smooth, int x_current_pos) { //Translate the X-axis a certain number of mm, smooth defines if smooth acceleration is used.


  int steps_to_turn = mm_to_steps(mm);

  int number_of_steps_turned = 0;

  int delay_amount = 0;

  while (number_of_steps_turned <= steps_to_turn);
  if (smooth)
  {
    x_axis_stepper.step(1);
    number_of_steps_turned++;
    x_current_pos = x_current_pos + 0.123;

    Serial.write(x_current_pos);

    delay_amount = 200 * ((number_of_steps_turned - steps_to_turn) / steps_to_turn) ^ 4;

    if (delay_amount >= 5)
    {
      delay(delay_amount);
    }
  }
  else {
    x_axis_stepper.step(1);
  }
  number_of_steps_turned++;
}
void x_move_to(int move_to, int x_current_pos) {
  int move_amount = 0;
  move_amount = move_to - x_current_pos;

  move_x_axis_mm(move_amount, true, x_current_pos);
}

void y_move_to(int move_to, int y_current_pos) {
  int move_amount = 0;
  move_amount = move_to - y_current_pos;

  move_x_axis_mm(move_amount, true,y_current_pos);
}

void loop(int x_current_pos, int y_current_pos) {
  if (Serial.available() > 0)
  {
    str = Serial.read();
    val = Serial.parseInt();
  }
  switch (str) {
    case 'x':
      x_move_to(val, x_current_pos);
      break;

    case 'y':
      y_move_to(val, y_current_pos);
      break;

    case 'a':
      y_move_to(val, y_current_pos);
      x_move_to(val, x_current_pos);
      break;

    case 'c':
      break;

    case 's':
      x_move_to(val, x_current_pos);
      y_move_to(val, y_current_pos);
      break;
  }
}

