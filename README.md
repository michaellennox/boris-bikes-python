[![Build Status](https://travis-ci.org/michaellennox/boris-bikes.svg?branch=master)](https://travis-ci.org/michaellennox/boris-bikes)

#Boris Bikes

This is a repeat of the boris-bikes challenge writting in Python instead of the original Ruby. [boris-bikes-challenge](https://github.com/makersacademy/course/blob/master/boris_bikes/0_challenge_map.md). You can find my original Ruby solution [at this repo](https://github.com/michaellennox/boris-bikes). The code in this repo should be treated as a WIP.

I have aimed to solve this challenge in a test driven manner with automated tests using the unittest library and the nose testrunner.

##Installation Instructions

##Useage Instructions

##Brief

London's Boris Bikes (well, 'Santander Cycles') are awesome. For a small fee, anyone can hire out a bike and ride it around London. Bikes are located at Docking Stations dotted throughout the city.

###Welcome to Being a Developer

Let's go back several years, to the days when there were no Boris Bikes. Imagine that you're a junior developer (congratulations! That was easy). Transport for London, the body responsible for delivery of a new bike system, come to you with a plan: a network of Docking Stations and bikes that anyone can use. They want you to build a program that will run all the Docking Stations, simulate all the Bikes, and emulate all the infrastructure (vans, repair staff, and so on) required to make their dream a reality. They call it - guess what? - 'Boris' Bikes, and they're offering a tasty sum of money.

These challenges will help to guide your first few steps when presented with any software project. There are 22 challenges, and they all build on one another. They require you to research things, to get stuck, and to find your own solutions. This is on purpose. A developer is a 'knowledge worker' - someone who will spend the majority of their time researching and learning how to solve problems. It'll suck for a bit, but with practice, you will get faster: and there's no better feeling than finding the answer to a problem that's been standing in your way for hours.

###User Stories

```
As a person,
So that I can use a bike,
I'd like a docking station to release a bike.

As a person,
So that I can use a good bike,
I'd like to see if a bike is working

As a member of the public
So I can return bikes I've hired
I want to dock my bike at the docking station

As a member of the public
So I can decide whether to use the docking station
I want to see a bike that has been docked

As a member of the public,
So that I am not confused and charged unnecessarily,
I'd like docking stations not to release bikes when there are none available

As a maintainer of the system,
So that I can control the distribution of bikes,
I'd like docking stations not to accept more bikes than their capacity.

As a system maintainer,
So that I can plan the distribution of bikes,
I want a docking station to have a default capacity of 20 bikes.

As a system maintainer,
So that busy areas can be served more effectively,
I want to be able to specify a larger capacity when necessary.

As a member of the public,
So that I reduce the chance of getting a broken bike in future,
I'd like to report a bike as broken when I return it.

As a maintainer of the system,
So that I can manage broken bikes and not disappoint users,
I'd like docking stations not to release broken bikes.

As a maintainer of the system,
So that I can manage broken bikes and not disappoint users,
I'd like docking stations to accept returning bikes (broken or not).

As a maintainer of the system,
So that I can manage broken bikes and not disappoint users,
I'd like vans to take broken bikes from docking stations and deliver them to garages to be fixed.
```

##Contributors

* [Michael Lennox](https://github.com/michaellennox) - michael@michaellennox.me
