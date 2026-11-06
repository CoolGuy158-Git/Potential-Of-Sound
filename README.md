# Potential of sound

---

## What is this

A simple project built on an arduino.
It connects to python, and is basically a digital audio synthesizer,
that uses a breadboard as the controller.

## How to use
It's simple really, just press the blue or red button or both,
and turn the potentiometer to increase the set frequency of each button.

## How it works
The arduino basically talks to python,
it sends the voltage coming from the potentiometer (because it's basically a resistor which resistance can be changed)
The python program interprets that voltage as how much to change the set freq by, by applying the following formula:

```txt
let

F = new freq
f = old freq
v = voltage

F = f + v * 20
```
The button presses on the other hand plays the frequencies, with each button having a set starting frequency,
just so that there's some diversity.

## Installation and configuration

(I'm assuming you're a dev sooo idc)

Compile and upload the sketch arduino file first,
After which run the python file.

As for the setting up of the arduino and breadboard, make sure 
```txt
--Potentiometer--
The potentiometer is plugged in, right positive, left ground.
Another jumper wire connecting the output of the potentiometer to analog input a2.

--Red button--
Connect one side of the button to ground, and the positive to digital PWM 2.

--Blue button--
Connect one side of the button to ground, and the positive to digital PWM 3.
```
