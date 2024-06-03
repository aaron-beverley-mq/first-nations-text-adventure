# First Nations Text-based Adventure Game

## Learning Intentions
- Understand how different languages can be representing in an application
- Understand the process or reading others code and refactoring it into a different coding paradigm
- Develop literature skills 
- Build skills in testing software
  
## Success Criteria
- The code is modified so that it is still functional but written using the Object-Oriented paradigm
- Have an appreciation for the First Nation Peoples language spoken in Darug Country
- Be able to show skills in developing internationalisation features for a software program
- Program is extended to support the marking criteria

## Syllabus
- describes methods used to plan, develop and engineer software solutions SE-11-01
- explains how structural elements are used to develop programming code SE-11-02
- applies language structures to refine code SE-11-08
- manages and documents the development of a software project SE-11-09
- applies tools and resources to design, develop, manage and evaluate software SE-11-06
- implements safe and secure programming solutions SE-11-07

### Cross-Curriculum Priorities
The application is to support the language of the Darug people developing and understanding of Aboriginal and Torres Strait Islander Histories and Cultures. It could also be adapted for EAD/L students in particular for the Asia and Australia’s Engagement with Asia curriculum priority by supporting other languages.

## Overview

**Target group:** Stage 6, NSW<br>
**Subject:** Software Engineering

A text-based adventure game is an interactive invented world described in text. It can be filled with different spaces, items, obstacles or anything your imagination allows. The player interacts with the world by typing commands and the game describes the result of the player's commands.

You are to create a text-based adventure game and use methods and attributes to interact with locations in the game. In this game you will move around by using the commands north, south, east, and west. Each time you move, you enter a new location and a description is shown. Your locations and items should be based on the Darug Country region using language documented in the book `The Sydney Language` by Jakelin Troy and other references like the [Aboriginal Heritage Office](https://www.aboriginalheritage.org/) and the [Dharug Dictionary](https://dharug.dalang.com.au/language/dictionary) to source relevant words and information about Darug Country.

An example of a location in your game might be on the edge of the Hawksbury River, described like this:
- You stand wurrungwuri dyiranbun (this side of the Hawksbury River) and see no way to cross.
- The garrigarrang (sea) is buruwi (east).
- The bulga (mountains) is bayinmarri (west).
- The muru (path) you came is balgayalang (south).

Basic support for internationalisation (i18n) is provided and you should extend the files with additional words and phrases that you will use.
- `en.yml` for English
- `darug.yml` for Darug

The starting map looks like:
```mermaid
 flowchart LR
  id1((Dyirabun /<br> Hawkesbury River))
  id2((Colomatta / <br> Blue Mountains))
  id3((Gayamay /<br> Manly Bay))
  id4((Wallumatta /<br> Maquarie Park))
  id5((Baramada / <br> Parramatta))
  id1 <--> id3
  id1 <--> id2
  id5 <--> id4
  id2 <--> id5
  id1 <--> id4
  id4 <--> id3
````

1. There are several bugs in the code. The most notable is that when you fish or hunt currently it does not check if you have crafted the correct items.This will need to
be fixed.
1. You are required to change the game so that it follows good object oriented practices. Remember to include OO concepts like polymorphism, encapsulation, abstraction, association in your code. Also try to use good design like [SOLID](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design) and [DRY](https://docs.getdbt.com/terms/dry). You should also use patterns from the [Gang of four](https://springframework.guru/gang-of-four-design-patterns/) where it makes sense.
1. The code should be extend to include a minimum of 8 locations visited, 5 are provided by default to get you started.
1. Items available in the game should be culturally correct and relevant to the area. 
1. Vocabulary should be as complete as possible.
1. Crafting can be part of your game. Remember the First Nations people have been recorded using methods of agriculture, horticulture and aquaculture.

## Task
### Design Folio
- You should create a design brief that communicates the purpose of your project including and sources of material you have used in researching First Nations people.
- You should include a class diagram and structure charts of any relevant design or coding choices you have made

### Marking Criteria
| Requirement | Marks |
| ----------- | ----- |
| Requirements: Clearly defined including you target audience and what you are creating | 10 |
| Specification: At least 8 correct functional specifications and 8 non-functional specifications | 10 |
| Design: <br>(a) At least 1 class diagram or structure chart of your solution<br>(b) A detailed description of at least 4 new features(locations, crafting, functionality) | 10 |
| Your solution has been respectful of First Nations people | 10 |
| The solution has a complete vocabulary of translations | 10 |
| You should ensure that the system has unit tests and has documentation on how to run it. | 10 |
| Your solution shows you have a solid understanding of OO Concepts and software development:<br>- code is well documented<br>- OO paterns are used to good effect<br>- Code is structured using OO concepts | 20 |

