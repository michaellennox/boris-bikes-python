#Boris Bikes

This is a repeat of the [boris-bikes-challenge](https://github.com/makersacademy/course/blob/master/boris_bikes/0_challenge_map.md) written in Python instead of the original Ruby. You can find my original Ruby solution [at this repo](https://github.com/michaellennox/boris-bikes).

I have aimed to solve this challenge in a test driven manner with automated tests using the unittest library and the nose testrunner.

##Installation Instructions

Clone the repository then change directory into it.

```
$ git clone git@github.com:michaellennox/boris-bikes-python.git
$ cd boris-bikes-python
```

Install and activate VirtualEnv

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Install required packages using pip and the requirements.txt file

```
$ pip install -r requirements.txt
```

Open the interpreter and import the application files

```python
$ python
>>> from app.bike import Bike
>>> from app.docking_station import DockingStation
>>> from app.garage import Garage
>>> from app.van import Van
```

Now you can use the boris bikes system.

##Usage Instructions

As a member of the public you can dock and remove bikes from the docking station. You can also report your bike as broken.

```python
>>> station = DockingStation()
>>> bike = Bike()

# To report your bike as broken use .report_broken()
>>> bike.report_broken()
>>> bike.isworking
False

# To dock at station, use .dock() on the station and pass the bike as an argument,
# you can then see bikes inside the station with .bikes
# This will fail if the docking station is full
>>> station.dock(bike)
>>> station.bikes
[<app.bike.Bike object at 0x103bd78d0>]

# To remove a working bike from the station use release_bike() with an argument of 'working'
# This will fail if there are no working bikes present at your docking station
>>> station.release_bike('working')
<app.bike.Bike object at 0x103bd7950>
```

As a system maintainer you can transport broken bikes from stations to garages to repair them. You can then repair them at the garage and transport them back to docking stations.

```python
>>> station = DockingStation()
>>> bike = Bike()
>>> van = Van()
>>> garage = Garage()

# To remove a broken bike from a station use .remove_bike from your van, passing the station and 'broken' as arguments
# To remove the broken bike from the van do the same from the garage
>>> van.remove_bike(station, 'broken')
>>> van.bikes
[<app.bike.Bike object at 0x103bd78d0>]
>>> garage.remove_bike(station, 'broken')
>>> garage.bikes
[<app.bike.Bike object at 0x103bd78d0>]

# To repair the bike use .repair_bike() passing the bike as an arguments
>>> garage.repair_bike(bike)
>>> bike.isworking
True

# You can then transport it back to the docking station in the same manner
>>> van.remove_bike(garage, 'working')
>>> station.remove_bike(van, 'working')
>>> station.bikes
[<app.bike.Bike object at 0x103bd78d0>]
```

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

As a maintainer of the system,
So that I can manage broken bikes and not disappoint users,
I'd like vans to collect working bikes from garages and distribute them to docking stations.
```

##Contributors

* [Michael Lennox](https://github.com/michaellennox) - michael@michaellennox.me
