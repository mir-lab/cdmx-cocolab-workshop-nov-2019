# cocolab workshop nov 2019

## Artist Instructors
Matthew Ragan | [matthewragan.com](https://matthewragan.com)  
Zoe Sandoval | [zoesandoval.com](https://zoesandoval.com)  
Materializing Interactive Research | [mir.works](https://mir.works)

## Dependencies
* [TouchDesigner099](https://www.derivative.ca/099/Downloads/)

## Recommended Tools
Having an external text editor is key to lots of work in Touch. I like VS Code these days, though Sublime is also a solid choice
* [VS Code](https://code.visualstudio.com/)
* [Sublime Text](https://www.sublimetext.com/)

## Before the Workshop
Before we meet there are a few things to make sure you’ve got in place. Here’s a quick run down of the pieces to make sure are in order before the workshop.

**Required**
* Make sure you’ve updated to the most recent stable build of TouchDesigner 099
* Download and install python 3.5.1. There's a link above to make sure you have the right version of Python. This version matches the same version Touch uses and will make sure we don't have any major hiccups while we're working together.
* Download the github repo linked above. We’ll be working with some files that are already set-up so we don’t have to make everything from scratch so it will be important to have these elements in place.
* Make sure you have your laptop charger packed in your bag :)

**Suggested**
* Download and install a text editor - you don’t need this, but it will make a world of difference when working with lots of Python. Our recommendation is to install VS Code as it has a built in terminal. 
* Reflect on the projects you’ve worked on in the past, and bring some questions about the problems you’ve encountered.
* Think about the wobbles you've had when working with Python, and bring some questions for the group to discuss.
* Don’t forget your three button mouse ;)

## Schedule

### Day 1 - Shared State Management
Time | Topic
---- | ----
10:00 | Context, Approach, and TouchDesigner
10:30 | A Simple Distributed Sandbox / How to think about Sync
11:30 | Handling Distributed Media Playback - A small example
12:30 | Lunch
13:30 | Handling Realtime Media Playback - A small example
14:30 | Communication Architecture - Building our Essential Machine to Machine Plumbing
15:30 | Controlling our Small Examples with our new Communication Structure
16:00 | Q&A / Experimentation Time
17:00 | Wrap

### Day 2 - Modular UI Strategies and Q&A
Time | Topic
---- | ----
10:00 | Recap of Day 1
10:15 | UI Design and Organization
11:30 | UI Wrappers for our simple Examples
12:30 | Lunch
13:30 | Sequencing and Playing Content - Video and Realtime
14:30 | Open QA and Case Studies Discussion
17:00 | Wrap

## Overview
### Day 1
Our first day is going to focus on the essential pieces of working with distributed systems. We'll look a the challenges in front of us, pull apart different types of sync, build a starting point sandbox, and then look at creating simple examples for synchronizing traditional media and real time media playback. These essential building blocks will be our foundational pieces for understanding how to address the challenges that come with building for systems that run across multiple severs. 

Importantly, we'll take a naive approach to this work as we start, and then refactor over over the course of the day. This means that we'll look at brute force solutions first - how do we solve the problems in front of us, then think about more elegant and considered approaches that will make future development smoother and less frustrating. In other words, we'll do all of this the hard way first, then course correct with more thoughtful approaches. Why do that? Brute force methods are often helpful in a pinch - and we don't always have time for an elegant solution. 

With any luck, by the end of the day we'll have written a communication framework that will serve as the backbone of our work on Day 2.

### Day 2
We'll start the day with a recap of what we covered on Day 1. We'll then look at some approaches for simplifying how we can tackle UI building in TouchDesigner. You may want a custom design, or just want to use a simple parameter COMP - either of these are fine solutions, and we should ensure that consider this need as we develop a system. This will also open up opportunities for us to controll TouchDesigner with custom web based UIs, or other control systems. 

Building from Day 1 we'll land on an approach that should provide for flexible control building that still follows a considered design pattern. 

We'll end Day 2 with some discussion of approaches that have worked well, and those that have fallen short of being useful for reliable systems. 